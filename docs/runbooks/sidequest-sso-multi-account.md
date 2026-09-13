# Side Quest — AWS IAM Identity Center (SSO) + multi-account

**GitHub issue:** #15
**Goal:** Enterprise-style access — SSO login URL, multiple accounts, per-account roles (admin / read-only), local CLI profiles, and no long-lived keys.

---

## What exists now

- **Organization:** `o-qfrdlof1bl`
- **Identity Center instance:** `arn:aws:sso:::instance/ssoins-72238b1ab04e06a5` (identity store `d-90667f46b7`)
- **Access portal (login URL):** `https://d-90667f46b7.awsapps.com/start`
- **SSO user:** `abd_builds` (principal id `d418b4c8-d031-708b-e535-167d794bc11e`)

**Accounts**
| Account | ID | Role |
|---|---|---|
| Management | `738281458957` | AdministratorAccess |
| Dev | `493387716675` | AdministratorAccess, ReadOnlyAccess |

**Local profiles** (`~/.aws/config`)
| Profile | Account | Role |
|---|---|---|
| `default` | Management | AdministratorAccess (SSO) |
| `mgmt-admin` | Management | AdministratorAccess |
| `dev-admin` | Dev | AdministratorAccess |
| `dev-readonly` | Dev | ReadOnlyAccess |

---

## Concepts (the 3 that get confused)

- **Account** = an isolated AWS box (Management, Dev, Prod). Not a profile.
- **Permission set** = an access level (admin / read-only) granted *in* an account. Behind the scenes it's an IAM role Identity Center manages for you.
- **Profile** = a *local* laptop shortcut for one (account + permission set) combo.

Analogy: account = building, permission set = keycard type, profile = the labeled card in your wallet.

---

## How it was built

1. **Enable IAM Identity Center** in console (us-east-1). Auto-created the Organization; this account became the management account.
2. **Bootstrap admin** (console, as root): create user `abd_builds`, create `AdministratorAccess` permission set, assign it to `abd_builds` on the management account. Activate the user via the email invite (password + MFA).
3. **Local SSO login:** write `~/.aws/config` (sso-session + profiles), then `aws sso login --profile mgmt-admin` (browser). Verify with `aws --profile mgmt-admin sts get-caller-identity`.
4. **Create Dev + roles** (CLI, as mgmt-admin):
   ```bash
   export AWS_PROFILE=mgmt-admin
   aws organizations create-account --email <you>+dev@gmail.com --account-name Dev   # async; poll describe-create-account-status
   aws sso-admin create-permission-set --instance-arn <inst> --name ReadOnlyAccess --session-duration PT4H
   aws sso-admin attach-managed-policy-to-permission-set --instance-arn <inst> --permission-set-arn <ro> --managed-policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
   aws sso-admin create-account-assignment --instance-arn <inst> --target-id <dev-id> --target-type AWS_ACCOUNT --permission-set-arn <ps> --principal-type USER --principal-id <abd_builds-id>   # x2 (admin + readonly)
   ```
5. **Add Dev profiles** to `~/.aws/config` (`dev-admin`, `dev-readonly`) — same SSO session, no re-login needed.
6. **Retire static keys:** `mv ~/.aws/credentials ~/.aws/credentials.iam-user.bak`; set `[default]` in config to the SSO mgmt-admin profile so tools still work.

---

## Daily use

```bash
aws sso login                          # once per session (token ~4h); opens browser
aws sts get-caller-identity            # default = Management admin
aws --profile dev-admin s3 ls          # act in Dev as admin
AWS_PROFILE=dev-admin python3 script.py
```

---

## ⚠️ Gotchas & Deviations

- **Limited IAM user couldn't build this.** The old CLI user (`Abdulrehman_saleem`) wasn't admin — couldn't even read its own IAM policies. Had to bootstrap admin via **root in the console** first, then switch to SSO admin for everything else.
- **zsh doesn't word-split unquoted vars.** `P="--profile x"; aws $P ...` fails in zsh (passes it as one arg). Use `export AWS_PROFILE=...` or `${=P}` instead.
- **Claude 4.x Bedrock stays in Management for now.** Best practice says workloads belong in Dev, but Bedrock model access was enabled in Management, so the course keeps running there (default profile). Moving to Dev would require re-enabling Bedrock there.
- **SSO tokens expire (~4h).** Unlike static keys, you must `aws sso login` again when the token lapses. Old keys are backed up at `~/.aws/credentials.iam-user.bak` as a fallback.

---

## Not done yet (follow-ups)

- **Prod account** — same as Dev (create account + assign admin/read-only + add `prod-admin`/`prod-readonly` profiles).
- **Codify in CDK (Python)** — express the permission sets + assignments as `aws-cdk-lib/aws-sso` for infra-as-code practice.

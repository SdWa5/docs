# SdWa5 — Services usage

Org-level usage overview for the SdWa5 organization's services. This covers
*what* each service is used for and *why* — technical/operational detail
(Docker setup, credentials, infrastructure) lives in
[`sdwa5-vps/docs/`](../sdwa5-vps/docs/).

## Dolibarr (ERP / accounting)

Dolibarr is the organization's ERP, used primarily for accounting given the
Kleinunternehmer status (§6 Abs. 1 Z 27 UStG — no VAT on invoices). Instance:
https://erp.sdwa5.org

**It also holds the organization's operational backlog**, in the Projects
module, since 2026-09-15. The repositories' `TODO.md` files stay technical, and
anything that is a purchase, a deadline, an event settlement or a piece of
Verein administration belongs here instead. The backlog is written in from a
gitignored JSON spec by `tools/dolibarr/sync-pm.sh`, which creates and updates
but never deletes, so closing a task stays a job for the Dolibarr UI. See
[`sdwa5-vps/docs/dolibarr.md`](../sdwa5-vps/docs/dolibarr.md#projects-and-tasks).

Users, measured 2026-09-08: three accounts, all enabled. The admin account is the only one in use,
last login 2026-07-27. The two other accounts were created on 2025-07-08 and have **never been
logged into**, so they are provisioned rather than planned.

Technical/ops detail: [`sdwa5-vps/docs/dolibarr.md`](../sdwa5-vps/docs/dolibarr.md)

## Vaultwarden (password manager)

Self-hosted Bitwarden-compatible password manager for org credentials.
Instance: https://vault.sdwa5.org

Users, measured 2026-09-08: four accounts, not one.

| Account | Org role |
|---|---|
| Stefan | Owner |
| second account | User |
| third account | not a member |
| fourth account | invited, never accepted |

**Three of the four are on PBKDF2 rather than Argon2id.** Only an account holder can change their own
KDF, so that is a message to them rather than an action here.

**The organization has a single Owner**, so until a Takeover grantee is confirmed, losing that account
loses the organization's data. Emergency access is being set up with a new member, as of 2026-09-08.
Tracked in [`sdwa5-vps/TODO.md`](../sdwa5-vps/TODO.md).

The two accounts that have never been used are **kept deliberately**, decided 2026-09-08. Neither
holds anything, so the exposure is a login rather than anything readable, and deleting an account
someone was invited to costs more explaining than it saves.

Technical/ops detail: [`sdwa5-vps/docs/vaultwarden.md`](../sdwa5-vps/docs/vaultwarden.md)

## Shopware (shop / merch)

Storefront at https://sdwa5.org used for merch distributed as voluntary
donations (no commercial sale, no VAT). Also hosts org content pages (About,
Events, Music/Mixes, Gallery, legal pages).

Technical/ops detail: [`sdwa5-vps/docs/shopware/README.md`](../sdwa5-vps/docs/shopware/README.md)

## Google Workspace / Drive

Mail, users, groups and central file storage (Shared Drive "SdWa5") for the
`sdwa5.org` domain — see [google-workspace.md](google-workspace.md).

## PayPal

The organization's only payment account — see
[organization.md](organization.md#bank--payments).

## Social / external accounts

| Service   | Account                                | Mail routing         |
|-----------|----------------------------------------|----------------------|
| Facebook  | https://www.facebook.com/sdwa5.system  | —                    |
| Instagram | https://www.instagram.com/sdwa5.system | —                    |
| YouTube   | https://www.youtube.com/@SdWa5         | `youtube@` → `mail@` |

SoundCloud: no org profile yet — board members use personal profiles. Playlist
`949270006` is embedded on [/Music-Mixes/](https://sdwa5.org/Music-Mixes/);
alias `sound@` → `mail@`.

## GitHub

Three repositories in the GitHub organization **[SdWa5](https://github.com/SdWa5)**, moved there from
the personal account `bestcodename` on 2026-09-12:
[docs](https://github.com/SdWa5/docs) (this repo, org documentation),
[vps](https://github.com/SdWa5/vps) (VPS infrastructure) and
[3d](https://github.com/SdWa5/3d) (speaker and stage models).

All three are still **private**. They are meant to become public, which is gated on the decisions in
[going-public.md](going-public.md) rather than on any work.

**They were moved by pushing into fresh, empty repositories rather than by GitHub's transfer
function**, on purpose. A transfer moves the same object store, so it would have carried the
pre-rewrite commits of both history rewrites into the organization. The three personal repositories
were deleted afterwards, which is what removed that cache.

## Minecraft (community server)

Fabric Minecraft server on the VPS, currently **inactive**.
Technical/ops detail: [`sdwa5-vps/docs/minecraft.md`](../sdwa5-vps/docs/minecraft.md)

## Ollama (LLM inference)

Local LLM inference server on the VPS.
Technical/ops detail: [`sdwa5-vps/docs/ollama.md`](../sdwa5-vps/docs/ollama.md)

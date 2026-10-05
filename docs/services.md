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

Some accounts are on PBKDF2 rather than Argon2id, and only an account holder can change their own KDF,
so that is a message to them rather than an action here. Emergency access is being set up. Both are
tracked in [`sdwa5-vps/TODO.md`](../sdwa5-vps/TODO.md).

**The account table and the recovery posture came out on 2026-09-15**, decided with the rest of that
day's audit. The thinning of 2026-09-12 had taken the per-account figures out and left the conclusions
standing, and a reachable host read next to a named owner, a count of weaker accounts and a stated
single point of failure is a targeting statement whatever the figures say. What is left is the part
somebody has to act on.

The two accounts that have never been used are **kept deliberately**, decided 2026-09-08. Neither
holds anything, so the exposure is a login rather than anything readable, and deleting an account
someone was invited to costs more explaining than it saves.

Technical/ops detail: [`sdwa5-vps/docs/vaultwarden.md`](../sdwa5-vps/docs/vaultwarden.md)

## Shopware (shop / merch)

Storefront at https://sdwa5.org used for merch distributed as voluntary
donations (no commercial sale, no VAT). Also hosts org content pages (About,
Events, Music/Mixes, Gallery, legal pages).

Technical/ops detail: [`sdwa5-vps/docs/shopware/README.md`](../sdwa5-vps/docs/shopware/README.md)

## Chimo Diazz (hosted for a third party)

Artist website for the DJ Chimo Diazz at https://chimodiazz.sdwa5.org, built on Shopware 6 used as a
CMS rather than as a shop. **This is not an SdWa5 service.** It is a favour: the site is developed by
its own author in the private repository `chimodiazz/website`, and SdWa5 provides the subdomain, the
VPS and the operations.

That arrangement is worth naming rather than leaving implicit, because it puts someone else's site on
the association's domain, its host and its Let's Encrypt contact address. Three consequences follow
from it.

- Anything the site publishes is published under `sdwa5.org`, so the association's Impressum and its
  reputation are attached to content it does not write.
- The host is shared. A second Shopware instance is the largest thing this VPS would then run twice,
  and a fault in it competes for memory with the shop and the ERP.
- The split of duties is deliberate and should stay written down. SdWa5 owns the VPS, DNS, TLS,
  Docker and the Shopware installation. The author owns theme, content, forms, blog, SEO and plugins.

As of 2026-09-15 the subdomain serves a static placeholder and no container runs.

Technical/ops detail: [`sdwa5-vps/docs/chimodiazz.md`](../sdwa5-vps/docs/chimodiazz.md)

## Google Workspace / Drive

Mail, users, groups and central file storage (Shared Drive "SdWa5") for the
`sdwa5.org` domain — see [google-workspace.md](google-workspace.md).

## PayPal

The organization's only payment account — see
[organization.md](organization.md#bank--payments).

A PayPal sync into Dolibarr has been live since 2026-10-05, still in dry run. The module is the fork
[SdWa5/banksync](https://github.com/SdWa5/banksync) of `vanyolai/dolibarr-banksync`, checked out as
`sdwa5-banksync/` next to the other repositories and deployed on the VPS at v1.2.0. A daily scheduled
job at 06:00 UTC fetches PayPal's transactions into bank account 4 from the cutover date 2026-09-09 on
and reports new queue items to mail@sdwa5.org. In dry run it posts nothing and only records what it
would post. Once `BANKSYNC_AUTOPOST_ENABLED` is switched on, it posts fees and payments that clearly
belong to one supplier invoice and leaves everything else in a queue where the Rechnungsprüfer
settles it together with its Belege. The hand-typed lines before the cutover stay as they are. Setup and behaviour are in the fork's `docs/paypal.md`, the deployment in
[`sdwa5-vps/docs/dolibarr.md`](../sdwa5-vps/docs/dolibarr.md#custom-modules), and the remaining
go-live steps in `sdwa5-vps/TODO.md`.

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

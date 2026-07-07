# SdWa5 — Google Workspace

Google Workspace usage for the `sdwa5.org` domain.

## Plan / Nonprofit status

Google Workspace for Nonprofits: **approved** (status checked 2026-07-04 on
https://www.google.com/nonprofits/), Workspace domain `sdwa5.org`.

## Admin

Super Admin: Stefan Ripper (`ripper@sdwa5.org`) — sole assigned administrator.
User management via the standard admin console (https://admin.google.com).

## Users

| User            | Address            | Notes                                                        |
|-----------------|--------------------|--------------------------------------------------------------|
| Stefan Ripper   | `ripper@sdwa5.org` | Super Admin; SMTP auth for Shopware (App Password) — see [`sdwa5-vps/docs/shopware/shop-config.md`](../sdwa5-vps/docs/shopware/shop-config.md#smtp); Caddy Let's Encrypt contact — see [`sdwa5-vps/docs/caddy.md`](../sdwa5-vps/docs/caddy.md); owns `restic-backups` Drive folder |
| Obmann-Stv.     | `sepp@sdwa5.org`   |                                                              |
| Obmann-Stv.     | (second mailbox)   |                                                              |

## Groups

One group **Allgemein** — `mail@sdwa5.org`, 3 members (all users), access type
custom. Also the PayPal account address (see
[organization.md](organization.md#bank--payments)).

Aliases of the group (all deliver to `mail@sdwa5.org`):

`help@` `all@` `info@` `noreply@` `sdwa5@` `shop@` `sound@` `youtube@`
`erp@` `vault@`

Notes:

- `shop@sdwa5.org` (Shopware sender / storefront contact) is a group alias,
  not a separate mailbox.
- `admin@sdwa5.org` / `github@sdwa5.org` (GitHub org plan, see
  [TODO.md](../TODO.md)) do not exist yet.

## Drive / Backup

VPS Restic backups land in Google Drive folder `restic-backups`, owned by
`ripper@sdwa5.org` (same Workspace account; rclone remote `[SdWa5]`, OAuth2) —
see [`sdwa5-vps/docs/backup.md`](../sdwa5-vps/docs/backup.md). Access:
restricted, only people with access can open the link.

Shared Drive (Geteilte Ablage) **SdWa5** — central storage for everything,
including the org documents folder (see
[organization.md](organization.md#documents)).

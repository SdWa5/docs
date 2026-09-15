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
| Stefan Ripper   | `ripper@sdwa5.org` | Super Admin |
| board member    | `sepp@sdwa5.org`   |                                                              |
| board member    | (second mailbox)   | Local-part withheld, see below                               |

**Which mailbox carries which service credential is not written down here**, decided 2026-09-15. This
row used to say in one sentence that one account holds the Shopware SMTP App Password, is the Caddy
Let's Encrypt contact, and owns the `restic-backups` Drive folder. None of those credentials is in any
repository, but the sentence told a reader exactly which mailbox to go after to take mail, certificates
and backups together. That each of the three exists is documented where it is used; which account it is
lives in the password manager.

The third user's local-part is the first syllable of a surname this repository otherwise does not
publish, so writing it here would republish by the back door what
[organization.md](organization.md) deliberately defers to the ZVR register. `sepp@` is a nickname and
carries no such reading, so it stands as written. Neither row names a board role any more, because
pairing a mailbox with "Obmann-Stv." was what made the table identifying in the first place.

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

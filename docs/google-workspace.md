# SdWa5 — Google Workspace

Google Workspace usage for the `sdwa5.org` domain.

## Known mailboxes

| Address              | Usage                                         |
|-----------------------|-----------------------------------------------|
| `ripper@sdwa5.org`    | SMTP auth for Shopware (App Password) — see [`sdwa5-vps/docs/shopware.md`](../sdwa5-vps/docs/shopware.md#smtp); Caddy Let's Encrypt contact — see [`sdwa5-vps/docs/caddy.md`](../sdwa5-vps/docs/caddy.md) |
| `shop@sdwa5.org`      | Shopware sender / storefront contact address  |
| `admin@sdwa5.org`     | Planned — GitHub org admin account (see [TODO.md](../TODO.md) item 4) |
| `github@sdwa5.org`    | Planned — GitHub org role address (see [TODO.md](../TODO.md) item 4) |

## TODO

- [ ] Confirm Google Workspace for Nonprofits enrollment status
- [ ] Document admin console access / user management process
- [ ] List all active mailboxes and groups
- [ ] Document shared drives usage (if any)
- [ ] Backup: confirm relation to Restic/rclone Google Drive backup target
      (see [`sdwa5-vps/docs/backup.md`](../sdwa5-vps/docs/backup.md)) — same
      Workspace account or separate?

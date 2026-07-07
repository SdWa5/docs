# SdWa5 — Services usage

Org-level usage overview for the SdWa5 organization's services. This covers
*what* each service is used for and *why* — technical/operational detail
(Docker setup, credentials, infrastructure) lives in
[`sdwa5-vps/docs/`](../sdwa5-vps/docs/).

## Dolibarr (ERP / accounting)

Dolibarr is the organization's ERP, used primarily for accounting given the
Kleinunternehmer status (§6 Abs. 1 Z 27 UStG — no VAT on invoices). Instance:
https://erp.sdwa5.org

Users: currently only Stefan; Sepp and Ziri planned.

Technical/ops detail: [`sdwa5-vps/docs/dolibarr.md`](../sdwa5-vps/docs/dolibarr.md)

## Vaultwarden (password manager)

Self-hosted Bitwarden-compatible password manager for org credentials.
Instance: https://vault.sdwa5.org

Users: currently only Stefan; Sepp and Ziri planned.

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

Repositories currently under the personal account `bestcodename`:
[sdwa5](https://github.com/bestcodename/sdwa5) (this repo, org docs) and
[sdwa5-vps](https://github.com/bestcodename/sdwa5-vps) (VPS infrastructure).
Migration to a GitHub organization `sdwa5` is planned — see [TODO.md](../TODO.md).

## Minecraft (community server)

Fabric Minecraft server on the VPS, currently **inactive**.
Technical/ops detail: [`sdwa5-vps/docs/minecraft.md`](../sdwa5-vps/docs/minecraft.md)

## Ollama (LLM inference)

Local LLM inference server on the VPS.
Technical/ops detail: [`sdwa5-vps/docs/ollama.md`](../sdwa5-vps/docs/ollama.md)

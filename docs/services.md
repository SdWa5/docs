# SdWa5 — Services usage

Org-level usage overview for the SdWa5 organization's services. This covers
*what* each service is used for and *why* — technical/operational detail
(Docker setup, credentials, infrastructure) lives in
[`sdwa5-vps/docs/`](../sdwa5-vps/docs/).

## Dolibarr (ERP / accounting)

Dolibarr is the organization's ERP, used primarily for accounting given the
Kleinunternehmer status (§6 Abs. 1 Z 27 UStG — no VAT on invoices). Instance:
https://erp.sdwa5.org

Technical/ops detail: [`sdwa5-vps/docs/dolibarr.md`](../sdwa5-vps/docs/dolibarr.md)

## Vaultwarden (password manager)

Self-hosted Bitwarden-compatible password manager for org credentials.
Instance: https://vault.sdwa5.org

Technical/ops detail: [`sdwa5-vps/docs/vaultwarden.md`](../sdwa5-vps/docs/vaultwarden.md)

## Shopware (shop / merch)

Storefront at https://sdwa5.org used for merch distributed as voluntary
donations (no commercial sale, no VAT). Also hosts org content pages (About,
Events, Music/Mixes, Gallery, legal pages).

Technical/ops detail: [`sdwa5-vps/docs/shopware/README.md`](../sdwa5-vps/docs/shopware/README.md)

## TODO

- [ ] Document any additional org tooling not yet covered here

# SdWa5

SdWa5 organization root repository — documentation, org info, and links to
sub-repositories.

SdWa5 (Musikverein Schmeiß die Wand an 5) is a non-profit association. This
repo is the entry point for the organization's documentation; it does not
itself contain a deployable application.

## Documentation

Documentation is split by audience: [`docs/`](docs/) holds the org-level
documentation (*what* services are used for and *why*), while
[`sdwa5-vps/docs/`](sdwa5-vps/docs/) holds the technical/ops documentation
(*how* they run: Docker, configs, operations).

See [`docs/`](docs/) for:

- [Organization](docs/organization.md) — legal/official info
- [Google Workspace](docs/google-workspace.md) — `sdwa5.org` Workspace usage
- [Services](docs/services.md) — usage overview of all org services
  (Dolibarr, Vaultwarden, Shopware, social accounts, GitHub, ...)
- [Going public](docs/going-public.md) — what publishing these repositories
  would disclose, and the decisions that are still open

## Sub-repositories

- [`sdwa5-vps`](sdwa5-vps) — VPS infrastructure, Docker Compose configs, and
  technical/ops documentation for all self-hosted services
- [`sdwa5-3d`](sdwa5-3d) — 3D models of the speakers and stage equipment,
  generated from specs, for Blender event previews and PA setup planning
- [`sdwa5-dsp`](sdwa5-dsp) — editor, command line and PHP library for the PA's
  t.racks 8x8 DSP over USB or LAN, with gain riders, measurements and Auto EQ,
  formerly trackdsp
- [`sdwa5-banksync`](https://github.com/SdWa5/banksync) — Dolibarr module, a fork of BankSync with
  a PayPal provider, automatic posting and a review queue with Belege

## Checks

[`.github/workflows/docs.yml`](.github/workflows/docs.yml) runs on every push.

- **Links.** Every relative link and every `#anchor` in this repository's markdown is resolved
  against the filesystem. External URLs are fetched weekly on Mondays instead of per push, so a
  rate limit never fails a build over an unrelated commit.
- **Secrets.** The working tree and the full history are scanned with
  [gitleaks](https://github.com/gitleaks/gitleaks). This runs in all three SdWa5 repositories,
  because they are going public and a public repository publishes every past commit at once.

Both checks run locally against the same configuration:

```sh
lychee --offline --include-fragments --config lychee.toml './*.md' './docs/**/*.md'
gitleaks dir . --redact --config .gitleaks.toml
gitleaks git . --redact --config .gitleaks.toml
```

The link check covers links into the sub-repositories, such as
[`../sdwa5-vps/docs/caddy.md`](sdwa5-vps/docs/caddy.md). Those are separate repositories that only
sit in subdirectories here and are gitignored, so CI clones them on its own. Locally they are already
present and the check just works.

## Contact

shop@sdwa5.org

## Licence

Two licences, because this repository is part tooling and part writing.

- **MIT** ([LICENSE](LICENSE)) for the code and configuration: `.github/`, `.idea/`, `lychee.toml`, `.gitleaks.toml` and `composer.json`.
- **CC BY-SA 4.0** ([LICENSE-docs](LICENSE-docs)) for the prose and data: `docs/`, `README.md`, `CHANGELOG.md` and `TODO.md`.

Attribute as "Musikverein Schmeiß die Wand an 5 (SdWa5)" with a link to the repository. Share-alike applies to the prose, so a
derivative of the documentation stays under the same licence. The code carries no such condition.

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

## Sub-repositories

- [`sdwa5-vps`](sdwa5-vps) — VPS infrastructure, Docker Compose configs, and
  technical/ops documentation for all self-hosted services
- [`sdwa5-3d`](sdwa5-3d) — 3D models of the speakers and stage equipment,
  generated from specs, for Blender event previews and PA setup planning

## Checks

[`.github/workflows/docs.yml`](.github/workflows/docs.yml) runs on every push.

- **Links.** Every relative link and every `#anchor` in this repository's markdown is resolved
  against the filesystem. External URLs are fetched nightly instead of per push, so a rate limit
  never fails a build over an unrelated commit.
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

## License

No license specified — all rights reserved unless stated otherwise per
sub-repo.

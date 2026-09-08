# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- `docs/services.md` records two decisions taken on 2026-09-08. Emergency access with a Takeover
  grantee is being set up with a new member, and the two Vaultwarden accounts holding zero
  items are kept rather than deleted, because neither holds data and deleting an account someone was
  invited to costs more explaining than it saves.

## [0.4.0] - 2026-09-08

### Fixed

- `docs/services.md` said both Dolibarr and Vaultwarden had "currently only Stefan; Sepp and Ziri
  planned". Neither was true, measured on 2026-09-08. Dolibarr has three enabled accounts, and the
  Sepp and Ziri ones were created on 2025-07-08 and have never been logged into, so they are
  provisioned rather than planned. Vaultwarden has four accounts, two of which are in active use with
  differing numbers of items.

### Added

- `docs/services.md` records the Vaultwarden accounts with their KDF, item count, last activity and
  organization role, and states plainly that the SdWa5 organization has a single Owner holding 32
  ciphers in 5 collections while `emergency_access` has zero rows, so losing that account loses the
  organization's data.

## [0.3.0] - 2026-07-30

### Added

- New sub-repository [`sdwa5-3d`](sdwa5-3d) — spec-driven parametric 3D models of the speakers and
  stage equipment, for Blender event previews and PA setup planning. Its own docs, TODO and
  changelog live in that repo
- `README.md`: `sdwa5-3d` listed under sub-repositories
- `TODO.md`: delegation to [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
- `.gitignore`: `/sdwa5-3d` — nested repos stay separate, same as `/sdwa5-vps`
- `.idea/vcs.xml`: `sdwa5-3d` registered as a VCS root; `.idea/developer-tools.xml` added

### Changed

- `composer.json`: description mentions `sdwa5-3d`

### Fixed

- `CHANGELOG.md`: backfilled the missing `0.2.0`–`0.2.8` entries from their commit messages, and
  corrected `0.1.0`, which listed `README.md`, `CHANGELOG.md` and `docs/` although those arrived in
  `0.2.0`

## [0.2.8] - 2026-07-07

### Removed

- `TODO.md`: TODO format consistency item — obsolete, docs TODO sections all resolved; numbered
  lists kept (resolved items get deleted, not checked off)

## [0.2.7] - 2026-07-07

### Changed

- `TODO.md`: infrastructure diagram item resolved (diagram in `sdwa5-vps/docs/infrastructure.md`)

## [0.2.6] - 2026-07-07

### Added

- `docs/services.md`: Google Workspace/Drive, PayPal, social accounts (Facebook, Instagram, YouTube,
  SoundCloud), GitHub, Minecraft, Ollama sections; Dolibarr/Vaultwarden user info
- `README.md`: explicit docs separation (`docs/` = org-level what/why, `sdwa5-vps/docs/` =
  technical how)

### Changed

- `TODO.md`: services.md TODO resolved, "resolve TODOs" item removed

### Removed

- `docs/services.md`: TODO section
- `docs/google-workspace.md`: `swda5.system@` alias (deleted in Workspace) + typo note

## [0.2.5] - 2026-07-04

### Fixed

- `docs/google-workspace.md`: Shared Drive "SdWa5" is central storage (previously stated no Shared
  Drives in use)

## [0.2.4] - 2026-07-04

### Added

- `docs/google-workspace.md`: nonprofit status, admin, users, group + aliases, drive/backup relation

### Changed

- `TODO.md`: google-workspace.md TODO resolved

### Removed

- `docs/google-workspace.md`: TODO section

## [0.2.3] - 2026-07-04

### Added

- `docs/organization.md`: board (Vorstand), Rechnungsprüfer, PayPal payment info, statutes summary,
  documents section
- `docs/organization.md`: public ZVR register fetch URL

### Changed

- `docs/organization.md`: legal identity extended (Sitz, founding date, registration authority,
  Zustellanschrift)
- `docs/google-workspace.md`, `docs/services.md`: links updated to split shopware docs
- `TODO.md`: organization.md TODO resolved

### Removed

- `docs/organization.md`: TODO section

## [0.2.2] - 2026-07-03

### Added

- `.idea/laravel-idea.xml` for Inertia package configuration

### Changed

- `TODO.md`: readability improved by replacing static paths with relative links
- `.idea/misc.xml`: removed redundant `SshConsoleOptionsProvider` component
- `.idea/sdwa5.iml`: added source directory mappings for custom plugins and test folders

## [0.2.1] - 2026-07-01

### Changed

- `TODO.md`: documentation tasks streamlined and refined. Removed outdated project description and
  added action to resolve TODOs in `docs/`

## [0.2.0] - 2026-07-01

### Added

- `README.md` with project overview and documentation references
- `CHANGELOG.md` adhering to Keep a Changelog format
- `docs/` — organization documentation: [organization.md](docs/organization.md) (legal and official
  organization information), [google-workspace.md](docs/google-workspace.md) (Google Workspace usage
  details), [services.md](docs/services.md) (overview of core services: Dolibarr, Vaultwarden,
  Shopware)
- `composer.json`: project description
- `.idea/git_toolbox_prj.xml` for IntelliJ Git settings

### Changed

- `TODO.md`: outdated entries removed and tasks streamlined

## [0.1.0] - 2026-07-01

### Added

- `.gitignore`
- `composer.json` with project metadata
- `TODO.md` with initial project documentation tasks
- Initial `.idea` project configuration: inspection profiles, module definition, dependency scopes

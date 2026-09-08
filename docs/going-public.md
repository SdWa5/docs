# Going public: what publishing would disclose

The three SdWa5 repositories are private and are meant to become public, tracked in
[`../TODO.md`](../TODO.md) item 2. Item 2.1.2.1 asks for a scan of the content first. **The
credential half of that is done and automated.** `gitleaks` runs over the working tree and the full
history of all three repositories in CI, and all three are clean as of 2026-09-08.

This document is the other half, the one a scanner cannot do. Nothing below is a leaked credential.
Every item is something real that publishing would make world-readable and search-engine-indexable,
and each is a decision rather than a defect.

**This file is itself public.** So it describes each item and names its location, and it deliberately
does not reproduce the address, the name or the value in question. Read it next to the file it points
at.

## The one that cannot be fixed later

**Every commit carries the identity that made it, and publishing a repository publishes all of them.**
Measured 2026-09-08:

| Repository | Commits | Authored as |
|---|---|---|
| `sdwa5` | 22 | a work address on a business domain |
| `sdwa5-3d` | 140 | the same work address |
| `sdwa5-vps` | 95 | **a private address on a third-party mail provider**, as author *and* committer |

Two things follow. The private address is published 95 times in `sdwa5-vps` no matter what any file
says, and the business domain is published 162 times across the other two, which links the
association's repositories to an unrelated employer.

**This is the only item on this list whose window is closing.** Rewriting author identities means
rewriting every commit, which changes every hash. Right now that is cheap, because the repositories
are private, there are exactly two clones of each (the workstation and the deploy checkout at
`/opt/docker`), and there are no forks, no pull requests and no external references. After going
public it is not practical.

Three options, and only the middle one actually removes the disclosure:

* **Accept it.** Publishing an email with your commits is ordinary in open source. GitHub can hide an
  address from its own UI, but the commit objects still carry it and anyone cloning reads it.
* **Rewrite before going public**, with `git filter-repo --mailmap`, mapping both identities to
  whatever the association wants to be known by, for example a role address on `sdwa5.org`. Then
  re-clone `/opt/docker`. This is the moment to do it or not at all.
* **A `.mailmap` file changes nothing.** It only affects how `git log` displays names locally. The
  stored commit objects are untouched, so it does not help here. Worth stating because it looks like
  the answer.

## Personal data of named people

**A private residential address**, in [`organization.md`](organization.md). The association's service
address is care-of a named board member at their home. The Austrian
[ZVR register](https://citizen.bmi.gv.at/at.gv.bmi.fnsweb-p/zvn/public/Registerauszug) already
publishes it against the association's ZVR number, so this discloses nothing legally private. It is
still an escalation, because a register you query on purpose is not the same as a page Google
indexes. Options are to keep it as the register has it, or to replace it with the ZVR number and the
register link and let a reader look it up.

**Four full names with roles and dates**, in the same file. Three are the sitting Vorstand, which the
ZVR register also publishes. The fourth is a **former** board member who left in 2024, and her name
and dates are the hardest of the four to justify keeping, because she is no longer involved and the
history is not needed for anyone to understand the association today.

**A private email address in `sdwa5-vps`.** Removed from all five places in the working tree in
1.24.0 and moved into `.env` on the host, which is gitignored, with the effective alert recipients
unchanged. The history still carries it, which is the item above.

## A combination that is more revealing than its parts

[`services.md`](services.md) documents the Vaultwarden accounts with their KDF, item count, last
activity and organization role. Only the Owner is named; the others are deliberately written as
"second account", "third account" and "fourth account", so somebody already thought about this.

What is left is that the table states an active account holds a number of items on the **weaker** KDF while
the Owner is on Argon2id. Published next to a named, reachable `vault.sdwa5.org`, that tells a reader
where the soft target is and roughly what it is worth. And there are only four accounts against three
named board members in [`organization.md`](organization.md), so the anonymisation is thinner than it
looks.

Nothing here is a credential and the finding is the pairing rather than either file. The cheap remedy
is to drop the per-account KDF and item counts and keep the one sentence that matters, namely that
three accounts are on PBKDF2 and only their holders can change that.

## Third parties who never agreed to any of this

`sdwa5-3d/docs/sources.md` sources many figures to **the owner of another sound system**, quoted
directly from private messages, roughly 40 attributions and 49 quoted strings. Publishing it
discloses another crew's inventory, cabinet dimensions and weights, together with their own words
about it. They gave the figures to help build a model, not to be published, and what a competing
system owns is commercially theirs.

The same file cites a rental company's published datasheets, which is ordinary use of public
material and needs no decision.

The recommendation is to ask the person before publishing that section, and to keep the figures
without the quotations if they would rather not be quoted. Provenance survives as "stated by the
owner" without reproducing the message.

**Minecraft player names and UUIDs**, in `sdwa5-vps` in `minecraft-data/ops.json`,
`minecraft-data/whitelist.json` and the `OPS` and `WHITELIST` environment variables in
`docker-compose.yml`. Four pseudonyms and their UUIDs, which any server they join already sees. Low
sensitivity, and untracking the two JSON files alone would achieve nothing while the same names sit in
the compose file. It is a disclosure decision rather than a leak.

## Infrastructure detail, which is deliberate

The hostname, the IPv6 address, the published ports, the container layout, the firewall rules and the
backup design are all documented and would all become public. **That is the stated intent**, since
`TODO.md` gives "No security by obscurity" as the guideline for this exercise, and a defence that only
works while undescribed is not a defence.

Two things were worth checking against that guideline rather than assuming, and both are fine. No
credential is committed anywhere, confirmed by `gitleaks` over tree and history in all three
repositories. And the identifiers that do appear are useless without access: Vaultwarden item UUIDs
name items inside a vault, and the Google Shared Drive ID names a drive that still requires
authentication.

## The licence, which is a separate decision

No repository has a `LICENSE` file, and the root `README.md` says "No license specified — all rights
reserved unless stated otherwise per sub-repo". Published unchanged, that means a reader may read the
documentation and reuse none of it, not a diagram, not a script, not a spec.

For a non-profit publishing its own operations documentation that is probably not the intent, and it
needs the owner's decision rather than a default. The usual shapes are a permissive licence for the
code and configuration, a Creative Commons licence for the prose and diagrams, or a deliberate
all-rights-reserved with that stated as a choice rather than as an omission.

## What is left to do

The credential scan is done and gated in CI. Every item above is a decision, and the first one is the
only one that gets harder with time.

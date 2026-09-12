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

## The one that could not be fixed later, and was done on 2026-09-08

**Every commit carries the identity that made it, and publishing a repository publishes all of them.**
What that used to be, measured before the rewrite:

| Repository | Commits | Authored as |
|---|---|---|
| `sdwa5` | 22 | a work address on a business domain |
| `sdwa5-3d` | 140 | the same work address |
| `sdwa5-vps` | 95 | a private address on a third-party mail provider, as author *and* committer |

So the private address was published 95 times no matter what any file said, and the business domain
162 times across the other two, which linked the association's repositories to an unrelated employer.

**All three histories are rewritten.** Every commit in every repository now carries a single identity,
`Stefan Ripper <7108645+bestcodename@users.noreply.github.com>`, as author and as committer, and
neither old address appears anywhere. Verified on GitHub as well as locally, and the commits are still
attributed to the `bestcodename` account, so the contribution graph survived.

**The content is provably untouched.** The tree hash at `HEAD` is identical to its pre-rewrite value in
all three repositories, so only the commit objects changed:

| Repository | Tree at `HEAD`, before and after |
|---|---|
| `sdwa5` | `dbbe151333fb` |
| `sdwa5-vps` | `e7d94eebd0ad` |
| `sdwa5-3d` | `1981e6b43b7b` |

How it was done, in case it is ever needed again. `git-filter-repo` runs as a single script and needs
no installation, driven by a two-line mailmap built from the repositories themselves rather than typed
out. It removes `origin`, so the remotes were re-added and each repository force-pushed with a
`--force-with-lease` on its exact pre-rewrite commit, so a concurrent push elsewhere would have
aborted it rather than been overwritten. Bare backups of all three were taken first.

**The two things that would have undone it, and were therefore also done.** `sdwa5-vps` carried a
*local* `user.email` override set to the private address, which is why that repository's commits
differed from the other two, so the next commit would have reintroduced exactly what the rewrite
removed. All three repositories now set the noreply address as a local identity, and the machine's
global identity is deliberately left alone, because the work address is correct for other projects.

And **`/opt/docker` on the VPS was moved with `fetch` plus `reset --hard`, never a re-clone.** It holds
the untracked runtime state of the whole stack, `minecraft-data` alone being 6.9 GiB, so a fresh clone
would have discarded it. Verified afterwards: 6.9 GiB still there, the rotated `server.properties`
still there, tree clean, and all eight health checks green.

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
unchanged.

**The history still carries it, and the item above is not the fix.** That rewrite replaced the author
and committer fields of every commit, which is a different thing from the contents of a file. Measured
on 2026-09-12: the current tree is clean, and **74 of the 113 commits still contain the address**, in
all five files at once — `README.md`, `monitoring/lib.sh`, `.env.example`, `docs/monitoring.md` and
`docs/infrastructure.md`. The earliest carrying commit is the first one on the branch and the latest is
1.5.0 on 2026-09-01.

So this needs a second rewrite, over file contents rather than over identities, and it is the one
remaining item on this list that **cannot** be done after the repository is public. A published commit
is fetched, forked and mirrored, and deleting it afterwards deletes only your copy.

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

**Decided on 2026-09-12, and the decision is to publish it.** The owner of GMSS and the Innschleife
crew are both known personally to the association's owner, who states that neither objects to their
inventory being public. The content was checked rather than taken on trust at the same time: all 60
distinct quoted strings in that file are dimension enumerations, cabinet names or phrases out of a
published datasheet. The longest thing anybody says is "the ones on the outside of the bottom row are
also turbo subs". There is no opinion in it, no third person, no price and no commercial term. Two of
the quotations reach past speakers into amplifiers and lighting, and those are inventory lists in the
same shape.

If that ever needs undoing, the figures can stay while the quotations go, because provenance survives
as "stated by the owner" without reproducing the message.

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

The credential scan is done and gated in CI, and the commit identities were rewritten on 2026-09-08.

**One item is work rather than a decision, and it is the only one that gets harder with time.** The
private email address sits in 74 of `sdwa5-vps`'s 113 commits and has to come out by a rewrite of file
contents before the repository is published. Everything else on this list can be changed afterwards.

The decisions still open are the board member's home address and the four names in
[`organization.md`](organization.md), the Vaultwarden KDF and item-count pairing in
[`services.md`](services.md), the Minecraft names in `sdwa5-vps`, and the licence. The third-party
question is settled and recorded above.

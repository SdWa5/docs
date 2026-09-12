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

**DECIDED 2026-09-12, and two of the three came out.** The board members' names now defer to the ZVR
register, the Vaultwarden posture is thinned, and the address stays. The reasoning for each is below,
kept because the address decision reverses the recommendation this file used to make.

**The tree is done and the histories are not.** the two Obmann-Stellvertreter still sit in 32 of
the root repository's 37 commits and 95 of `sdwa5-vps`'s 115, and the former Obmann-Stellvertreterin in 32 of the
root's. Removing a name from the working tree does not remove it from the history, which is the same
trap the email address set. **A second rewrite over both repositories is outstanding**, and it is the
one item on this list that cannot be done after the repositories are public.

**A private residential address**, in [`organization.md`](organization.md). The association's service
address is care-of a named board member at their home. The Austrian
[ZVR register](https://citizen.bmi.gv.at/at.gv.bmi.fnsweb-p/zvn/public/Registerauszug) already
publishes it against the association's ZVR number, so this discloses nothing legally private. It is
still an escalation, because a register you query on purpose is not the same as a page Google
indexes.

**Kept, and the recommendation this file used to make was wrong.** The shop's own Impressum at
<https://sdwa5.org/Impressum> publishes `Mühlenstraße 24` today, and an Austrian webshop is required
by law to state a Zustellanschrift. Taking it out of git while the shop publishes it is theatre, and
it is in all 115 commits of `sdwa5-vps` for exactly that reason. **What did come out is the `c/o
<name>` prefix**, so the repositories no longer say whose home it is, which the Impressum does not say
either. The only real remedy would be a Zustellanschrift that is not a private home, and that is a ZVR
filing rather than a documentation change.

**Four full names with roles and dates**, in the same file. **Three of the four now defer to the ZVR
register and one is kept**, decided on the same evidence as the address.

The former board member who left in 2024 is gone entirely, name and dates, because she is no longer
involved and the current ZVR extract does not list her either. the two Obmann-Stellvertreter
are replaced by their roles, because the Impressum does **not** name them, so this repository would
have been the only publisher. `Stefan Ripper` stays: the Impressum names him as Obmann by law and he
authored all 304 commits, so taking the name out of three documents while every commit carries it
would be the same theatre as the address.

**A private email address in `sdwa5-vps`.** Removed from all five places in the working tree in
1.24.0 and moved into `.env` on the host, which is gitignored, with the effective alert recipients
unchanged.

**The history still carries it, and the item above is not the fix.** That rewrite replaced the author
and committer fields of every commit, which is a different thing from the contents of a file. Measured
on 2026-09-12: the current tree is clean, and **74 of the 113 commits still contain the address**, in
all five files at once — `README.md`, `monitoring/lib.sh`, `.env.example`, `docs/monitoring.md` and
`docs/infrastructure.md`. The earliest carrying commit is the first one on the branch and the latest is
1.5.0 on 2026-09-01.

**Done on 2026-09-12 in `sdwa5-vps` 1.30.0.** A second rewrite, over file contents rather than over
identities, removed the address together with its separator rather than substituting it, because on
every line it stood next to `ripper@sdwa5.org` as the second recipient. Verified afterwards: `HEAD`'s
tree hash is unchanged at `c887c215`, which it must be since the tree was already clean, the commit
count is 113 before and after, zero commits reachable from `origin/main` contain the address, and no
file anywhere in the history carries a doubled recipient. `.gitleaks.toml`'s allowlisted commit did
not move, checked rather than assumed.

**What remains is GitHub's own copy, and it is the same for all three repositories.** A force-pushed
commit stays reachable by its SHA on GitHub until the repository is garbage-collected, so `da46b79`
and its 74 siblings are still fetchable there by anyone who knows the hash. The two identity rewrites
of 2026-09-08 left the same residue in `sdwa5` and `sdwa5-3d`.

**GitHub's garbage collection has no schedule worth planning around.** It is internal and triggered by
repository maintenance rather than by a clock, and GitHub's own guidance for removing sensitive data
is to contact Support rather than to wait. Support can run one on request, which is free and
open-ended in time.

**Nothing is exposed while the repositories are private**, since an unreachable object is unreachable
to anyone without access to the repository. The whole risk is ordering, so the cache has to be cleared
before the flip to public rather than after it.

**Done on 2026-09-12, by pushing into fresh repositories rather than by transferring.** GitHub's
transfer function moves the same repository and the same object store, so a transfer into the
organization would have carried every cached pre-rewrite commit along with it and quietly undone both
rewrites. Three empty repositories were created in [SdWa5](https://github.com/SdWa5) instead and
pushed into, and the three personal repositories were then deleted, which is what removed the cache.
Verified: each new repository's `main` matches its local `HEAD`, zero commits on `SdWa5/vps` hold the
address, and all three old paths answer "Not Found".

Nothing was lost by doing it that way. All three were private with **0 forks, 0 tags and 0 releases**,
no pull requests and no issues, at 54 KB, 6380 KB and 980 KB. What went is the Actions run history,
every run of which had failed on billing, and one stargazer on `sdwa5-vps`.

## A combination that is more revealing than its parts

[`services.md`](services.md) documents the Vaultwarden accounts with their KDF, item count, last
activity and organization role. Only the Owner is named; the others are deliberately written as
"second account", "third account" and "fourth account", so somebody already thought about this.

What is left is that the table states an active account holds a number of items on the **weaker** KDF while
the Owner is on Argon2id. Published next to a named, reachable `vault.sdwa5.org`, that tells a reader
where the soft target is and roughly what it is worth. And there are only four accounts against three
named board members in [`organization.md`](organization.md), so the anonymisation is thinner than it
looks.

Nothing here is a credential and the finding is the pairing rather than either file.

**Done on 2026-09-12.** The per-account KDF and item counts are out of the table and one sentence is
left, that three accounts are on PBKDF2 and only their holders can change that. Upgrading those three
to Argon2id would be the real remedy and would make the old figures describe a state that no longer
exists, but it depends on the account holders, so publication cannot wait on it. The values are still
in 23 of this repository's commits and go with the outstanding rewrite named at the top.

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

**Decided on 2026-09-12 and applied to all three repositories.** MIT in `LICENSE` for the code and
configuration, CC BY-SA 4.0 in `LICENSE-docs` for the prose, documentation and data, with each
`README.md` naming which directories fall on which side. Two carve-outs are stated rather than left
implied: `sdwa5-vps/shopware-html-data/` is store-installed plugin content under its vendors' own
terms, and any mesh a `sdwa5-3d` spec reaches through `mesh_override` is third-party CAD, deliberately
uncommitted, with its provenance recorded in that repository's `docs/sources.md`.

## What is left to do

The credential scan is done and gated in CI, and the commit identities were rewritten on 2026-09-08.

**The work items are done.** The commit identities were rewritten on 2026-09-08 and the private email
address was rewritten out of `sdwa5-vps`'s file contents on 2026-09-12.

**The move is done too.** On 2026-09-12 the three repositories were pushed into fresh, empty
repositories in the [SdWa5](https://github.com/SdWa5) organization and the personal originals were
deleted, which removed GitHub's cache of both rewrites' pre-rewrite commits. They are
[docs](https://github.com/SdWa5/docs), [vps](https://github.com/SdWa5/vps) and
[3d](https://github.com/SdWa5/3d), and all three are still **private**.

**Every decision on this list is now made**, on 2026-09-12. The address stays because the Impressum
publishes it by law, the `c/o <name>` prefix went with it. Two board members' names defer to the ZVR
register and the Obmann's stays, because his Impressum names him. The former board member is gone. The
Vaultwarden posture is thinned to one sentence. The Minecraft pseudonyms stay, being low sensitivity
and all-or-nothing. The licence is MIT plus CC BY-SA 4.0. The third-party gear figures are cleared by
their owners.

**One work item is left, and it is the only thing here that cannot be done after publication.** The
names came out of the trees and are still in the histories: the two Obmann-Stellvertreter in 32
of this repository's 37 commits and 95 of `sdwa5-vps`'s 115, the former Obmann-Stellvertreterin in 32 of this
repository's, and the Vaultwarden values in 23. A rewrite over both repositories is prepared but was
refused by the environment's `[Git Destructive]` guard, so it needs a hand. `SdWa5/3d` needs nothing.

After that, the flip to public is one switch per repository, and it is also what gives CI its minutes
back.

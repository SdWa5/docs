1. improve docs [docs](docs)
    1. keep docs split by topic — one service/topic per file (like docs/shopware/); split future files if they grow too
       big
2. [sdwa5-vps/TODO.md](sdwa5-vps/TODO.md)
3. [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
4. Cleanup and refresh Google Drive together with this repo and all sub repos
    1. the account's My Drive root holds **four files all named `AmpLimiterCalc.csv`**, re-measured 2026-09-08 with
       three distinct sizes, 7700, 7718 and 7432 bytes with the last appearing twice at the same timestamp. So they
       are **hand-kept versions rather than redundant copies**, and only one pair is a true duplicate. Reconciling
       them is a reading job rather than a delete. `Audio Routing.xlsx` sits there too rather than in the shared
       drive, which is why the `SdWa5:` rclone remote cannot see it without a `--drive-team-drive ""` override.
       Deleting or renaming anything needs a write scope, since that remote is `scope = drive.readonly`. See `SIG-1`
       in [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
5. Mapping engine inspired by Mapshroom and Resolume, possibly as a new sibling repository
    1. Resolume's UI does not suit us, and Mapshroom is only a simple vibe so far. The goal is a powerful engine of
       our own that covers most of Resolume's features. Decide first between a new UI on top of Resolume and a
       rebuild in the spirit of Mapshroom that grows those features.
    2. The first USP is a video feedback loop that gives at least what Mapshroom offers. A camera makes a simple 3D
       scan of the whole venue. The camera is then mounted onto the projector, and the software picks fixed
       reference points, using the projector's own light as a helper. While the mapping runs, the camera feed stays
       on as the correction source.
    3. The second USP is a doubled perspective correction for real 3D immersion. The first pass uses the video
       feedback to put the pregenerated or live generated scenes as exactly as possible onto their faces, for
       example deco panels or the white top speakers of our friends. The second pass corrects the rendering
       perspective of the 3D content so it looks true from the crowd's point of view.
    4. The engine has to be as hardware efficient as possible and is at the same time a webserver, so a browser or a
       phone can control it.
    5. The stack is still open, because a real-time GPU video pipeline lies outside the PHP default. Check whether
       the browser control can reuse the approach of the `sdwa5-dsp` browser editor.
6. Pass the Statutenänderung drafted in [docs/statuten-entwurf.md](docs/statuten-entwurf.md)
    1. Invite to the Generalversammlung at least one week ahead, in writing and digitally, with the full draft on
       the agenda (§ 8 Abs. 3 and 5). The filed statutes still apply to this GV and have no VirtGesG clause, so it
       has to meet in person; the online rules of § 16 apply only from the following GV. An informal pre-check of the draft by the BH Braunau before the invitation
       would be a proposal. After the two-thirds resolution, notify the BH Braunau, at roughly 21 € plus 6 € per
       page. The latest sensible date is the Generalversammlung that re-elects the Vorstand before the current
       Funktionsperiode ends on 2027-10-26.
    2. Deferred: elect at least one Rechnungsprüfer outside the Vorstand. Both auditors hold Vorstand roles today,
       which § 13 Abs. 1 and § 5 Abs. 5 VerG rule out, and the Verein accepts it for now because of its size.
    3. Found a German sister e.V. once there are enough members in Germany. § 4 Abs. 1 VerG requires an Austrian
       Sitz, so it cannot be a Zweigverein; the draft's § 1 Abs. 3 allows cooperation and membership instead.
    4. Check whether a liability insurance is worth it. Under § 24 Abs. 7 VerG it covers the indemnity an unpaid
       Vorstand member can claim from the Verein for damages owed to third parties.
    5. Check whether the notification of the new Zustellanschrift under § 14 Abs. 3 VerG was filed, and whether the
       Impressum, Datenschutz and AGB pages, Dolibarr, Google Workspace, PayPal and the domain registrant carry the
       new address. The repository has no record of the filing, the four weeks from 2026-09-14 ended on
       2026-10-12, and the 0.10.0 changelog listed all those places as still showing the old address.
    6. Once the amendment is registered, replace [docs/statuten.md](docs/statuten.md) with the new text and delete
       the draft. Move the competent authority in [docs/organization.md](docs/organization.md) to the
       BH Salzburg-Umgebung and update its key points, and change the AGB place of jurisdiction to Hof bei Salzburg
       ([sdwa5-vps/docs/shopware/shop-config.md](sdwa5-vps/docs/shopware/shop-config.md)).

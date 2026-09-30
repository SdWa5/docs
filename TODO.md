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
       the browser control can reuse the approach of the `trackdsp` browser editor.

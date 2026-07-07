1. improve docs [docs](docs)
    1. infrastructure diagram — one overview graphic (Caddy → containers, domains, backup flow) in
       [sdwa5-vps/docs/infrastructure.md](sdwa5-vps/docs/infrastructure.md); mermaid renders on GitHub natively
        1. check documentation on freshness and consistency before
    2. TODO format consistency — TODO.md files use numbered lists, docs use `- [ ]` checkboxes — unify
       (checkboxes show progress on GitHub)
    3. link check CI — GitHub Action (e.g. `lychee` or `markdown-link-check`) validates relative links + anchors in
       both repos; cross-repo links like `../sdwa5-vps/docs/...` break silently otherwise
    4. keep docs split by topic — one service/topic per file (like docs/shopware/); split future files if they
       grow too big
2. go public with all sdwa5 repos
    1. github account/org plan (DECIDED)
        1. create GitHub Organization `sdwa5` + admin account on @sdwa5.org
           (domain already wired to google workspace)
            1. use role address (e.g. git@sdwa5.org)
            2. apply for GitHub non-profit discount
        2. then: transfer both (all sdwa5) repos into the org
            1. Scan content for sensitive stuff (guideline: No security by obscurity) and decide transfer method
            2. bestcodename/sdwa5-vps (https://github.com/bestcodename/sdwa5-vps/) -> sdwa5/vps
            3. bestcodename/sdwa5 (https://github.com/bestcodename/sdwa5) -> sdwa5/docs
    2. configure repos as public
3. [sdwa5-vps/TODO.md](sdwa5-vps/TODO.md)

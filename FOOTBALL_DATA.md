# Historical draft data

The draft contains 10 curated club-season pools and 129 unique player identities.
These are eligible selections, not exhaustive first-team squad lists. A player
must have played for that club during the specified season; domestic cup
appearances count. January arrivals such as Reyes and Pandev are eligible.

Each round draws one club-season with enough undrafted players for every manager.
The player card exposes only that season. The draft handler independently derives
the edition from the drawn squad, so changing a select element cannot select an
unrelated version. A player identity can still be drafted only once across all
managers. January market editions also use these explicit club-season ratings.

Pool counts and setup validation use eligible historical players. Categories
without enough players and a reserve for complete rounds cannot start; they
never fall back to an all-era fantasy squad. With the current coverage, World Cup,
European Championship and Ballon d'Or categories cannot support two full XIs.

## Ratings

Ratings are manually curated retrospective game estimates on a 72–99 scale,
not official EA ratings, scraped match ratings, or a statistical model. The
assessment considers production relative to position, influence and minutes,
defensive/goalkeeping contribution, contemporary individual recognition, and
that season's standing. Team trophies provide context rather than an automatic
boost. No nearest-season edition, blanket scaling or career-peak rating is used.

- 97–99: exceptional all-time individual seasons.
- 93–96: leading world-class seasons and major individual award contenders.
- 88–92: elite starters and outstanding contributors.
- 82–87: strong contributors, with role and availability reflected.
- 72–81: developing or limited-impact seasons.

Examples: Ronaldo is 98 for United 2007–08 and 96 for 2008–09; Benzema is 84
for Madrid 2017–18; Fàbregas is 72 for Arsenal 2003–04. The 2008 Ballon d'Or was
awarded during 2008–09, principally recognizing Ronaldo's 2007–08 achievements.
Both United seasons are available, as distinct editions of the same identity.

## Reference material

- UEFA Champions League finals handbook: historical finalists, lineups and player appearances:
  https://editorial.uefa.com/resources/0282-18407a7a3056-fed61d05639b-1000/ucl_202223_finals_md13.pdf
- Barcelona's 2010–11 archive:
  https://players.fcbarcelona.com/en/chronology/2010
- Premier League registered squads, 2018–19:
  https://www.premierleague.com/en/news/844127
- UEFA on Ronaldo's 2008 Ballon d'Or and 42-goal campaign:
  https://www.uefa.com/uefachampionsleague/news/01d4-0e707fe4919f-772c18bc5bc3-1000--ballon-d-or-crowns-ronaldo-s-golden-year/
- Manchester City's 2022–23 annual report: production and individual recognition:
  https://www.mancity.com/annualreport2023/mens-team/
- UEFA on Ribéry's 2012–13 Best Player in Europe award:
  https://www.uefa.com/uefachampionsleague/news/0250-0c50fe103b73-0fcc5456ac81-1000--ribery-is-crowned-uefa-best-player-in-europe/
- Premier League 2004–05 season review:
  https://www.premierleague.com/en/news/59017

The sources inform historical context; the exact numerical ratings are editorial
judgments and can be adjusted in each squad's explicit `ratings` map.

## Verification

Run `python3 tests/check_football_draft.py` on macOS (uses system JavaScriptCore).
It exercises all enabled manager/category combinations through randomized complete
drafts, rejects unrelated editions and ineligible players, checks known roster
anachronisms, runs a full season with January transfers, and verifies local real
badge coverage and PNG signatures. Browser rendering is not covered by this check.

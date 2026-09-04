# The Automated Ads Market — Who's Building the AI That Runs Meta, Google and TikTok Ads

**Research date: 3 September 2026.** Scope: software that helps businesses create, launch and optimize paid advertising on Meta, Google, TikTok and adjacent platforms using AI. Segmented by customer type, then extended to the adjacent layers advertisers depend on. ~123 companies with funding, valuations, founders, scale and ad-library links.

**How to read the numbers.** Figures marked "est." come from Latka, Tracxn, Growjo or PitchBook and are modelled, not disclosed. Figures without that label come from company announcements, press releases, SEC filings or credible press. Where sources conflict, both are shown. "n/a" means not found, never guessed.

---

## 1. Executive summary — the market cut by who the buyer is

Product categories are the wrong lens for a build-or-invest decision, because several products serve totally different buyers with totally different economics. Cut by **who actually opens the tool**, the market resolves into four cohorts.

| Cohort | Who the user is | Cohort size | Willingness to pay | Verdict |
|---|---|---|---|---|
| **1. Owner-operator** | The business owner is the media buyer | ~10M Meta + ~7M Google advertisers; SMBs = 27% of US digital ad spend (~$225B) | $27–$500/mo | Avoid as a standalone product |
| **2. In-house growth team** | Professional media buyer / creative strategist | DTC brands at $50K–$5M/mo spend | $1K–$10K/mo, multiple tools | **Best risk-adjusted** |
| **3. App UA manager** | Quantitative UA team | $94B global app install spend (2026) | Media-scale budgets | Closed to newcomers |
| **4. Enterprise & agency** | Marketing ops, agency teams | Most of the $836B digital market; retail media $200.4B | $100K–$1M+/yr | Defensible in the agency slice |

### Cut 1 — The owner-operator

- **User:** The business owner *is* the media buyer
- **Cohort size:** ~10M active advertisers on Meta, ~7M on Google Ads. SMBs are 27% of the US digital ad market — roughly **$225B of US spend**, growing 22% in 2025.
- **Willingness to pay:** $27–$500/month. No expertise, no time, no dedicated marketer.
- **Top players:** Meta Advantage+ (free, and the default), LocaliQ/WordStream, Podium ($3B), Birdeye, Blaze, Kliken (embedded in Wix/WooCommerce), Eulerity (franchise), Plai, Ryze, AdAmigo
- **Verdict:** **Worst unit economics in the market.** Huge logo count, tiny ACV, savage churn. Every venture-backed pure-play here is stuck under $5M ARR. Meta's URL-plus-budget product lands directly on this cohort around Q4 2026, for free.

### Cut 2 — The in-house growth team

- **User:** A professional media buyer or creative strategist
- **Cohort size:** DTC and consumer brands spending $50K–$5M/month. The core of Meta and TikTok direct-response revenue; TikTok alone is ~$44B globally.
- **Willingness to pay:** $1K–$10K/month, and they buy several tools at once.
- **Top players:** Motion (~$50M ARR), Foreplay, Atria, Superads, Triple Whale, Northbeam, Haus, Prescient AI, Madgicx, Arcads ($15M ARR), Creatify, AdManage.ai
- **Verdict:** **The best risk-adjusted cohort.** Sophisticated buyers with existing budget and low education cost. Creative volume is a permanent constraint the platforms do not solve — they redistribute your assets, they do not invent concepts. Motion reached ~$50M ARR on $42M raised; Arcads ~$15M ARR reportedly with eight people.

### Cut 3 — The app UA manager

- **User:** A quantitative user-acquisition team
- **Cohort size:** **$94B of global app install spend in 2026**, up from $81B in 2025. Non-gaming grew 18% to $53B. iOS CPI $5.84, Android $1.92.
- **Willingness to pay:** Six to eight figures of annual spend, bought as media not software.
- **Top players:** AppLovin AXON (~$104B market cap), Moloco (~$400M revenue), Liftoff ($4.3B, IPO filed), AppsFlyer ($1B Series E), Adjust, Branch, Remerge, Bidease
- **Verdict:** **Effectively closed.** Winner-take-most, decided by data scale and network effects. A new entrant without proprietary inventory or a supply-side asset has no wedge.

### Cut 4 — The enterprise brand & agency

- **User:** Marketing ops, agency account teams, procurement
- **Cohort size:** The majority of the $836B digital ad market by value. Retail media alone is **$200.4B in 2026**, +17.6% YoY, heading to $312B by 2030.
- **Willingness to pay:** $100K–$1M+ per year, long cycles, heavy governance requirements.
- **Top players:** Smartly ($101M ARR), Skai, Pixis, StackAdapt ($500M+ revenue), Fluency ($3B spend under management), Adobe GenStudio, VidMob, Celtra, The Trade Desk, Zeta Global
- **Verdict:** **Slow, sticky, and PE roll-up territory.** But the agency sub-segment is genuinely defensible: the platforms will never build well for agencies, because agencies are precisely who platform automation is designed to disintermediate.

### A fifth, smaller cut worth knowing

**B2B demand generation.** US B2B digital ad spend is only ~$19–23B, and LinkedIn ad revenue is ~$9.7–11.4B depending on the source (WARC and other trackers disagree materially). Small, but the least AI-disrupted cohort in the report, because the hard problem is identity and intent data rather than creative generation. Players: Metadata.io, Influ2, Primer, HockeyStack, Dreamdata, RollWorks, Demandbase, 6sense.

### Where a new player should play

**Build for Cut 2, and specifically in the creative supply chain rather than the analytics layer.**

The reasoning is the three-vector test from the seed-tier section. Creative volume is the only input the platforms structurally cannot supply: Advantage+ and Performance Max redistribute the assets you give them, they do not originate concepts, actors or campaigns. It is also the one thing a general-purpose assistant cannot do from a chat window. And the buyer already has budget and needs no education.

The evidence backs it. Motion reached ~$50M ARR on $42M raised. Arcads reached ~$15M ARR, profitable, reportedly with eight people. HeyGen reached $200M ARR having burned ~$25M. Capital efficiency in this cohort is the best in the dataset.

The caution: the *analytics* half of Cut 2 is crowding fast — Motion, Foreplay, Atria and Superads are converging on the same buyer — and analytics is exactly what an assistant absorbs first. Sell production and rights, not dashboards.

**The contrarian alternative: sell to the retailer, not the advertiser.** The fastest-growing line in this entire report is retail media at $200.4B and +17.6% YoY, and the tooling that lets a retailer run its own network is strikingly under-built. Koddi bootstrapped to $28.2M ARR with no outside capital; Topsort raised $43.2M at a $150M valuation. Every mid-size retailer, marketplace and delivery app now wants an ad business and cannot build the auction themselves. That is a picks-and-shovels position with an enterprise buyer, and it is not on the path of Meta's roadmap at all.

**What to avoid:** a standalone SMB ad tool (Cut 1) unless you already own distribution — the Podium and Kliken model of embedding where the SMB already works, with ads as a feature rather than the product. And app UA (Cut 3) without proprietary inventory.
---

## 1. The one fact that governs this entire market

The platforms are absorbing the product.

| Platform signal | Figure | Date |
|---|---|---|
| Meta Advantage+ annual revenue run rate | $75B+ | Q2 2026 |
| Meta small businesses using a generative-AI creative tool | 9M+ | Q2 2026 |
| Meta ad revenue, quarter | $59.4B, +27% YoY | Q2 2026 |
| Google advertisers on Performance Max | 1M+, 71% of all advertisers (75% US) | 2026 |
| TikTok global ad revenue | ~$44B | 2026 |
| AppLovin market cap / TTM revenue | ~$104B / $6.83B | Jun 2026 |
| AI-controlled ad spend, US | $35B (8% of ad revenue) → $142B (26%) | 2025 → 2030 |

Mark Zuckerberg's stated 2026 goal is that a business supplies a URL, a budget and a bank account, and Meta generates the image, video and copy, picks the audience, allocates the budget and reports the result. Public launch is expected around Q4 2026. Google is auto-upgrading Dynamic Search Ads to AI Max from September 2026. TikTok wired Symphony's creative automation directly into Smart+ buying in April 2026. AppLovin opened its AXON self-serve engine to all global advertisers in June 2026, aiming at a retail ad market it sizes near $170B.

Creative generation, audience targeting and budget optimization — the three things most third-party tools charged for — are becoming free platform features. Marin Software, once a Nasdaq-listed leader in search ad management, approved a plan of dissolution in April 2025, was delisted in June and sold its assets for $5.5M in a Chapter 11 process. That is the base case for undifferentiated tooling.

Five positions survive because the platforms structurally cannot or will not build them:

1. **Cross-platform.** Meta will never optimize your TikTok budget against your Meta budget.
2. **Creative volume and originality.** Platforms remix your assets. They do not invent concepts, actors or campaigns.
3. **Independent measurement.** A platform grading its own homework is a permanent conflict of interest.
4. **Workflow, governance and scale.** Bulk launch, QA, approvals, multi-account and multi-client agency operations.
5. **Embedded and vertical distribution.** Merchants inside Shopify or WooCommerce, and franchise networks, that platform self-serve funnels do not reach.

---

## 2. Market map by category

### A. SMB and self-serve ad management

Tools a small business or small agency buys directly, usually under $500/month.

| Company | HQ | Founded | Raised | Valuation | Revenue | Status |
|---|---|---|---|---|---|---|
| [AdCreative.ai](https://www.adcreative.ai) | Paris | 2021 | undisclosed seed | $38.7M exit | €24.3M (2024) | Acquired by Appier, Mar 2025 |
| [Optmyzr](https://www.optmyzr.com) | Palo Alto | 2013 | $0 bootstrapped | n/a | $14.6M ARR (2023); $23.9M (2026, unverified) | Independent |
| [Madgicx](https://madgicx.com) | Tel Aviv | 2018 | ~$0 (disputed) | $20.5M est. | $6.8M ARR est. | Independent |
| [Opteo](https://opteo.com) | London | 2013 | $0 bootstrapped | n/a | $3.6M ARR est. | Independent |
| [Bïrch (ex-Revealbot)](https://bir.ch) | Barcelona | 2016 | $0 bootstrapped | n/a | $2.8M ARR est. | Independent |
| [Adzooma](https://www.adzooma.com) | Nottingham | 2015 | $14.5M (unverified) | n/a | $2.5M ARR est. | Independent |
| [Zocket](https://zocket.com) | SF / Chennai | 2021 | $3.47M | n/a | n/a | Independent |
| [Blaze.ai](https://www.blaze.ai) | San Francisco | 2023 | ~$45–50M via Almanac | n/a | $7M ARR (Mar 2025) → ~$10M | Independent |
| [Hunch](https://www.hunchads.com) | New York | 2017 | ~$4.3M | $25.7M est. | $8.6M ARR est. | Independent |
| [Alison.ai](https://alison.ai) | Tel Aviv | 2021 | $18.4M | n/a | $7.9M ARR est. | Independent |
| [WordStream / LocaliQ](https://localiq.com) | New York | 2007 | — | $150M exit | ~$450M+ annualized segment | Gannett (NYSE: GCI) |
| [Kliken](https://www.kliken.com) | Tampa | 2007 | $14.5M | n/a | $2.1M ARR est. | Independent |
| [Adext AI](https://adext.ai) | Palo Alto | 2016 | $3–8M | $20M (2016) | $1.3M (2024) | **Ceased operations 2024** |

The pattern is stark. Bootstrapped incumbents (Optmyzr, Opteo, Bïrch) run profitably at $3M–$24M. Every venture-backed pure-play SMB self-serve tool is stuck under $5M ARR. The two largest outcomes both came from leaving the category: WordStream sold into a local-media roll-up, AdCreative.ai sold into an ad-tech acquirer.

Notable founders here: **Frederick Vallaeys** (Optmyzr) was one of Google's first 500 employees and spent a decade on AdWords, including Quality Score and the founding AdWords Editor team. **Larry Kim** built WordStream to $55M+ revenue and a $150M exit to Gannett. **Karthik Venkateswaran** (Zocket) previously built GoBumpr to 400+ staff and sold it to TVS. **Adam Nathan** (Blaze) has a Duke and Harvard MBA background and pivoted Almanac, which had raised a $34M Series A from Tiger Global, into Blaze, reaching roughly $10M revenue in about 18 months.

### B. Generative-AI ad creative and UGC video

The fastest-growing and best-funded part of the market.

| Company | HQ | Founded | Raised | Valuation | Revenue | Status |
|---|---|---|---|---|---|---|
| **[Higgsfield AI](https://higgsfield.ai)** | San Francisco | 2023 | ~$530M+ | **$5.4B** (Aug 2026) | **~$700M annualized** (Jul 2026) | Independent |
| **[HeyGen](https://www.heygen.com)** | Los Angeles | 2020 | $74.6M | $500M (2024) | **$200M ARR** (Jun 2026) | Independent |
| [Mirage (ex-Captions)](https://captions.ai) | New York | 2021 | $175M+ | $500M (2024) | $28.4M in-app (TTM) | Independent |
| **[Motion](https://motionapp.com)** | Toronto | 2021 | $42M | n/a | **~$50M ARR** (Aug 2025) | Independent |
| [Waymark](https://waymark.com) | Detroit | 2014 | $129M | n/a | n/a | Independent |
| [Creatify](https://creatify.ai) | Mountain View | 2023 | $23M | n/a | $9M ARR (May 2025) | Independent |
| [Arcads](https://www.arcads.ai) | Paris | 2024 | $16M | n/a | **$15M ARR** (Apr 2026), profitable | Independent |
| [Pencil](https://www.trypencil.com) | London | 2018 | ~$2.8M pre-exit | undisclosed exit | $23M ARR est. | Brandtech Group, 2023 |
| [Omneky](https://www.omneky.com) | San Francisco | 2018 | $13M+ | $80M (StartEngine 2025) | $8.3M ARR est. | Independent |
| [Marpipe](https://www.marpipe.com) | New York | 2019 | $10.9M | n/a | n/a | Independent |
| [Poolday.ai](https://poolday.ai) | Paris | 2023 | $8.7M | n/a | $1.4M ARR | Independent |
| [Foreplay](https://www.foreplay.co) | Toronto | 2021 | $0 bootstrapped | n/a | $1.2M ARR est. | Independent |
| [VidMob](https://vidmob.com) | New York | 2015 | $208.9M | $54.8M est. | $18.3M ARR est. | Independent |
| [Icon](https://icon.com) | New York | 2024 | $9.2M | n/a | $5M ARR claimed | **Collapsed, then pivoted to a human ad agency** |

Higgsfield quadrupled its valuation in eight months, from $1.3B in January 2026 to $5.4B in August 2026 on a $400M Series B, with roughly $700M annualized revenue and 30M users. HeyGen is the capital-efficiency standout: $200M ARR having burned only about $25M of $74M raised, roughly $2.70 of ARR per dollar of equity — better than Zoom or Datadog at IPO.

At the opposite end, VidMob has raised $208.9M against an estimated $18.3M ARR and a Latka-implied valuation of $54.8M. That is a down-round profile.

### C. Enterprise and mid-market cross-channel platforms

| Company | HQ | Founded | Raised | Valuation | Revenue | Status |
|---|---|---|---|---|---|---|
| [StackAdapt](https://www.stackadapt.com) | Toronto | 2014 | $537M | **$2.5B** (Feb 2025) | **$500M+** | Independent |
| [MNTN](https://mountain.com) | Austin | 2009 | IPO May 2025 | ~$886M market cap | $290.1M FY2025, +28.6% | Public (NYSE: MNTN) |
| [Smartly](https://www.smartly.io) | Helsinki | 2013 | $22.8M + €200M buyout | $299.3M est. | $101M ARR est. | Providence Equity |
| [Pixis](https://pixis.ai) | San Francisco | 2018 | $209M | n/a | n/a | Independent |
| [Skai (ex-Kenshoo)](https://skai.io) | Tel Aviv | 2006 | Sequoia, Bain-backed | n/a | $78.9M ARR est. | Independent |
| [Fluency](https://www.fluency.inc) | Burlington VT | 2017 | $40M | n/a | $3B media spend powered | Independent |
| [Persado](https://www.persado.com) | New York | 2012 | $120M+ | n/a | n/a | Independent |
| [VidMob](https://vidmob.com) | New York | 2015 | $208.9M | $54.8M est. | $18.3M ARR est. | Independent |
| [Celtra](https://celtra.com) | Boston | 2006 | $25.2M | n/a | n/a | Independent |
| [Albert.ai](https://albert.ai) | Israel | 2010 | — | asset sale | — | **Zoomd, Mar 2022** |
| [Marin Software](https://www.marinsoftware.com) | San Francisco | 2006 | was Nasdaq-listed | **$5.5M asset sale** | — | **Dissolved 2025** |

Fluency is the quiet outlier: profitable since 2020, bootstrapped to roughly $3B in annual media spend and 250,000 campaigns a month, then took a single $40M Series A from Integrity Growth Partners in December 2025.

### D. B2B advertising automation

| Company | HQ | Founded | Raised | Last round | Notes |
|---|---|---|---|---|---|
| [Metadata.io](https://metadata.io) | SF / Ramat Gan | 2015 | $58M+ | $40M Series B, Next47 | Autonomous B2B paid-social experiments |
| [HockeyStack](https://www.hockeystack.com) | Middletown DE | 2021 | $50M | $20M Series A, Bessemer, Jan 2025 | YC alumni, B2B revenue intelligence |
| [Dreamdata](https://dreamdata.io) | Copenhagen | 2018 | n/a | $55M, Oct 2025 | B2B attribution |
| [Primer](https://www.sayprimer.com) | San Francisco | 2020 | $12M+ | $12M Series A, Craft Ventures | B2B audience matching into ad platforms |
| [Influ2](https://www.influ2.com) | New York | 2017 | ~$11.4M | $8M Series A, Rally Ventures | Person-based advertising to named buyers |
| RollWorks (NextRoll) | San Francisco | 2007 | — | — | Native account-based advertising, ~$13–60K/yr |
| [Demandbase](https://www.demandbase.com) | San Francisco | 2006 | — | — | Mid-enterprise, ~$40–250K/yr |
| [6sense](https://6sense.com) | San Francisco | 2013 | — | — | Enterprise, ~$80K–$1M+/yr |

B2B is the least AI-disrupted segment, because the hard problem is identity and intent data, not creative generation. Meta's automation does not help you reach 40 named buyers at one target account.

### E. Ecommerce, marketplace, app and local

| Company | HQ | Founded | Raised | Valuation | Revenue | Status |
|---|---|---|---|---|---|---|
| [AppLovin](https://www.applovin.com) | Palo Alto | 2012 | public | **~$104B mkt cap** | $6.83B TTM | Public (Nasdaq: APP) |
| [Moloco](https://www.moloco.com) | Redwood City | 2013 | ~$500M | $1.5–2.0B | ~$400M (2025) | Independent |
| [Pacvue](https://pacvue.com) | Seattle | 2018 | **$0 — no VC** | nine-figure exit | n/a | Assembly, Oct 2021 |
| [Teikametrics](https://www.teikametrics.com) | Boston | 2015 | $65M | n/a | n/a | Independent |
| [Triple Whale](https://www.triplewhale.com) | Columbus | 2021 | $55.4M | n/a | $21.6M (2025) | Independent |
| [Northbeam](https://www.northbeam.io) | Los Angeles | 2019 | ~$30M | n/a | $25B ad spend tracked | Independent |
| [Proxima](https://www.proxima.ai) | New York | 2022 | $12M | n/a | 400%+ growth | Independent |
| [Eulerity](https://eulerity.ai) | New York | 2016 | n/a | n/a | n/a | Independent |

### F. The new agentic AI media buyers (2024–2026)

The ad-optimization AI category took $110.5M across five deals, at a median round of $20.5M.

| Company | Amount | Stage | Date | Lead | What it is |
|---|---|---|---|---|---|
| **MAI** | $25M | Seed | Oct 2025 | Kleiner Perkins | AI agents that run performance marketing for SMBs |
| Brandlight | $30M | Series A | Feb 2026 | n/a | AI-search brand visibility |
| Koah | $20.5M | Series A | Feb 2026 | Theory Ventures | Ads inside AI apps |
| [Bluefish](https://www.bluefishai.com) | $20M | Series A | Aug 2025 | NEA | Generative engine optimization, ~80% Fortune 500 |
| Spangle AI | $15M | Series A | Jan 2026 | Theory Ventures | n/a |

MAI is the purest expression of the thesis: agents that plan, launch and optimize campaigns autonomously, already managing millions of dollars of Google Ads spend per month and claiming 40% higher sales for ecommerce clients.

Incumbent platforms are shipping agents too. PubMatic's AgenticOS cut campaign setup time 87% in an early December 2025 deployment. In the week before Cannes Lions in June 2026, at least eight major platforms shipped autonomous buying agents or the infrastructure they need.


### The seed-stage agentic tier (2024–26)

The layer closest to an SMB typing a prompt and getting live campaigns. Mostly founded 2024–25, mostly under $25M raised, and the most exposed position in the whole market. Runable is the only one here with a disclosed valuation; five have no disclosed funding at all.

| Company | Raised | Valuation | Traction | Status | Ad libraries |
|---|---|---|---|---|---|
| [Runable](https://runable.com) | $21M Series A | $65M post-money (Aug 2026) | ~1.7M registered users; $2M ARR run rate within 3 weeks of launching payments | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Runable&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=runable.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Runable) |
| [Uplane](https://uplane.com) | $4.5M seed | n/a | Claims 30–60% ROAS uplift | Independent (YC F25) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Uplane&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=uplane.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Uplane) |
| [Pomo](https://usepomo.com) | $4.5M seed | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Pomo&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=usepomo.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Pomo) |
| [Sprites](https://sprites.ai) | $4.45M | n/a | Claims 20+ hours/week saved per team | Independent (YC W22) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Sprites&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=sprites.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=Sprites) |
| [Lapis](https://trylapis.com) | ~$0.5M–$1M (sources differ) | n/a | 1,500+ marketing teams, 30+ enterprises, 10 languages | Independent (YC F25) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Lapis&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=trylapis.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Lapis) |
| [InstaAgent](https://instaagent.com) | n/a | n/a | $1M ARR in 10 months; 500+ clients in 10+ countries | Independent (YC P26) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=InstaAgent&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=instaagent.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=InstaAgent) |
| [Plai](https://plai.io) | $125K (YC) | n/a | From $27/mo; $297/mo white-label | Independent (YC S21) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Plai&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=plai.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Plai) |
| [Gooseworks](https://gooseworks.ai) | n/a | n/a | 200+ paying users; 30,000+ creatives generated in two months | Independent (YC W23) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Gooseworks&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=gooseworks.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=Gooseworks) |
| [AdAmigo.ai](https://adamigo.ai) | n/a | n/a | 700+ brands and agencies; claims ~28% average lift in month one | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AdAmigo.ai&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=adamigo.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=AdAmigo.ai) |
| [AdStellar](https://adstellar.ai) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AdStellar&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=adstellar.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=AdStellar) |
| [Revnu](https://revnu.com) | n/a | n/a | n/a | Independent (YC P26) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Revnu&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=revnu.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Revnu) |
| [Hyper](https://hyper.inc) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Hyper&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=hyper.inc) · [LI](https://www.linkedin.com/ad-library/search?keyword=Hyper) |
| [Ryze AI](https://get-ryze.ai) | $0 — never raised | n/a | Claims 2,000+ clients, 700+ agencies, $500M+ ad spend managed | Independent — pivoting | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Ryze%20AI&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=get-ryze.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=Ryze%20AI) |

- **Runable** — Co-led by Susquehanna Venture Capital and Nexus Venture Partners with Together Fund and Array VC. Indian, founded 2025, pivoted from browser/scraping tech. A general business agent — sites, apps, decks, prospect lists, marketing videos — where ads are one surface of growth, not the whole product.
- **Uplane** — Seed led by Play Ventures with YC, 20VC, Rebel Fund and Multimodal Ventures. Founded 2025 by Julius Körfgen (CEO), Lukas Vollmer and Marvin Abdel-Massih — Körfgen led growth and Abdel-Massih was Chief of Staff at Enpal, the German greentech unicorn. Generates hundreds of ads with matching landing pages and steers spend across Meta, Google and LinkedIn using CRM and ERP data.
- **Pomo** — Launched April 2026. Kindred Ventures led, with Databricks Ventures, SV Angel, Seven Stars, Timeless Partners and 645 Ventures; angels include Scott Belsky. Founders Praneet Dutta (CEO, ex-Google DeepMind) and Joe Cheuk (CTO, ex-Google/Databricks). Watches your campaigns alongside competitors' and returns briefs — decision support rather than autonomous buying.
- **Sprites** — San Francisco, founded 2021. Ride Home Fund and Cathexis Ventures among nine investors. Ads plus SEO agent across Meta, Google, LinkedIn, Reddit and TikTok via a natural-language interface.
- **Lapis** — Five people in San Francisco. Builds, launches and scales paid campaigns end-to-end for DTC and SaaS — copy, images, landing pages, optimization. Founders Varunram Ganesh (CEO, ex-Head of Growth at Warp, scaled it to $2.5M revenue; bitcoin research at MIT Media Lab) and Sai Surbehera (CTO, ex-ML at Walmart Tech).
- **InstaAgent** — Scales one campaign across hundreds of personas on Meta and TikTok, each with its own content, voice and targeting. Co-founders Kyle Wong (CEO — eight years at Goldman Sachs covering China TMT, and previously co-founded a gaming startup that onboarded 1M+ users in a month) and Colin Tseung, friends since middle school.
- **Plai** — Founded by Logan Welbaum. The cheapest entry point in the category — create, launch and optimize across Facebook, Google, LinkedIn and TikTok. The oldest of this cohort and a useful counter-example: four years in, still tiny.
- **Gooseworks** — Founded 2022 by Himanshu Bamoria and Shiv Sakhuja; five people in San Francisco. An AI creative engine that indexes existing brand material — videos, product shots, testimonials, past ad performance — into a continuous stream of short-form video ads for Meta and TikTok.
- **AdAmigo.ai** — Three agents — Action for budget, Ads for creative, Chat for ops. An official Meta Business Technology Partner, which matters for API stability. Built by media buyers who say they have spent $300M+ on ads.
- **AdStellar** — Generates image, video and UGC-style avatar creative from a product URL, clones competitor ads out of the Meta Ad Library, and pushes them into a campaign in one pass.
- **Revnu** — Runs an entire go-to-market motion — outbound, ads, SEO and social — for founders who would rather not hire. Ads are one channel among several.
- **Hyper** — Runs Meta and Google as a single agent rather than two disconnected tools, extending to TikTok and Amazon, and reports blended ROAS across them. Sourced from a third-party comparison rather than the company, so treat the detail as unverified.
- **Ryze AI** — San Francisco, operated by Meow AI, LLC; $89/month flat. Audits campaigns, reallocates budget, rotates creative and reports across Google, Meta and SEO. **Founder attribution conflicts:** press names Ira Bodnar, Tracxn lists Ramazan Rakhmatullin, and the company's own About page names neither. See the case study below.

**On completeness:** this tier cannot be enumerated exhaustively. Most of these companies are too small for the funding databases, several have raised nothing, and the cohort turns over in months. This list was built from the Y Combinator company directory (which yields batch labels), funding trackers, and practitioner comparison round-ups — so it is biased toward YC and toward companies that announced a raise. Bootstrapped tools and non-US startups are certainly under-represented. Names welcome; that has already worked better than my searches.

Also adjacent but excluded on scope: **Adalysis** (established Google Ads RSA testing, from ~$149/mo, not an AI-native startup) and **Kular** (YC W22 — AI lead generation over email and LinkedIn, not paid ads).

#### Case study: the squeeze arriving from a direction nobody priced in

In February 2026 Ryze's founder posted that **"Claude just killed our startup."** After Anthropic and Manus shipped features that overlapped Ryze's product, the company's deal close rate fell from roughly **70% to 20%** within months of launch. The founder noted that Claude could analyze ad data but could not yet act inside a Google Ads account, and expected that to change within months. Ryze is pivoting toward complex AI workflows for large agencies.

This revises the thesis in this report. I framed the threat as the ad platforms absorbing third-party features. Ryze was not killed by Meta or Google. It was killed by a **general-purpose AI assistant** — and the assistant did not even need write access to ad accounts to destroy the sales motion; the expectation of it was enough.

So there are three squeeze vectors, not two:

1. **The ad platforms** absorb creative, targeting and bidding into free features (Advantage+, Performance Max, Smart+).
2. **General-purpose assistants** absorb the analysis, reporting and recommendation layer — the thin-wrapper business — before they can even execute.
3. **The channel owners** buy the remaining independents outright (Walmart/Vibe.co at $1.4B, DoubleVerify/Rockerbox and Scibids, Smartly/INCRMNTAL).

In candor: I am Claude, so the second vector is one I am part of. It does not change the finding, and the honest read is that a tool whose value is *"we look at your ad data and tell you what to do"* has the shortest remaining runway of anything in this report. What survives is what an assistant cannot do from a chat window — hold write access and accountability for spend, generate volumes of original creative, run independent measurement, or own distribution the assistant cannot reach.

Within this cohort that test separates them cleanly. **Uplane, Lapis, InstaAgent, Gooseworks and AdAmigo** hold write access, produce creative, or own a channel relationship. **Pomo, and much of Sprites and Ryze**, sit on the advice side of the line.

### G. The platforms themselves

Meta Advantage+, Google Performance Max and AI Max, TikTok Smart+ and Symphony, Amazon's ad AI, and AppLovin AXON. These are not competitors to the startups in one segment. They are the substrate, and they are moving up the stack every quarter.

---

## 3. Ad library links

Meta ad library, Google Ads Transparency Center and LinkedIn ad library, for every company covered. Meta and LinkedIn links are keyword searches; Google links are advertiser-domain lookups.

| Company | Meta | Google | LinkedIn |
|---|---|---|---|
| [AdCreative.ai](https://www.adcreative.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AdCreative.ai&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=adcreative.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=AdCreative.ai) |
| [Madgicx](https://madgicx.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Madgicx&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=madgicx.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Madgicx) |
| [Optmyzr](https://www.optmyzr.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Optmyzr&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=optmyzr.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Optmyzr) |
| [Opteo](https://opteo.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Opteo&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=opteo.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Opteo) |
| Bïrch / Revealbot | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Birch%20Revealbot&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=bir.ch) | [ads](https://www.linkedin.com/ad-library/search?keyword=Birch%20Revealbot) |
| [Adzooma](https://www.adzooma.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Adzooma&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=adzooma.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Adzooma) |
| [Zocket](https://zocket.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Zocket&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=zocket.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Zocket) |
| [Blaze.ai](https://www.blaze.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Blaze.ai&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=blaze.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Blaze.ai) |
| [Hunch](https://www.hunchads.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Hunch%20Ads&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=hunchads.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Hunch) |
| [Alison.ai](https://alison.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Alison.ai&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=alison.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Alison.ai) |
| LocaliQ / WordStream | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=LocaliQ&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=localiq.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=LocaliQ) |
| [AdManage.ai](https://admanage.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AdManage.ai&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=admanage.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=AdManage.ai) |
| [Kliken](https://www.kliken.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Kliken&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=kliken.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Kliken) |
| [Higgsfield](https://higgsfield.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Higgsfield&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=higgsfield.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Higgsfield) |
| [HeyGen](https://www.heygen.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=HeyGen&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=heygen.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=HeyGen) |
| Mirage / Captions | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Captions&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=captions.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Captions) |
| [Motion](https://motionapp.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Motion+app&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=motionapp.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Motion) |
| [Creatify](https://creatify.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Creatify&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=creatify.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Creatify) |
| [Arcads](https://www.arcads.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Arcads&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=arcads.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Arcads) |
| [Omneky](https://www.omneky.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Omneky&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=omneky.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Omneky) |
| [Pencil](https://www.trypencil.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Pencil%20AI&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=trypencil.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Pencil) |
| [Poolday.ai](https://poolday.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Poolday&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=poolday.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Poolday) |
| [Foreplay](https://www.foreplay.co) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Foreplay&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=foreplay.co) | [ads](https://www.linkedin.com/ad-library/search?keyword=Foreplay) |
| [Marpipe](https://www.marpipe.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Marpipe&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=marpipe.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Marpipe) |
| [Atria](https://www.tryatria.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Atria&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=tryatria.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Atria) |
| [Waymark](https://waymark.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Waymark&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=waymark.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Waymark) |
| [VidMob](https://vidmob.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=VidMob&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=vidmob.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=VidMob) |
| [Smartly](https://www.smartly.io) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Smartly&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=smartly.io) | [ads](https://www.linkedin.com/ad-library/search?keyword=Smartly) |
| [Skai](https://skai.io) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Skai&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=skai.io) | [ads](https://www.linkedin.com/ad-library/search?keyword=Skai) |
| [Pixis](https://pixis.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Pixis&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=pixis.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Pixis) |
| [Fluency](https://www.fluency.inc) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Fluency&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=fluency.inc) | [ads](https://www.linkedin.com/ad-library/search?keyword=Fluency) |
| [StackAdapt](https://www.stackadapt.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=StackAdapt&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=stackadapt.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=StackAdapt) |
| [MNTN](https://mountain.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=MNTN&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=mountain.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=MNTN) |
| [Persado](https://www.persado.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Persado&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=persado.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Persado) |
| [Metadata.io](https://metadata.io) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Metadata&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=metadata.io) | [ads](https://www.linkedin.com/ad-library/search?keyword=Metadata) |
| [Influ2](https://www.influ2.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Influ2&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=influ2.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Influ2) |
| [Primer](https://www.sayprimer.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Primer&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=sayprimer.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Primer) |
| [HockeyStack](https://www.hockeystack.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=HockeyStack&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=hockeystack.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=HockeyStack) |
| [Moloco](https://www.moloco.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Moloco&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=moloco.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Moloco) |
| [AppLovin](https://www.applovin.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AppLovin&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=applovin.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=AppLovin) |
| [Triple Whale](https://www.triplewhale.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Triple+Whale&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=triplewhale.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Triple%20Whale) |
| [Northbeam](https://www.northbeam.io) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Northbeam&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=northbeam.io) | [ads](https://www.linkedin.com/ad-library/search?keyword=Northbeam) |
| [Proxima](https://www.proxima.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Proxima&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=proxima.ai) | [ads](https://www.linkedin.com/ad-library/search?keyword=Proxima) |
| [Pacvue](https://pacvue.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Pacvue&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=pacvue.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Pacvue) |
| [Teikametrics](https://www.teikametrics.com) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Teikametrics&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=teikametrics.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Teikametrics) |
| [Eulerity](https://eulerity.ai) | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Eulerity&search_type=keyword_unordered) | [ads](https://adstransparency.google.com/?region=anywhere&domain=eulerity.com) | [ads](https://www.linkedin.com/ad-library/search?keyword=Eulerity) |
| MAI | [ads](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=MAI&search_type=keyword_unordered) | — | [ads](https://www.linkedin.com/ad-library/search?keyword=MAI) |

---

## 4. Founders — who I would bet on

My filter: a founder in this market is being graded on one question. **When Meta or Google ships your feature for free, do you still have a business?** Distribution, brand and even revenue are weak evidence. Prior experience of being run over by a platform, and a deliberate choice of ground the platform will not take, are strong evidence.

### Tier 1 — I would write the cheque

**Yuchen Wu — Co-founder & CEO, MAI.** [X](https://x.com/yuchen__wu) · LinkedIn profile not resolvable in a people database — deliberately not guessed
Ten years, 2010–2020, as an engineering director at Google building the advertising system. Then VP of Engineering at Instacart running logistics platform technology. Tsinghua bachelor's, Northwestern PhD. Co-founder Jian Wang is also ex-Google and ex-Instacart. Founded December 2024, raised $25M seed led by Kleiner Perkins by October 2025, already managing millions of dollars of Google Ads spend monthly.

Why I'd bet: this is the single best founder–market fit in the entire dataset. He spent a decade building the machine that everyone else is trying to out-guess from the outside. He knows exactly which parts of Google's auction are opaque, which levers still matter after automation, and where the residual alpha lives. When an advertiser asks "what can you do that Performance Max can't", he is one of a handful of people on earth who can answer from first principles. A $25M seed is a large bet on an unproven category, and the round size tells you Kleiner sees the same thing.

Risk: the SMB segment is where platform automation lands hardest and cheapest, and SMB churn is brutal. He is fishing in the most contested pond.

**Joshua Xu — Co-founder & CEO, HeyGen.**
CMU master's in CS, former lead engineer at Snapchat. $200M ARR as of June 2026, doubled in eight months, having burned roughly $25M of $74M raised. Roughly $2.70 of ARR per dollar of equity raised, better capital efficiency than Zoom or Datadog at IPO.

Why I'd bet: these are the best fundamentals in the entire market and it is not close. Growing at that rate while cash-flow break-even means the product sells itself and the unit economics work without a subsidy. HeyGen also sits on the right side of the platform question — Meta will generate variants of your existing assets, but it will not give you a consistent synthetic spokesperson in 40 languages. The moat is model quality plus an identity/likeness rights layer that is genuinely hard to replicate.

Risk: video model quality is converging fast, and the frontier labs are a real threat. The defensibility has to come from workflow and rights, not raw generation.

**Alex Mashrabov — Founder & CEO, Higgsfield AI.**
His mother designed rockets for the Soviet space program. He started programming at 10 and was ranked top-3 globally in competitive programming by 20. Co-founded AI Factory, which built on-device neural networks and was acquired by Snap for $166M in 2020; the technology became the backbone of Snapchat's face filters and Cameos. He then spent three years as Snap's Director of Generative AI, shipping MyAI and GenAI AR to hundreds of millions of users. Left in September 2023 to found Higgsfield with Yerzat Dulat (CTO, generative video researcher) and Mahi de Silva (CSO).

Why I'd bet on the person: a prior exit to a platform, then running generative AI inside that platform at consumer scale, is close to a perfect preparation for building consumer-scale generative video. The results back it: roughly $700M annualized revenue and 30M users, with valuation going $1.0B (Sept 2025) → $1.3B (Jan 2026) → $5.4B (Aug 2026).

The catch, and it is a real one: **the price**. At $5.4B on roughly $700M of consumption revenue, you are underwriting continued hypergrowth in a category where switching costs are low and credit-based revenue can decay as fast as it compounds. I would bet on Mashrabov the founder without hesitation. I would think hard before buying at this entry.

**Reza Khadjavi — Co-founder & CEO, Motion.** [LinkedIn](https://www.linkedin.com/in/reza-khadjavi-46802918/) · [X](https://x.com/rezakhadjavi)
The most instructive story in the whole market. He co-founded Shoelace in 2015, one of the first apps to automate Facebook advertising for Shopify merchants. In 2018 Facebook and Shopify deepened their direct integration and eliminated the gap Shoelace existed to bridge. In his words: "The writing was on the wall that the market didn't really need a product like ours anymore." By 2020 gross monthly revenue churn hit 9%, nearly double the SaaS average. He chose to pivot into an agency rather than die — "it eventually came down to pivoting to an agency or death... I decided: let's choose to live" — and then rebuilt the company into Motion.

Why I'd bet: **he has already been killed once by exactly the force that threatens every company in this report, and he survived it and learned the lesson.** Motion is deliberately positioned where the platforms have no incentive to go: cross-platform creative analytics for the human creative strategist. Roughly $50M ARR as of August 2025, having gone from single-digit millions to eight figures within three months of launching AI Employees, on only $42M raised across all rounds. That is a founder who chose his ground with scar tissue.

### Tier 2 — strong, would look hard

- **Ikkjin Ahn (Moloco)** — early ML engineer on YouTube/Google. Built roughly $400M of revenue as an independent ranking engine for everyone who isn't Meta or Google. Superb pedigree; late-stage entry at $1.5–2.0B.
- **Melissa Burdick (Pacvue)** — ten years at Amazon, then bootstrapped Pacvue to a nine-figure exit **with zero VC**. The purest capital-efficiency record in the dataset and a genuine category definer in retail media.
- **Romain Torres and Dylan Fournier (Arcads)** — roughly $15M ARR, profitable, reportedly with about 8 people, on a $16M seed from Eurazeo. Revenue per employee here is extraordinary. If those figures hold, this is the best hidden risk-adjusted bet in the set.
- **Eric Mayhew and Mike Sullivan (Fluency)** — profitable since 2020, bootstrapped to $3B in media spend under management and 250,000 campaigns a month before taking a single $40M round. Unglamorous ad-ops infrastructure for franchises and agencies, which is precisely why the platforms won't touch it.
- **Vitaly Pecherskiy (StackAdapt)** — co-founder who stepped up from COO to CEO in 2024 and now runs a $500M+ revenue business at a $2.5B valuation.
- **Gil Allouche (Metadata.io)** — ex-VP Marketing at Qubole who built the tool for his own job. B2B is the segment least exposed to Meta's automation.
- **Frederick Vallaeys (Optmyzr)** — Google's first ~500 employees, a decade on AdWords, now bootstrapped to $15–24M with $5.3B in spend managed. Won't be a venture outcome; will still be here in ten years.

### Tier 3 — I would pass, and why

- **Anything that is a thin wrapper on Advantage+ or Performance Max.** Most sub-$5M-ARR SMB self-serve tools in Section A fall here. Their roadmap is written by Meta's product team.
- **Companies whose raise vastly exceeds their revenue.** VidMob has raised $208.9M against roughly $18.3M estimated ARR. The cap table is now the problem.
- **Single-channel rules engines.** This is precisely what Marin Software was, and it liquidated for $5.5M.
- **"Autonomous AI media buyer" with no platform-insider pedigree.** See the graveyard below.

### The graveyard — read this before betting on any agentic ad startup

Every pre-LLM "autonomous AI media buyer" is dead:

- **Adext AI** — raised at a $20M valuation in 2016 promising fully automated audience and budget management. Ceased operations 2024.
- **Albert.ai** — the best-known autonomous media buyer of its generation. Assets sold to Zoomd in March 2022.
- **Icon (icon.com)** — the cautionary tale of this cycle. Founded 2024 by Kennan Davison (previously founder of Skio), backed by Founders Fund with a $9.2M seed plus executives from OpenAI, Ramp, Flexport, Cognition and Pika. Paid **$12M for the icon.com domain** in April 2025. Claimed $5M ARR and 76 staff. The autonomous "AI CMO" never worked reliably; users reported poor AI voice quality, a clunky interface and billing problems. The team vanished from LinkedIn by February 2026 and reporters declared it dead in March 2026. **The site is now back online selling human-made UGC ads — "38 Human UGC ads (100% real / not AI)" — a complete inversion of the founding thesis.** Note the shutdown was inferred by journalists; the company never announced one.

The lesson is not that agentic ad buying can't work. It is that the wrapper-around-an-API version doesn't, and that "we'll automate the media buyer" is a claim the market has heard and punished three times already. That is exactly why the MAI profile — a decade inside Google's ad system — matters more than the pitch deck.

### If I could make only one bet

**MAI at seed, Motion at growth.** MAI has the best founder–market fit and the highest ceiling if agentic buying works at all; Yuchen Wu is the person most likely to know where the residual edge is after the platforms automate everything. Motion is the best risk-adjusted position: a founder who has already survived platform absorption, deliberately building on ground Meta has no reason to take, at roughly $50M ARR on $42M raised.

**Best pure business today, if you can get in:** HeyGen. Nothing else in this dataset combines $200M ARR, doubling in eight months and cash-flow break-even.

---

## 5. Caveats

- Private-company revenue is largely modelled. Latka, Tracxn and Growjo estimates are labelled "est." throughout and are frequently wrong by a wide margin, especially for companies with usage-based pricing.
- Valuations are last-round post-money unless noted, so they reflect the date of the round, not today.
- Two source conflicts worth flagging: a PitchBook-derived snippet claimed Proxima raised an $80M seed in January 2026, but the verifiable round is a $12M Series A from April 2024 led by Mucker Capital; and Madgicx is listed as bootstrapped by Latka and Crunchbase while a Tracxn/PitchBook snippet names PeakSpan Capital as an investor.
- Icon's shutdown was inferred by reporters from a password-walled site and employees leaving LinkedIn. The company never confirmed it, and icon.com is live again as a human ad agency.
- Meta and LinkedIn ad-library links are keyword searches and will return other advertisers mentioning the same term. Google links are advertiser-domain lookups and are exact. An empty result usually means the company isn't currently running ads on that platform.
- Founder LinkedIn URLs are included where a profile surfaced verbatim in search results. LinkedIn blocks automated profile fetching (HTTP 999), so several are search links rather than direct profiles.

## 6. Principal sources

Market: [Madison and Wall AI advertising forecast](https://madisonandwall.substack.com/p/how-ai-powered-advertising-totals) · [Meta Q2 2026 earnings](https://finance.yahoo.com/markets/stocks/articles/meta-platforms-inc-meta-q2-050330313.html) · [Zuckerberg full-automation plans](https://finance.yahoo.com/news/mark-zuckerberg-meta-aims-fully-174128047.html) · [Google Gemini in Performance Max](https://blog.google/products/ads-commerce/gemini-models-are-coming-to-performance-max/) · [Google AI Max 2026 guide](https://www.groas.com/post/google-ads-ai-max-complete-2026-guide) · [TikTok automation updates](https://newsroom.tiktok.com/en-us/tiktok-announces-new-automation-updates-for-advertisers) · [Tracxn AdTech sector](https://tracxn.com/d/sectors/adtech/__Ak0O6DnFtScWvUjt88Kfxjn0bRF95Kelyp4HRUsraNs) · [AI sales & marketing funding analysis](https://newmarketpitch.com/blogs/news/ai-sales-anding-funding-analysis)

Companies: [Higgsfield $400M Series B](https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/) · [HeyGen $200M ARR](https://www.businesswire.com/news/home/20260625305891/en/HeyGen-Doubles-to-$200M-ARR-in-Eight-Months-on-the-Rise-of-Identity-First-AI-Video) · [Mirage $75M](https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-app-captions/) · [Motion Series B](https://betakit.com/motion-closes-30-million-usd-series-b-in-bid-to-become-command-centre-for-creative-strategists/) · [Motion ARR, Sacra](https://sacra.com/c/motion/) · [Shoelace near-death](https://betakit.com/how-adtech-startup-shoelace-ended-up-at-the-brink-of-death/) · [MAI $25M seed](https://www.prnewswire.com/news-releases/mai-raises-25m-to-automate-performance-marketing-with-ai-agents-driving-revenue-for-brands-302571065.html) · [MAI pitch deck](https://www.adweek.com/media/mai-marketing-ai-pitch-deck-25m-kleiner-perkins/) · [StackAdapt $235M](https://techcrunch.com/2025/02/04/canadas-stackadapt-snaps-up-235m-for-its-ai-based-programmatic-platform/) · [Fluency $40M](https://www.fluency.inc/news/fluency-secures-40m-series-a-ai-powered-digital-advertising-operating-system) · [Marin dissolution](https://www.businesswire.com/news/home/20250410517913/en/Marin-Software-Announces-Plan-of-Dissolution) · [Icon collapse](https://techstartups.com/2026/03/05/icon-the-ai-ad-startup-shuts-down-after-spending-12m-on-the-icon-com-domain/) · [Appier acquires AdCreative.ai](https://www.appier.com/en/press-media/appier-acquires-adcreative.ai-in-strategic-move) · [AppLovin AXON](https://ppc.land/applovins-1-84b-q1-beats-guidance-as-axon-platform-opens-to-all-in-june/) · [MNTN 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102725000022/mntn-20250930.htm) · [Mashrabov profile](https://svicons.com/p/alex-mashrabov-founder-of-higgsfield)

Detailed per-company research notes, including every source URL, are in `research/segments/`.

---

## 8. Expanded market map — adjacent categories

The first pass covered tools built specifically to run ads. This section covers the rest of the stack an advertiser actually touches: the model layer that makes the creative, the measurement layer that scores it, the channels beyond Meta and Google, and the plumbing underneath. Roughly 50 further companies, same sourcing rules.

### AI video & creative model layer

The foundation models advertisers now use to manufacture ad creative. None of these were built as ad tools, but they are where a growing share of ad creative is actually produced — and they are far better capitalized than anything ad-native.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Runway](https://runwayml.com) | $860M | $5.3B (Feb 2026) | ~$300M est. ARR | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Runway&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=runwayml.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Runway) |
| [Synthesia](https://synthesia.io) | $536.6M | $4B (Jan 2026) | $150M ARR at Series E; ~$100M (2025 est.) | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Synthesia&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=synthesia.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Synthesia) |
| [Typeface](https://typeface.ai) | $165M | $1B (2023) | $34.3M est. ARR | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Typeface&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=typeface.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=Typeface) |
| [Jasper](https://jasper.ai) | $131M+ | ~$1.5B (2022) | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Jasper&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=jasper.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=Jasper) |
| [Copy.ai](https://copy.ai) | ~$140M | ~$500M (2025) | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Copy.ai&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=copy.ai) · [LI](https://www.linkedin.com/ad-library/search?keyword=Copy.ai) |
| [Anyword](https://anyword.com) | $30.1M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Anyword&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=anyword.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Anyword) |
| [Superside](https://superside.com) | $35.1M | ~$400M (2021) | $44.9M ARR (2024 est.) | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Superside&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=superside.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Superside) |
| [Coframe](https://coframe.com) | $9.3M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Coframe&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=coframe.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Coframe) |

- **Runway** — $315M Series E led by General Atlantic, up from $3.3B in Apr 2025
- **Synthesia** — $200M Series E led by GV, with Nvidia and Alphabet VC arms; 65,000+ businesses, 90%+ of the Fortune 100; NRR >140%; 737 staff
- **Typeface** — Founded by Abhay Parasnis, former CTO of Adobe; Salesforce Ventures led
- **Jasper** — Brand-voice anchor of the enterprise AI copy set
- **Copy.ai** — $63M Series C in 2025, after a $63M Series B at ~$200M
- **Anyword** — Predictive performance scoring for ad copy; 1M+ registered users; The New York Times is a strategic backer
- **Superside** — Repositioned Jan 2025 as an AI-first creative partner; also ships Superads, a creative-analytics tool
- **Coframe** — Seed co-led by Khosla Ventures and NFDG; AI that continuously rewrites landing pages and campaign assets

### Creative automation platforms (enterprise CMPs)

The pre-generative-AI creative production layer, now retrofitting AI. Mordor sizes creative automation software at $2.51B in 2026, growing to $5.51B by 2031 (17.0% CAGR).

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Bannerflow](https://bannerflow.com) | n/a | n/a | n/a | PE-owned | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Bannerflow&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=bannerflow.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Bannerflow) |
| [Storyteq](https://storyteq.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Storyteq&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=storyteq.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Storyteq) |
| [Papirfly](https://papirfly.com) | n/a | n/a | n/a | PE-owned | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Papirfly&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=papirfly.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Papirfly) |
| [Creatopy](https://creatopy.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Creatopy&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=creatopy.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Creatopy) |

- **Bannerflow** — Tenzing Private Equity invested July 2024; connects to 100+ ad platforms and is a certified Amazon Ads third-party ad server
- **Storyteq** — DAM with creative automation layered on top; self-serve from ~€2,400/mo
- **Papirfly** — 1M+ users across 1,500+ organisations (Mercedes-Benz, Mondelez, Goldman Sachs)
- **Creatopy** — Rebranded as The Brief

### UGC creator marketplaces

Where brands buy human-made creator ads. The category the AI-UGC tools are trying to replace — and, in Icon's case, retreated back into.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Billo](https://billo.app) | ~$13.9M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Billo&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=billo.app) · [LI](https://www.linkedin.com/ad-library/search?keyword=Billo) |
| [Insense](https://insense.pro) | ~$4.9M (sources conflict) | n/a | $13.6M est. ARR (Jul 2025) | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Insense&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=insense.pro) · [LI](https://www.linkedin.com/ad-library/search?keyword=Insense) |
| [Trend.io](https://trend.io) | ~$3M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Trend.io&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=trend.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Trend.io) |
| [Aspire](https://aspire.io) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Aspire&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=aspire.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Aspire) |

- **Billo** — $8.49M Series A, June 2024
- **Insense** — Latka lists it as effectively bootstrapped; Tracxn shows small rounds
- **Trend.io** — Pharrell Williams is an investor; co-founded by Ramon Berrios and Zach Moosbrugger
- **Aspire** — Influencer/creator marketing for ecommerce brands

### Mobile app user acquisition & measurement

The largest pool of pure performance spend outside Meta and Google, and the segment where machine-learning bidding matured first.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Liftoff](https://liftoff.io) | Blackstone-owned | $4.3B (May 2025) | n/a | IPO filed | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Liftoff&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=liftoff.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Liftoff) |
| [AppsFlyer](https://appsflyer.com) | $1.3B | $2.7B–$4.0B (sources conflict) | $395M ARR (2023); $500M ARR (2026 est.) | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AppsFlyer&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=appsflyer.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=AppsFlyer) |
| [Branch](https://branch.io) | n/a | ~$4B | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Branch&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=branch.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Branch) |
| [Adjust](https://adjust.com) | — | ~$1B (2021 exit) | n/a | AppLovin | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Adjust&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=adjust.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Adjust) |
| [Aarki](https://aarki.com) | $14.25M | — | n/a | Skillz | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Aarki&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=aarki.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Aarki) |
| [Remerge](https://remerge.io) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Remerge&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=remerge.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Remerge) |
| [Bidease](https://bidease.com) | $11M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Bidease&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=bidease.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Bidease) |

- **Liftoff** — S-1 filed with the SEC for a ~$400M IPO; backed by Blackstone and General Atlantic
- **AppsFlyer** — $1B Series E from a consortium of Meta, Google, Unity and Moloco; 80,000+ apps, ~12,000 paying customers
- **Branch** — Mobile measurement and deep linking
- **Adjust** — Acquired by AppLovin in 2021 for a reported $1B
- **Aarki** — Acquired by Skillz, 8 Jan 2025
- **Remerge** — In-app programmatic retargeting DSP
- **Bidease** — Mobile DSP

### Retail media infrastructure

Software that lets retailers run their own ad businesses, and lets brands buy across them. The fastest-growing ad channel after social and search.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Topsort](https://topsort.com) | $43.2M | $150M (Series A) | $3.7M (company-cited) | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Topsort&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=topsort.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Topsort) |
| [Koddi](https://koddi.com) | $0 — bootstrapped | n/a | $28.2M est. ARR | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Koddi&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=koddi.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Koddi) |
| [CitrusAd](https://citrusad.com) | — | — | ~$80.8M est. revenue | Publicis | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=CitrusAd&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=citrusad.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=CitrusAd) |
| [Criteo](https://criteo.com) | public | — | Retail media revenue $264M (2025) | Public (Nasdaq: CRTO) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Criteo&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=criteo.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Criteo) |
| [Flywheel Digital](https://flywheeldigital.com) | — | $835M (2023 exit) | n/a | Omnicom | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Flywheel%20Digital&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=flywheeldigital.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Flywheel%20Digital) |
| [Intentwise](https://intentwise.com) | $0 — bootstrapped | n/a | $8.8M est. ARR | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Intentwise&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=intentwise.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Intentwise) |

- **Topsort** — Backed by W23, the VC fund behind Tesco, Ahold Delhaize, Woolworths, Empire/Sobeys and Shoprite
- **Koddi** — 256 employees, never raised outside capital
- **CitrusAd** — Acquired by Publicis Groupe, July 2021; 7,000+ brands, 70+ retail distributors
- **Criteo** — Retail media revenue fell 17% in Q4 2025 after two large clients changed scope
- **Flywheel Digital** — Omnicom paid $835M; Perpetua had been a Flywheel/Ascential bolt-on acquisition
- **Intentwise** — Founded 2015 by Sreenath Reddy and Raghu Kashyap

### Performance CTV

Streaming TV sold on direct-response terms. The segment produced the largest single exit in this entire report.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Vibe.co](https://vibe.co) | $50M raised | $1.4B (2026 exit) | n/a | Walmart | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Vibe.co&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=vibe.co) · [LI](https://www.linkedin.com/ad-library/search?keyword=Vibe.co) |
| [tvScientific](https://tvscientific.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=tvScientific&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=tvscientific.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=tvScientific) |
| [Tatari](https://tatari.tv) | $0 — bootstrapped | n/a | $37.1M est. ARR | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Tatari&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=tatari.tv) · [LI](https://www.linkedin.com/ad-library/search?keyword=Tatari) |
| [Simulmedia](https://simulmedia.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Simulmedia&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=simulmedia.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Simulmedia) |

- **Vibe.co** — Walmart announced the $1.4B acquisition 23 June 2026 and closed it 4 Aug 2026 — $1.2B cash plus ~$180M to executives. Had been valued at $410M after a $50M raise. Walmart's biggest CTV move since buying Vizio for $2.3B
- **tvScientific** — Self-serve performance CTV for mid-market advertisers
- **Tatari** — Linear plus streaming, with incrementality measurement
- **Simulmedia** — Cross-screen TV performance buying

### Measurement, incrementality & attribution

The independent scorekeepers. Structurally protected, because a platform grading its own homework is a permanent conflict of interest — which is exactly why the platforms are buying into this layer.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Haus](https://haus.io) | $55.3M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Haus&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=haus.io) · [LI](https://www.linkedin.com/ad-library/search?keyword=Haus) |
| [Rockerbox](https://rockerbox.com) | — | — | n/a | DoubleVerify | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Rockerbox&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=rockerbox.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Rockerbox) |
| [Scibids](https://scibids.com) | — | $125M (2023 exit) | n/a | DoubleVerify | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Scibids&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=scibids.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Scibids) |
| [INCRMNTAL](https://incrmntal.com) | n/a | n/a | n/a | Being acquired | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=INCRMNTAL&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=incrmntal.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=INCRMNTAL) |
| [Prescient AI](https://prescientai.com) | $18M | n/a | $11.4M revenue (Sep 2025) | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Prescient%20AI&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=prescientai.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Prescient%20AI) |
| [Measured](https://measured.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Measured&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=measured.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Measured) |
| [Fospha](https://fospha.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Fospha&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=fospha.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Fospha) |

- **Haus** — Series B April 2025 plus $20M from 01 Advisors; geo-based causal experiments, now Causal MMM and Causal Attribution
- **Rockerbox** — Acquisition completed 13 March 2025
- **Scibids** — Cash-and-stock deal plus earn-out; custom bidding algorithms across DV360, The Trade Desk and Xandr
- **INCRMNTAL** — Smartly signed a letter of intent to acquire it — the buying layer absorbing the measurement layer
- **Prescient AI** — $10M Series A led by Headline and CEAS; 49 employees; media-mix modelling for DTC
- **Measured** — Large-scale geo holdout experiments using synthetic control
- **Fospha** — Focused on UK/EU DTC brands whose paid-social prospecting is undervalued by last-click

### Programmatic AI & the big DSPs

Where AI bidding runs at the largest scale outside the walled gardens.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [The Trade Desk](https://thetradedesk.com) | public | — | $2.44B (2024) | Public (Nasdaq: TTD) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=The%20Trade%20Desk&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=thetradedesk.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=The%20Trade%20Desk) |
| [Zeta Global](https://zetaglobal.com) | public | — | $1.305B FY2025, +30% | Public (NYSE: ZETA) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Zeta%20Global&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=zetaglobal.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Zeta%20Global) |
| [Viant](https://viantinc.com) | public | — | n/a | Public (Nasdaq: DSP) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Viant&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=viantinc.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Viant) |
| [Basis Technologies](https://basis.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Basis%20Technologies&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=basis.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Basis%20Technologies) |

- **The Trade Desk** — Kokai platform with the Koa AI forecasting engine and Unified ID
- **Zeta Global** — 2026 guidance $1.749–1.762B. Athena by Zeta, built with OpenAI, hit GA in Q1 2026; agentic interactions rose sevenfold in week one and became 60%+ of AI usage
- **Viant** — AI-driven DSP for the open internet
- **Basis Technologies** — Automation across programmatic, search and social for agencies

### AI-native ad networks (ads inside AI products)

The newest category in the report: advertising placed inside chatbots and AI assistants rather than feeds. Tiny today, and the most speculative bet in the market.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Nexad](https://nex.ad) | $6M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Nexad&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=nex.ad) · [LI](https://www.linkedin.com/ad-library/search?keyword=Nexad) |
| [Kontext](https://kontextso.com) | $10M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Kontext&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=kontextso.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Kontext) |
| [Rembrand](https://rembrand.com) | $46M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Rembrand&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=rembrand.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Rembrand) |

- **Nexad** — Seed co-led by a16z and Prosus Ventures, April 2025, with Point72 Ventures and a Sequoia scout fund; claims 2x conversion vs traditional ads
- **Kontext** — Seed round; places branded links beneath chatbot responses for Amazon, Uber and Canva
- **Rembrand** — $23M Series A led by super{set} with The Trade Desk and Naver; AI virtual product placement moving from social into CTV

### Local & multi-location marketing platforms

How the long tail of Main Street businesses actually buys advertising — bundled into an operating system they already use.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Podium](https://podium.com) | $421.6M | $3B (2025) | $219.9M est. ARR | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Podium&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=podium.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Podium) |
| [Birdeye](https://birdeye.com) | $93M | n/a | ~$100M+ revenue | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Birdeye&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=birdeye.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Birdeye) |
| [Thryv](https://thryv.com) | public | — | n/a | Public (Nasdaq: THRY) | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Thryv&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=thryv.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Thryv) |

- **Podium** — 60,000 local businesses; AI revenue grew roughly 300% in a year; ~1,500 staff
- **Birdeye** — 100,000+ businesses; expanding agentic AI for multi-location marketing
- **Thryv** — SMB marketing and operations suite

### Product feed management

Unglamorous plumbing that decides whether a Shopping or catalog ad can run at all. Consolidating fast.

| Company | Raised | Valuation | Revenue | Status | Ad libraries |
|---|---|---|---|---|---|
| [Feedonomics](https://feedonomics.com) | — | — | n/a | BigCommerce | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Feedonomics&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=feedonomics.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Feedonomics) |
| [Productsup](https://productsup.com) | $91M | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Productsup&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=productsup.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Productsup) |
| [Channable](https://channable.com) | n/a | n/a | n/a | Independent | [Meta](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=Channable&search_type=keyword_unordered) · [Google](https://adstransparency.google.com/?region=anywhere&domain=channable.com) · [LI](https://www.linkedin.com/ad-library/search?keyword=Channable) |

- **Feedonomics** — Founded 2014 by Brian Roizen and Shawn Lipman; serves 30%+ of the top 1,000 internet retailers
- **Productsup** — Feed management, marketplace integration and content syndication
- **Channable** — Connects catalogs to 3,000+ marketplaces and ad platforms
---

## 7. Founder profile directory

Every link below was resolved against a professional-profile database rather than inferred from a name pattern. Five URLs a name-pattern guess would have produced were wrong — Mark Douglas is `/in/teachmehow2douglas`, not `/in/markadouglas`; Ikkjin Ahn, Shubham Mishra, Vrushali Prasade and Assaf Baciu were likewise corrected.

| Founder | Company | LinkedIn |
|---|---|---|
| Alex Mashrabov | Higgsfield AI | [linkedin.com/in/amashrabov](https://www.linkedin.com/in/amashrabov) |
| Joshua Xu | HeyGen | [linkedin.com/in/buffxz](https://www.linkedin.com/in/buffxz) |
| Reza Khadjavi | Motion | [linkedin.com/in/reza-khadjavi-46802918](https://www.linkedin.com/in/reza-khadjavi-46802918) |
| Gaurav Misra | Mirage (Captions) | [linkedin.com/in/gamisra1](https://www.linkedin.com/in/gamisra1) |
| Yinan Steven Na | Creatify | [linkedin.com/in/nayinan](https://www.linkedin.com/in/nayinan) |
| Romain Torres | Arcads | [linkedin.com/in/romain-torres-arcads](https://www.linkedin.com/in/romain-torres-arcads) |
| Dylan Fournier | Arcads | [linkedin.com/in/dylan-fournier-732b1972](https://www.linkedin.com/in/dylan-fournier-732b1972) |
| Hikari Senju | Omneky | [linkedin.com/in/hisenju](https://www.linkedin.com/in/hisenju) |
| Alexei Chemenda | Poolday.ai | [linkedin.com/in/alexeichemenda](https://www.linkedin.com/in/alexeichemenda) |
| Dan Pantelo | Marpipe | [linkedin.com/in/danpantelo](https://www.linkedin.com/in/danpantelo) |
| Ray Jang | Atria | [linkedin.com/in/rayjbjang](https://www.linkedin.com/in/rayjbjang) |
| Alex Collmer | VidMob | [linkedin.com/in/alexcollmer](https://www.linkedin.com/in/alexcollmer) |
| Ikkjin Ahn | Moloco | [linkedin.com/in/ikkjin-ahn-a090937](https://www.linkedin.com/in/ikkjin-ahn-a090937) |
| Adam Foroughi | AppLovin | [linkedin.com/in/adamforoughi](https://www.linkedin.com/in/adamforoughi) |
| Melissa Burdick | Pacvue | [linkedin.com/in/melissaburdick](https://www.linkedin.com/in/melissaburdick) |
| Alex Song | Proxima | [linkedin.com/in/alexjsong](https://www.linkedin.com/in/alexjsong) |
| Austin Harrison | Northbeam | [linkedin.com/in/maustinharrison](https://www.linkedin.com/in/maustinharrison) |
| Vitaly Pecherskiy | StackAdapt | [linkedin.com/in/vitalypecherskiy](https://www.linkedin.com/in/vitalypecherskiy) |
| Mark Douglas | MNTN | [linkedin.com/in/teachmehow2douglas](https://www.linkedin.com/in/teachmehow2douglas) |
| Eric Mayhew | Fluency | [linkedin.com/in/ericmayhew](https://www.linkedin.com/in/ericmayhew) |
| Shubham Mishra | Pixis | [linkedin.com/in/shubham015](https://www.linkedin.com/in/shubham015) |
| Vrushali Prasade | Pixis | [linkedin.com/in/vprasade](https://www.linkedin.com/in/vprasade) |
| Assaf Baciu | Persado | [linkedin.com/in/assaf-baciu-17a4b3](https://www.linkedin.com/in/assaf-baciu-17a4b3) |
| Kristo Ovaska | Smartly (now Taito.ai) | [linkedin.com/in/kristoovaska](https://www.linkedin.com/in/kristoovaska) |
| Frederick Vallaeys | Optmyzr | [linkedin.com/in/frederickvallaeys](https://www.linkedin.com/in/frederickvallaeys) |
| Adam Nathan | Blaze.ai | [linkedin.com/in/adampnathan](https://www.linkedin.com/in/adampnathan) |
| Karthik Venkateswaran | Zocket | [linkedin.com/in/karthik-venkateswaran-04680940](https://www.linkedin.com/in/karthik-venkateswaran-04680940) |
| Sinisa (Siggi) Rakovich | Hunch | [linkedin.com/in/sinisarakovic](https://www.linkedin.com/in/sinisarakovic) |
| Asaf Yanai | Alison.ai | [linkedin.com/in/asaf-yanai](https://www.linkedin.com/in/asaf-yanai) |
| Gil Allouche | Metadata.io | [linkedin.com/in/gilallouche](https://www.linkedin.com/in/gilallouche) |
| Dmitri Lisitski | Influ2 | [linkedin.com/in/lisitski](https://www.linkedin.com/in/lisitski) |
| Emir Atli | HockeyStack | [linkedin.com/in/emircatli](https://www.linkedin.com/in/emircatli) |
| Larry Kim | Customers.ai (ex-WordStream) | [linkedin.com/in/larrykim](https://www.linkedin.com/in/larrykim) |
| Kennan Jenner (formerly Davison) | Icon (ex-Skio) | [linkedin.com/in/kennanjenner](https://www.linkedin.com/in/kennanjenner) |

**Deliberately unlinked** (not resolvable in the database, so not guessed): **Yuchen Wu** and **Jian Wang** (MAI) — primary references are the [funding release](https://www.prnewswire.com/news-releases/mai-raises-25m-to-automate-performance-marketing-with-ai-agents-driving-revenue-for-brands-302571065.html) and the [Adweek pitch-deck story](https://www.adweek.com/media/mai-marketing-ai-pitch-deck-25m-kleiner-perkins/); also **Yahav Hartman** (Madgicx), **Zachary Murray** (Foreplay), **Mikhail Trofimov** (Bïrch) and **Mike Sullivan** (Fluency).

One update the lookup surfaced: Icon's founder now appears as **Kennan Jenner** (previously Kennan Davison / Frost), self-reported headline "Founder @ Icon & Skio ($105M cash exit)", with Icon still listed as current — which sits awkwardly against the March 2026 collapse reports and reinforces that the shutdown was inferred, never announced.

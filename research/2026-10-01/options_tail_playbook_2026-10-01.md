# Options Tail-Bet Playbook: AI-Infrastructure Cohort

**As of:** Oct 1, 2026, pre-market. Option data are Sep 30 closing quotes (CBOE delayed / Yahoo) and must be **re-priced live before any order**.
**Framework (the user's):** ten $1M slots. Losing any single slot entirely is acceptable; the goal is for 2–3 slots to return 10–20x.

**Status:** Analytical scenario work, not personalized investment advice. There is no buy or sell instruction, and no trade has been placed.

- Long-premium structures only: the maximum loss on each slot equals the premium paid.
- Short or naked option selling is excluded.

---

## 0. The honest base rate

- **No directional edge has been evidenced.** Both thesis candidates were rejected or weakened at Red Team (see the supervisor reconciliation report, §6).
- **The only measurable edge is volatility pricing.** Where options price a smaller move than the stock historically delivers, long tails are cheaper than usual.
- **How often have ≥30% earnings-day moves happened?** In 4 of 46 reports across the cohort (≈9%):
  - APLD −35.9% and +31.0%
  - NBIS +34.1%
  - ORCL +35.9%
- **Getting 10x from an out-of-the-money option needs roughly a 30–50% move.** That requires short-dated options bought just before the event (§3). Longer-dated options (Dec, Jan) mostly cap out at 3–8x even on 35–50% moves.
- **The ten slots are not independent.** All seven names load on the same AI-capex factor. To diversify, the book mixes **upside and downside tails** and keeps **3 slots in reserve**.

## 1. Volatility pricing by event (the measurable edge)

Table key: Event-only implied move is the move the options price for the earnings day itself. "Implied vs history" compares that implied move with each name's own past moves on earnings days.

| Ticker | Event (status) | Event-only implied move | Historical avg abs move | Implied vs history | IV rank / percentile (1y, single source) | Short % float |
|---|---|---|---|---|---|---|
| APLD | Oct 7 after close (confirmed) | 10.8–11.8% | avg 14.6%, median 9.1%, last-4 8.3% | 0.8x avg, 1.3x median → **not cheap** | 31 / 15% | 22.1% |
| CLS | Oct 26 after close / Oct 27 (confirmed week) | ~11% | 10.7% | ~1.0x → **fair** | 43 / 51% | 3.1% |
| SNDK | Oct 29 after close (confirmed) | 7.3–7.7% | 7.8% (last-4: 9.3%) | ~0.8–1.0x → **fair to slightly cheap** | 48 / 12%; 60-day realized vol 114% vs IV 73% | 6.0% |
| CRWV | ~Nov 11 after close (unconfirmed) | ~10% | 16.4% / 14.8% | **~0.6x → cheapest** | 13 / 6% | 17.6% |
| NBIS | ~Nov 10 before open (unconfirmed) | ~12% | 14.5% / 13.5% | **~0.85x → cheap** | 2 / 1% | 19.8% |
| IREN | ~Nov 5 (estimate); Horizon 2–4 acceptance anytime in Q4 | ~7% | 8.0% | ~0.85x | 29 / 1% | 21.7% |
| ORCL | Dec 10–14 (unconfirmed) | ~8% | 7.6% (last-6: 13.3%) | ~1.0x | 41 / 31% | 2.7% |

## 2. Slot map: illustrative structures, each needing live re-pricing

Payoff multiples are model estimates (Black-Scholes, post-event IV drop assumed), not guarantees.

| Slot | Bet | Why this tail (evidence) | Illustrative structure | What gets 10x | Kill / exit rules |
|---|---|---|---|---|---|
| 1 | **CRWV earnings, both tails, put-tilted (~60/40)** | Options are the cheapest vs history in the book. 4 of 6 past reports fell 11–21%. Interest = 25% of revenue. $10.6B of debt matures by end-2027. ~$92B obligation stack. Form 144 insider sales of ≈$45M+ filed Sep 29–30. Upside: 17.6% short interest, Aug +19% reaction. | Build slowly in Dec 18 options now while IV is cheap (rank ~13). Shift the bulk to the first post-earnings weekly (Nov 13/20) once the date is confirmed. Strikes ~25–35% out of the money. | Short-dated 25% OTM put on a −30% move: ~16x. 25% OTM call on a +40% move: ~15x. | Don't add if event IV rises above ~1.0x the historical move. Exit the day after earnings unless deep in the money. |
| 2 | **NBIS earnings, both tails, ~50/50** | IV is at a 1-year low (rank ~2). Reactions: +34%, +19%, +16% upside, −7% downside. The corrected FD EV ($78.5–84.9B, 24.5–26.5x revenue) raises the downside tail. Opaque operating-MW disclosure means a binary print. | Same mechanics as Slot 1. Nov 20 expiry (report is before the open, ~Nov 10). | Short-dated 25% OTM call on +40%: ~13x. Put on −30%: ~13x. | Same as Slot 1. |
| 3 | **APLD Oct 7, call-tilted, half size ($0.5M)** | 22% short interest; stock −35% over 3 months; two ≥30% moves in history. The real swing factor is rent on the 75 MW plus a funding answer for PF3/Delta Forge. Fit-out will probably flatter headline revenue vs the $116–135M consensus. Options are **not** cheap. | Oct 9 / Oct 16 options, 20–30% out of the money. | 30% OTM Oct 16 call on +50%: ~20x. | **$1M does not fit**: ~40k contracts vs ~60k total Oct 16 call open interest. Cap at a few thousand contracts. If APLD announces an equity raise or ATM before Oct 7, the call side is dead. |
| 4 | **SNDK Oct 29, put-tilted** | Consensus FQ1 EPS ($46.18) is above the top of the $44–46 guide. NBM price ceilings cap upside. Micron (Sep 30) showed NAND pricing slowing (+30% vs +85%). The last report opened −13%. Realized vol (114%) is well above implied (73%). | Nov 20 puts 15–20% out of the money. Optional small call wing (Sep 18 call frenzy shows upside tails too). | Nov 20 20% OTM put on −45%: ~9x. A true 10x needs an Oct 30 weekly bought just before the event. | Wide dollar spreads ($10–13): limit orders at mid only. Cut the put idea if the FQ2 guide clears the $12.23B consensus. |
| 5 | **ORCL downside tail into Dec earnings and financing stress** | $288B of uncommenced leases. Trailing FCF −$28.7B. ATM equity program exhausted. Force-majeure notice on the Stargate New Mexico site (Sep 24). **Ellison has pledged ~418M shares**, a reflexive selling risk if the stock falls. Offsets: reported $7B Tencent deal, $664B RPO. | Jan 2027 puts 25–30% out of the money, bought in tranches. Add Dec weekly puts once the date is confirmed (~Dec 1–3). | Jan 30% OTM put on −45%: ~12x. | Close if ORCL confirms Tencent plus project-level returns at Q2, or if the stock reclaims ~$160 with falling IV. |
| 6 | **CLS Oct 27, put-tilted, half size** | The bar is high: ~$19 FY27 EPS / ~9% margin (Red Team). Jabil beat and raised on Sep 30 and still fell −10%. CLS +24% in 1 month. Call skew makes puts relatively cheaper. Recent reports: −13% and −14%. | Nov 20 puts ~20% out of the money. The Oct 30 weekly is too thin to use. | −45%: ~10x. Realistically ~3–6x on a −25–35% move. | Abort if Q3 margin is ≥8.4% and the FY27 framework is ≥$19 EPS. |
| 7 | **IREN acceptance binary, call-tilted** | IV percentile ~1%. Short interest 21.7%. Horizon 2–4 (150 MW, Microsoft) acceptance targeted Q4 2026; a short squeeze is possible on the announcement. Grace periods run to Q2 2027, so slippage is the downside tail. | Ladder Nov/Dec monthly calls 20–30% out of the money, sized to absorb monthly decay. | Realistically a **3–5x** candidate. Historical moves are small (8%), so 10x is unlikely. | Stop laddering if the earnings call pushes acceptance into the grace period. |
| 8–10 | **Reserve ($3M)** | Correlation means the seven names are closer to 2–3 independent bets. Better entries tend to appear **after** events: IV crush, gap moves, IREN news, ORCL date confirmation. | Deploy only on a new, dated, evidenced catalyst. | — | — |

## 3. Why timing matters (model, Sep 30 inputs)

- **Bought today, longer-dated:** a Dec 18 CRWV 50%-OTM call returns only ~4x on a +50% earnings move. Time value and the post-event IV drop eat the convexity.
- **Bought the day before the event, short-dated:** the same thesis with a 25–35% OTM option returns **~7–20x on a ±30–40% move**.
- **The rule this implies:** use cheap longer-dated options now only as a small starter. Concentrate in short-dated tails within ~1–3 days of each event, after checking that event IV has not become expensive relative to history.

## 4. Pre-trade checklist (every slot)

1. Re-price the chain live. All figures here are Sep 30 closing data.
2. Event-only implied move should be ≤ the historical average absolute move. Otherwise wait, or shrink the size.
3. Earnings date confirmed by the company. CRWV, NBIS, IREN and ORCL are **not yet confirmed**.
4. Liquidity: contracts ≤ ~10–20% of the strike's open interest. Limit orders at or near mid. Enter in 3–4 tranches.
5. Pre-commit exits: sell ⅓–½ at 3–5x; exit event plays the morning after unless deep in the money; no averaging down after the event.
6. Check broker position limits and margin, and have tax and legal implications reviewed for $10M of premium.

## 5. Calendar: what to watch

| Date | Item |
|---|---|
| Oct 1–6 | APLD entry window (expect pre-event IV ~114%); watch for any financing 8-K |
| **Oct 7** | APLD Q1 FY27: 75 MW rent vs fit-out, PF3 / Delta Forge funding |
| ~Oct 9 | Sep 30 short-interest data (APLD, IREN, NBIS, CRWV) |
| Mid–late Oct | CRWV / NBIS / IREN date announcements; reposition Slots 1, 2 and 7 |
| **Oct 26/27** | CLS Q3 + Investor Day: FY27 framework vs ~$19 EPS / 9% margin |
| **Oct 29** | SNDK FQ1: FQ2 guide vs $12.23B; NBM minimum ($93.9B), guarantees ($16.5B), any amendments |
| ~Nov 5 | IREN FQ1 (estimate); Horizon 2–4 status |
| ~Nov 10 / 11 | NBIS (before open) / CRWV (after close), estimates |
| Q4, any day | IREN Horizon 2–4 acceptance 8-K |
| ~Dec 1–3 | ORCL date notice; Q2 ~Dec 10–14 |

## 6. Unverified inputs

- Live Oct 1 option quotes.
- 52-week IV rank from a second source (opti-view only; some internal inconsistencies).
- Confirmed earnings dates for CRWV, NBIS, IREN and ORCL.
- CLS release timing (Oct 26 after close vs Oct 27).
- The Ellison pledge source filing.
- Oracle or Tencent confirmation of the reported deal.
- Black-Scholes payoff multiples assume a post-event IV and ignore skew and the bid/ask spread. Realized multiples will be lower.

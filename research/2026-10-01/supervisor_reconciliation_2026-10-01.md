# Thesis Supervisor — Reconciliation & Research-Status Report

**Cohort:** CRWV · ORCL · APLD · IREN · NBIS · CLS · SNDK
**As of:** October 1, 2026 (prices = September 30, 2026 close)
**Horizon:** 0–3 months (event-driven), 3–12 months context
**Type:** Thesis update / narrow follow-up — **not a final thesis**. Research conclusions only; no buy/sell/hold, no price targets, no personalized advice.

**Inputs reconciled:**
- Agent 6 *Comparative Catalyst Analysis* (Oct 1)
- Agent 7 *Valuation & Market Setup Handoff* (Sep 30 close)
- Agent 8 *Red Team Monitoring* (Oct 1, 09:33 UTC)

**Supervisor follow-ups commissioned (Oct 1):**
- A5 — Consensus reconstruction: SNDK, CLS, APLD
- A4a — Capacity-stage verification: APLD, IREN
- A4b — Obligations and margin quality: CRWV, ORCL, CLS
- A7 — Fully diluted EV re-performance: SNDK, ORCL, CLS, NBIS
- A8 — Red Team on two thesis candidates: CLS, SNDK

**Protocol limitation:** `research-protocol.md` was not provided to this workspace.
- Evidence grades follow the scheme used across the specialist reports: A = filing or release; B = transcript, dated aggregator or reputable press; C = secondary or undated.
- The 0–9 stage ladder comes from the Agent 7 handoff.
- The September 30 authoritative record ("R0") was also unavailable. Fully diluted EV anchors were therefore re-performed independently from SEC filings (§3).

---

## 1. Supervisor bottom line

1. **No final thesis is permitted for any of the seven names.** Completion gates are unmet:
   - Agent 3 (theme) never ran.
   - Agent 5 consensus exists only for SNDK, CLS and APLD, at grade B.
   - Red Team review exists only for the two candidates in §6.
2. **Several prior anchors were wrong or mislabeled and are corrected here** (§3). The most material corrections:
   - **NBIS:** FD EV is understated by 16–26%.
   - **SNDK:** the "26–28% current-scale margin" is mislabeled. The real guided operating margin is about 79%; 26–28% is a normalized margin applied to FY27 consensus revenue.
   - **APLD:** current-revenue capacity is 100 MW, not 175 MW.
   - **CLS:** the 6.5–7.0% "full-cycle" margin is above every full-year result before 2025.
   - **ORCL:** recorded leases are $43.8B, not $34.6B.
3. **Two thesis candidates emerged and were sent to Red Team:**
   - **CLS:** FY27 consensus margin versus management's margin-expansion framework.
   - **SNDK:** a single-digit multiple on FY27 consensus earnings versus NBM contract durability.

   All other names stay in **monitoring / evidence-gathering status**.

---

## 2. Contradiction log and adjudication

| # | Issue | Prior claim | Verified finding (source, grade) | Ruling |
|---|---|---|---|---|
| C1 | APLD current-revenue MW | A6: "175 MW verified live and revenue-producing" | 100 MW has filed base rent: FY26 base rent $99.8M; Q4 base rent $44.1M. The 75 MW B2 Phase 1 reached Ready-for-Service (RFS) on 6/30/26 per the 7/1 and 7/27 releases (A). No acceptance or rent-commencement disclosure exists. | **Current-revenue denominator = 100 MW.** 175 MW is "RFS/live" and an upper bound only. Re-test at the Oct 7 Q1 FY27 results. |
| C2 | APLD 10-K labeling | A8: 10-K says "75 MW RFS by July 2026" | "75 MW" does not appear in the 10-K. The 10-K's building numbering conflicts with the press releases, and the first building's operational date is given as both Oct and Nov 2025 (A). | A8 is partly corrected. Building labels stay ambiguous; record buildings by ELN-0x identifier. |
| C3 | IREN 40 MW vs 50 MW | A6/A7/A8: "may overlap" | 40 MW was operating at 6/30/26 (10-K). Horizon 1 (50 MW IT) was accepted by Microsoft in Aug 2026 (8-K of 8/13, A). Operating ARR rose from about $0.5B to $1B after acceptance (B). | **Additive, ~90 MW**, with a basis mismatch: the 40 MW figure has no stated basis, while the 50 MW is IT. Firm floor of customer-accepted hyperscaler IT = 50 MW. |
| C4 | IREN EV/MW | A6: "~51M per MW" | $17.85B ÷ 350–380 MW = $47.0–51.0M (CALC) | Use the **$47–51M range**. A6 used the low end of the denominator only. |
| C5 | SNDK guidance | A6: "revenue 10.8B … EPS 46" | Revenue $10.30–10.80B; non-GAAP GM 83–85%; EPS $44–46 (Aug 5 release, A) | A6 quoted the top of each range as a point. Use the ranges. |
| C6 | SNDK margin method | A6/A7: "26–28% current-scale operating margin" | The guided non-GAAP operating margin is about 78–80% (CALC from the GM and opex guide). $268.4B ÷ 20.5x = $13.1B ÷ FY27 consensus revenue of $48.95B = 26.8%. | **Relabel** as "normalized margin on FY27 consensus revenue". Both normalization methods stay, but they are scenario margins, not current scale. |
| C7 | SNDK revenue base | Not stated | Both methods imply a revenue base of about $46–52B, which matches FY27 consensus ($48.95B). | Disclose that the anchor multiples are forward (FY27) based. |
| C8 | NBIS FD EV | A7: $67.5B "fully diluted", 21.1x | The anchor reproduces only if two items are excluded: NVIDIA's 21.07M pre-funded warrant shares, and about 47.5M shares from the in-the-money converts (which the anchor treats as debt at face). True FD = **$78.5–84.9B, 24.5–26.5x** the 2026 revenue midpoint (A7 re-performance, A). | **Anchor replaced.** NBIS valuation burden is higher than reported. |
| C9 | ORCL leases | A8: $34.6B recorded leases | $34.6B operating + $9.2B finance = **$43.8B recorded**. Neither is in the $504.6B. A further $288B has not commenced (10-Q, A). | Lease-adjusted EV ≈ $549–557B. The $288B is shown as a memo item, not added to EV. |
| C10 | ORCL Q2 date | A6/A7: Dec 14 "confirmed" | Not announced by Oracle. Vendors show Dec 10 or Dec 14 (C). | **Downgrade to "estimated".** |
| C11 | ORCL capex | "95B" | FY27 guidance is $90–95B gross and ≤$70B net cash capex (call, B) | Use the range, and show net of customer prepayments separately. |
| C12 | CRWV FY26 guidance | "$13.2B revenue / $39B capex" | $12.4–13.2B revenue; $35–39B capex (call, B) | Top-of-range quoted as a point. Corrected. |
| C13 | CRWV Q2 capex | $9.4B | $9.4B is management's accrual figure. GAAP cash PP&E purchases were $6.42B (A). | For FCF use cash: H1 FCF = −$10.45B (CALC). |
| C14 | CRWV Sept convert | A8: $3.0B | Upsized and **settled at $4.2B**: 2.875% coupon, 4/1/2033 maturity, up to 52.6M shares (8-K, A) | Corrected. The CRWV FD EV ($78.0B) was **not re-performed** and should be refreshed for this. |
| C15 | CLS Q3 guide | "5.55B" | $5.25–5.55B, midpoint $5.40B; adj. EPS $2.88–3.08 (A) | Top of range quoted as a point. Corrected. |
| C16 | CLS normalized margin | A6/A7: 6.5–7.0% "full-cycle" | Adj. op margin history: 2.7% (2019) → 7.5% (2025). The 2019–25 average is 5.0–5.4%. No completed downturn exists in the post-2022 business mix (A). | **Anchor challenged.** 6.5–7.0% is a mid-cycle-to-favorable assumption, not a trough. Add a ~5.5% downside method. |
| C17 | CLS FD EV share count | $41.9B | It uses pre-offering shares. The Aug 2026 offering added 11.13M shares and $3.39B of cash; consistent FD EV = $42.8B (A). | Minor: +2.2%. Use $42.8B. |
| C18 | 12-month return bases | A7 table | SNDK, NBIS and CLS are measured from Oct 1, 2025; ORCL and QQQ from Sep 30, 2025. On a consistent Sep 30 base, SNDK is about +1,451% (not +1,337%), NBIS +110%, CLS +47%. | Mixed base dates. Restate on a single convention. |
| C19 | APLD earnings date | Oct 7 | Company: Oct 7 after the close. Benzinga/ScanX say Oct 8 (B). | **Oct 7** (company source controls). |

---

## 3. Corrected valuation anchors (Sep 30, 2026 close)

| Ticker | Prior FD EV | Re-performed FD EV | Status | Notes |
|---|---|---|---|---|
| SNDK | $269.2B | $268.4B (157M diluted shares; no debt; cash $4.76B) | Reproduced (−0.3%) | Multiples (CALC): 21.1x FY26 non-GAAP op income ($12.70B); ~8x FQ1-guided annualized op income; 8.1x FY27 consensus EPS. |
| ORCL | $504.6B | $505.5–513.5B excl. leases; $549–557B incl. $43.8B recorded leases | Reproduced, excl. leases | Memo: $288B uncommenced leases, 15–19 yr terms. |
| CLS | $41.9B | $42.8B (post-offering, 127.3M FD shares) | Reproduced (+2.2%) | Multiples: 34.6x TTM adj. op income; 24.9x FY26 guide; ~14.4x FY27 at 8.4%; ~17.2x at 7.0%. |
| NBIS | $67.5B | **$78.5–84.9B** | **Not reproduced** | 24.5–26.5x 2026 revenue midpoint ($3.2B). |
| CRWV | $78.0B | Not re-performed | Stale | Needs the $4.2B Sept convert, DDTL 5.5 draws, and leases ($16.5B recorded + $35.5B uncommenced). |
| APLD | $11.4B | Not re-performed | Stale | Needs Series E/E-1/G preferred, the 2030 converts (~46.1M shares), the CoreWeave warrant (13.06M at $7.19), and the restricted vs unrestricted cash split. |
| IREN | $17.85B | Not re-performed | Stale | — |

**APLD EV per MW** uses the same stale $11.4B numerator for all three figures:
- **$114M per revenue-producing MW** (100 MW)
- **$65M per RFS MW** (175 MW)
- **$14.3M per risk-adjusted MW** (~797 MW; the risk-adjustment method sits in the unavailable R0 record)

---

## 4. Obligation stacks (CALC; these mix discounted and undiscounted amounts, so indicative only)

**CRWV**
- Debt principal: $35.6B at 6/30/26; ~$39.8B pro forma for the Sept convert.
- Recorded leases: $16.5B.
- Uncommenced leases: $35.5B undiscounted, plus a separate site capped at $14.7B.
- Indicative total: **~$92B**.
- Interest: Q2 interest was 24.9% of revenue. The Q3 guide implies interest of 3.5–4.5x adjusted operating income.
- Maturities: $10.6B of principal matures by end-2027.
- Capacity: active power is 1.5 GW, or 36% of the 4.2 GW contracted.

**ORCL**
- Debt: $125.3B.
- Recorded leases: $43.8B.
- Uncommenced leases: $288B.
- Indicative total: **~$457B**.
- Cash flow: trailing four-quarter FCF = −$28.7B. Q1 operating cash flow included $11.4B of customer prepayments.
- RPO: due within 12 months ≈ $86B, against $90–95B of gross capex.

**APLD**
- Cash at 5/31/26: $1.59B unrestricted vs $2.56B restricted.
- Completion guarantees on three note issues.
- **No committed financing found for PF3, Delta Forge 1 or Delta Forge 2** (810 MW).
- No cost-to-complete disclosed.

---

## 5. Expectations-gap screen

Consensus data is Yahoo as of Oct 1 (grade B) unless noted.

| Ticker | Market expectation (consensus) | Management / evidence view | Comparable? | Gap | Status |
|---|---|---|---|---|---|
| CLS | FY27 revenue $35.45B; EPS $14.96, which implies ~7.0% adj. op margin at 127.3M shares (CALC) | 2027 revenue growth >65% with EPS growing faster than revenue on a higher margin (Jul 27 release, A). At 8.4%, FY27 EPS ≈ $18.18. | Yes: same FY, adjusted basis. The FY27 EPS source is a snippet (B/C). | ≈ **+21%** to EPS if the 8.4% margin holds | Candidate → Red Team |
| SNDK | FQ1 EPS $46.18, above the top of the $44–46 guide. FY27 EPS $213.90; FY28 $263.49. | Guided current-scale op margin ~79%. Consensus already models growth into FY28. | Yes | Not a near-term gap: consensus already sits above guidance. The debate is the multiple (8.1x FY27). | Candidate → Red Team |
| APLD | Q1 revenue $116–135M; consensus appears to exclude fit-out | Q4 FY26 fit-out alone was $152.4M, and fit-out runs at ~4.6% gross contribution | Not on a like-for-like basis | Any headline beat may be low-quality fit-out revenue. The real test is rent on the 75 MW. | Monitoring |
| CRWV, ORCL, NBIS, IREN | Not reconstructed | — | — | **Not verified.** | Agent 5 needed |

---

## 6. Thesis candidates and Red Team

*Pending; see §6 once Agent 8 returns.*

---

## 7. Research status by ticker

| Ticker | Status | Next decisive evidence | Date |
|---|---|---|---|
| APLD | Monitoring; anchors corrected | Rent or acceptance on the 75 MW; base rent vs fit-out split; PF3/Delta Forge funding | **Oct 7** (Q1 FY27) |
| CLS | Candidate; see §6 | FY27 margin framework; Q3 vs $5.25–5.55B / 8.4% guide; inventory and A/R sales | **Oct 27** |
| SNDK | Candidate; see §6 | GM vs 83–85%; FQ2 guide vs $12.23B consensus; NBM disclosure | **Oct 29** |
| CRWV | Monitoring; FD EV stale | Active vs contracted power; Q3 interest vs $860–940M guide; refinancing | Nov (estimated) |
| NBIS | Monitoring; **EV corrected upward** | Operating IT MW by site; ARR vs $7–9B target | Nov 10–13 (estimated) |
| IREN | Monitoring; overlap resolved (additive) | Horizon 2–4 acceptance; grace period runs mid-Q4 2026 to start of Q2 2027 | Q4 2026 |
| ORCL | Monitoring; leases corrected | RPO 12-month conversion; net capex vs ≤$70B; lease commencements | Dec 10 or 14 (unconfirmed) |

## 8. Missing evidence, still Not verified

- Consensus for CRWV, ORCL, NBIS, IREN.
- A dated consensus revision series for any name.
- Positioning data: short interest and options-implied moves.
- **APLD:**
  - Cost-to-complete.
  - Financing for PF3, Delta Forge 1 and Delta Forge 2.
  - Principal of the 2030 convertible notes.
- **IREN:**
  - The basis of the 40 MW figure.
  - The start date of GAAP revenue for Horizon 1.
- **NBIS:**
  - Operating IT MW.
  - Cash at Sep 30.
- **CRWV:**
  - Customer concentration within the backlog.
  - Draws on the DDTL 5.5 facility.
- **ORCL:**
  - Customer concentration within RPO.
- **SNDK:**
  - NBM contract terms. This is being worked by Agent 8.
- Sector-benchmark and peer-basket relative performance (only QQQ is available).
- 6-month returns for five names.

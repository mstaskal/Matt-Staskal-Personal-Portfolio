# Group 7 Project Notes: NFL Ad Package Optimization

Running notes so the project context survives between sessions.
Last updated: 2026-09-28 (end of the "getting up to speed" review, before next steps).

---

## 1. Project context

- **Class:** Applied Optimization, group project (Group 7).
- **Requirement:** build an optimization problem around a real-world scenario, using real data.
  (Rubric details not reviewed here. The notebooks cite: at least 50 decision variables,
  50 constraints, 3 constraint families, and two conflicting objectives.)
- **Scenario (from Ed, who works at an ad agency):** a CBS affiliate sells season-long NFL ad
  packages (one :30 spot in each of 27 games). The station picks which advertisers to sell to
  and at what price, while ratings are uncertain. If delivered ratings fall short of what was
  promised, the station owes makegoods (underdelivery penalties), which differ by advertiser.
- **The core problem:** Ed's real-world detail (guarantees, discounts, game-level pricing,
  CPM adjustments, reallocating salespeople after the schedule comes out) has made the model
  hard to follow, in code, in theory, and as a business story.
- **Guiding constraint:** the final model should stay close to the level and style of the
  base model (below): something the group can understand and explain, and that the professor
  will recognize as matching class work (gurobipy, plain dictionaries, `addVars`,
  `addConstrs`, `quicksum`).

---

## 2. Files (repo root, `main`)

| File | What it is |
|---|---|
| `Group7_Project_setup_code.ipynb` | Base model. Theoretical data, class-level complexity and style. The yardstick. |
| `Group7_PlanA_Skeleton.ipynb` | Plan A outline. The model chooses the guarantee level itself (345 vars, 167 constraints). |
| `Group7_PlanB_Skeleton.ipynb` | **Plan B outline. The agreed target.** Loops over guarantee levels outside the model (126 vars, 70 constraints). |
| `NFL Ad PKG MAIN.xlsx` | Ed's real data, 5 tabs. **Use this, not the CSV.** |
| `NFL Ad PKG MAIN.csv` | Only the "Schedule Release 1-Min Qualifier" tab (a CSV can't hold tabs). Its row/column positions are shifted one up and one left from the .xlsx. |

Note: the notebooks point to `data/raw/NFL_Ad_PKG_2.xlsx`; the file in the repo is `NFL Ad PKG MAIN.xlsx`.

---

## 3. Base model summary (`Group7_Project_setup_code.ipynb`)

- 30 prospects (goal CPM, penalty per missing viewer), 4 packages
  (conservative 1.8M / $90K / $50.00 CPM, medium 2.1M / $100K / $47.62,
  premium 2.5M / $110K / $44.00, aggressive 3.0M / $125K / $41.67).
- Expected penalty and expected profit are precomputed for every customer-package pair.
- Binary `x[c,s]`; constraints: at most one package per customer, package CPM <= goal CPM,
  at most 20 spots. Objective: maximize expected profit.
- Result: 20 spots sold, revenue $1,970,000, expected penalties $300,500,
  expected profit $1,669,500.

### Base model cleanup items (to fix as we go)

1. The "Underdelivery Factor" column in the prospect table isn't used in the code.
2. A comment says "exactly 20" spots, but the constraint is `<= 20`.
3. "Grocery Store A" appears twice (C03 and C24). *Fixed in the .xlsx: C24 is now "Grocery Store C".*
4. **Scenario probabilities:** the setup text lists 80% / 60% / 45% / 35% as if they were
   scenario probabilities, but they are "at least this many viewers" (cumulative) probabilities
   and sum to 220%. The code correctly converts them to range probabilities
   (20% / 20% / 15% / 10% / 35%). The write-up should say they are "at least" probabilities
   and show the derived table.
5. State two assumptions openly in the write-up:
   - 1.5M is a chosen stand-in value for the "below 1.8M" range.
   - Each range is valued at its lower bound (e.g., 1.8M-2.1M counts as 1.8M), which slightly
     overstates expected penalties (a cautious, defensible choice).

---

## 4. Data map (`NFL Ad PKG MAIN.xlsx`)

All cell references below match the notebooks' references.

- **Pre-Schedule Release** (July, Stage 1 view): 5 game types, rows 13-17, totals row 18.
  27 games, $108,000, 1631.3 thousand households (000s), package CPM $66.20.
  "Regional" = KC, MIN, CHI, GB (cost more).
- **Schedule Release** (August, Stage 2 view): 27 actual games, rows 13-39, totals row 40.
  Original 000s 1651.38; Revised 000s 1465.938 (low-interest cuts: x0.7 for one low-interest
  team, x0.6 for two; only game 25, NO/CIN, has two). All cuts verified against the team list.
- **Schedule Release 1-Min Qualifer** (sheet name spelled this way): same 27 games and identical
  Revised 000s, plus cols M-O (+15/20/25% bumps; totals 1685.83 / 1759.13 / 1832.42) and the
  scenario table at T6:U8 (probabilities 50% / 35% / 15%). The notebooks read this tab.
- **Prospect Data Table**: rows 4-33. Same 30 prospects and goal CPMs as the base model, plus
  salesperson (SP1-SP6, 5 prospects each), close ratio, and 2x/3x/4x penalties
  (replacing the base model's 0.05-0.25).
- **Salesperson Table**: rows 5-9. 12 hours available, 3.75 (col F) and 5 (col G) hours.

### Data flags

1. SP6 is missing from the Salesperson Table (owns 5 prospects, close ratio 0.62).
2. Cols F and G in the Salesperson Table have the same header. Notebooks assume F = hours per
   fix, G = hours per new sale.
3. Hours conflict: spreadsheet says 12 available / 3.75 / 5; Ed's plan doc says 8 / 3.5 / 3.
4. Col E of the Salesperson Table reads "Known after optimization of stage 1, 2, 3, 4, 5":
   looks like an Excel autofill slip. Harmless (not read by the notebooks).

---

## 5. Plan B summary (the target)

- **Stage 1 (July):** binary `pitch[i,d]`, pitch prospect i at discount d (0 / 5 / 10%).
  A pitch counts as `p_close[i,d]` of an expected sale.
- **Stage 2 (August, per Nielsen scenario):** integer `sell[k,s]` and `fix[k,s]` per
  salesperson. A fix swaps the 2x-4x makegood for Local News at 1.75x.
- **Guarantee level** (0 / 15 / 25%) is looped outside the model.
- **Two objectives:** maximize expected revenue; minimize expected makegood cost.
  Trade-off curve by capping makegood cost at a series of budgets and maximizing revenue.
- All "set to 0 if negative" math happens in pandas before Gurobi, so the model stays linear.
- Open questions for Ed and decisions for Sunday are listed at the end of the Plan B notebook.

---

## 6. Observations after review (hold; don't fix yet)

1. **The timeline and the scenarios don't match (biggest issue).** What becomes known in August
   is the *schedule* (the dud games), but Plan B gives Stage 2 a separate plan for each
   *Nielsen* scenario, as if salespeople in August knew the 1-minute-rule bump (not known until
   the season is underway). Meanwhile the schedule is treated as known with certainty. The Sunday
   questions "one model or two?" and "per scenario or expected delivery?" both come from this.
2. **Neither version of the goal CPM rule works well with this data.**
   - Hard cutoff: at a 0% guarantee even the 10% discount gives $59.58 CPM, above every goal
     (max $58.81), so nobody can be pitched.
   - Slope (0.0025): a $40-goal prospect offered $66 still keeps 44% of a 60% close chance,
     so goal CPM barely matters.
3. **Stage 2 sales carry no risk.** An August sale counts as a certain $108K with no close
   probability and no makegood exposure; presales carry both. That imbalance may drive results
   more than any real trade-off.
4. **The trade-off only appears at the highest guarantee.** With the package-total shortfall,
   0% never underdelivers, and in the July view only 25% does, so the two-objective curve may
   have little to show at lower levels.
5. **Some complexity is there only to hit rubric counts** (e.g., fixes by salesperson and
   scenario, splitting Ed's one profit objective into two). Fine where it matches a real
   decision; otherwise it's what makes the model hard to explain.

**Direction:** aim for a Plan B that is a direct extension of the base model: keep the familiar
skeleton (binary assign-a-package decision, precomputed expected values) and add one or two of
Ed's real features, each chosen because it creates a clear trade-off. Every kept feature should
be explainable in one sentence.

---

## 7. Build plan (agreed)

Start from the base model and add Plan B's features one at a time. Check and explain each
before moving on; stop when it meets the rubric and every part can be explained (the MVP).
Each step gets its own notebook.

1. **Tidy the base model.** `Group7_Step1_Base_Model.ipynb`. Done: cleanup items 1-5 in
   section 3 fixed, `scenarios` renamed to `packages`, unused code removed.
   Results identical to the original ($1,669,500 expected profit).
2. **Real-data base model.** `Group7_Step2_Real_Data.ipynb`. Done: same model, data read from
   `NFL Ad PKG MAIN.xlsx`. Packages = guarantee levels 0/15/20/25% (team assumption) on the
   $108K package; outcomes = the 3 Nielsen scenarios; penalty = multiplier x shortfall x package CPM.
   Result: 8 of 20 sold, revenue $864,000, expected penalties $87,066, expected profit $776,934.
   Only 8 prospects meet their goal CPM even at +25% (observation 2 in action).
3. **Add features one at a time:** (a) discounts (`Group7_Step3a_Discounts.ipynb`, done:
   discounts 0/5/10%, x[c,p,d], 360 vars / 391 constraints; 17 of 20 sold, revenue $1,695,600,
   expected penalties $85,710.60, expected profit $1,609,889.40; model trades discount vs.
   guarantee by penalty multiplier, e.g. C26 2x takes risk, C25 4x takes discount), (b) close probability (SKIPPED, see below), (c) schedule
   release / dud-game cuts, (d) two objectives + trade-off curve, (e) salesperson hours only if needed.
4. **Rubric check and write-up.**

Work happens on branch `claude/project-explanation-context-i37v2a`.

## 8. Assumptions to confirm with Ed

1. Guarantee levels of 0 / 15 / 20 / 25% (chosen to match the Nielsen increases; Plan B used 0 / 15 / 25%).
2. The missing audience is valued at the package CPM.
3. **The makegood is valued at the CPM the customer actually paid, after the discount** (Step 3a).
4. Discount options of 0 / 5 / 10%.

**Team modeling assumption (not for Ed):** a prospect whose goal CPM is met buys the package; we
don't model the chance a sale falls through. Step 3b (close probability) was skipped on purpose:
as a simple multiplier it scales every option for a customer equally, so it changes no decisions;
the version where odds fall above goal CPM (Plan B's idea) adds an unsupported assumption and makes
the first decision hard to explain. Mention it in the write-up as a possible extension.

## 9. Status

- Done: walked through the project, base model, both plans, and all data tabs.
- Done: Step 1 (tidy base model). Kept 1.5M stand-in as a stated assumption (0 would give
  expected profit $936,000 vs $1,669,500; goes away with real data).
- Done: Step 2 (real-data base model).
- Done: Step 3a (discounts).
- Step 3b skipped (see section 8).
- Next: Step 3c (schedule release / dud-game cuts).
- Reminder for running any notebook: keep `NFL Ad PKG MAIN.xlsx` in the same folder as the
  notebook, and make sure `openpyxl` is installed (Anaconda includes it).

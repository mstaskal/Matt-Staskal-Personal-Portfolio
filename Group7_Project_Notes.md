# Group 7 Project Notes: NFL Ad Package Optimization

Running notes so the project context survives between sessions.
Last updated: 2026-10-03 (MVP reviewed with professor; now writing the final report).

---

## RESUME HERE (saved 2026-09-28)

**To pick back up:** start a new session and say *"Read `Group7_Project_Notes.md` and let's pick up
where we left off."* Everything needed is in this file.

**Where we stopped:** the MVP is done and delivered for the group meeting. Matt is reviewing it with
the group and will come back with decisions and Ed's answers.

**Update 2026-10-03:** the group meeting went well, and the professor reviewed the MVP and liked it.
Group members are finalizing the notebook; Matt is writing the **Model** section of the final report.
The `.to_numpy()` chart fix worked on Matt's machine (old matplotlib + new pandas).

**Where the files are (on `main`):**
- `AO_Group_7_Project/`: everything for the meeting: `Group7_MVP_Model.ipynb`,
  `Group7_MVP_Meeting_Guide.md`, `Group7_MVP_Tradeoff.png`, `NFL Ad PKG MAIN.xlsx`, `clean_data/`,
  a copy of these notes, and a README.
- Repo top folder: the step notebooks (`Group7_Step1` ... `Group7_Step3d`), the original setup notebook,
  the Plan A/B skeletons, the data files, and these notes. Step notebooks stay there for now (Matt's choice).
- Working branch `claude/project-explanation-context-i37v2a` = `main` (everything merged).

**MVP in one line:** 30 prospects x 4 guarantee levels x 3 discounts = 360 binary variables; 62
constraints in 4 families (one package per customer, CPM requirement per customer, 20-package
inventory, makegood budget); 2 objectives (max expected revenue vs. min expected makegood cost),
traced as a trade-off curve. Max-profit point: $1,690,200 revenue, $504,307 makegoods,
$1,185,893 profit, 17 of 20 sold.

**Waiting on the group meeting (decisions):**
1. Balance point: max-profit point (proposed) or a more cautious one? Must be defended in the report.
2. Dud games: keep (real risk, timeline simplification) or remove (clean timeline, ~$215K risk)?
3. Simplify: remove the conservative package (identical results, 270 vars)?
4. Next extension, if any: salesperson hours (Plan B's Stage 2 / Step 3e, skipped so far)?
5. Report assignments.

**Waiting on Ed (most important):**
1. Are the prospect goal CPMs and 2x/3x/4x multipliers real station data? They're identical to the
   theoretical base model; the rubric forbids made-up or AI-generated data.
2. Sources of the Nielsen probabilities, low-interest cuts, rates, and audience estimates.
3. What was anonymized/rescaled, and why.
4. Permission to share (ask the professor before Week 5 if unsure).
5. Confirm the assumptions in section 9.

**Before final submission (to do when Matt says so; not done yet):**
1. **Remove `import course_utils`** from the MVP notebook. Nothing uses it, and if the professor
   doesn't have that file, the first cell fails. (Alternative: include `course_utils.py` in the zip.)
2. **Add a friendly missing-file check** right after `RAW_FILE = ...`:
   `if not os.path.exists(RAW_FILE): raise FileNotFoundError("Can't find '...'. Unzip the project and
   keep the .xlsx in the same folder as this notebook.")`
3. **README: openpyxl note.** If pandas says "Missing optional dependency 'openpyxl'", run
   `%pip install openpyxl` in a cell (or `conda install openpyxl` / `pip install openpyxl`), then
   restart the kernel. **Fallback:** openpyxl is only needed for Part 1 (reading the raw .xlsx); the
   zip includes `clean_data/`, so skipping Part 1 still runs Parts 2+ with the same results.
4. **README: unzip first**, and open the notebook from inside the unzipped folder (relative paths
   `RAW_FILE`/`CLEAN_DIR` work on any OS as long as the folder stays together and nothing is renamed).
5. **Chart fix:** in the first `ax.plot(...)`, use `df_results["penalty"].to_numpy() / 1000` and
   `df_results["revenue"].to_numpy() / 1000` (works with old and new matplotlib/pandas).
6. **README: clean environment** for anyone with version errors:
   `conda create -n ao python=3.11 numpy pandas matplotlib openpyxl jupyter`, `conda activate ao`,
   `pip install gurobipy`. Use conda (not pip) for everything except gurobipy.
7. **Data visibility:** the repo is **public**, so Ed's `.xlsx` is visible online. Check with Ed; if
   not OK, move the project to a private repo (removing the file alone leaves it in git history).
   For the group, share via the zip in Teams (Files tab) rather than the public repo link.

**How Matt likes to work (keep doing this):**
- Go slowly, one step at a time; confirm understanding before moving on (a "10-4" when Matt is
  just explaining).
- Keep complexity minimal and explainable in class terms (gurobipy, dicts, `addVars`/`addConstrs`/
  `quicksum`, same style as the base model). Every feature must create a real decision.
- After each step: push to GitHub, show the updated code in chat, and give a plain-language overview.
- Always remind: use the `.xlsx` (not the `.csv`), keep it in the same folder as the notebook, and
  `openpyxl` must be installed (Anaconda includes it).
- Merge to `main` when Matt asks. Don't open pull requests unless asked.
- Hold observations and fixes until Matt is ready for them; ask before design forks (like Step 3b).

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
   guarantee by penalty multiplier, e.g. C26 2x takes risk, C25 4x takes discount),
   (c) schedule release (`Group7_Step3c_Schedule_Release.ipynb`, done: actual audience =
   revised_000s x (1 + increase); 17 sold, revenue $1,690,200, expected penalties $504,307.43,
   expected profit $1,185,892.57; only C26 switches to medium 5% off),
   (d) two objectives + trade-off (`Group7_Step3d_Tradeoff.ipynb`, chart
   `Group7_Step3d_Tradeoff.png`, done: maximize revenue vs. minimize makegood cost via a
   makegood budget constraint (Constraint 4), 10 budget levels + Ed's point; 360 vars,
   392 constraints, 4 families, 2 objectives. Curve: ~$5 revenue per $1 risk at the left,
   Ed's max-profit point at $504,307 risk / $1,690,200 revenue / $1,185,893 profit;
   last $203K of risk buys only $70K revenue (shift to aggressive at smaller discounts)), (b) close probability (SKIPPED, see below), (c) schedule
   release / dud-game cuts, (d) two objectives + trade-off curve, (e) salesperson hours only if needed.
4. **Rubric check and write-up.** Done (MVP for the group meeting, not the final project):
   `Group7_MVP_Model.ipynb`, `Group7_MVP_Meeting_Guide.md`, `Group7_MVP_Tradeoff.png`, `clean_data/`.
   Rubric fixes: CPM rule rewritten per customer (the old `x <= eligible` was a single-variable
   bound, which the rubric doesn't count: 32 -> 62 non-trivial constraints, 4 families);
   tie-breaker so the riskiest end of the curve is well defined; raw -> clean CSVs, model reads
   only clean files; team assumptions in their own cell. Removal tests: conservative package and
   inventory limit can go with identical results; CPM rule, discounts, guarantees, budget cannot.

Work happens on branch `claude/project-explanation-context-i37v2a`.

## 8. Key concepts (for our own understanding and the presentation)

### Why discounts matter: they create the trade-off

**The one-sentence version:** there are two ways to lower a customer's price per thousand:
promise more audience (a bigger guarantee, which is risky) or charge less (a discount, which costs
money for certain). The model picks the cheaper way for each customer, based on their penalty
multiplier.

**Without discounts (Step 2), there is no real decision:**
- The only way to lower the CPM is a bigger guarantee, so the answer is one rule: give each
  customer the smallest guarantee that meets their goal CPM.
- Only 8 of 30 prospects qualify; the 20-spot limit never matters.
- The only way to cut risk is to drop customers, so the revenue-vs-risk trade-off (Step 3d)
  would be a few jumps across 8 customers.
- A professor could fairly ask why this needs an optimizer.

**With discounts (Step 3a), every customer is a real choice between risk and revenue:**
- 17 prospects buy, and expected profit roughly doubles ($776,934 to $1,609,889).
- **C26 (2x penalty)** takes premium at full price: $108,000 - $4,500 expected penalty =
  $103,500, beating medium at 5% off ($102,600). Low multiplier: the risk is cheaper than
  the discount.
- **C25 (4x penalty)** takes medium at 5% off: $102,600 with no risk, beating premium at
  full price ($108,000 - $9,000 = $99,000). High multiplier: the discount is cheaper than
  the risk.
- In Step 3d, cutting makegood risk means moving customers from "big guarantee, full price"
  to "safe guarantee, a bit off", so each point on the trade-off curve is a meaningful
  business choice.
- After Step 3c (dud-game cuts), guarantees fall short more often, so discounts become the
  station's main protection, and matter even more.

**Contrast with the close ratio (Step 3b, skipped):** discounts change *which* option each
customer gets; the close ratio would only have scaled every option equally and changed no
decisions. That's the test for every feature we keep: does it create a real decision?

## 8b. Step 3c: schedule release (DONE, minimal version chosen)

**What the schedule does:** after the dud-game cuts, the package baseline drops from 1631.3 to
1465.938 (000s) (total of col I, 'Schedule Release 1-Min Qualifer'). Delivered audience:

| Nielsen increase | July view (no duds) | August view (duds cut) |
|---|---:|---:|
| +15% | 1,876.0 | 1,685.8 |
| +20% | 1,957.6 | 1,759.1 |
| +25% | 2,039.1 | 1,832.4 |

In the August view, every guarantee above 0% falls short in every scenario (medium, risk-free in
Step 3a, now misses by 44-190).

**Effect on the Step 3a plan:**

| | Expected penalties | Expected profit |
|---|---:|---:|
| Step 3a plan, as July expects it | $85,711 | $1,609,889 |
| Same plan, after the August schedule | $513,444 | $1,182,156 |
| Re-planned knowing about the duds | $504,307 | $1,185,893 |

- Dud games multiply makegood risk about 6x (Ed's real-world problem).
- Re-planning barely changes decisions (only C26 switches: premium 0% off -> medium 5% off;
  +$3,700). With one profit objective, every sale still pays for itself.
- This sets up Step 3d: ~$500K of risk gives the revenue-vs-risk trade-off real weight
  (vs. only $86K without 3c).

**Proposed minimal 3c:** load `revised_000s` (1465.938); change one line so
actual audience = `revised_000s x (1 + increase)`; guarantees and CPMs stay on the July baseline
(that's what was promised); comparison table goes in the markdown, no extra code.

**Timeline caveat (state in the report):** the station really sells in July, before it knows the
duds. The model plans as if it expects the dud cuts, using the August schedule as its best estimate
("the station plans for dud risk"). Reacting after the schedule (Plan B's salesperson stage) is the
natural extension.

**Alternative considered:** keep the July view and only evaluate against August in a separate cell.
Avoids the caveat, but Step 3d would then work with the small $86K risk.

## 9. Assumptions to confirm with Ed

1. Guarantee levels of 0 / 15 / 20 / 25% (chosen to match the Nielsen increases; Plan B used 0 / 15 / 25%).
2. The missing audience is valued at the package CPM.
3. **The makegood is valued at the CPM the customer actually paid, after the discount** (Step 3a).
4. Discount options of 0 / 5 / 10%.

**Team modeling assumption (not for Ed):** a prospect whose goal CPM is met buys the package; we
don't model the chance a sale falls through. Step 3b (close probability) was skipped on purpose:
as a simple multiplier it scales every option for a customer equally, so it changes no decisions;
the version where odds fall above goal CPM (Plan B's idea) adds an unsupported assumption and makes
the first decision hard to explain. Mention it in the write-up as a possible extension.

## 10. Status

- Done: walked through the project, base model, both plans, and all data tabs.
- Done: Step 1 (tidy base model). Kept 1.5M stand-in as a stated assumption (0 would give
  expected profit $936,000 vs $1,669,500; goes away with real data).
- Done: Step 2 (real-data base model).
- Done: Step 3a (discounts).
- Step 3b skipped (see section 8).
- Done: Step 3c (minimal version: plan for the duds; see section 8b).
- Done: Step 3d (two objectives + trade-off curve). All rubric counts met.
- Step 3e (salesperson hours) skipped for now.
- Done: Step 4 (MVP notebook + meeting guide).
- Next: group meeting. Decisions: balance point, keep/remove dud games, simplify, next extension,
  report assignments. **Most important:** Ed's answers on data provenance (prospect goal CPMs are
  identical to the theoretical base model; must be real data per the rubric).
- Reminder for running any notebook: keep `NFL Ad PKG MAIN.xlsx` in the same folder as the
  notebook, and make sure `openpyxl` is installed (Anaconda includes it).

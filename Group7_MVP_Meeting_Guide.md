# Group 7 MVP: Meeting Guide

**Purpose of the meeting:** walk through the MVP model together so everyone understands it, and make
the key decisions for the final project. **The MVP is not the final project.**

Main file: `Group7_MVP_Model.ipynb`. Everything below is also explained in that notebook.

---

## Notes to remember

1. **Use `NFL Ad PKG MAIN.xlsx`, not the `.csv`.** The `.xlsx` has all 5 tabs; the `.csv` has one tab
   and is not the raw data.
2. **Keep the `.xlsx` in the same folder as the notebook.** The code opens it by name.
3. **`openpyxl` must be installed** (pandas uses it to read `.xlsx`). Anaconda includes it, and `matplotlib`.
4. **Run cells top to bottom.** Part 1 creates `clean_data/`, which Part 2 reads.
5. **Never edit the raw spreadsheet.** The rubric requires the original. All changes go in code.
6. The sheet name `'Schedule Release 1-Min Qualifer'` is misspelled in Ed's file; the code matches it.

---

## Suggested walk-through (about 60 minutes)

| Time | Topic | Where |
|---|---|---|
| 5 min | The story: what the station decides, and why it's hard | Notebook: "The problem" |
| 10 min | Data: raw file → clean files, and the checks | Parts 1-2 |
| 5 min | Team assumptions: what's ours vs. Ed's | Part 3 |
| 15 min | The model: sets, variable, 4 constraint families, 2 objectives | Part 4 (math + plain-words table) |
| 10 min | Solving and reading the trade-off curve | Parts 5-6 |
| 15 min | Decisions (below) | Notebook: "Decisions for the group meeting" |

---

## The model in five sentences

1. The station sells one $108,000 package (27 games) and decides, for each of 30 prospects,
   **which guarantee (0/15/20/25%) and which discount (0/5/10%)**, or no sale.
2. A customer only buys if the **CPM they pay is at or below their goal CPM**.
3. There are two ways to lower the CPM: **promise more audience** (risky: if the station falls short,
   it owes a makegood of 2x-4x the missing audience's value) or **charge less** (costs revenue for certain).
4. Dud games and the uncertain Nielsen increase mean **every guarantee above 0% can fall short**.
5. The two goals conflict: **maximize expected revenue vs. minimize expected makegood cost.** The
   trade-off curve shows the best revenue for every level of risk.

---

## Key concepts to be able to explain

**Why discounts matter.** Without discounts, the only way to lower CPM is a bigger guarantee, so each
customer gets the smallest guarantee that works, and the only way to cut risk is to turn customers
away. Only 8 prospects can buy, and the max-profit plan is just "sell to all 8." Nothing to balance.
With discounts, each customer is a real choice: a 2x-penalty customer (C26 in Step 3a) takes the
risk; a 4x-penalty customer (C25) takes the discount.

**Why this is the minimum complexity** (each piece tested by removing it):

| Remove... | What happens |
|---|---|
| Guarantees | No makegood risk, so no second objective |
| CPM requirement | Sell 20 at full price, no guarantee: $2.16M revenue, $0 risk. No conflict; only 32 constraints |
| Discounts | Only 8 buyers; max profit = sell everyone; no real trade-off |
| Makegood budget | Only one point, no trade-off curve |
| One package per customer | Unrealistic (a customer buying several packages) |

**How to read the curve.** Steepness = revenue per extra dollar of risk. Steep at the left (~$5 per $1),
flat at the right (the last $203K of risk buys $70K). The max-profit point is where extra risk stops
paying for itself.

**Rubric counts (printed by the notebook from Gurobi):** 360 variables; 62 constraints, none of them
bounds on a single variable; 4 structurally distinct families (one package per customer, CPM
requirement, station inventory, makegood budget); 2 conflicting objectives.

---

## Decisions to make

1. **How we balance the objectives** (the rubric says we decide and defend).
   - Proposal: **max-profit point** ($1,690,200 revenue, $504,307 makegood cost, $1,185,893 profit).
     Defense: up to this point, each extra dollar of risk brings in more than a dollar of revenue.
   - Alternative: a cautious point, e.g. the $353K budget: $161K less profit, 30% less exposure.
2. **Dud games: keep or remove?**
   - Keep: real risk (~$500K), Ed's real-world problem. Cost: we assume the station anticipates duds
     in July (a timeline simplification).
   - Remove: clean timeline, but risk is only ~$215K, and 10 customers buy with no risk at all.
3. **Simplify?** The conservative package is never bought. Removing it changes nothing (270 variables).
   Removing the inventory limit also changes nothing today, but leaves exactly 3 families (not recommended).
4. **Next extension?** Salesperson hours after the schedule (Plan B's Stage 2). It addresses the
   timeline issue, but it's the most complex piece. Skip unless needed.
5. **Report assignments**, including the data provenance paragraph.

---

## Questions for Ed (data provenance: the most important item)

1. **Prospect table:** are the goal CPMs and 2x/3x/4x multipliers real (anonymized or rescaled) station
   data? They're identical to our original theoretical base model. If they were made up, by us or with
   AI help, the rubric doesn't allow them, and we need real ones.
2. **Sources:** where do the Nielsen probabilities (50/35/15%), the low-interest team list and the
   30%/40% cuts, the rates, and the audience estimates come from?
3. **Anonymization:** what was changed (market name, prospect names, numbers), and why?
4. **Permission to share:** if unsure, ask the professor **before Week 5**.
5. **Confirm our assumptions:** guarantee levels, discounts, makegood valued at the discounted CPM,
   package-total (not game-by-game) shortfall.

The notebook has a provenance paragraph template to fill in once Ed answers.

---

## Questions the professor may ask

- **"Why isn't the close ratio used?"** It multiplies every option for a customer equally, so it
  wouldn't change who we sell to or how. We assume a customer whose goal CPM is met buys.
- **"The station sells in July. How does it know the dud games?"** It doesn't. We assume it plans for
  dud risk using the August schedule as its best estimate, and state this as a simplification.
  Reacting after the schedule is the natural extension.
- **"Why is the curve bumpy?"** Each sale is yes/no, so the best plan can jump between budgets.
- **"What's the tie-breaker?"** Among plans with equal revenue, prefer less risk. It's too small to trade
  real revenue for risk; it just makes the riskiest end of the curve well defined.
- **"Why these guarantee levels and discounts?"** Guarantees match the three Nielsen increases (plus
  none); discounts are a team choice. Both are listed as assumptions to confirm with Ed.

---

## File map

| File | What it is |
|---|---|
| `Group7_MVP_Model.ipynb` | **The MVP.** Start here |
| `Group7_MVP_Meeting_Guide.md` | This guide |
| `Group7_MVP_Tradeoff.png` | The trade-off chart |
| `clean_data/` | Clean files the model reads (created by the notebook) |
| `NFL Ad PKG MAIN.xlsx` | Ed's raw data (submit as is) |
| `Group7_Step1` ... `Group7_Step3d` | How we built up to the MVP, one idea at a time |
| `Group7_Project_Notes.md` | Full project notes and history |

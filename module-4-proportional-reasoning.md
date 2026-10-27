# SSA Math Coaching Module 4 Specification
## Title: Proportional Reasoning, Unit Rates & Scale Transformations

---

### 1. Module Overview & Standard Alignment
* **5th Grade Baseline Standards:**
  * **NC.5.OA.3:** Generate two numerical patterns from rules, plot ordered pairs on a coordinate plane (Quadrant I), and analyze relationships.
  * **NC.5.MD.1:** Convert measurement units within a given system.
* **6th Grade Acceleration Bridge Standards:**
  * **NC.6.RP.1:** Understand ratio concepts as multiplicative relationships between quantities.
  * **NC.6.RP.2:** Understand and find equivalent unit ratios ($1:n$ and $n:1$).
  * **NC.6.RP.3:** Use ratio tables, double number lines, tape diagrams, and coordinate graphs to solve real-world problems.
  * **NC.6.RP.4:** Solve percent problems using ratios and benchmark percents.

---

### 2. The SSA Rigor Jump
* **Standard Classroom Question:** Find the unit rate if 4 pounds of peaches cost $5.00.
* **SSA Rigor Acceleration:** "Recipe A uses 5 lemons for every 2 quarts of water, while Recipe B uses 2 lemons for every 1 quart of water. Plot both ratio relationships on a single dynamic coordinate plane with origin $(0,0)$. Calculate both unit ratios for each recipe ($\text{lemons per quart}$ and $\text{quarts per lemon}$). Determine which recipe has a stronger lemon taste and explain how the slope/steepness of the plotted lines visually proves your conclusion."

---

### 3. Interactive Visual Model Technical Specification
* **Component Name:** `SynchronizedRatioRayPlotter` (SVG / Canvas 3-in-1 Widget)
* **Visual Mechanics:**
  * Linked 3-pane interface: Ratio Table $\leftrightarrow$ Double Number Line $\leftrightarrow$ Coordinate Grid $(x,y)$.
  * Editing a cell in the Ratio Table dynamically animates coordinate points along the ray passing through $(0,0)$.
  * Comparative Ray Toggle: Plots Recipe A ($y = 2.5x$) and Recipe B ($y = 2x$) simultaneously with interactive slope angle readouts.
* **State Machine Interface:**
  ```typescript
  interface RatioRayPlotterState {
    recipeA: { name: string; lemons: number; quarts: number; unitRate: number }; // 2.5 lemons/qt
    recipeB: { name: string; lemons: number; quarts: number; unitRate: number }; // 2.0 lemons/qt
    activeView: 'table' | 'numberLine' | 'coordinateGrid';
    plottedPointsA: Array<[number, number]>;
    plottedPointsB: Array<[number, number]>;
    selectedUnitRatioMode: 'lemonsPerQuart' | 'quartsPerLemon';
  }
  ```

---

### 4. 4-Stage Pedagogical Loop Execution Blueprint
1. **Stage 1: Deconstruct & Visualize**
   * *Knowns:* Recipe A $= 5\text{ lemons} : 2\text{ qts}$; Recipe B $= 2\text{ lemons} : 1\text{ qt}$.
   * *Target:* Unit rates $\frac{\text{lemons}}{\text{quart}}$ and visual slope comparison.
   * *Manipulative Action:* Populate ratio tables, scale Recipe A to $1\text{ qt} \implies 2.5\text{ lemons}$, and plot rays on coordinate grid.
2. **Stage 2: Pathway Reconstruction**
   * *Sanity Check:* "Will $5\text{ lemons for } 2\text{ quarts}$ be stronger or weaker than $2\text{ lemons for } 1\text{ quart}$?" ($5/2 = 2.5 > 2.0 \implies$ Recipe A is stronger).
   * *Logical Pathway:* Step 1: Calculate unit rate A: $5 \div 2 = 2.5\text{ lemons/qt}$. Step 2: Calculate unit rate B: $2 \div 1 = 2.0\text{ lemons/qt}$. Step 3: Compare $2.5 > 2.0$. Steeper ray $y = 2.5x$ proves higher concentration per water unit.
3. **Stage 3: Distractor Forensics**
   * **Option A (Recipe A is stronger at $2.5\text{ lemons/qt}$ vs $2.0$ - Target):** Correct unit rate calculation and slope interpretation.
   * **Option B (Recipe B is stronger - Additive Fallacy Trap):** Compares differences $5 - 2 = 3$ vs $2 - 1 = 1$, misinterpreting raw numbers without scaling to unit water.
   * **Option C (Both recipes taste identical - Misscaling Trap):** Claims $5:2$ and $2:1$ are equivalent by rounding $2.5 \approx 2$.
   * **Option D (Recipe A needs $0.4\text{ qts/lemon}$ - Inverse Unit Ratio Confusion):** Calculates inverse unit rate $\text{quarts per lemon}$ ($2 \div 5 = 0.4$) but mistakes smaller number for weaker taste.
4. **Stage 4: Curiosity Engine**
   * *What-If Toggle:* "What if we mix 1 quart of Recipe A with 1 quart of Recipe B?"
   * *Invariance Discovery:* Combined mixture has $2.5 + 2 = 4.5\text{ lemons}$ in $2\text{ quarts} \implies 2.25\text{ lemons/qt}$. The combined unit rate is the exact arithmetic mean of the two individual unit rates.

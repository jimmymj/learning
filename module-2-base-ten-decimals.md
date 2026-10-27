# SSA Math Coaching Module 2 Specification
## Title: Base-Ten Operations, Decimal Precision & Multi-Digit Fluency

---

### 1. Module Overview & Standard Alignment
* **5th Grade Baseline Standards:**
  * **NC.5.NBT.1:** Recognize place value relationships where a digit in one place represents 10 times or $1/10$ of the place to its left/right.
  * **NC.5.NBT.3:** Read, write, and compare decimals to thousandths.
  * **NC.5.NBT.5:** Fluently multiply up to 3-digit by 2-digit numbers using standard algorithm / area models.
  * **NC.5.NBT.6:** Find whole-number quotients with up to 4-digit dividends and 2-digit divisors using area models and partial quotients.
  * **NC.5.NBT.7:** Add, subtract, multiply, and divide decimals to thousandths using concrete models or drawings.
* **6th Grade Acceleration Bridge Standards:**
  * **NC.6.NS.2:** Fluently divide using long division with multi-digit divisors and interpret contextual remainders.
  * **NC.6.NS.3:** Fluently add, subtract, multiply, and divide multi-digit decimals using standard algorithms.
  * **NC.6.NS.4:** Find GCF and LCM; apply the distributive property to factor sums ($a \cdot b + a \cdot c = a(b + c)$).

---

### 2. The SSA Rigor Jump
* **Standard Classroom Question:** Calculate $0.425 \times 12.8$.
* **SSA Rigor Acceleration:** "An automated assembly line fills chemical containers at a rate of $0.425\text{ liters/second}$. A student claims that multiplying $0.425 \times 12.8$ will yield a product with 4 decimal places because there are 3 decimal places in $0.425$ and 1 in $12.8$. Perform Distractor Forensics to evaluate the student's claim using place value decomposition, identify why trailing zeros collapse the final decimal digits, and calculate the exact required filling capacity."

---

### 3. Interactive Visual Model Technical Specification
* **Component Name:** `BaseTenDecimalZoomer` (SVG Grid & Canvas)
* **Visual Mechanics:**
  * Multi-tiered zoomable area grid: $10 \times 10$ main grid zooming into hundredths and thousandths sub-grids.
  * Overlapping translucent color overlays: Horizontal stripes for $0.425$ (cyan) and vertical stripes for $12.8$ (yellow).
  * Intersecting region highlights in green representing partial products: $4 \times 12$, $0.2 \times 0.8$, etc.
* **State Machine Interface:**
  ```typescript
  interface DecimalAreaGridState {
    factorA: number; // 0.425
    factorB: number; // 12.8
    zoomLevel: 'ones' | 'tenths' | 'hundredths' | 'thousandths';
    highlightPartialProducts: boolean;
    collapsedTrailingZeros: number;
    activePartialProductSum: number;
  }
  ```

---

### 4. 4-Stage Pedagogical Loop Execution Blueprint
1. **Stage 1: Deconstruct & Visualize**
   * *Knowns:* Rate $= 0.425\text{ L/s}$, Time $= 12.8\text{ s}$.
   * *Target:* Total Volume $= 0.425 \times 12.8$.
   * *Manipulative Action:* Set base grid to $12.8$ units wide and shade $0.425$ height. Zoom into the thousandths grid to observe $5,440$ thousandths.
2. **Stage 2: Pathway Reconstruction**
   * *Sanity Check:* "Will $0.425 \times 12.8$ be greater than $5$ or less than $5$?" (Since $0.425 < 0.5$, the answer must be less than $12.8 \times 0.5 = 6.4$, and greater than $12.8 \times 0.4 = 5.12$).
   * *Logical Pathway:* Step 1: Multiply whole numbers $425 \times 128 = 54,400$. Step 2: Account for $10^3 \times 10^1 = 10^4$ place value denominator $\implies 54,400 / 10,000 = 5.4400$. Step 3: Collapse trailing zeros $\implies 5.44\text{ Liters}$.
3. **Stage 3: Distractor Forensics**
   * **Option A ($5.44\text{ L}$ - Target):** Accurately applies decimal placement $54,400 / 10,000 = 5.4400$ and simplifies trailing zeros.
   * **Option B ($5.4400\text{ L}$ / Claim Verification - Partial Representation Trap):** Correct numeric value but misunderstands that trailing zeros in decimal representation do not add precision without contextual uncertainty.
   * **Option C ($54.4\text{ L}$ - Place Value Shift Trap):** Miscounts total decimal places as 2 instead of 4 ($425 \times 12.8 \rightarrow 54.4$).
   * **Option D ($0.544\text{ L}$ - Over-Correction Trap):** Divides by $100,000$ instead of $10,000$.
4. **Stage 4: Curiosity Engine**
   * *What-If Toggle:* "What happens to the product if we multiply $0.425$ by $10$ while dividing $12.8$ by $10$?"
   * *Invariance Discovery:* $4.25 \times 1.28 = 5.44$. Multiplicative associative property preserves the product invariant.

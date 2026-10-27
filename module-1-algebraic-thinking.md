# SSA Math Coaching Module 1 Specification
## Title: Algebraic Thinking, Variable Abstraction & Equation Modeling

---

### 1. Module Overview & Standard Alignment
* **5th Grade Baseline Standards:**
  * **NC.5.OA.2:** Write, interpret, and evaluate numerical expressions with parentheses, brackets, and nested grouping symbols using order of operations.
  * **NC.5.OA.3:** Generate two numerical patterns from rules, identify apparent relationships between corresponding terms, and plot ordered pairs in Quadrant I.
* **6th Grade Acceleration Bridge Standards:**
  * **NC.6.EE.1:** Evaluate numerical expressions involving whole-number exponents, brackets, and braces.
  * **NC.6.EE.2:** Write, read, and evaluate algebraic expressions in which letters stand for numbers.
  * **NC.6.EE.3:** Apply properties of operations (distributive, associative, commutative) to generate equivalent expressions.
  * **NC.6.EE.6 & NC.6.EE.7:** Model and solve one-step algebraic equations of the form $x + p = q$ and $p \cdot x = q$ for non-negative rational numbers.

---

### 2. The SSA Rigor Jump
* **Standard Classroom Question:** Evaluate $3 \times (4 + 5)$.
* **SSA Rigor Acceleration:** "A shipping crate has a base area represented by $[2^3 + 4]\text{ ft}^2$ and a height $h\text{ ft}$. If the total volume is $144\text{ ft}^3$, write an equation using variable $h$, evaluate the bracketed base expression $[2^3 + 4]$, and solve for $h$ working forward from the contextual balance model rather than guessing."

---

### 3. Interactive Visual Model Technical Specification
* **Component Name:** `AlgebraicBalanceScale` (SVG/Canvas)
* **Visual Mechanics:**
  * Dual-pan interactive balance beam reflecting mass equilibrium dynamically.
  * Drag-and-drop tiles: Variable boxes ($x$) representing unknown quantities, and unit mass spheres representing constants ($1$).
  * Dynamic Operation Buttons: "Subtract Constant from Both Pans", "Divide Both Pans into Equal Groups".
* **State Machine Interface:**
  ```typescript
  interface BalanceScaleState {
    leftPan: { variables: number; constants: number };
    rightPan: { variables: number; constants: number };
    isEquilibrium: boolean;
    tiltAngle: number; // -15deg to +15deg
    stepLog: string[];
  }
  ```

---

### 4. 4-Stage Pedagogical Loop Execution Blueprint
1. **Stage 1: Deconstruct & Visualize**
   * *Knowns:* Volume $= 144\text{ ft}^3$, Base Area $= [2^3 + 4]\text{ ft}^2$.
   * *Unknown:* Height $h$.
   * *Manipulative Action:* Place $h$ groups of tile set $[2^3 + 4]$ on Left Pan, and $144$ units on Right Pan.
2. **Stage 2: Pathway Reconstruction**
   * *Sanity Check:* "Will $h$ be greater than or less than $10$? Why?" ($[2^3+4] = 12$; since $12 \times 10 = 120 < 144$, $h$ must be greater than $10$).
   * *Logical Pathway:* Step 1: Simplify $[2^3 + 4] = [8 + 4] = 12$. Step 2: Formulate equation $12 \cdot h = 144$. Step 3: Divide both sides by $12 \implies h = 12\text{ ft}$.
3. **Stage 3: Distractor Forensics**
   * **Option A ($12\text{ ft}$ - Target):** Correctly evaluates $[2^3 + 4] = 12$ and solves $144 \div 12 = 12$.
   * **Option B ($14.4\text{ ft}$ - Partial Step Trap):** Evaluates base as $10$ by computing $2 \times 3 + 4 = 10$, then $144 \div 10 = 14.4$.
   * **Option C ($132\text{ ft}$ - Operation Reversal Trap):** Evaluates base as $12$, then subtracts $144 - 12 = 132$ instead of dividing.
   * **Option D ($36\text{ ft}$ - Exponent Trap):** Evaluates $2^3$ as $2 \times 3 = 6 \implies 6 + 4 = 10$ or ignores grouping.
4. **Stage 4: Curiosity Engine**
   * *What-If Slider:* "What happens to height $h$ if the base area is doubled while keeping volume at $144\text{ ft}^3$?"
   * *Invariance Discovery:* Doubling the base cuts the required height in half ($h = 6\text{ ft}$), demonstrating the inverse multiplicative relationship $B \cdot h = V$.

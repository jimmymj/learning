# SSA Math Coaching Module 3 Specification
## Title: Advanced Fraction Structures, Division Mechanics & Conceptual Bridges

---

### 1. Module Overview & Standard Alignment
* **5th Grade Baseline Standards:**
  * **NC.5.NF.1:** Add and subtract fractions with unlike denominators using related fractions.
  * **NC.5.NF.3:** Interpret a fraction as division of numerator by denominator ($a/b = a \div b$).
  * **NC.5.NF.4:** Multiply fractions and mixed numbers using area and length models.
  * **NC.5.NF.7:** Divide unit fractions by whole numbers and whole numbers by unit fractions.
* **6th Grade Acceleration Bridge Standards:**
  * **NC.6.NS.1:** Interpret and compute quotients of fractions; solve word problems involving division of fractions by fractions using visual models and common denominators.

---

### 2. The SSA Rigor Jump
* **Standard Classroom Question:** Solve $4 \div \frac{1}{3}$.
* **SSA Rigor Acceleration:** "A highway construction crew has $1 \frac{1}{2}$ miles of road to pave. Their equipment paves $\frac{2}{3}$ of a mile per hour. Using common unit subdivisions ($\frac{9}{6}$ miles and $\frac{4}{6}$ miles/hour), construct a double tape diagram to determine how many hours it takes. Articulate precisely what the fractional remainder $\frac{1}{4}$ hour represents in the context of the total job versus one hour of work."

---

### 3. Interactive Visual Model Technical Specification
* **Component Name:** `DualTapeFractionResizer` (SVG Interactive Manipulative)
* **Visual Mechanics:**
  * Top bar representing Dividend ($1 \frac{1}{2} = \frac{3}{2}$ miles, colored gold).
  * Bottom bar representing Divisor ($\frac{2}{3}$ mile/hour group, colored orange).
  * Interactive "Subdivide Units" slider: Converts both bars to a common denominator grid ($6^{\text{ths}}$).
  * Measurement overlay: Counts how many 4-block groups ($\frac{4}{6}$) fit into the 9-block bar ($\frac{9}{6}$), leaving 1 block leftover ($\frac{1}{6}$ mile).
* **State Machine Interface:**
  ```typescript
  interface DualTapeFractionState {
    dividend: { whole: number; num: number; den: number }; // 1 1/2
    divisor: { num: number; den: number }; // 2/3
    commonDenominator: number; // 6
    subdividedDividendBlocks: number; // 9
    subdividedDivisorBlocks: number; // 4
    fullGroupsCount: number; // 2
    remainderBlocks: number; // 1
    fractionalRemainderOfGroup: string; // "1/4"
  }
  ```

---

### 4. 4-Stage Pedagogical Loop Execution Blueprint
1. **Stage 1: Deconstruct & Visualize**
   * *Knowns:* Total Distance $= 1 \frac{1}{2} = \frac{3}{2}\text{ miles}$, Paving Rate $= \frac{2}{3}\text{ mile/hour}$.
   * *Target:* Time $h = \frac{3}{2} \div \frac{2}{3}$.
   * *Manipulative Action:* Drag Common Denominator slider to $6$. Observe Dividend $= \frac{9}{6}$ blocks and Divisor $= \frac{4}{6}$ blocks.
2. **Stage 2: Pathway Reconstruction**
   * *Sanity Check:* "Will the answer be greater than $2$ hours or less than $2$ hours?" (Since $2 \times \frac{2}{3} = \frac{4}{3} = 1 \frac{1}{3} < 1 \frac{1}{2}$, it will take more than $2$ hours).
   * *Logical Pathway:* Step 1: Convert to common units $\frac{9}{6} \div \frac{4}{6}$. Step 2: Divide numerators $9 \div 4 = \frac{9}{4} = 2 \frac{1}{4}\text{ hours}$. Step 3: Interpret remainder: $1$ leftover block out of a $4$-block hour group $= \frac{1}{4}\text{ hour} = 15\text{ minutes}$.
3. **Stage 3: Distractor Forensics**
   * **Option A ($2 \frac{1}{4}\text{ hours}$ - Target):** Accurately computes common denominator division $\frac{9}{6} \div \frac{4}{6} = 2 \frac{1}{4}$.
   * **Option B ($1\text{ hour}$ - Multiplication Reversal Trap):** Multiplies $\frac{3}{2} \times \frac{2}{3} = 1\text{ hour}$.
   * **Option C ($2 \frac{1}{6}\text{ hours}$ - Remainder Context Trap):** Interprets $1$ leftover $6^{\text{th}}$ block as $\frac{1}{6}$ hour instead of $\frac{1}{4}$ of the $\frac{4}{6}$ group.
   * **Option D ($\frac{4}{9}\text{ hour}$ - Inverted Division Trap):** Computes divisor $\div$ dividend ($\frac{2}{3} \div \frac{3}{2} = \frac{4}{9}$).
4. **Stage 4: Curiosity Engine**
   * *What-If Toggle:* "What if the crew's paving speed doubles to $1 \frac{1}{3}$ miles/hour ($\frac{8}{6}$)?"
   * *Invariance Discovery:* New time $= \frac{9}{6} \div \frac{8}{6} = \frac{9}{8} = 1 \frac{1}{8}\text{ hours}$. Doubling rate cuts total time in half ($2 \frac{1}{4} \div 2 = \frac{9}{8}$).

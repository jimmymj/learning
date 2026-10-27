# Complete Product Requirement Document (PRD), Pedagogical Coaching Guidelines & Technical Specification
## Interactive 5th Grade Single Subject Acceleration (SSA) Math Coaching Web Application

---

## SECTION E: UI/UX & Technical Architecture Guidelines (Single-File HTML5 Compilation Engine)

This specification provides explicit engineering guidelines for compiling any module from this document into a self-contained, standalone HTML5/CSS3/JavaScript application.

### 1. Visual Aesthetic & Theme ("Math Lab / Explorer")
* **Target Audience Alignment:** Designed specifically for 10–11-year-old academically gifted scholars. Avoids elementary cartoon aesthetics; employs a modern, clean, high-contrast "Laboratory / Explorer" aesthetic.
* **Design Tokens & Palette:**
  * Primary Canvas Dark: `#0F172A` (Slate 900)
  * Workspace Panel Light: `#F8FAFC` (Slate 50)
  * Accent Primary (Interactive Manipulatives): `#2563EB` (Royal Blue)
  * Target Accent (Correct / Positive Invariance): `#059669` (Emerald Green)
  * Diagnostic Trap Accent (Distractors / Misconceptions): `#D97706` (Amber)
  * Focus Glow / Selection: `#8B5CF6` (Violet)
  * Typography: `Noto Sans`, `Inter`, `Manjari` (sans-serif) for body text; `KaTeX` or custom SVG typesetting for stacked mathematical fractions and exponents.

---

### 2. Layout & Interface Architecture
The application enforces a 50/50 responsive split-screen grid layout:

```
┌─────────────────────────────────────────┬─────────────────────────────────────────┐
│ LEFT PANEL: SOCRATIC COACH & PROBLEM    │ RIGHT PANEL: VISUAL SANDBOX & SCRATCH   │
│ ┌─────────────────────────────────────┐ │ ┌─────────────────────────────────────┐ │
│ │ Header: Deep Thinking Streak & Gems │ │ │ SVG/Canvas Manipulative Canvas     │ │
│ ├─────────────────────────────────────┤ │ │ (Interactive Balance, Area Grid,    │ │
│ │ Problem Context & 3-Column Schema   │ │ │ Tape Resizer, or 3D Prism Slicer)   │ │
│ ├─────────────────────────────────────┤ │ └─────────────────────────────────────┘ │
│ │ 4-Stage Socratic Dialogue Box       │ │ ┌─────────────────────────────────────┐ │
│ │ (Deconstruct ➔ Solve ➔ Forensics)   │ │ │ Interactive Scratchpad & Vector Pen │ │
│ └─────────────────────────────────────┘ │ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┴─────────────────────────────────────────┘
```

---

### 3. Gamification with Purpose Mechanics
* **Deep Thinking Streaks:** Replaces anxiety-inducing speed timers. Tracks continuous minutes of thoughtful engagement, multi-step justification, and absence of erratic guessing.
* **Trap-Hunter Badges:** Awarded when a scholar successfully identifies and explains a peer's misconception in "Spot the Trap" mode.
* **Curiosity Gems:** Unlocked when scholars use "What-If" sliders to stress-test edge cases and articulate mathematical invariants.

---

## SECTION F: Gold-Standard Worked Archetypes

### Archetype 1: Fractions & Bar Modeling (Fraction Division Bridge)
* **Problem Narrative:** "A highway construction crew has $1 \frac{1}{2}$ miles of road to pave. Their equipment paves $\frac{2}{3}$ of a mile per hour. Using common units ($\frac{9}{6}$ miles and $\frac{4}{6}$ miles/hour), construct a double tape diagram to determine how many hours it takes. Explain what the fractional remainder represents."

#### 1. Socratic Coach & Student Dialogue Trace
* **Coach:** "Before calculating, look at your total distance $1 \frac{1}{2}$ miles and your hourly rate $\frac{2}{3}$ mile/hour. Will the required time be greater than $2$ hours?"
* **Scholar:** "Yes, because $2 \times \frac{2}{3} = \frac{4}{3} = 1 \frac{1}{3}$ miles. Since $1 \frac{1}{2} = 1 \frac{3}{6}$ is greater than $1 \frac{2}{6}$, it will take more than $2$ hours."
* **Coach:** "Excellent benchmark prediction! Now use the 'Subdivide Units' slider on your tape resizer to find a common unit."
* **Scholar:** "I set the common denominator slider to $6$. The distance tape shows $9$ shaded blocks ($\frac{9}{6}$), and the rate tape shows $4$ shaded blocks ($\frac{4}{6}$)."
* **Coach:** "How many full $4$-block rate groups fit into the $9$-block distance bar, and what remains?"
* **Scholar:** "Fit $2$ full groups of $4$ blocks ($8$ blocks total). $1$ block remains. The leftover block is $1$ out of a $4$-block hour group, which means $\frac{1}{4}$ of an hour ($15$ minutes). Total time is $2 \frac{1}{4}$ hours."

#### 2. Visual Model State Matrix
* **Manipulative Type:** `DualTapeFractionResizer`
* **Dividend Tape:** $1 \frac{1}{2} \implies 9$ subdivisions ($6^{\text{ths}}$ grid).
* **Divisor Tape:** $\frac{2}{3} \implies 4$ subdivisions ($6^{\text{ths}}$ grid).
* **Quotient Mapping:** $9 \div 4 = 2\text{ full groups} + \frac{1}{4}\text{ fractional group remainder}$.

#### 3. Distractor Forensics Matrix

| Option | Value | Forensic Classification | Underlying Misconception Logic |
| :--- | :--- | :--- | :--- |
| **Option A** | $2 \frac{1}{4}\text{ hours}$ | **Target (Correct)** | Correctly converts to common units $\frac{9}{6} \div \frac{4}{6} = 2 \frac{1}{4}$. |
| **Option B** | $1\text{ hour}$ | **Operation Reversal Trap** | Multiplies $\frac{3}{2} \times \frac{2}{3} = 1$, confusing division with reciprocal multiplication cancellation without context. |
| **Option C** | $2 \frac{1}{6}\text{ hours}$ | **Remainder Context Trap** | Interprets the $1$ leftover block as $\frac{1}{6}$ hour relative to $1$ whole mile, rather than $\frac{1}{4}$ hour relative to the $\frac{4}{6}$ divisor unit. |
| **Option D** | $\frac{4}{9}\text{ hour}$ | **Inverted Dividend Trap** | Divides rate by distance ($\frac{2}{3} \div \frac{3}{2} = \frac{4}{9}$). |

#### 4. Curiosity Extension ("What If?")
* *Mutation:* "What happens if the crew works for $4.5$ hours? How many miles do they pave?"
* *Invariance Proof:* $4.5 \times \frac{2}{3} = \frac{9}{2} \times \frac{2}{3} = \frac{18}{6} = 3\text{ miles}$. Doubling the time ($2.25 \text{ hrs} \rightarrow 4.5 \text{ hrs}$) doubles the distance paved ($1.5 \text{ mi} \rightarrow 3 \text{ mi}$).

---

### Archetype 2: 3D Spatial Reasoning (Composite Volume & Surface Area Net Bridge)
* **Problem Narrative:** "An L-shaped storage container is composed of two non-overlapping rectangular prisms with a total volume of $223\text{ m}^3$. Prism A has known dimensions $3\text{ m} \times 2\text{ m} \times 3\text{ m}$. Prism B has a base area of $30\text{ m}^2$. Work backward to determine the missing height of Prism B. Then unfold the L-shaped container into a flat 2D net and compute its total exterior surface area."

#### 1. Socratic Coach & Student Dialogue Trace
* **Coach:** "Let's deconstruct the composite solid. What is the volume of Prism A?"
* **Scholar:** "Prism A volume $= 3\text{ m} \times 2\text{ m} \times 3\text{ m} = 18\text{ m}^3$."
* **Coach:** "If the total combined volume is $223\text{ m}^3$, what must be the volume of Prism B?"
* **Scholar:** "Prism B volume $= 223\text{ m}^3 - 18\text{ m}^3 = 205\text{ m}^3$."
* **Coach:** "Prism B has a base area $B = 30\text{ m}^2$. How do you find its height $h$?"
* **Scholar:** "Since $V = B \cdot h$, height $h = 205 \div 30 = 6 \frac{25}{30} = 6 \frac{5}{6}\text{ m}$ ($6.83\text{ m}$)."

#### 2. Visual Model State Matrix
* **Manipulative Type:** `3DCompositePrismSlicer` (WebGL / Canvas)
* **Prism A Dimensions:** $3 \times 2 \times 3 \implies V_A = 18\text{ m}^3$.
* **Prism B Dimensions:** $B = 30\text{ m}^2, h = 6 \frac{5}{6}\text{ m} \implies V_B = 205\text{ m}^3$.
* **Net Unfolder Mode:** Flattens 3D composite figure into 10 exterior rectangular faces, highlighting and subtracting the $2$ interior overlapping boundary faces.

#### 3. Distractor Forensics Matrix

| Option | Value | Forensic Classification | Underlying Misconception Logic |
| :--- | :--- | :--- | :--- |
| **Option A** | $h = 6 \frac{5}{6}\text{ m}$ | **Target (Correct)** | Subtracts $V_A = 18$ from $223 \implies 205$, then divides by $B = 30$. |
| **Option B** | $h = 7.43\text{ m}$ | **Partial Step Trap** | Divides total volume $223 \div 30 = 7.43\text{ m}$, failing to subtract Prism A volume first. |
| **Option C** | $h = 6.00\text{ m}$ | **Additive Boundary Trap** | Confuses Prism A volume ($18$) with Prism A base area ($6$), leading to $223 - 43 = 180 \implies 180 / 30 = 6\text{ m}$. |
| **Option D** | $h = 13.6\text{ m}$ | **Dimension Multiplicity Trap** | Divides $205$ by $15$ instead of $30$. |

#### 4. Curiosity Extension ("What If?")
* *Mutation:* "What happens to the exterior surface area if we slide Prism A along the top face of Prism B toward the edge versus placing it squarely in the middle?"
* *Invariance Proof:* The total exterior surface area remains invariant regardless of position, provided Prism A stays entirely on the face without overhanging, because the covered boundary area subtracted from both prisms remains identical ($2 \times \text{contact area}$).

---

### Archetype 3: Algebraic Patterns & Coordinate Plane (Covariance & Rays)
* **Problem Narrative:** "Two scholars track earnings over time: Sam earns $\$2$ every day (Rule: $y = 2x$), while Terri earns $\$4$ every day (Rule: $y = 4x$). Plot both dataset rays on a coordinate grid starting at origin $(0,0)$. Analyze the relationship between corresponding terms, identify independent vs dependent variables, and determine how many days it takes for Terri to earn $\$20$ more than Sam."

#### 1. Socratic Coach & Student Dialogue Trace
* **Coach:** "Look at the rules for Sam ($y = 2x$) and Terri ($y = 4x$). What is the relationship between Terri's total earnings and Sam's total earnings on any given day $x$?"
* **Scholar:** "Terri's earnings are always double Sam's earnings ($4x = 2 \cdot (2x)$)."
* **Coach:** "When you plot both dataset rays on the coordinate plane, how do their visual slopes compare?"
* **Scholar:** "Terri's ray is twice as steep as Sam's ray because her unit rate ($\$4/\text{day}$) is double Sam's unit rate ($\$2/\text{day}$)."
* **Coach:** "How do you find the day when Terri has earned $\$20$ more than Sam?"
* **Scholar:** "Daily difference $= 4 - 2 = \$2/\text{day}$. To reach a $\$20$ difference: $20 \div 2 = 10\text{ days}$. On Day 10, Sam has $\$20$ and Terri has $\$40$."

#### 2. Visual Model State Matrix
* **Manipulative Type:** `SynchronizedRatioRayPlotter`
* **Sam's Ray:** Plotted coordinates $(0,0), (1,2), (2,4), (3,6), (4,8), (5,10), \dots, (10,20)$.
* **Terri's Ray:** Plotted coordinates $(0,0), (1,4), (2,8), (3,12), (4,16), (5,20), \dots, (10,40)$.
* **Covariance Readout:** Ratio of corresponding terms $\frac{\text{Terri}}{\text{Sam}} = \frac{4}{2} = 2.0$ (constant scale factor across all $x > 0$).

#### 3. Distractor Forensics Matrix

| Option | Value | Forensic Classification | Underlying Misconception Logic |
| :--- | :--- | :--- | :--- |
| **Option A** | $10\text{ days}$ | **Target (Correct)** | Solves difference equation $(4-2)x = 20 \implies 2x = 20 \implies x = 10\text{ days}$. |
| **Option B** | $5\text{ days}$ | **Partial Step Trap** | Finds the day when Terri reaches $\$20$ total earnings ($20 \div 4 = 5$), rather than a $\$20$ difference. |
| **Option C** | $20\text{ days}$ | **Rule Confusion Trap** | Uses Sam's rate alone ($20 \div 1 = 20$), ignoring Terri's accumulation. |
| **Option D** | $8\text{ days}$ | **Additive Bias Trap** | Evaluates difference at $x=4$ where Terri has $\$16$ and Sam has $\$8$ (difference $\$8$). |

#### 4. Curiosity Extension ("What If?")
* *Mutation:* "What if Sam receives an initial gift of $\$10$ on Day 0 (Rule: $y = 2x + 10$), while Terri starts at $\$0$ (Rule: $y = 4x$)? Does the line for Sam still pass through the origin $(0,0)$?"
* *Invariance Proof:* Sam's line now intersects the $y$-axis at $(0,10)$, making it a non-proportional linear relationship. Terri catches up to Sam on Day 5 ($2(5)+10 = 20 = 4(5)$), where the two lines intersect at point $(5,20)$.

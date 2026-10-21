# Product Specification Document: CMS 5th Grade AIG Math Q1 Interactive Learning Suite

**Document Version:** 1.0.0  
**Curriculum Authority:** Charlotte-Mecklenburg Schools (CMS) Academically or Intellectually Gifted (AIG) / Illustrative Mathematics K–5 / NC SCOS  
**Target Pacing:** Quarter 1 (Weeks 1–9)  
**Target Learner Persona:** Aria Vance (10yo, 5th Grade AIG Scholar; accelerated spatial/quantitative reasoning, high working memory, needs low-friction, high-density interactive tools with pre-algebraic depth)  
**Parent PRD:** `cms-5th-grade-aig-math-q1-prd.md`  

---

## 1. Executive Summary & Curriculum Scope

The **CMS 5th Grade AIG Math Q1 Interactive Learning Suite** deepens and accelerates First Quarter (Q1) Grade 5 mathematical standards for gifted learners. Instead of procedural drill, it delivers high-abstraction spatial modeling, algebraic generalizations, algorithm cryptarithms, and competition-style non-routine logic puzzles (AMC 8 / Math Olympiad level).

### Pacing & Unit Alignment Matrix (Weeks 1–9)

| Week Window | Illustrative Math Unit | NC SCOS Standards | Core Topic Scope | AIG Acceleration & Pre-Algebra Vector |
| :--- | :--- | :--- | :--- | :--- |
| **Weeks 1–2** | **IM Unit 1: Finding Volume** | `NC.5.MD.3`, `NC.5.MD.4`, `NC.5.MD.5a-b` | Unit cube packing; $V = l \cdot w \cdot h$ and $V = B \cdot h$. | 3D coordinate matrices; fractional packing density; $SA:V$ optimization; cubic scaling ($2^3 = 8\times$); space diagonals ($d = \sqrt{l^2+w^2+h^2}$). |
| **Week 3** | **IM Unit 1: Additive Volume & Numerical Expressions** | `NC.5.MD.5c`, `NC.5.OA.2` | 2-part L-shaped composite solids; numerical expressions with parentheses. | 3+ non-overlapping prism decomposition; hollow-core subtractions ($V_{\text{gross}} - V_{\text{void}}$); density & mass calculations; nested grouping symbols ($[\{\}]$). |
| **Weeks 4–5** | **IM Unit 4: Multi-Digit Whole Number Operations** | `NC.5.NBT.5` | Standard multiplication algorithm ($3\text{-digit} \times 2\text{-digit}$). | Missing-digit cryptarithms; algebraic product expansion ($100ac + 10(ad+bc) + bd$); partial products error analysis. |
| **Week 6** | **IM Unit 4: Multi-Digit Whole Number Division** | `NC.5.NBT.6` | $4\text{-digit} \div 2\text{-digit}$ division via partial quotients and area models. | Modular arithmetic ($a \pmod b$); remainder rounding constraints (round up vs. drop vs. fraction); prime factor cancelation. |
| **Week 7** | **IM Unit 5: Place Value Patterns & Decimal Operations** | `NC.5.NBT.1`, `NC.5.NBT.2` | Base-ten shifts ($10\times, \frac{1}{10}$); powers of 10 ($10^3$). | Multi-position scaling ($10^k, 10^{-k}$); base-10 logarithmic shifts; scientific notation foundations ($a \times 10^b$); recursive decimal series. |
| **Week 8** | **IM Unit 5: Decimal Representation & Comparison** | `NC.5.NBT.3a-b` | Reading, writing, expanded form, comparing decimals to thousandths. | Expanded exponential form ($\sum d_i \cdot 10^{-i}$); rational number density between thousandths; algebraic inequalities. |
| **Week 9** | **IM Unit 5: Decimal Addition & Subtraction** | `NC.5.NBT.7` | Adding and subtracting decimals to thousandths. | Multi-variable decimal systems ($x+y = A, x-y = B$); missing-digit cryptarithms; compensation mental math heuristics. |

---

## 2. The 3 Modules & 10 Core Topics

### Module 1: Spatial Volume Reasoning & 3D Geometry
- **Topic 1:** Unit Cube Packing, Layering & Spatial Foundations (`NC.5.MD.3`, `NC.5.MD.4`)
- **Topic 2:** Rectangular Prism Volume Formulas ($V = l \cdot w \cdot h$, $V = B \cdot h$) (`NC.5.MD.5a-b`)
- **Topic 3:** Additive Volume of Composite & Hollow Solids (`NC.5.MD.5c`)
- **Topic 4:** Order of Operations & Numerical Expressions in Geometric Contexts (`NC.5.OA.2`)

### Module 2: Multi-Digit Whole Number Operations
- **Topic 5:** Multi-Digit Algorithm Multiplication & Cryptarithms (`NC.5.NBT.5`)
- **Topic 6:** Multi-Digit Partial Quotients Division & Modular Remainder Optimization (`NC.5.NBT.6`)

### Module 3: Decimal Place Value, Comparison & Addition/Subtraction
- **Topic 7:** Base-Ten Place Value Structure & Multiplicative Shifts ($10\times, \frac{1}{10}$) (`NC.5.NBT.1`)
- **Topic 8:** Powers of 10 Patterns, Exponents & Scientific Notation Roots (`NC.5.NBT.2`)
- **Topic 9:** Decimal Expanded Form, Density & Thousandths Inequalities (`NC.5.NBT.3a-b`)
- **Topic 10:** Decimal Addition & Subtraction Systems to Thousandths (`NC.5.NBT.7`)

---

## 3. Three-Tier Rigor Architecture

1. **Tier 1 — High-Complexity NCSCoS Level 4/5 Mastery (30% of Items):**
   - Deep operational fluency with upper-bound numbers (e.g. $4\text{-digit} \times 2\text{-digit}$, decimals to thousandths).
   - Real-world multi-step contextual word problems.
2. **Tier 2 — Multi-Step Non-Routine AIG Logic & Optimization (50% of Items):**
   - Missing-variable reverse engineering (e.g. given Volume and Height, find base perimeter).
   - Dimensional constraints, container block packing with remainders, and algorithm cryptarithms.
   - Choice board logic puzzles and multi-constraint optimization ($SA:V$ ratios).
3. **Tier 3 — Grade 6 Pre-Algebra Bridging & Competition Math (20% of Items):**
   - Linear variable edge lengths ($x, x+3, 2x$) and space diagonal calculations ($d = \sqrt{l^2+w^2+h^2}$).
   - Modular arithmetic remainder systems, scientific notation equations, and systems of decimal equations.
   - AMC 8 / Math Olympiad structural patterns.

---

## 4. Interactive Manipulatives & Spatial Laboratory Requirements

The app must feature **9 responsive, interactive digital manipulatives**:

1. **3D Rotatable Rectangular Prism Sandbox (CSS 3D / HTML5 Canvas Isometric):**
   - Interactive orbit/rotation controls (drag to rotate in 3D).
   - Sliders for Length ($l$), Width ($w$), and Height ($h$).
   - Toggleable unit cube wireframe grid and layer-by-layer slicing animation showing $V = B \cdot h$.
   - Live telemetry: Base Area $B$, Volume $V$, Surface Area $SA$, and Space Diagonal $d$.
2. **3D Composite & Hollow Solid Decomposer:**
   - Visual model of L-shaped composite prisms and hollow-core blocks ($V_{\text{outer}} - V_{\text{void}}$).
   - Sliders adjusting outer and void dimensions with live mass calculation based on density ($\text{g/cm}^3$).
3. **Order of Operations Expression Tree Builder (`NC.5.OA.2`):**
   - Interactive nested bracket evaluator with step-by-step collapse from inner parentheses to brackets.
4. **Standard Algorithm & Partial Products Area Model (`NC.5.NBT.5`):**
   - Dynamic $3\text{-digit} \times 2\text{-digit}$ partition canvas displaying partial products.
   - Digit error inspector highlighting missing placeholder zeros.
5. **Multiplication Cryptarithm Solver & Inspector:**
   - Interactive digit tile grid allowing students to test missing digits $A$ and $B$ to satisfy arithmetic constraints.
6. **Partial Quotients & Remainder Sandbox (`NC.5.NBT.6`):**
   - Dynamic chunk-subtraction tool ($100\times$, $10\times$, $5\times$, $1\times$) showing cumulative quotients, remaining dividends, and remainder interpretations (discrete vs. mixed number).
7. **Base-Ten Multiplicative Shift & Exponent Scale (`NC.5.NBT.1`, `NC.5.NBT.2`):**
   - Exponential power-of-10 slider from $10^{-3}$ to $10^6$.
   - Real-time digit position shifter relative to the fixed decimal point.
8. **Dense Decimal Number Line with Thousandths Magnifier (`NC.5.NBT.3`):**
   - Interactive zoomable number line placing values between $0.450$ and $0.460$.
   - Inequality interval highlighter with open/closed bounds.
9. **Thousandths Decimal Addition & Subtraction Balancer (`NC.5.NBT.7`):**
   - Column alignment visualizer with regrouping animations and mental math compensation slider.

---

## 5. Assessment Engine & Diagnostic Feedback Architecture

### Question Bank Calibration
- **Total Flagship Graded Items:** Exactly 60 high-rigor, verified questions (20 items per module: 6 Tier 1, 10 Tier 2, 4 Tier 3; exactly 6 questions per topic).
- **Format Diversity:** Multiple Choice, Numeric Expression Input, Visual 3D Spatial Selection, and Drag & Drop Matching.
- **Dynamic Shuffling:** Fisher-Yates runtime shuffling for answer choices and drag trays with object-level answer validation.

### 4-Part Diagnostic Feedback Panel
Every question renders an explicit 4-part resolution upon submission:
1. **Step-by-Step Resolution Path:** Detailed multi-stage worked solution with mathematical rigor.
2. **Underlying Mathematical Principle:** Identifies the foundational law (e.g., Associative Property of Multiplication, Base-10 Positional Shift Law, Additive Volume Property).
3. **Misconception & Distractor Analysis:** Explains why incorrect options were chosen (e.g., confusing surface area with volume, dropping placeholder zeros, "longer decimal is larger" bias).
4. **Fast-Track / Mental Math Shortcut:** An advanced heuristic for gifted learners (e.g., compensation, factoring, landmark numbers).

### Auxiliary EdTech Capabilities
- **Aria's AI Socratic Hint Drawer:** 3 progressive hint tiers (Conceptual Nudge $\to$ Strategic Setup $\to$ Guided Walkthrough).
- **Interactive Whiteboard Scratchpad:** Canvas overlay with pen, highlighter, eraser, color palette, and clear tools.
- **Web Audio Sound Effects:** Browser-native audio oscillator chimes for correct streaks, hints, and error tones (no external audio files).
- **Offline Self-Contained Delivery:** Zero CDN runtimes, zero raw LaTeX (100% native Unicode & semantic HTML math formatting).

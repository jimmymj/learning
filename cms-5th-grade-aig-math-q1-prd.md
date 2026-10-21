# Product Requirement Document (PRD) & Content Specification Architecture
**Target Audience:** Charlotte-Mecklenburg Schools (CMS) 5th Grade Academically or Intellectually Gifted (AIG) Mathematics  
**Timeline Focus:** First Quarter (Q1 — Weeks 1–9)  
**Authoring Standard:** Advanced Curriculum Architecture & EdTech Engineering  
**Document Status:** Ready for Engineering, UI/UX, and Content Authoring Teams  

---

## 1. Q1 Timeline, Scope & CMS Pedagogical Alignment

### 1.1 Q1 Launch Vision & Value Proposition
The **CMS Q1 AIG Math Interactive Learning System** is a personalized, high-abstraction digital environment designed to serve gifted 5th-grade students across Charlotte-Mecklenburg Schools. Grounded in personalized learning frameworks, the platform transitions instruction from traditional, teacher-controlled computational drill to student-controlled pathways, learning playlists, and conceptual choice boards. 

Rather than prematurely pushing students into disjointed higher-grade topics, the application deepens **First Quarter (Q1) Grade 5 standards**. It transforms baseline procedural fluency into non-routine logic puzzles, spatial 3D optimization, and pre-algebraic abstractions, enabling AIG students to reach **NCSCoS Level 4/5 (Superior/Exceeds Standards)** mastery while fostering rapid abstraction and cognitive autonomy.

---

### 1.2 Isolated Q1 Standards & Pacing Calendar
In alignment with the **Illustrative Mathematics (IM) Grade 5 Scope and Sequence** adopted by CMS, Quarter 1 encompasses **IM Unit 1 (Finding Volume)**, **IM Unit 4 (Multi-Digit Whole Number Operations)**, and **IM Unit 5 (Place Value Patterns & Decimal Operations)**. All topics from Quarters 2–4 (such as complex fraction multiplication/division and 4-quadrant coordinate geometry) are strictly isolated out, except where leveraged as direct Grade 6 pre-algebra bridging vectors.

| Week Window | CMS Curriculum Unit | Primary NCSCoS Standards | Standard Baseline Pace | AIG Accelerated Pacing & Differentiation Vector |
| :--- | :--- | :--- | :--- | :--- |
| **Weeks 1–2** | **IM Unit 1: Volume & Spatial Reasoning** | `NC.5.MD.3`<br>`NC.5.MD.4`<br>`NC.5.MD.5a-b` | Counting unit cubes; building rectangular prisms; establishing $V = l \times w \times h$ and $V = B \times h$. | **Condensed Concrete Phase (2 Days):** Rapid transition from unit cubes to variable-length algebraic dimensions, optimization of surface-area-to-volume ratios, and polynomial volume expressions ($V(x)$). |
| **Week 3** | **IM Unit 1: Additive Volume & Numerical Expressions** | `NC.5.MD.5c`<br>`NC.5.OA.2` | Decomposing 2-part L-shaped composite solids; writing simple expressions with parentheses. | **Multi-Prism Decomposition:** 3+ non-overlapping composite solids with missing dimensions solved via systems of linear equations; evaluating nested order of operations. |
| **Weeks 4–5** | **IM Unit 4: Multi-Digit Whole Number Multiplication** | `NC.5.NBT.5` | Standard algorithm fluency for $3\text{-digit} \times 2\text{-digit}$ whole numbers. | **Algorithm Cryptarithms & Error Analysis:** Cryptarithmetic digit-reconstruction puzzles, base-$n$ matrix multiplication logic, and efficiency comparison between partial products and standard algorithms. |
| **Week 6** | **IM Unit 4: Multi-Digit Whole Number Division** | `NC.5.NBT.6` | $4\text{-digit} \div 2\text{-digit}$ division using area models, partial quotients, and remainders. | **Modular Remainder Optimization:** Partial quotient efficiency challenges, real-world constraint-driven remainder interpretations, and prime factor decomposition strategies. |
| **Week 7** | **IM Unit 5: Decimal Place Value & Powers of 10** | `NC.5.NBT.1`<br>`NC.5.NBT.2` | Base-ten shifts ($10\times$, $\frac{1}{10}$); powers of 10 represented as whole-number exponents ($10^3$). | **Exponential Base Structures & Scientific Notation Roots:** Multiplicative place-value shifts across negative exponents ($10^{-k}$), base-10 logarithmic scaling, and scientific notation bridging ($a \times 10^b$). |
| **Week 8** | **IM Unit 5: Decimal Representation & Comparison** | `NC.5.NBT.3a-b` | Reading, writing, expanded form, and comparing decimals to thousandths. | **Algebraic Decimal Inequalities:** Expanded exponential form ($\sum d_i \cdot 10^{-i}$), dense decimal number-line topology, and variable-bound inequality systems. |
| **Week 9** | **IM Unit 5: Decimal Addition & Subtraction** | `NC.5.NBT.7` | Adding and subtracting decimals to thousandths using place value strategies and estimation. | **Multi-Variable Financial & Physical Optimization:** Multi-step decimal equations with missing addends, error-propagation analysis, and mental math benchmark shortcuts. |

---

### 1.3 User Persona: CMS 5th Grade AIG Math Student
* **Persona Name:** Aria Vance (10 years old, 5th Grade AIG Scholar at CMS)
* **Cognitive Profile:** Operates at an advanced spatial and quantitative reasoning level. Possesses high working memory capacity and rapidly synthesizes symbolic patterns.
* **Behavioral Motivators:** Highly autonomous; prefers choice boards, menu playlists, and inquiry-driven project tasks over linear instruction.
* **Pain Points with Traditional EdTech:** Expresses frustration with repetitive computational drills ("skill-and-drill"), slow-paced visual animations, and forced linear progressions on concepts she masters in 1–2 attempts.
* **Target Interface Experience:** Needs clean, low-friction, high-density UI/UX with dynamic 3D manipulation models, instant diagnostic feedback, LaTeX math rendering, and competitive logic challenges.

---

## 2. Technical & Q1 Content Specifications

### 2.1 Mathematical Engine Requirements
1. **LaTeX Rendering Engine (KaTeX/MathJax Integration):**
   * Real-time rendering of scientific notation: $a \times 10^n$.
   * Expanded place value summation notation: $4 \times 10^1 + 3 \times 10^0 + 8 \times 10^{-1} + 5 \times 10^{-3}$.
   * Algebraic volume expressions: $V = (2x + 1)(x + 4)(3x)$.
2. **Multi-Digit Algorithmic Bracket Renderer:**
   * Dynamic UI components for partial quotients division and grid-aligned standard algorithm multiplication, allowing students to inspect intermediate step errors.
3. **3D Volume Spatial Canvas (WebGL / Three.js):**
   * Interactive, rotatable 3D rectangular prisms and composite solids.
   * Features toggleable unit-cube wireframes, layer-by-layer slicing animations, and dynamic dimension slider controls for $V = B \times h$ visualization.

---

### 2.2 Rigid 60-Question Architecture per Q1 Topic
Every single identified Q1 topic must possess a dedicated, fully authored item bank of **exactly 60 distinct questions**, structured across three rigor tiers:

* **Tier 1: Baseline Mastery & High-Complexity NCSCoS Level 4/5 (Questions 1–20)**
  * *Target:* Deep operational fluency and single-to-two-step contextual word problems.
  * *Rigor:* Standard curriculum limits pushed to upper-bound multi-digit values and complex phrasing.
* **Tier 2: Multi-Step AIG Problem Solving & Non-Routine Logic (Questions 21–45)**
  * *Target:* Multi-constraint logic, optimization, missing-variable reverse engineering, and choice board conceptual puzzles.
  * *Rigor:* Introduces hidden variables, dimensional constraints, and real-world trade-off scenarios.
* **Tier 3: Grade 6 Bridging, Algebraic Abstractions & Competition Math (Questions 46–60)**
  * *Target:* Seamless extension into Grade 6 standards (`NC.6.EE`, `NC.6.NS`, `NC.6.RP`) and competition math structures (AMC 8 / Math Olympiad).
  * *Rigor:* Involves linear variables, scientific notation roots, prime factorization matrices, and exponential equations.

---

### 2.3 Diagnostic Explanation System Architecture
For **every question** across all 60 items per topic, the engine must render a 4-part diagnostic feedback panel upon response submission:

1. **Step-by-Step Resolution Path:** Fully worked solution using LaTeX formatting and visual breakdown.
2. **Underlying Mathematical Principle:** Core property or theorem (e.g., Associative Property, Base-10 Shift Law).
3. **Misconception & Distractor Analysis:** Deconstruction of incorrect options (e.g., Option B reflects failure to line up decimal places; Option C conflates perimeter with volume).
4. **Fast-Track / Mental Math Strategy:** An advanced shortcut or pattern-recognition heuristic for gifted learners.

---

## 3. Exhaustive Q1 Module Breakdown (10 Core Topics)

---

### MODULE 1: Spatial Volume Reasoning & 3D Geometry (`NC.5.MD.3`, `NC.5.MD.4`, `NC.5.MD.5`, `NC.5.OA.2`)

#### Topic 1: Unit Cube Packing, Layering & Spatial Volume Foundations
* **Standard Code:** `NC.5.MD.3`, `NC.5.MD.4`
* **Baseline Objective:** Understand volume as an attribute of 3D space measured by packing $1\text{-unit}$ cubes without gaps or overlaps.
* **AIG Extension Vector:** Transition from concrete unit counts to 3D spatial coordinate matrices, fractional unit packing density, and variable surface-area-to-volume ratio ($SA:V$) optimizations.
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 12):* A rectangular box is packed with $1\text{-cm}$ unit cubes. The bottom layer has 7 rows of 8 cubes. If there are 6 identical layers, calculate the total volume.
  * *Tier 2 (Item 34):* A container with interior dimensions $12\text{ cm} \times 15\text{ cm} \times 20\text{ cm}$ is filled with smaller cubic blocks of edge length $3\text{ cm}$. Calculate the maximum number of blocks that fit without exceeding container boundaries, and identify the remaining empty volume.
  * *Tier 3 (Item 52):* A rectangular prism has integer side lengths $x$, $y$, and $z$. If its volume is $210\text{ cm}^3$, find the dimensions that minimize the surface area $SA = 2(xy + yz + xz)$.
* **Diagnostic Feedback Guidelines:** Ensure students differentiate between total spatial occupancy ($V$) and boundary surface area ($SA$). Address the common error of multiplying dimensions when gaps exist due to non-integer unit fitting.

---

#### Topic 2: Rectangular Prism Volume Formulas ($V = l \cdot w \cdot h$ & $V = B \cdot h$)
* **Standard Code:** `NC.5.MD.5a-b`
* **Baseline Objective:** Apply the formulas $V = l \cdot w \cdot h$ and $V = B \cdot h$ to solve real-world problems involving rectangular prisms.
* **AIG Extension Vector:** Algebraic equation solving for unknown edge dimensions where $l, w, h$ are expressed as algebraic terms ($x, x+2, 2x$), and volumetric scaling analysis (doubling dimensions yields $2^3 = 8\times$ volume).
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 08):* A storage crate has a base area $B = 144\text{ sq ft}$ and a height $h = 9\text{ ft}$. Calculate the total volume in cubic feet.
  * *Tier 2 (Item 28):* The volume of a rectangular prism is $1,260\text{ in}^3$. Its height is $12\text{ in.}$, and its length is $3\text{ in.}$ longer than its width. Determine the perimeter of the base.
  * *Tier 3 (Item 58):* A rectangular prism has dimensions $(x)\text{ cm} \times (x + 3)\text{ cm} \times (2x)\text{ cm}$. If the volume is $320\text{ cm}^3$, solve for $x$ and determine the length of the longest space diagonal $d = \sqrt{x^2 + (x+3)^2 + (2x)^2}$.
* **Diagnostic Feedback Guidelines:** Reiterate that $B$ represents the 2D area of the base ($l \cdot w$). Highlight how scaling one dimension scales volume linearly, whereas scaling all three dimensions scales volume cubically.

---

#### Topic 3: Additive Volume of Composite Non-Overlapping 3D Figures
* **Standard Code:** `NC.5.MD.5c`
* **Baseline Objective:** Calculate the volume of complex 3D solid figures composed of two non-overlapping rectangular prisms by adding their individual volumes.
* **AIG Extension Vector:** Multi-prism decomposition (3+ structures) involving hidden structural dimensions, hollow core subtractions ($V_{\text{total}} = V_{\text{outer}} - V_{\text{hollow}}$), and optimization of architectural models.
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 18):* Calculate the total volume of an L-shaped structure formed by joining Prism A ($4\text{ m} \times 3\text{ m} \times 5\text{ m}$) and Prism B ($6\text{ m} \times 3\text{ m} \times 2\text{ m}$) along a common face.
  * *Tier 2 (Item 40):* A concrete pedestal consists of three stacked concentric square prisms. The bottom prism has side $10\text{ ft}$, height $2\text{ ft}$; middle has side $8\text{ ft}$, height $2\text{ ft}$; top has side $6\text{ ft}$, height $2\text{ ft}$. Calculate total concrete volume and total exposed surface area (excluding the bottom base).
  * *Tier 3 (Item 55):* A hollow steel block has outer dimensions $25\text{ cm} \times 20\text{ cm} \times 15\text{ cm}$. A rectangular hole of dimensions $10\text{ cm} \times 10\text{ cm}$ is drilled through the center along the height. Find the total volume of steel remaining and the mass if steel density is $7.85\text{ g/cm}^3$.
* **Diagnostic Feedback Guidelines:** Reinforce the additive property ($V_1 + V_2$) and subtractive property ($V_{\text{gross}} - V_{\text{void}}$). Correct double-counting errors along shared internal faces.

---

#### Topic 4: Order of Operations & Numerical Expressions in Geometric Contexts
* **Standard Code:** `NC.5.OA.2`
* **Baseline Objective:** Write, evaluate, and interpret numerical expressions involving parentheses and brackets for two-step problems.
* **AIG Extension Vector:** Nested grouping symbols ($[\{ \}]$), operational properties (distributive, associative) applied to volumetric expressions, and translating verbal geometric relationships into algebraic functions.
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 05):* Evaluate the expression representing the combined volume of two crates: $2 \times (8 \times 5 \times 4) + (12 \times 6 \times 3)$.
  * *Tier 2 (Item 30):* Write a single numerical expression with grouping symbols to represent: "Subtract the volume of a $3\text{ in.}$ cube from the product of the base area $(15 \times 8)$ and height $(10)$ of a larger prism, then divide the result by 5."
  * *Tier 3 (Item 48):* Evaluate and simplify the algebraic expression for $x = 4$: $\left[ 3(x^3 + 2x) - \frac{100}{x} \right] \div (x + 1)$.
* **Diagnostic Feedback Guidelines:** Enforce the hierarchy of operations (Parentheses/Brackets $\rightarrow$ Exponents $\rightarrow$ Multiplication/Division left-to-right $\rightarrow$ Addition/Subtraction left-to-right). Explicitly point out common errors where students distribute incorrectly across subtraction.

---

### MODULE 2: Multi-Digit Whole Number Operations (`NC.5.NBT.5`, `NC.5.NBT.6`)

#### Topic 5: Multi-Digit Whole Number Multiplication via Standard Algorithm
* **Standard Code:** `NC.5.NBT.5`
* **Baseline Objective:** Fluently multiply up to a $3\text{-digit}$ whole number by a $2\text{-digit}$ whole number using the standard algorithm.
* **AIG Extension Vector:** Extension to $4\text{-digit} \times 3\text{-digit}$ products, missing-digit cryptarithms, error analysis of partial products, and lattice/matrix multiplication structural comparisons.
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 15):* Calculate the exact product of $487 \times 63$ using the standard algorithm.
  * *Tier 2 (Item 32):* Solve the cryptarithm to find the missing digits $A$ and $B$:  
    $$\begin{array}{r@{\quad}l} 3A5 \\ \times \quad B4 \\ \hline 1,460 \\ + \quad 10,350 \\ \hline 11,810 \end{array}$$
  * *Tier 3 (Item 50):* Prove that for any two $2\text{-digit}$ numbers $10a + b$ and $10c + d$, their product equals $100(ac) + 10(ad + bc) + bd$, and use this identity to mentally calculate $94 \times 97$.
* **Diagnostic Feedback Guidelines:** Track positional value alignment errors, particularly forgetting the zero placeholder ($10^1$ shift) on the second partial product row.

---

#### Topic 6: Multi-Digit Whole Number Division via Partial Quotients & Area Models
* **Standard Code:** `NC.5.NBT.6`
* **Baseline Objective:** Find whole-number quotients and remainders with up to $4\text{-digit}$ dividends and $2\text{-digit}$ divisors using area models and partial quotients.
* **AIG Extension Vector:** Modular arithmetic ($a \pmod b$), contextual remainder optimization (rounding up vs. dropping remainders vs. expressing as mixed numbers), and prime factor cancelation strategies.
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 10):* Find the quotient and remainder for $3,458 \div 32$ using the partial quotients method.
  * *Tier 2 (Item 27):* A CMS logistics center needs to transport $5,200$ laptops. Each shipping crate holds $38$ laptops. How many total crates are required so that no laptop is left behind? How many empty slots remain in the final crate?
  * *Tier 3 (Item 56):* Determine the smallest positive integer $N > 1,000$ such that when $N$ is divided by $45$, $30$, and $18$, it leaves a constant remainder of $7$.
* **Diagnostic Feedback Guidelines:** Analyze student handling of remainders. Distinguish between theoretical mathematical division ($Q\text{ R }R$), continuous fractional division ($Q \frac{R}{D}$), and real-world discrete rounding constraints.

---

### MODULE 3: Decimal Place Value, Comparison & Addition/Subtraction (`NC.5.NBT.1`, `NC.5.NBT.2`, `NC.5.NBT.3`, `NC.5.NBT.7`)

#### Topic 7: Base-Ten Place Value Structure & Multiplicative Shifts ($10\times$, $\frac{1}{10}$)
* **Standard Code:** `NC.5.NBT.1`
* **Baseline Objective:** Explain that in a multi-digit number, a digit in one place represents 10 times as much as it represents in the place to its right and $\frac{1}{10}$ of what it represents to its left (from millions to thousandths).
* **AIG Extension Vector:** Multi-step place value shifts across non-adjacent positions ($10^k$ and $10^{-k}$ scaling), base-ten logarithmic logic, and algebraic place value equations ($100x = y$).
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 03):* How does the value of the digit $7$ in $4.572$ compare to the value of the digit $7$ in $45.72$?
  * *Tier 2 (Item 22):* A number $N$ is multiplied by $10^3$, then divided by $10^5$, resulting in $0.084$. Determine the original value of $N$ and express the net place-value shift as a power of 10.
  * *Tier 3 (Item 47):* In the decimal $0.d_1d_2d_3\dots$, $d_n$ represents the $n$-th digit after the decimal point. If $d_n$ follows the recursive rule $d_n = (3 \cdot d_{n-1}) \pmod{10}$ with $d_1 = 2$, write the first 6 digits and determine the exact value of the 100th decimal place.
* **Diagnostic Feedback Guidelines:** Address misconceptions regarding decimal movement. Emphasize that the digits shift positions relative to the fixed decimal point, rather than the decimal point "moving."

---

#### Topic 8: Powers of 10 Patterns & Exponential Operations
* **Standard Code:** `NC.5.NBT.2`
* **Baseline Objective:** Use whole-number exponents to denote powers of 10 ($10^1, 10^2, 10^3$) and explain patterns in placement of decimal points when multiplying/dividing by powers of 10.
* **AIG Extension Vector:** Scientific notation concepts ($a \times 10^b$ where $1 \le a < 10$), negative integer exponents ($10^{-1} = 0.1, 10^{-2} = 0.01$), and operational rules for multiplying powers of 10 ($10^m \cdot 10^n = 10^{m+n}$).
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 14):* Evaluate $48.5 \times 10^3$ and $48.5 \div 10^2$.
  * *Tier 2 (Item 36):* Convert the expression $(3.2 \times 10^4) + (4.5 \times 10^3)$ into standard decimal form and express the final sum in scientific notation.
  * *Tier 3 (Item 54):* Solve for $x$ in the exponential equation: $\frac{0.00056 \times 10^8}{1.4 \times 10^x} = 400$.
* **Diagnostic Feedback Guidelines:** Clarify that the exponent $k$ in $10^k$ indicates the number of places digits shift, NOT simply "adding $k$ zeros" (which fails for decimals, e.g., $3.4 \times 10^2 \neq 3.400$).

---

#### Topic 9: Reading, Writing, Expanded Form & Decimal Comparisons to Thousandths
* **Standard Code:** `NC.5.NBT.3a-b`
* **Baseline Objective:** Read, write, and compare decimals to thousandths using base-ten numerals, number names, expanded form, and symbols ($>, =, <$).
* **AIG Extension Vector:** Expanded form with negative powers of ten ($\sum d_i \cdot 10^{-i}$), density of rational numbers (finding decimals strictly bounded between two close thousandths), and algebraic decimal inequalities.
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 07):* Express $304.058$ in expanded form using fractions or decimals: $(3 \times 100) + (4 \times 1) + (5 \times \frac{1}{100}) + (8 \times \frac{1}{1000})$.
  * *Tier 2 (Item 25):* Identify all decimal values for $x$ rounded to thousandths that satisfy the inequality: $0.458 < x < 0.460$, where $x$ contains the digit '9' in the ten-thousandths place.
  * *Tier 3 (Item 49):* Order the following numbers from least to greatest without converting entirely to standard form, justifying via place value structure:  
    $$A = 3 \times 10^0 + 4 \times 10^{-2} + 9 \times 10^{-3}, \quad B = 3.048, \quad C = \frac{3051}{1000}, \quad D = 3 \times 10^0 + 5 \times 10^{-2}$$
* **Diagnostic Feedback Guidelines:** Watch for "longer is larger" misconceptions (e.g., student incorrectly thinking $0.4589 > 0.46$ because $4589 > 46$). Enforce column-by-column left-to-right place value evaluation.

---

#### Topic 10: Decimal Addition & Subtraction to Thousandths
* **Standard Code:** `NC.5.NBT.7`
* **Baseline Objective:** Add and subtract decimals to thousandths using concrete models, place value strategies, and estimation.
* **AIG Extension Vector:** Multi-variable algebraic decimal systems, missing digit sum/difference cryptarithms, error propagation analysis in financial transactions, and mental math strategies (compensation, landmark numbers).
* **Question Archetypes (out of required 60):**
  * *Tier 1 (Item 16):* Calculate the exact difference: $84.025 - 29.387$.
  * *Tier 2 (Item 38):* A scientific scale measures masses to thousandths of a gram. Three samples are weighed: Sample A = $14.285\text{ g}$, Sample B is $3.89\text{ g}$ heavier than Sample A, and Sample C is $2.047\text{ g}$ lighter than Sample B. Find the combined total mass of all three samples.
  * *Tier 3 (Item 60):* Solve for $x$ and $y$ in the system of decimal equations:  
    $$x + y = 12.458, \quad x - y = 3.892$$  
    Use compensation mental strategies to verify your solution without traditional paper-and-pencil stack alignment.
* **Diagnostic Feedback Guidelines:** Emphasize place value alignment (lining up the decimal point, adding trailing zero placeholders). Reinforce estimation prior to calculation as a check for reasonableness.

---

## 4. Master Q1 Data & Content Inventory Table

The following master inventory table summarizes the complete content specification requirement for the Q1 launch. The authoring pipeline must deliver **60 questions + 60 step-by-step diagnostic solutions per topic**, yielding an aggregate total of **600 unique, validated items**.

| Q1 Week Window | Domain & Standard Code | Q1 Topic Name | Baseline Scope Summary | AIG Acceleration & Enrichment Vector | Content Quota per Topic | Total Output Target |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Weeks 1–2** | `NC.5.MD.3`<br>`NC.5.MD.4` | **1. Unit Cube Packing & 3D Spatial Layers** | Unit cube counting; building prisms; spatial volume concepts. | Spatial coordinate matrices; fractional packing density; $SA:V$ optimization. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Weeks 1–2** | `NC.5.MD.5a-b` | **2. Rectangular Prism Volume Formulas** | $V = l \cdot w \cdot h$ and $V = B \cdot h$ applications. | Algebraic edge terms ($x, x+2$); cubic scaling factors; space diagonals. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 3** | `NC.5.MD.5c` | **3. Additive Volume of Composite Solids** | Decomposing 2-part L-shaped non-overlapping solids. | 3+ prism stacks; hollow-core subtractions; density and mass calculations. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 3** | `NC.5.OA.2` | **4. Numerical Expressions & Order of Ops** | Two-step expressions with parentheses in volume context. | Nested grouping symbols ($[\{\}]$); algebraic expansion; order of ops hierarchy. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Weeks 4–5** | `NC.5.NBT.5` | **5. Multi-Digit Algorithm Multiplication** | Fluency in $3\text{-digit} \times 2\text{-digit}$ standard algorithm. | $4\text{-digit} \times 3\text{-digit}$ products; digit cryptarithms; polynomial product proofs. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 6** | `NC.5.NBT.6` | **6. Multi-Digit Partial Quotients Division** | $4\text{-digit} \div 2\text{-digit}$ quotients, area models, remainders. | Modular arithmetic ($a \pmod b$); remainder rounding logic; prime factor division. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 7** | `NC.5.NBT.1` | **7. Base-Ten Place Value Structure ($10\times, \frac{1}{10}$)** | Shifts from millions to thousandths across adjacent positions. | Multi-position scaling ($10^k$); base-10 logarithms; recursive decimal sequences. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 7** | `NC.5.NBT.2` | **8. Powers of 10 & Exponential Operations** | Whole-number exponents ($10^3$) and decimal point shifts. | Scientific notation ($a \times 10^b$); negative exponents ($10^{-k}$); exponential equations. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 8** | `NC.5.NBT.3a-b` | **9. Decimal Expanded Form & Comparisons** | Read, write, compare decimals to thousandths via symbols. | Negative power expanded form; density of rational numbers; algebraic bounds. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **Week 9** | `NC.5.NBT.7` | **10. Decimal Addition & Subtraction** | Add/subtract to thousandths using place value & estimation. | Multi-variable decimal systems; cryptarithms; mental math landmark compensation. | 60 Questions + 60 Solutions | 120 Content Artifacts |
| **TOTALS** | **Q1 Core** | **10 Master Q1 Topics** | **Complete Q1 NCSCoS Coverage** | **Exhaustive AIG Acceleration** | **600 Questions + 600 Solutions** | **1,200 Total Content Artifacts** |

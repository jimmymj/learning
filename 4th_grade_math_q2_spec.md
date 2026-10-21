# Product Specification Document: 4th Grade Interactive Math Learning App (CMS / NC SCOS Quarter 2 Curriculum)

## 1. System Architecture & Pedagogical Framework Overview

The strategic alignment between software interface engineering and the Charlotte-Mecklenburg Schools (CMS) Quarter 2 mathematics curriculum is an essential driver of elementary learning outcomes. Built upon the Illustrative Mathematics (IM K–5) framework and aligned directly to the North Carolina Standard Course of Study (NC SCOS), the CMS Quarter 2 curriculum marks a critical transition point in 4th-grade mathematical development. During this window, students move from foundational whole-number operations and simple fraction mechanics to fraction-decimal equivalence, multi-digit arithmetic, place-value structures up to 100,000, and spatial measurement applications.

Software design must avoid treating digital interactions as static, digitalized worksheets. Instead, the application UI/UX must function as an interactive conceptual bridge, translating concrete visual models—such as partitioned tape diagrams, dual 10x10 decimal grids, partial-product area models, open timeline jumpers, and fractional line plot builders—into dynamic, reactive digital manipulatives. By enabling learners to directly manipulate mathematical structures and receive real-time, diagnostically targeted feedback, the digital software architecture fosters deep conceptual understanding, spatial intuition, and procedural fluency.

### Pedagogical Foundations & Design Principles

The CMS elementary mathematics philosophy dictates that mathematical proficiency develops when students actively engage with concrete manipulatives, solve contextual word problems, and articulate their reasoning both orally and in writing. In Quarter 2, instruction spans three interconnected content units: completing the study of fraction operations (Unit 3 continuation), expanding place value patterns, decimal concepts, and multi-digit operations (Unit 4), and initiating measurement, area, perimeter, and fractional data applications (Unit 5). The application architecture operationalizes these instructional targets into three core interactive UI/UX clusters.

| Cluster ID | Core Topic Cluster Description | Illustrative Math Units | Target Mathematical Domains & NC SCOS Standards |
| :--- | :--- | :--- | :--- |
| **Cluster 1** | Fractions Continuation & Decimal Notation | Unit 3 (Continuation) & Unit 4 (Part A) | Number & Operations–Fractions (NC.4.NF): NC.4.NF.1, NC.4.NF.2, NC.4.NF.3, NC.4.NF.6, NC.4.NF.7 *(Note: NC SCOS folds decimal fraction addition into NC.4.NF.6 and NC.4.NF.3)* |
| **Cluster 2** | Place Value, Multi-Digit Operations & Multiplicative Comparison | Unit 4 (Part B) | Number & Operations in Base Ten (NC.4.NBT): NC.4.NBT.1, NC.4.NBT.2, NC.4.NBT.5, NC.4.NBT.6; Operations & Algebraic Thinking (NC.4.OA): NC.4.OA.1, NC.4.OA.2, NC.4.OA.3 *(Note: 4-digit by 1-digit is Q2 core; 2-digit by 2-digit is Q3 Readiness)* |
| **Cluster 3** | Area, Perimeter, Measurement & Fractional Data | Unit 5 (Initiation) | Measurement & Data (NC.4.MD): NC.4.MD.1, NC.4.MD.2, NC.4.MD.3, NC.4.MD.4, NC.4.MD.8 |

*Architectural Alignment Footnote: While national Common Core standards designate standard number 4.NF.5 for expressing tenths as hundredths and adding decimal fractions (3/10 + 45/100), the official North Carolina Standard Course of Study (NC SCOS) taxonomy skips NC.4.NF.5 entirely, folding these concepts directly under NC.4.NF.6 and NC.4.NF.3. All assessment tags and engine schemas in this software specification strictly adhere to NC SCOS standard numbering.*

*Scope Reconciliation Footnote: According to CMS curriculum pacing, Quarter 2 Unit 4 prioritizes 4-digit by 1-digit multiplication (NC.4.NBT.5). Multi-digit multiplication of 2-digit by 2-digit numbers is formally introduced in Unit 6 during Quarter 3. The app engine treats 4-digit by 1-digit multiplication as the core Quarter 2 target, while framing 2-digit by 2-digit multiplication (24 × 13) as an "Advanced Extension / Q3 Readiness Component."*

### Standards for Mathematical Practice Integration
- **MP1 (Make sense of problems and persevere in solving them)**: Multi-step contextual problems paired with dynamic scaffolding panels. When an incorrect response is recorded, the UI deploys progressive visual hints and manipulative call-to-action prompts.
- **MP4 (Model with mathematics)**: Software components require students to generate and manipulate visual representations—such as partitioning area models, plotting fractional measurement data on line plots, or shading side-by-side decimal grids—before generating abstract numerical equations.
- **MP5 (Use appropriate tools strategically)**: The interface offers dynamic digital tools—including dual 10x10 grids, fraction-decimal slider scales, 10x place-value magnification charts, rectilinear grid slicing tools, and timeline jumpers.

---

## 2. Cluster 1 Specification: Fractions Continuation & Decimal Notation (NC.4.NF.1, NC.4.NF.2, NC.4.NF.3, NC.4.NF.6, NC.4.NF.7)

### 2.1 Pedagogical Foundations & Standards Alignment
Instruction follows a deliberate conceptual sequence:
1. Deepening fraction equivalence through visual length and area models (NC.4.NF.1, NC.4.NF.2).
2. Expressing a fraction with denominator 10 as an equivalent fraction with denominator 100 (e.g., 7/10 = 70/100).
3. Adding two fractions with respective denominators 10 and 100 by converting to a common denominator (NC.4.NF.6 and NC.4.NF.3, e.g., 3/10 + 45/100 = 30/100 + 45/100 = 75/100).
4. Connecting base-ten fractions to decimal notation (NC.4.NF.6), recognizing that 7/10 = 0.7 and 70/100 = 0.70.
5. Comparing two decimals up to hundredths (NC.4.NF.7) by reasoning about their spatial size relative to the same whole and applying symbols (>, =, <).

### 2.2 Interactive & Visual App UI Components
- **Interactive 10x10 Decimal Grid Component**: Side-by-side dual 10x10 grids. Left grid has 10 vertical columns (tenths); right grid has 100 individual squares (hundredths). Shading columns on left automatically synchronizes with 10 squares per column on right with real-time equivalence readouts: `4/10 = 40/100 ↔ 0.4 = 0.40`.
- **Dynamic Number Line & Fraction-Decimal Slider**: Horizontal number line anchored from 0 to 1 with dual tick marks above (fractions: 0/10 to 10/10 and 0/100 to 100/100) and below (decimals: 0.00 to 1.00). Snaps to benchmark positions (0.25, 0.50, 0.75) with magnification lens.

### 2.3 Question Distribution (20 Items)
- **Easy (6 Items)**: Direct grid identification, basic fraction-to-decimal translations (e.g., 6/10 = 0.6).
- **Medium (10 Items)**: Converting tenths to hundredths for addition (3/10 + 25/100); plotting decimals on interactive number lines; comparing decimals with different place lengths (0.8 vs 0.74).
- **Hard (4 Items)**: Multi-step contextual word problems involving fraction-decimal conversions, liquid volume (5/10 L + 28/100 L = 0.78 L), and sorting decimal magnitudes.

---

## 3. Cluster 2 Specification: Place Value, Multi-Digit Operations & Multiplicative Comparison (NC.4.NBT.1, NC.4.NBT.2, NC.4.NBT.5, NC.4.NBT.6, NC.4.OA.1, NC.4.OA.2, NC.4.OA.3)

### 3.1 Pedagogical Foundations & Standards Alignment
- **Place Value Structure (NC.4.NBT.1, NC.4.NBT.2)**: Numbers up to 100,000. Shifting one place value to the left multiplies positional value by 10 (e.g., 4 in ten-thousands is 10 times greater than 4 in thousands).
- **Multiplicative Comparison (NC.4.OA.1, NC.4.OA.2)**: Distinguishing additive ("3 more than") from multiplicative ("3 times as many as") relationships. Modeling with tape diagrams and equations.
- **Multi-Digit Multiplication (NC.4.NBT.5)**: 4-digit by 1-digit multiplication via partial products and area models. 2-digit by 2-digit (24 × 13 = 312) included as Q3 Readiness Extension.
- **Division with Remainders (NC.4.NBT.6)**: Up to 3-digit dividends by 1-digit divisors via partial quotients. Contextual interpretation of remainders (e.g. 125 students in 8-passenger vans requires 16 vans).

### 3.2 Interactive & Visual App UI Components
- **Place Value Chart with 10x Magnification Animation**: Columns for Ten-Thousands, Thousands, Hundreds, Tens, Ones. Dragging digit tiles left triggers 10x zoom animation and unit block regrouping.
- **Dynamic Area Model Generator for Multiplication**: Interactive canvas with input fields for 4x1 and 2x2 multiplication. Visual partition lines split factors by expanded form, calculating sub-region partial products and total product.
- **Partial Quotients & Remainder Visualizer**: Visual stack subtraction with custom divisor chunking, displaying quotient and visual remainder highlights.

### 3.3 Question Distribution (20 Items)
- **Easy (6 Items)**: Place value identification up to 100,000, basic multiplicative comparison equations (8 × 4 = c), single-digit multiplication fact fluency.
- **Medium (10 Items)**: 4-digit by 1-digit partial products, 3-digit by 1-digit division with partial quotients, 10x place value shift calculations.
- **Hard (4 Items)**: Multi-step word problems with variables, 2-digit by 2-digit multiplication extension (24 × 13), division word problems requiring real-world remainder rounding.

---

## 4. Cluster 3 Specification: Area, Perimeter, Measurement & Fractional Data (NC.4.MD.1, NC.4.MD.2, NC.4.MD.3, NC.4.MD.4, NC.4.MD.8)

### 4.1 Pedagogical Foundations & Standards Alignment
- **Area & Perimeter (NC.4.MD.3)**: Rectangles (A = l × w, P = 2l + 2w) and missing side lengths.
- **Rectilinear Figures (NC.4.MD.3)**: Decomposing non-overlapping L-shaped shapes into sub-rectangles and summing areas.
- **Fractional Line Plots (NC.4.MD.4)**: Displaying measurement data with unit fractions (1/2, 1/4, 1/8) on interactive line plots and solving operational data questions.
- **Metric System Conversions (NC.4.MD.1)**: Relative sizes and two-column conversion tables (km → m, kg → g, l → ml).
- **Elapsed Time & Measurement Word Problems (NC.4.MD.2, NC.4.MD.8)**: Calculating elapsed time crossing hour marks using open timeline jumps.

### 4.2 Interactive & Visual App UI Components
- **Interactive Area & Perimeter Rectilinear Grid Tool**: Corner stretch handles and dotted decomposition slicing tool for L-shaped figures.
- **Interactive Fractional Line Plot Builder Component**: Horizontal line plot scaled in eighths and fourths, dragging data points from a measurement table, and difference ruler tool.
- **Interactive Metric Conversion Two-Column Tables**: Drag-and-drop rule markers ("Multiply by 1,000") with animated calculations.
- **Digital Time Wheel / Elapsed Time Open Number Line**: Dual clock (analog + digital) and timeline jumper with discrete interval jumps (+15 mins, +2 hrs).

### 4.3 Question Distribution (20 Items)
- **Easy (6 Items)**: Direct calculation of area and perimeter for simple rectangles, direct metric table lookups, plotting fractional data points.
- **Medium (10 Items)**: Finding missing side length given area or perimeter, decomposing L-shaped figures (24 + 6 = 30 sq m), metric conversions with multi-digit multiplication, line plot difference questions.
- **Hard (4 Items)**: Fixed area perimeter optimization (36 sq ft pen with minimum perimeter = 6 ft × 6 ft, P = 24 ft), multi-step elapsed time crossing hour marks (10:45 AM to 1:15 PM = 2 hrs 30 mins), multi-step line plot spread problems.

---

## 5. System Engine & Assessment Delivery Architecture
- **Total Questions**: 60 questions (20 questions per cluster, strictly balanced).
- **Dynamic Shuffling**: Fisher-Yates runtime shuffling for all multiple-choice options, visual cards, and draggable items with dynamic letter badging (A, B, C, D) and object-level answer validation.
- **Visual Solution Breakdown**: Interactive SVG diagrams and kid-friendly explanations for every question.
- **Misconception Remediation Drawers**: Instant slide-up mini-interventions diagnosing specific root causes (whole-number decimal bias, denominator addition, additive comparison confusion, area/perimeter confusion, base-10 clock subtraction).
- **Pip the Math Fox Mascot**: Encouraging mascot voice read-aloud and guidance.
- **Interactive Whiteboard Scratchpad**: Full-screen canvas overlay with pen, highlighter, eraser, color palette, and clear tools.

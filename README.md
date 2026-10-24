# 🌟 LearningHub | Interactive Educational Lab Suite

An open-source collection of browser-native, interactive educational visualizers, simulators, and mastery challenges designed for Honors STEM students and educators.

Deployed at: **[GitHub Repository](https://github.com/jimmymj/learning)**

---

## 📂 Repository Directory Structure

```text
learning/
├── index.html                                        # Central LearningHub Portal & App Launcher
├── README.md                                         # Project Documentation & Guide
├── science_olympiad_coach_4th_grade_app_module.md    # Comprehensive 4th Grade ASO App Module Spec
├── 5th_grade_aig_math_q1_spec.md                     # Comprehensive 5th Grade AIG Math Q1 Spec
├── 4th_grade_math_q2_spec.md                         # Comprehensive 4th Grade Math Q2 Spec
├── 4th_grade_math_spec.md                            # Comprehensive 4th Grade Math Q1 Spec
├── .gitignore                                        # Standard repository ignores
├── .agents/                                          # Workspace Customizations & Skills
│   └── skills/
│       └── learning-app/                             # AI Learning App & Simulation Architect Skill
├── apps/                                             # Interactive Learning Applications
│   ├── science/                                      # Science Olympiad & Scientific Inquiry Suite
│   │   ├── index.html                                # Scalable Science Olympiad Coaching Portal (Div A, B, C)
│   │   └── science_olympiad_coach_4th_grade.html     # Division A & Foundations Olympiad Coach, Simulations & Misconception Lab (Grades 3-6+)
│   └── math/                                         # Mathematics Subject Area
│       ├── 5th_grade_aig_math_volume_operations_decimals_q1.html             # Spatial Volume, Algorithms & Decimal Systems Lab (Q1 AIG)
│       ├── 4th_grade_math_decimals_multi_digit_measurement_q2.html           # Decimals, Operations & Measurement (Q2)
│       ├── 4th_grade_math_factors_fractions_operations.html                  # Factors, Multiples & Fractions Lab (Q1)
│       ├── 8th_grade_honors_math_functions_linear_quadratic_exponential.html # Function Velocity & Growth Lab
│       └── 8th_grade_honors_math_visualizer_dilations_similarity_slope.html  # Dilations, Similarity & Slope Lab
└── assets/                                           # Shared Portal Assets
    ├── css/
    │   └── portal.css                                # Glassmorphic Modern Design System
    └── js/
        └── portal.js                                 # Dynamic Canvas Animations & Modal Runner
```

---

## 🚀 Available Learning Apps & Portals

### 0. 🏆 Science Olympiad Coaching Portal & Division A Foundations Lab
- **Portal Location:** [`apps/science/index.html`](apps/science/index.html)
- **Flagship App Location:** [`apps/science/science_olympiad_coach_4th_grade.html`](apps/science/science_olympiad_coach_4th_grade.html)
- **Target Audience:** Science Olympiad Competitors across Elementary & Junior grades (Division A: Grades 3-6+, Division B: Middle School 6-8, Division C: High School 9-12)
- **Curriculum Domains (Division A & Foundations):**
  - **Domain 1: Physical Science:** Matter, Mass, Volume & Relative Density (`ρ = m / V`), Buoyant Forces (`F_b = ρ_fluid · V_sub · g`), Stratification of immiscible liquids, Simple Machines (Levers, mechanical advantage force-distance tradeoffs), Energy Transformations, and Electrical Circuit conduction.
  - **Domain 2: Earth & Space Science:** The Water Cycle (solar radiation energy source + gravity force vector), Weather systems, Earth-Moon-Sun orbital geometry, 8 Lunar Phases, and Earth's 23.5° axial tilt seasonal insolation angle (busting the orbital distance myth).
  - **Domain 3: Life Science:** Wetland Food Webs & Trophic Cascades (predator removal triggering competitive release and overgrazing on producers), 10% Energy Pyramid Rule, Structural vs. Behavioral desert adaptations (Fennec Fox), and Interconnected Body Systems during exercise.
  - **Domain 4: Scientific Inquiry & Nature of Science:** Experimental Design & Single-Variable Fair Tests (Independent, Dependent, and Controlled Variables), Confounding Variable Audits, and Phase Change Cooling Curve Temperature Plateaus (Latent Heat of Fusion).
- **Core Features:**
  - **Scalable Olympiad Hub:** Dynamic JSON registry (`OLYMPIAD_REGISTRY`) supporting quick filtering by Division (A, B, C), Domain (Physical, Earth, Life, Inquiry), and Status (Active vs. Roadmap), plus an embedded modal runner and personal training log (`localStorage`).
  - **4 Synchronized Dynamic Simulations:** Density Stratification Column with thermal expansion heating, Wetland Trophic Cascade Network with pesticide mortality slider and prey shift toggles, Circuit Conductor Fair-Test Bench with live Ammeter current and bulb filament lumens, and Earth-Moon-Sun Orbit Model with axial tilt controls.
  - **4-Step Olympiad Solving Routine:** Metacognitive discipline embedded in every challenge (*Step 1: Identify Core Principle*, *Step 2: Eliminate Impossible Edge Cases*, *Step 3: Test Remaining Logic*, *Step 4: Verify with Scientific Principles*).
  - **Coach's Pit Stop Misconception Engine:** Interactive slide-up drawer for wrong answers analyzing cognitive traps (Size vs Density Fallacy, Open Switch Fallacy, Confounding Variables, Inverted Density, Reverse Physiology) with Retry Token support.
  - **Coach Nova Voice Mentor & Whiteboard Scratchpad:** Text-to-Speech synthesis read-aloud and a full-screen drawing/annotation overlay with pen, highlighter, eraser, and color palette.
  - **12 Graded Tournament Challenges:** Exhaustive coverage with 60s countdown timer (with Zen Mode toggle), score HUD, streak multipliers, and procedural Web Audio API feedback.
  - **Custom Non-Intrusive Messaging:** 100% custom in-app glassmorphic toast notifications and confirmation modals (Zero disruptive browser `alert()` or `confirm()` popup windows).

### 1. 🧊 CMS 5th Grade AIG Math: Spatial Volume, Algorithms & Decimal Systems Lab (Q1)
- **Location:** [`apps/math/5th_grade_aig_math_volume_operations_decimals_q1.html`](apps/math/5th_grade_aig_math_volume_operations_decimals_q1.html)
- **Target Audience:** 5th Grade Academically or Intellectually Gifted (AIG) Mathematics (CMS Quarter 1 / Illustrative Math Units 1, 4, 5 / NC SCOS)
- **Curriculum Standards:**
  - **Module 1 (NC.5.MD.3, 4, 5a-c; NC.5.OA.2):** Spatial Volume Reasoning & 3D Geometry (unit cube packing, associative volume `V = (l × w) × h`, layer-by-layer slicing `V = B × h`, composite L-shaped solids, hollow-core cavity void subtraction `V_outer - V_void`, surface-area-to-volume ratio optimization, space diagonal `d = √(l² + w² + h²)`).
  - **Module 2 (NC.5.NBT.5, 6):** Multi-Digit Whole Number Operations & Algorithmic Reasoning (standard algorithm place-value alignment, partial products area models up to 3-digit × 2-digit, partial quotients division up to 4-digit ÷ 2-digit, algorithmic cryptarithms `3A5 × B4 = 11,810`, and real-world remainder interpretations).
  - **Module 3 (NC.5.NBT.1, 2, 3a-b, 7):** Decimal Place Value Patterns, Exponents & Operations (base-10 exponential powers `10⁻³` to `10⁶`, metric metric prefix shifts, thousandths expanded notation, decimal inequalities `<, =, >`, benchmark rounding, and mental compensation arithmetic).
- **Features:**
  - **Interactive 3D Prism Sandbox:** Rotatable 3D wireframe prism with pitch/yaw mouse drag, dynamic wireframe render, internal space diagonal telemetry, layer-by-layer slicing toggle, and live volume calculations.
  - **Partial Products Area Model & Cryptarithm Solver:** Interactive 3×2 grid multiplier with live digit cryptarithm puzzle generator.
  - **Base-10 Exponential Shifter:** Interactive slider exploring powers of 10 from $10^{-3}$ to $10^{6}$ with place-value column migration.
  - **60-Question AIG Mastery Quest:** 20 questions per module across 10 curriculum topics spanning 3 rigor tiers (Tier 1 Level 4/5 Mastery, Tier 2 Non-Routine AIG Logic, Tier 3 Pre-Algebra/Competition).
  - **4-Part Diagnostic Feedback Panels:** Every question features Step-by-Step Walkthrough, Core Mathematical Principle, Common Misconceptions Diagnosis, and Fast-Track Competition Shortcut.
  - **Aria Vance Gifted Scholar Persona:** Elegant, high-density, low-friction dark obsidian interface calibrated for intellectual rigor without childish clutter.
  - **Interactive Whiteboard Scratchpad & Audio Synth:** Full canvas scratchpad with pen, highlighter, eraser, multi-color palette, and Web Audio sound feedback.

### 2. 📊 CMS 4th Grade Math: Decimals, Multi-Digit Operations & Measurement Lab (Q2)
- **Location:** [`apps/math/4th_grade_math_decimals_multi_digit_measurement_q2.html`](apps/math/4th_grade_math_decimals_multi_digit_measurement_q2.html)
- **Target Audience:** 4th Grade Elementary Mathematics (CMS Quarter 2 / Illustrative Math / NC SCOS)
- **Curriculum Standards:**
  - **Cluster 1 (NC.4.NF.1, 2, 3, 6, 7):** Fractions Continuation & Decimal Notation (tenths/hundredths equivalence `0.4 = 40/100`, decimal number line with 10× zoom, decimal comparisons `<, =, >`, mixed number decimal conversions).
  - **Cluster 2 (NC.4.NBT.1, 2, 5, 6; NC.4.OA.1, 2, 3):** Place Value, Multi-Digit Operations & Multiplicative Comparison (10× place-value shifter, multi-digit partial products area model `243 × 6 = 1,200 + 240 + 18 = 1,458`, partial quotients division visualizer `432 ÷ 4`, two-step word problems).
  - **Cluster 3 (NC.4.MD.1, 2, 3, 4, 8):** Area, Perimeter, Measurement & Fractional Data (rectilinear composite polygon decomposition `24 + 6 = 30 m²`, two-pan metric/customary conversion balance, fractional pencil line plot with difference calculations, analog/digital elapsed time timeline).
- **Features:**
  - **9 Interactive Digital Manipulatives:** Dual Tenths/Hundredths Grids, Decimal Number Line with 10× Magnifying Zoom, Place-Value Base-Ten Shifter, Multi-Digit Partial Products Area Model, Partial Quotients Visualizer, Rectilinear L-Shaped Polygon Decomposer, Two-Pan Measurement Unit Balance, Fractional Pencil Line Plot, and Elapsed Time Timeline.
  - **Pip the Math Fox Mascot:** Friendly, voice-enabled guide offering encouraging feedback, mastery tracking, and Socratic hints.
  - **Interactive Whiteboard Scratchpad:** Canvas overlay with pen, highlighter, eraser, multi-color palette, and full undo/clear support for student problem-solving.
  - **60-Question Adaptive Mastery Quest:** 20 questions per cluster (6 Easy, 10 Medium, 4 Hard) across Multiple Choice, Visual Selection, Interactive Number Line, and Drag & Drop formats.
  - **Balanced Answer Choices & Shuffling:** Dynamic runtime Fisher-Yates shuffling across options and trays with object-level answer validation.
  - **Misconception Remediation Drawers:** Interactive slide-up mini-interventions diagnosing root mathematical misconceptions in real time with visual diagram breakdowns.

### 2. 🦊 CMS 4th Grade Math: Factors, Multiples & Fractions Lab (Q1)
- **Location:** [`apps/math/4th_grade_math_factors_fractions_operations.html`](apps/math/4th_grade_math_factors_fractions_operations.html)
- **Target Audience:** 4th Grade Elementary Mathematics (CMS Quarter 1 / Illustrative Math / NC SCOS)
- **Curriculum Standards:**
  - **NC.4.OA.4:** Factors and multiples for whole numbers 1–100, factor pairs, prime and composite classification, and multiplicative thinking.
  - **NC.4.NF.1 & NC.4.NF.2:** Fraction equivalence `a/b = (n × a)/(n × b)` and benchmark comparisons against 0, 1/2, and 1 for standard denominators (2, 3, 4, 5, 6, 8, 10, 12, 100).
  - **NC.4.NF.3 & NC.4.NF.4:** Decomposing fractions into unit fractions, addition and subtraction with like denominators, and multiplying whole numbers by unit fractions (`n × 1/b`) via repeated addition jump models.
- **Features:**
  - **9 Interactive Visual Manipulatives:** Area Grid Arrays, 12 × 12 Skip-Count Matrices, Equal-Group Remainder Bundlers, Stacked Tape Strips, Dual Number Lines, Area Partitioners, Decomposition Tile Canvases, Length Tape Models, and Repeated Addition Jump Tools.
  - **Pip the Math Fox Mascot:** Friendly, voice-enabled guide offering encouraging feedback, mastery tracking, and Socratic hints.
  - **Interactive Whiteboard Scratchpad:** Canvas overlay with pen, highlighter, eraser, multi-color palette, and full undo/clear support for student problem-solving.
  - **60-Question Adaptive Mastery Quest:** 20 questions per unit (6 Easy, 8 Medium, 6 Hard) across Multiple Choice, Visual Selection, Interactive Number Line, and Drag & Drop formats.
  - **Balanced Answer Choices & Shuffling:** Dynamic runtime Fisher-Yates shuffling across options and trays with object-level answer validation.
  - **Misconception Remediation Drawers:** Interactive slide-up mini-interventions diagnosing root mathematical misconceptions in real time with visual diagram breakdowns.

### 3. 📈 CMS 8th Honors Math: Function Velocity & Growth Lab
- **Location:** [`apps/math/8th_grade_honors_math_functions_linear_quadratic_exponential.html`](apps/math/8th_grade_honors_math_functions_linear_quadratic_exponential.html)
- **Target Audience:** 8th Grade Honors Mathematics / Math 1 Bridge
- **Curriculum Standards:**
  - **NC.8.F.1:** Function definition, notation `f(x)`, mapping, evaluating functions, continuous vs. discrete domain/range, and asymptotic behavior.
  - **NC.8.F.2:** Comparing properties and rates of change of two functions represented algebraically, graphically, or numerically.
  - **NC.8.F.3:** Distinguishing linear from non-linear relationships via first differences, second differences, and constant ratios.
  - **NC.8.F.4:** Constructing function models to interpret rate of change (`m = Δy / Δx`) and initial values in real-world contexts.
  - **NC.8.F.5:** Qualitative graphing, analyzing symmetry, intervals of increase/decrease, and long-term exponential growth dominance.
- **Features:**
  - **Function Triad Explorer:** Real-time graphing canvas for Linear (`mx + b`), Quadratic (`ax² + bx + c`), and Exponential (`a · bˣ`) functions with responsive parameter sliders.
  - **Secant Rate-of-Change Engine:** Interactive `[x₁, x₂]` interval selector displaying the secant line, slope triangle (`Δx, Δy`), and live computed Average Rate of Change (`Δy / Δx`).
  - **The Great Growth Race:** Particle race simulation visualizing how exponential growth inevitably overtakes linear and polynomial models.
  - **Difference Engine:** Dynamic table tester computing 1st differences, 2nd differences, and ratios to prove algebraic classification.
  - **20-Question Honors Mastery Challenge:** Graded quiz with 45s countdown timer, score HUD, streak multipliers, step-by-step explanations, and a "Retry Missed Questions" flow.

### 4. 📐 CMS 8th Honors Math: Dilations, Similarity & Slope Lab
- **Location:** [`apps/math/8th_grade_honors_math_visualizer_dilations_similarity_slope.html`](apps/math/8th_grade_honors_math_visualizer_dilations_similarity_slope.html)
- **Target Audience:** 8th Grade Honors Mathematics / Accelerated Pre-Algebra & Math 1
- **Curriculum Standards:**
  - **NC.8.G.3:** Coordinate transformations and algebraic rules `(x, y) → (kx, ky)` with arbitrary center of dilation `(cx, cy)`.
  - **NC.8.G.4:** Similarity transformation sequences (composition of translations, reflections, rotations, and dilations).
  - **NC.8.EE.6:** Using similar right slope triangles to prove constant rate of change and derive `y = mx + b`.
- **Features:**
  - **Coordinate Dilations Explorer:** Real-time scaling from origin `(0, 0)` or any custom center `(cx, cy)` with reduction (`k < 1`) and enlargement (`k > 1`) indicators.
  - **Similarity Sequence Laboratory:** Step-by-step animated multi-transformation pipeline demonstrating angle preservation and proportionality.
  - **Slope Triangles Engine:** Visual proof showing that the ratio of vertical change to horizontal change (`Δy / Δx`) is constant along any two points on a line.
  - **Honors Formula Cheat Sheet:** Comprehensive definitions, scale factor rules, and algebraic notation summary.
  - **20-Question Graded Quiz:** Rigorous multiple-choice assessment with instant answer validation and scoring.

---


## 💻 How to Run Locally

Because the apps are built using vanilla web technologies (HTML5, CSS3, JavaScript, Canvas API), no build step, Node.js server, or dependencies are required.

1. **Directly in Browser:**
   - Double-click [`index.html`](index.html) to open the LearningHub portal in any modern browser (Chrome, Edge, Firefox, Safari).
   - From the portal, launch the lab in fullscreen or embedded preview mode.

2. **Using a Local Server (Optional):**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Or Node.js
   npx serve .
   ```
   Open `http://localhost:8000` in your web browser.

---

## 🌐 Enabling GitHub Pages

To make the apps accessible on the public web at `https://jimmymj.github.io/learning/`:

1. Open your repository on GitHub: [https://github.com/jimmymj/learning](https://github.com/jimmymj/learning)
2. Go to **Settings** > **Pages** (under the "Code and automation" sidebar section).
3. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
4. Set branch to **`main`** and folder to **`/(root)`**.
5. Click **Save**. Within 1–2 minutes, your portal will be live at `https://jimmymj.github.io/learning/`!

---

## 🛠️ Adding New Apps to the Suite

To add a new interactive learning app:
1. Place the new HTML application under `apps/<subject>/<app_name>.html` (e.g. `apps/physics/pendulum_motion.html`).
2. Add a new card or link entry in [`index.html`](index.html).
3. Commit and push your changes to GitHub!

---

## 📄 License
MIT License. Free for educational and non-commercial classroom use.

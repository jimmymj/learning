# 🌟 LearningHub | Interactive Educational Lab Suite

An open-source collection of browser-native, interactive educational visualizers, simulators, and mastery challenges designed for Honors STEM students and educators.

Deployed at: **[GitHub Repository](https://github.com/jimmymj/learning)**

---

## 📂 Repository Directory Structure

```text
learning/
├── index.html                                        # Central LearningHub Portal & App Launcher
├── README.md                                         # Project Documentation & Guide
├── 4th_grade_math_spec.md                            # Comprehensive 4th Grade Math Curriculum & Spec
├── .gitignore                                        # Standard repository ignores
├── .agents/                                          # Workspace Customizations & Skills
│   └── skills/
│       └── learning-app/                             # AI Learning App & Simulation Architect Skill
├── apps/                                             # Interactive Learning Applications
│   └── math/                                         # Mathematics Subject Area
│       ├── 4th_grade_math_factors_fractions_operations.html                  # Factors, Multiples & Fractions Lab
│       ├── 8th_grade_honors_math_functions_linear_quadratic_exponential.html # Function Velocity & Growth Lab
│       └── 8th_grade_honors_math_visualizer_dilations_similarity_slope.html  # Dilations, Similarity & Slope Lab
└── assets/                                           # Shared Portal Assets
    ├── css/
    │   └── portal.css                                # Glassmorphic Modern Design System
    └── js/
        └── portal.js                                 # Dynamic Canvas Animations & Modal Runner
```

---

## 🚀 Available Learning Apps

### 1. 🦊 CMS 4th Grade Math: Factors, Multiples & Fractions Lab
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

### 2. 📈 CMS 8th Honors Math: Function Velocity & Growth Lab
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

### 3. 📐 CMS 8th Honors Math: Dilations, Similarity & Slope Lab
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

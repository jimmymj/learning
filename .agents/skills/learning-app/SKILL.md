---
name: learning-app
description: Build complete, production-grade, standalone single-file HTML/CSS/JS interactive learning applications for school students (K-12) from any academic topic, worksheet, image, PDF, or prompt. Features grade-calibrated multi-perspective framing, 3-tier scaffolding, synchronized 2D/3D simulations (SVG, Canvas, CSS 3D, WebGL), bulletproof browser-native Unicode/HTML math formatting, zero-native-popup in-app messaging, seamless adaptive dark/light contrast theming with canvas synchronization, gamified assessments with token/timer/Web Audio mechanics, interactive whiteboard scratchpad, Socratic hint drawers, adaptive mastery engines, and mandatory 3-point fact-checking for questions, answers, and explanations. Use whenever creating educational web apps, interactive visualizers, practice quizzes, classroom simulators, or digital study aids.
---
# Learning App Master Engine

Act as a principal educational software architect, instructional designer, and subject-matter verifier. Transform any academic topic, worksheet, curriculum standard, or prompt into a complete, standalone, single-file HTML/CSS/JS interactive micro-learning application.

## When to Use

- Building interactive web-based educational tools, visualizers, or classroom simulators for K-12 or self-study students.
- Converting worksheets, textbook problems, or exam prep topics into gamified digital practice apps with step-by-step explanations.
- Creating 2D/3D interactive math manipulatives, science labs, or multi-level study aids that run directly in any browser.

---

## Core Architecture & 8-Pillar Design Requirements

### 1. Grade Calibration, Multi-Perspective Framing & 3-Tier Scaffolding

- **Grade-Level Calibration** (infer target grade if unspecified, defaulting to Middle School with level toggles):
  - **Elementary (K-5)**: Playful, narrative-driven, high-contrast colorful visuals, friendly mascot/story guides, large touch-friendly buttons, and tactile exploration.
  - **Middle School (6-8)**: Gamified quest or mystery framing, discovery challenges, interactive badges, and cause-and-effect experimentation.
  - **High School (9-12)**: Sleek, analytical dashboard, real-world engineering/scientific context, data overlays, and rigorous depth.
- **Creative Multi-Perspective Lenses**: Frame concepts through distinct angles (*Story Hook*, *Data/Evidence Angle*, *Practical Playbook*, and *Real-World Application*) so students experience ideas beyond rote memorization.
- **3-Tier Scaffolding Tabs**: Inside the Concept Hub, structure explanations into progressive tabs or toggles:
  - **Level 1 (Intuitive/Visual)**: Concrete real-world analogies, plain-language summaries, and visual hooks.
  - **Level 2 (Operational/Core)**: Standard formulas, core definitions, and guided 4-step logic.
  - **Level 3 (Applied/Mastery)**: Edge-case mechanics, complex multi-step syntheses, and real-world applications.

---

### 2. Strict Mathematical & Scientific Expression Formatting (Browser-Native & Offline)

To strictly uphold **Zero External Dependencies** and guarantee flawless offline rendering without relying on external LaTeX renderers (such as KaTeX or MathJax CDNs), all mathematical, geometric, and scientific notations MUST follow these typography and formatting rules:

#### A. Prohibition of Raw LaTeX Markup
- **Never Output Raw LaTeX Delimiters**: Do **NOT** use `$...$`, `$$...$$`, `\(...\)`, or `\[...\]` in HTML text, explanations, Canvas text, or quiz option strings.
- **Never Output Raw LaTeX Commands**: Do **NOT** leave unparsed commands such as `\frac{a}{b}`, `\cdot`, `\times`, `\leq`, `\geq`, `\pm`, `\sqrt{x}`, `\Delta`, or `\to`. In a browser without a LaTeX engine, these display as raw, unreadable code (e.g., `Quadratic ($ax^2+bx+c$)` instead of `Quadratic (ax² + bx + c)`).

#### B. Standardized Native Unicode & HTML Substitution Matrix
Always use clean, native HTML tags (`<sup>`, `<sub>`, `<code>`) and standard Unicode mathematical glyphs:

| Mathematical Concept | Do NOT Use (LaTeX/Raw) | MUST Use (Native Unicode / HTML) | HTML Entity / Code Example |
| :--- | :--- | :--- | :--- |
| **Exponents / Powers** | `$x^2$`, `$a^n$`, `$b^x$` | `x²`, `x³`, `x⁴`, `bˣ`, `aⁿ` or `x<sup>n</sup>` | `&sup2;`, `&sup3;`, `ax² + bx + c` |
| **Subscripts / Indices** | `$x_1$`, `$y_2$`, `$a_n$` | `x₁`, `y₂`, `aₙ` or `x<sub>1</sub>` | `(x₁, y₁)`, `(x₂, y₂)` |
| **Multiplication** | `$a \cdot b$`, `$3 \times 4$`, `3*4` | `a · b` (middle dot) or `3 × 4` | `&middot;`, `&times;` |
| **Division / Fractions** | `$\frac{\Delta y}{\Delta x}$`, `$\frac{a}{b}$` | `Δy / Δx`, `a / b`, or `a ÷ b` | `&Delta;y / &Delta;x` or semantic fraction |
| **Rate of Change / Delta** | `$\Delta$`, `\Delta` | `Δ` (capital Greek Delta) | `&Delta;`, `Δy = y₂ - y₁` |
| **Inequalities** | `$\leq$`, `$\geq$`, `$\neq$`, `$\approx$` | `≤`, `≥`, `≠`, `≈` | `&le;`, `&ge;`, `&ne;`, `&asymp;` |
| **Plus-Minus** | `$\pm$` | `±` | `&plusmn;`, `±3` |
| **Coordinates & Mappings** | `$(x,y) \to (kx,ky)$` | `(x, y) → (kx, ky)` | `&rarr;`, `(x, y) → (kx, ky)` |
| **Square Roots & Radicals** | `$\sqrt{x}$`, `$\sqrt{b^2 - 4ac}$` | `√x`, `√(b² - 4ac)` | `&radic;`, `√(x² + y²)` |
| **Set Theory & Infinity** | `$\infty$`, `$\in$`, `$\cup$`, `$\cap$` | `∞`, `∈`, `∉`, `∪`, `∩`, `ℝ` | `&infin;`, `(-∞, ∞)` |
| **Geometry** | `$\angle ABC$`, `$\Delta$`, `$\perp$`, `$\parallel$` | `∠ABC`, `△ABC`, `⊥`, `∥`, `°` | `∠A = ∠D`, `△ABC ~ △DEF` |
| **Constants & Symbols** | `$\pi$`, `$\theta$` | `π`, `θ` | `&pi;`, `&theta;`, `2πr` |
| **Chemistry & Physical Units** | `$H_2O$`, `$CO_2$`, `$\Omega$` | `H₂O`, `CO₂`, `O₂`, `Ω`, `g/cm³` | `H<sub>2</sub>O`, `&Omega;`, `g/cm³` |

#### C. Visual Styling & Semantic Tagging
- **Semantic Code Wrapping**: Wrap equations, function definitions, and coordinate transformations in `<code>` tags or `<span class="mono">...</span>` styled with a readable monospaced font (e.g., `font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;`).
- **Consistent Operator Spacing**: Always include spaces around binary operators (`+`, `-`, `=`, `·`, `×`, `<`, `>`) for visual clarity (e.g., `y = 2x + 5`, not `y=2x+5`).
- **Semantic Fractions in Rich Cards**: When an equation benefits from vertical display, use clean CSS-based fraction elements rather than raw LaTeX:
  ```html
  <span class="inline-fraction">
    <span class="numerator">Δy</span>
    <span class="fraction-line">/</span>
    <span class="denominator">Δx</span>
  </span>
  ```

#### D. Dynamic Canvas & SVG Graphics Typography
- When rendering labels, coordinate axes, slope triangles, or telemetry directly into an HTML5 Canvas (`ctx.fillText`) or SVG `<text>`, use the native Unicode strings directly:
  ```javascript
  ctx.font = '12px "JetBrains Mono", monospace';
  ctx.fillText('f(x) = a · bˣ', 20, 40);
  ctx.fillText('Rate of Change: Δy/Δx = ' + rate.toFixed(2), 20, 60);
  ```

#### E. Quiz Assessment String Hygiene
- In quiz data arrays (`questions = [...]`), every `question`, `options` array, `hint`, and `explanation` MUST be formatted exclusively using native Unicode/HTML. Never allow raw LaTeX to pass through dynamically generated quiz templates.

---

### 3. Synchronized 2D & 3D Interactive Simulation Lab

- **Core Dynamic Visualizer**: Identify the primary spatial, structural, or dynamic mechanism of the topic and build an interactive simulation workspace.
- **Technical Rendering Standards**:
  - **2D Visuals**: High-DPI (`devicePixelRatio`) HTML5 Canvas with `requestAnimationFrame` or interactive inline SVG for coordinate planes, geometric transformations, fraction models, force vectors, density columns, circuit boards, and continuous graphs.
  - **3D Visuals**: Pure CSS 3D (`transform-style: preserve-3d; perspective: 900px;`) with pointer/touch drag handlers updating `--rotateX` and `--rotateY`, or HTML5 Canvas/WebGL 3D projection routines for polyhedra, planetary orbits, molecular structures, and spatial models.
- **Visual-Text Synchronization & Live Telemetry**: Pair interactive controls (range sliders, toggles, preset scenario buttons) with real-time HUD telemetry gauges and dynamic formula readouts that highlight and update instantaneously as the student manipulates variables.

---

### 4. Seamless Adaptive Dark/Light Mode & Contrast Continuity

The interface MUST provide a high-contrast, beautiful, and completely readable presentation across both Dark and Light screen modes, ensuring seamless transition with zero unreadable text or washed-out controls:

- **CSS Variable-Driven Architecture**:
  - All colors, surfaces, text, borders, and shadows MUST be defined using semantic CSS custom properties on `:root` (dark mode default) and `[data-theme="light"]` (or `.light-mode`):
    ```css
    :root {
      --bg-base: #090d16;
      --bg-surface: #0f172a;
      --bg-card: rgba(30, 41, 59, 0.7);
      --bg-glass: rgba(15, 23, 42, 0.75);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --border-color: rgba(255, 255, 255, 0.1);
      --border-glow: rgba(56, 189, 248, 0.25);
      --accent-gold: #fbbf24;
      --accent-cyan: #22d3ee;
      --accent-emerald: #34d399;
      --canvas-bg: #0b1120;
      --canvas-grid: rgba(255, 255, 255, 0.08);
      --canvas-text: #cbd5e1;
    }

    [data-theme="light"], .light-mode {
      --bg-base: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.9);
      --bg-glass: rgba(248, 250, 252, 0.85);
      --text-primary: #0f172a;
      --text-secondary: #334155;
      --text-muted: #64748b;
      --border-color: rgba(0, 0, 0, 0.1);
      --border-glow: rgba(2, 132, 199, 0.25);
      --accent-gold: #d97706;
      --accent-cyan: #0284c7;
      --accent-emerald: #059669;
      --canvas-bg: #f1f5f9;
      --canvas-grid: rgba(0, 0, 0, 0.08);
      --canvas-text: #1e293b;
    }
    ```
- **WCAG AAA/AA Contrast Compliance**:
  - Guarantee minimum 4.5:1 (AA) and target 7:1 (AAA) contrast ratios for all body text, headings, formulas, and interactive controls against their background in both modes.
  - Ban hardcoded inline text colors (e.g. `style="color: white"` or `style="color: #000"`) that become illegible when the theme flips. Always use semantic CSS classes or variables (`var(--text-primary)`, `var(--text-secondary)`).
- **Synchronized Canvas & SVG Objects Color Adaptability**:
  - HTML5 Canvas drawing routines and SVG visualizers MUST adapt dynamically when the mode changes:
    - Listen to theme change events or re-read active CSS variable colors (`getComputedStyle(document.documentElement).getPropertyValue('--canvas-grid')`).
    - Ensure coordinate axes, tick lines, labels, vectors, particle trails, and measurement markers remain crisp, distinct, and high-contrast in both dark and light modes.
    - Automatically trigger a canvas re-render cycle upon theme toggle.

---

### 5. Zero Native Browser Popups & Modern In-App Messaging Standard

To preserve student immersion, prevent UI freezing, and uphold a premium educational experience, native browser dialog windows are strictly prohibited:

- **Strict Prohibition of Native Browser Windows**:
  - **NEVER** use `window.alert()`, `window.confirm()`, or `window.prompt()`.
  - Native browser popups freeze the JavaScript thread, stop animation frames, crash full-screen/kiosk mode, and look unstyled and abrasive against custom designs.
- **Custom In-App Floating Toast Notifications**:
  - All informative feedback, hypothesis simulation triggers, copy confirmations, formula verification results, and telemetry notices MUST use an in-app glassmorphic floating toast (`#customToast` or similar).
  - Toast specifications:
    - Positioned smoothly at the top-center or bottom-right with CSS slide/fade animations (`opacity-0 -translate-y-6` to `opacity-100 translate-y-0`).
    - Structured with an icon badge (`💡`, `🔥`, `⚡`, `🧪`, `🏆`), bold title, detailed descriptive message, and an accessible close button (`✕`).
    - Configured with an auto-dismiss timer (typically 4–5.5 seconds) with timer cancellation on manual dismiss.
    - Accompanied by non-intrusive Web Audio API chimes for sensory reinforcement.
- **Custom In-App Confirmation & Input Modals**:
  - All critical actions requiring student confirmation (e.g., *Reset Training Log*, *Clear Scratchpad*, *Restart Quest*, *Submit Early*) MUST use an in-app modal overlay (`#customConfirmModal`).
  - Modal specifications:
    - Backdrop blur (`backdrop-filter: blur(8px); background: rgba(0, 0, 0, 0.6);`).
    - Explicit, styled action buttons (*Cancel* / *Confirm Action*) with keyboard support (`Escape` key dismiss).
    - Fully reactive callbacks without interrupting background simulation loops.

---

### 6. Comprehensive Curriculum Coverage & Gamified Assessment Engine

- **Question Ingestion & Autonomous Expansion**:
  - **When user provides questions/worksheets**: Include 100% of supplied questions without omission or truncation. Autonomously synthesize additional high-value edge-case and challenge questions aligned with adjacent curriculum standards.
  - **When user provides a topic only**: Generate 8 to 12 progressive, grade-calibrated questions (unless a specific count is requested).
- **Interactive Assessment Mechanics**:
  - **1-at-a-Time Presentation**: Dedicated quiz view with progress indicator, supporting both Multiple Choice and Numeric/Expression Input.
  - **HUD Score, Streak & Retry Token Economy**: Track points, active streaks, and a Retry Token system that rewards accuracy and allows constructive second-chance attempts.
  - **Grade-Scaled Countdown Timer**: Adjustable per-question timer calibrated to grade level (45-60s for K-5, 30-45s for 6-8, 20-30s for 9-12) with an accessible Pause/Zen Mode toggle.
  - **4-Step Solution Breakdown**: Present explanations in four clear stages (*Step 1: Understand*, *Step 2: Model*, *Step 3: Solve*, *Step 4: Verify*) paired with a dynamic visual diagram for every question.
  - **Procedural Web Audio API Feedback**: Synthesize pleasant chimes, streak fanfares, and gentle error tones using native `AudioContext` oscillators (zero external MP3/WAV dependencies) with a mute toggle.

---

### 7. Futuristic Next-Gen EdTech Capabilities

- **Interactive Scratchpad & Whiteboard Overlay**: Embed a toggleable transparent HTML5 Canvas drawing layer over the problem workspace (with pen, highlighter, eraser, and clear tools) so students can work out math or annotate diagrams directly on screen via mouse, stylus, or touch.
- **AI Socratic Coach & Progressive Hint Engine**: Instead of giving away the answer on a wrong attempt, provide a 3-stage Socratic Hint Drawer (*Hint 1: Conceptual Nudge*, *Hint 2: Formula/Strategy Setup*, *Hint 3: Guided Walkthrough*) that diagnoses specific distractor misconceptions.
- **Coach's Pit Stop Misconception Deconstruction**: For science and higher-order math apps, provide an interactive diagnostic drawer analyzing cognitive traps (e.g., Size vs. Density Fallacy, Open Switch Fallacy, Confounding Variables, Inverted Rates) with retry token support.
- **Adaptive Mastery & Telemetry Radar**: Track performance by sub-skill tag in `localStorage`, displaying an SVG Mastery Radar or Skill Bar Chart on the end-of-session Review Dashboard alongside a **"Retry Missed Questions"** mode and printable/exportable JSON/CSV progress summary.
- **Voice Read-Aloud & Accessibility Suite**: Integrate native browser `window.speechSynthesis` (Text-to-Speech) buttons for concept cards and questions, paired with a Dark/Light theme toggle and High-Contrast/Dyslexia-friendly typography mode (`Noto Sans` / `system-ui`).
- **Built-In "Download Offline App" Button**: Include a top-nav utility button that packages and downloads the running `index.html` file directly via a `Blob` link.

---

### 8. Mandatory 3-Point Subject-Matter Fact-Checking Protocol (Questions, Answers & Explanations)

Every single learning application MUST undergo a rigorous 3-point fact-checking validation pass across all questions, answers, and explanations prior to and during generation. This protocol is non-negotiable and guarantees mathematical and scientific truth:

#### Point 1: Question Verification & Domain Rigor
- **Physical & Scientific Laws**: Verify that all scenarios adhere strictly to established natural laws (e.g., conservation of mass, energy, momentum; thermodynamic laws; fluid buoyancy $\rho = m/V$; Ohm's law $V = I \cdot R$; Keplerian orbital mechanics; trophic energy loss 10% rule).
- **Mathematical Integrity**: Verify that all equations have mathematically sound solutions, non-zero denominators, valid geometric dimensions (triangle inequality theorem, positive volumes), and realistic numerical constants.
- **Standard Alignment**: Ensure questions accurately align with official grade standards (NGSS, NC SCOS, State Science Olympiad Official Rules) without confusing level-inappropriate definitions or introducing unscientific colloquialisms.
- **Confounding Variables & Fair Tests**: In experimental science questions, guarantee that test setups have strictly controlled variables and only one independent variable.

#### Point 2: Answer Key & Distractor Rigor
- **Unique Correctness**: Mathematically and scientifically prove that the designated correct answer is unambiguously, provably, and uniquely correct under all standard conditions.
- **Distractor Validity & Misconception Diagnosis**: Verify that all 3 incorrect options (distractors) are definitively incorrect, but engineered around authentic, diagnosable student misconceptions (e.g. confusing volume with density, confusing heat with temperature, inverted fraction division, treating correlation as causation).
- **No Ambiguity**: Confirm that no distractor could be construed as technically correct under an alternative standard interpretation.

#### Point 3: Explanations & Socratic Hints Fact-Check
- **True Causal Explanations**: Verify that step-by-step explanations (*Understand*, *Model*, *Solve*, *Verify*) state the exact physical, chemical, or mathematical causality. Never use scientifically flawed shortcuts or oversimplified "rules of thumb" that instill bad habits (e.g., avoid "mass makes things sink"; explicitly teach "average density relative to fluid density determines buoyancy").
- **Coach's Pit Stop Trap Analysis**: Verify that the diagnostic explanation for wrong choices correctly identifies the cognitive trap and proves why it fails with mathematical or empirical proof.
- **Calculation Verification**: Double-calculate all numerical values, intermediate steps, and unit conversions (e.g. grams to kilograms, cm³ to mL, seconds to hours) shown in the explanation.

---

## Critical Second-Level Validation & Post-Generation Audit Block

Perform a rigorous two-stage verification pass before and immediately after generating the application code:

- **Stage 1: Zero-Placeholder & Code Integrity Gate**:
  - Ban all `// TODO`, `/* ... */`, truncated question arrays, or ellipsis omissions. Every DOM selector, state transition, event listener, and SVG/Canvas routine must be complete and executable.
  - Ensure all math strings use clean native Unicode/HTML, preventing any unparsed LaTeX from reaching the client DOM.
  - Verify zero native `alert()`, `confirm()`, or `prompt()` calls exist in the script.
- **Stage 2: Mandatory Post-Generation Audit Block**:
  - Immediately after the `html` code block, output a structured **Second-Level Validation & Fact-Check Report** table verifying:
    1. **3-Point Subject-Matter Fact-Check Table**: An itemized list of all questions verifying Question validity, Answer key proof, and Explanation scientific accuracy.
    2. **Theme & Contrast Verification**: Confirmation that CSS custom variables govern all elements and canvas/SVG visualizers synchronize across Dark and Light modes.
    3. **Math & Science Expression Audit**: Confirmation that all notations use browser-native Unicode/HTML with zero unparsed LaTeX.
    4. **In-App Messaging & Functional Completeness**: Confirmation that all user messages use custom toasts/modals and the app has zero dependencies.

---

## Response Delivery Format

Deliver every response in three structured sections:

1. **Architectural & Pedagogical Blueprint**: Concise executive summary of target grade calibration, creative framing lens, 3-tier scaffolding structure, dark/light theme tokens, and 2D/3D simulation telemetry design.
2. **Complete Standalone Application (`index.html`)**: A single, un-truncated `html` code block ready to save and open in any modern browser.
3. **Critical Second-Level Validation & Fact-Check Report**: An explicit post-generation audit table verifying the 3-point fact-check (Questions, Answers, Explanations), theme adaptability, math formatting compliance, and zero-popup messaging integrity.

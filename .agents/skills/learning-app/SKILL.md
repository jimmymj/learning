---
name: learning-app
description: Build complete, production-grade, standalone single-file HTML/CSS/JS interactive learning applications for school students (K-12) from any academic topic, worksheet, image, PDF, or prompt. Features grade-calibrated multi-perspective framing, 3-tier scaffolding, synchronized 2D/3D simulations (SVG, Canvas, CSS 3D, WebGL), bulletproof browser-native Unicode/HTML math formatting, gamified assessments with token/timer/Web Audio mechanics, interactive whiteboard scratchpad, Socratic hint drawers, adaptive mastery engines, and mandatory post-generation fact-checking and code verification. Use whenever creating educational web apps, interactive visualizers, practice quizzes, classroom simulators, or digital study aids.
---
# Learning App Master Engine

Act as a principal educational software architect, instructional designer, and subject-matter verifier. Transform any academic topic, worksheet, curriculum standard, or prompt into a complete, standalone, single-file HTML/CSS/JS interactive micro-learning application.

## When to Use

- Building interactive web-based educational tools, visualizers, or classroom simulators for K-12 or self-study students.
- Converting worksheets, textbook problems, or exam prep topics into gamified digital practice apps with step-by-step explanations.
- Creating 2D/3D interactive math manipulatives, science labs, or multi-level study aids that run directly in any browser.

---

## Core Architecture & 6-Pillar Design Requirements

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
  - **2D Visuals**: High-DPI (`devicePixelRatio`) HTML5 Canvas with `requestAnimationFrame` or interactive inline SVG for coordinate planes, geometric transformations, fraction models, force vectors, and continuous graphs.
  - **3D Visuals**: Pure CSS 3D (`transform-style: preserve-3d; perspective: 900px;`) with pointer/touch drag handlers updating `--rotateX` and `--rotateY`, or HTML5 Canvas/WebGL 3D projection routines for polyhedra, molecular structures, and spatial models.
- **Visual-Text Synchronization & Live Telemetry**: Pair interactive controls (range sliders, toggles, preset scenario buttons) with real-time HUD telemetry gauges and dynamic formula readouts that highlight and update instantaneously as the student manipulates variables.

---

### 4. Comprehensive Curriculum Coverage & Gamified Assessment Engine

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

### 5. Futuristic Next-Gen EdTech Capabilities

- **Interactive Scratchpad & Whiteboard Overlay**: Embed a toggleable transparent HTML5 Canvas drawing layer over the problem workspace (with pen, highlighter, eraser, and clear tools) so students can work out math or annotate diagrams directly on screen via mouse, stylus, or touch.
- **AI Socratic Coach & Progressive Hint Engine**: Instead of giving away the answer on a wrong attempt, provide a 3-stage Socratic Hint Drawer (*Hint 1: Conceptual Nudge*, *Hint 2: Formula/Strategy Setup*, *Hint 3: Guided Walkthrough*) that diagnoses specific distractor misconceptions.
- **Adaptive Mastery & Telemetry Radar**: Track performance by sub-skill tag in `localStorage`, displaying an SVG Mastery Radar or Skill Bar Chart on the end-of-session Review Dashboard alongside a **"Retry Missed Questions"** mode and printable/exportable JSON/CSV progress summary.
- **Voice Read-Aloud & Accessibility Suite**: Integrate native browser `window.speechSynthesis` (Text-to-Speech) buttons for concept cards and questions, paired with a Dark/Light theme toggle and High-Contrast/Dyslexia-friendly typography mode (`Noto Sans` / `system-ui`).
- **Built-In "Download Offline App" Button**: Include a top-nav utility button that packages and downloads the running `index.html` file directly via a `Blob` link.

---

### 6. Critical Second-Level Validation & Post-Generation Fact-Check Protocol

Perform a rigorous two-stage verification pass before and immediately after generating the application code:

- **Stage 1: Zero-Placeholder & Code Integrity Gate**:
  - Ban all `// TODO`, `/* ... */`, truncated question arrays, or ellipsis omissions. Every DOM selector, state transition, event listener, and SVG/Canvas routine must be complete and executable.
  - Ensure all math strings use clean native Unicode/HTML, preventing any unparsed LaTeX from reaching the client DOM.
- **Stage 2: Mandatory Post-Generation Audit Block**:
  - Immediately after the `html` code block, output a structured **Second-Level Validation & Fact-Check Report** verifying:
    1. **Mathematical & Curriculum Fact-Check**: Independently recalculate every question's correct answer, verify that no distractor is accidentally equivalent to the correct answer, and confirm domain constraints (e.g., $a \neq 0$ in quadratics, non-zero denominators, triangle inequality validity).
    2. **Math Expression Audit**: Confirm all equations and variables follow strict native Unicode/HTML formatting without raw LaTeX syntax.
    3. **Simulation & UI State Audit**: Confirm 2D/3D canvas/SVG responsiveness, timer pause/reset safety, scratchpad toggle behavior, and 100% question completeness.

---

## Response Delivery Format

Deliver every response in three structured sections:

1. **Architectural & Pedagogical Blueprint**: Concise executive summary of target grade calibration, creative framing lens, 3-tier scaffolding structure, and 2D/3D simulation telemetry design.
2. **Complete Standalone Application (`index.html`)**: A single, un-truncated `html` code block ready to save and open in any modern browser.
3. **Critical Second-Level Validation & Fact-Check Report**: An explicit post-generation audit table verifying mathematical accuracy of every question key, math formatting compliance, and functional completeness.

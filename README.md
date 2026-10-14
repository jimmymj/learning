# 🌟 LearningHub | Interactive Educational Lab Suite

An open-source collection of browser-native, interactive educational visualizers, simulators, and mastery challenges designed for Honors STEM students and educators.

Deployed at: **[GitHub Repository](https://github.com/jimmymj/learning)**

---

## 📂 Repository Directory Structure

```text
learning/
├── index.html                                        # Central LearningHub Portal & App Launcher
├── README.md                                         # Project Documentation & Guide
├── .gitignore                                        # Standard repository ignores
├── apps/                                             # Interactive Learning Applications
│   └── math/                                         # Mathematics Subject Area
│       └── 8th_grade_honors_math_visualizer_dilations_similarity_slope.html  # Dilations, Similarity & Slope Lab
└── assets/                                           # Shared Portal Assets
    ├── css/
    │   └── portal.css                                # Glassmorphic Modern Design System
    └── js/
        └── portal.js                                 # Dynamic Canvas Animations & Modal Runner
```

---

## 🚀 Available Learning Apps

### 1. 📐 CMS 8th Honors Math: Dilations, Similarity & Slope Lab
- **Location:** [`apps/math/8th_grade_honors_math_visualizer_dilations_similarity_slope.html`](apps/math/8th_grade_honors_math_visualizer_dilations_similarity_slope.html)
- **Target Audience:** 8th Grade Honors Mathematics / Accelerated Pre-Algebra & Math 1
- **Curriculum Standards:**
  - **NC.8.G.3:** Coordinate transformations and algebraic rules $(x, y) \rightarrow (kx, ky)$ with arbitrary center of dilation $(cx, cy)$.
  - **NC.8.G.4:** Similarity transformation sequences (composition of translations, reflections, rotations, and dilations).
  - **NC.8.EE.6:** Using similar right slope triangles to prove constant rate of change and derive $y = mx + b$.
- **Features:**
  - **Coordinate Dilations Explorer:** Real-time scaling from origin $(0,0)$ or any custom center $(cx, cy)$ with reduction ($k < 1$) and enlargement ($k > 1$) indicators.
  - **Similarity Sequence Laboratory:** Step-by-step animated multi-transformation pipeline demonstrating angle preservation and proportionality.
  - **Slope Triangles Engine:** Visual proof showing that the ratio of vertical change to horizontal change ($\frac{\Delta y}{\Delta x}$) is constant along any two points on a line.
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

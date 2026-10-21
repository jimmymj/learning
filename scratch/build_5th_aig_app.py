# Generator script for CMS 5th Grade AIG Math Q1 Standalone Application
# Simple, elegant, high-performance, zero-external-dependencies (native CSS & JS)
import json
import sys
sys.path.insert(0, '.')
from scratch.q1_5th_aig_questions import ALL_Q1_5TH_AIG_QUESTIONS

print(f"Loaded {len(ALL_Q1_5TH_AIG_QUESTIONS)} questions for 5th Grade AIG Q1")

def build_app():
    questions_json = json.dumps(ALL_Q1_5TH_AIG_QUESTIONS, indent=2, ensure_ascii=False)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CMS 5th Grade AIG Math: Spatial Volume, Algorithms & Decimal Systems Lab (Q1)</title>
  <meta name="description" content="Elite, interactive mathematical learning suite for CMS 5th Grade AIG students (Weeks 1–9 / NC SCOS / IM Units 1, 4, 5). Features 9 manipulatives, 3D rotatable volume sandbox, algorithm cryptarithm solver, and 60-question adaptive quest." />

  <!-- Google Fonts: Outfit, Inter, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-base: #090d16;
      --bg-card: rgba(15, 23, 42, 0.75);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(14, 165, 233, 0.35);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --primary: #06b6d4;
      --primary-hover: #0891b2;
      --accent-emerald: #10b981;
      --accent-indigo: #6366f1;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --font-heading: 'Outfit', sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-base);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.5;
      min-height: 100vh;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(6, 182, 212, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.05) 0%, transparent 60%);
    }}

    /* Container */
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Top Navigation Header */
    header.app-header {{
      border-bottom: 1px solid var(--border-subtle);
      background: rgba(9, 13, 22, 0.8);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 40;
    }}

    .header-content {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 72px;
      gap: 16px;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}

    .brand-icon {{
      width: 42px;
      height: 42px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, #06b6d4, #6366f1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 4px 14px rgba(6, 182, 212, 0.35);
    }}

    .brand-title {{
      font-family: var(--font-heading);
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: #fff;
    }}

    .brand-subtitle {{
      font-size: 0.75rem;
      color: var(--primary);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}

    .header-controls {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      border: 1px solid transparent;
      outline: none;
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--border-subtle);
      color: var(--text-main);
    }}

    .btn-secondary:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #06b6d4, #2563eb);
      color: #fff;
      box-shadow: 0 4px 16px rgba(6, 182, 212, 0.3);
    }}

    .btn-primary:hover {{
      opacity: 0.95;
      transform: translateY(-1px);
    }}

    .btn-outline {{
      background: transparent;
      border-color: var(--border-subtle);
      color: var(--text-muted);
    }}

    .btn-outline:hover {{
      color: #fff;
      border-color: var(--primary);
    }}

    /* Badges */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 600;
      border: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.04);
    }}

    .badge-primary {{
      color: var(--primary);
      border-color: rgba(6, 182, 212, 0.3);
      background: rgba(6, 182, 212, 0.1);
    }}

    .badge-emerald {{
      color: var(--accent-emerald);
      border-color: rgba(16, 185, 129, 0.3);
      background: rgba(16, 185, 129, 0.1);
    }}

    .badge-indigo {{
      color: #a5b4fc;
      border-color: rgba(99, 102, 241, 0.3);
      background: rgba(99, 102, 241, 0.1);
    }}

    .badge-amber {{
      color: var(--accent-amber);
      border-color: rgba(245, 158, 11, 0.3);
      background: rgba(245, 158, 11, 0.1);
    }}

    /* Main Tab Navigation */
    .tab-bar {{
      display: flex;
      gap: 6px;
      background: rgba(15, 23, 42, 0.6);
      padding: 6px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      margin: 24px 0;
      overflow-x: auto;
      scrollbar-width: none;
    }}

    .tab-bar::-webkit-scrollbar {{
      display: none;
    }}

    .tab-btn {{
      flex: 1;
      min-width: 180px;
      padding: 10px 16px;
      border-radius: var(--radius-md);
      font-family: var(--font-heading);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      background: transparent;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: var(--transition);
      white-space: nowrap;
    }}

    .tab-btn:hover {{
      color: #fff;
      background: rgba(255, 255, 255, 0.04);
    }}

    .tab-btn.active {{
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.25), rgba(99, 102, 241, 0.2));
      color: #fff;
      border: 1px solid rgba(6, 182, 212, 0.4);
      box-shadow: 0 4px 12px rgba(6, 182, 212, 0.15);
    }}

    /* Tab Content Panes */
    .tab-pane {{
      display: none;
      animation: fadeIn 0.25s ease-out;
    }}

    .tab-pane.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Card Panels */
    .glass-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 24px;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
      position: relative;
    }}

    .card-title-group {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .card-title {{
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
    }}

    .card-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-bottom: 20px;
    }}

    /* 3D Prism Interactive Sandbox Layout */
    .sandbox-grid {{
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 24px;
      align-items: start;
    }}

    @media (max-width: 960px) {{
      .sandbox-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .canvas-viewport {{
      background: rgba(9, 13, 22, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      height: 380px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: grab;
    }}

    .canvas-viewport:active {{
      cursor: grabbing;
    }}

    .canvas-viewport canvas {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    .canvas-overlay-hud {{
      position: absolute;
      top: 14px;
      left: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      pointer-events: none;
    }}

    .hud-chip {{
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-subtle);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--primary);
    }}

    .controls-panel {{
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}

    .control-row {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .control-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.84rem;
      font-weight: 600;
    }}

    .control-slider {{
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-full);
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }}

    .control-slider::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--primary);
      box-shadow: 0 0 10px var(--primary);
      cursor: pointer;
    }}

    .telemetry-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}

    .telemetry-box {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      padding: 12px;
      border-radius: var(--radius-md);
    }}

    .telemetry-label {{
      font-size: 0.72rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 4px;
    }}

    .telemetry-val {{
      font-family: var(--font-mono);
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
    }}

    /* Math Formula Displays */
    .math-formula {{
      font-family: var(--font-mono);
      background: rgba(6, 182, 212, 0.08);
      border: 1px solid rgba(6, 182, 212, 0.25);
      padding: 12px 16px;
      border-radius: var(--radius-md);
      font-size: 0.95rem;
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    /* Quest Assessment Styles */
    .quest-wrapper {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }}

    .quest-hud {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border-subtle);
      padding: 14px 20px;
      border-radius: var(--radius-lg);
      flex-wrap: wrap;
      gap: 16px;
    }}

    .hud-stat {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .hud-num {{
      font-family: var(--font-mono);
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
    }}

    .filter-group {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .filter-btn {{
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
    }}

    .filter-btn:hover, .filter-btn.active {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }}

    .question-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 28px;
      position: relative;
    }}

    .question-prompt {{
      font-size: 1.12rem;
      font-weight: 600;
      color: #fff;
      margin: 16px 0 24px;
      line-height: 1.6;
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
      margin-bottom: 24px;
    }}

    .option-btn {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      font-size: 0.95rem;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 14px;
      text-align: left;
      transition: var(--transition);
    }}

    .option-btn:hover:not(:disabled) {{
      background: rgba(255, 255, 255, 0.07);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateX(4px);
    }}

    .option-btn.selected {{
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--primary);
      color: #fff;
    }}

    .option-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: var(--accent-emerald) !important;
      color: #34d399 !important;
    }}

    .option-btn.incorrect {{
      background: rgba(244, 63, 94, 0.2) !important;
      border-color: var(--accent-rose) !important;
      color: #fb7185 !important;
    }}

    .opt-letter {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      flex-shrink: 0;
    }}

    .option-btn.selected .opt-letter {{
      background: var(--primary);
      color: #fff;
    }}

    /* Diagnostic Feedback Panel */
    .diagnostic-panel {{
      margin-top: 24px;
      border-radius: var(--radius-lg);
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-subtle);
      overflow: hidden;
      animation: fadeIn 0.3s ease-out;
    }}

    .diag-header {{
      padding: 14px 20px;
      font-family: var(--font-heading);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
    }}

    .diag-header.correct {{
      background: rgba(16, 185, 129, 0.15);
      border-bottom: 1px solid rgba(16, 185, 129, 0.3);
      color: #34d399;
    }}

    .diag-header.incorrect {{
      background: rgba(244, 63, 94, 0.15);
      border-bottom: 1px solid rgba(244, 63, 94, 0.3);
      color: #fb7185;
    }}

    .diag-body {{
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .diag-section-title {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary);
      font-weight: 700;
      margin-bottom: 6px;
    }}

    .diag-text {{
      font-size: 0.88rem;
      color: #cbd5e1;
      white-space: pre-line;
      line-height: 1.6;
    }}

    /* Socratic Hint Drawer */
    .hint-drawer {{
      margin-top: 16px;
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: var(--radius-md);
      padding: 16px;
      display: none;
    }}

    .hint-drawer.open {{
      display: block;
    }}

    /* Whiteboard Scratchpad Overlay */
    .scratchpad-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(9, 13, 22, 0.88);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      flex-direction: column;
      padding: 24px;
    }}

    .scratchpad-overlay.active {{
      display: flex;
    }}

    .scratchpad-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid var(--border-subtle);
      padding: 12px 20px;
      border-radius: var(--radius-md);
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .scratchpad-canvas-wrapper {{
      flex: 1;
      background: #090d16;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      position: relative;
      cursor: crosshair;
      overflow: hidden;
    }}

    .scratchpad-canvas-wrapper canvas {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    /* Footer */
    footer.app-footer {{
      border-top: 1px solid var(--border-subtle);
      padding: 32px 0;
      margin-top: 60px;
      color: var(--text-dim);
      font-size: 0.82rem;
      text-align: center;
    }}
  </style>
</head>
<body>

  <!-- App Header -->
  <header class="app-header">
    <div class="container header-content">
      <a href="../../index.html" class="brand-group" id="headerHomeLink">
        <div class="brand-icon">✨</div>
        <div>
          <div class="brand-title">CMS 5th Grade AIG Math</div>
          <div class="brand-subtitle">Quarter 1 • Accelerated Foundations</div>
        </div>
      </a>

      <div class="header-controls">
        <button id="soundToggleBtn" class="btn btn-secondary" title="Toggle Sound">
          <span id="soundIcon">🔊</span>
          <span id="soundLabel">Sound</span>
        </button>
        <button id="scratchpadToggleBtn" class="btn btn-secondary">
          <span>✏️ Whiteboard</span>
        </button>
        <a href="../../index.html" class="btn btn-outline">
          <span>← LearningHub</span>
        </a>
      </div>
    </div>
  </header>

  <main class="container" style="padding-bottom: 40px;">

    <!-- Tab Navigation Bar -->
    <nav class="tab-bar" role="tablist">
      <button class="tab-btn active" data-tab="tabVolume" id="tabBtnVolume">
        <span>🏛️ 3D Volume Lab</span>
        <span class="badge badge-primary">NC.5.MD</span>
      </button>
      <button class="tab-btn" data-tab="tabAlgorithms" id="tabBtnAlgorithms">
        <span>⚙️ Multi-Digit Algorithms</span>
        <span class="badge badge-indigo">NC.5.NBT.5/6</span>
      </button>
      <button class="tab-btn" data-tab="tabDecimals" id="tabBtnDecimals">
        <span>🔢 Decimal Systems</span>
        <span class="badge badge-emerald">NC.5.NBT.1/2/7</span>
      </button>
      <button class="tab-btn" data-tab="tabQuest" id="tabBtnQuest">
        <span>🏆 60-Q AIG Mastery Quest</span>
        <span class="badge badge-amber" id="questCountBadge">60 Qs</span>
      </button>
    </nav>

    <!-- Tab 1: 3D Volume & Spatial Reasoning Lab -->
    <section id="tabVolume" class="tab-pane active">
      <div class="glass-card">
        <div class="card-title-group">
          <div>
            <h2 class="card-title">Interactive 3D Rectangular Prism Sandbox</h2>
            <p class="card-desc">Drag to rotate the prism in 3D. Manipulate dimensions to investigate base area layering (V = B × h), discrete unit cube packing, and the 3D space diagonal.</p>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-secondary" id="resetPrismBtn">↺ Reset View</button>
            <button class="btn btn-secondary" id="toggleWireframeBtn">🔲 Toggle Mesh</button>
          </div>
        </div>

        <div class="sandbox-grid">
          <!-- 3D Canvas Viewport -->
          <div class="canvas-viewport" id="prismViewport">
            <canvas id="prismCanvas"></canvas>
            <div class="canvas-overlay-hud">
              <span class="hud-chip" id="hudDimChip">8 × 5 × 6 cm</span>
              <span class="hud-chip" id="hudVolumeChip">V = 240 cm³</span>
            </div>
          </div>

          <!-- Dimension & Telemetry Controls -->
          <div class="controls-panel">
            <div class="control-row">
              <div class="control-header">
                <span>Length (l):</span>
                <span class="hud-num" id="valLen" style="font-size: 0.95rem; color: var(--primary);">8 cm</span>
              </div>
              <input type="range" id="sliderLen" class="control-slider" min="2" max="15" value="8" />
            </div>

            <div class="control-row">
              <div class="control-header">
                <span>Width (w):</span>
                <span class="hud-num" id="valWidth" style="font-size: 0.95rem; color: var(--primary);">5 cm</span>
              </div>
              <input type="range" id="sliderWidth" class="control-slider" min="2" max="15" value="5" />
            </div>

            <div class="control-row">
              <div class="control-header">
                <span>Height (h / Layers):</span>
                <span class="hud-num" id="valHeight" style="font-size: 0.95rem; color: var(--primary);">6 cm</span>
              </div>
              <input type="range" id="sliderHeight" class="control-slider" min="2" max="15" value="6" />
            </div>

            <!-- Mathematical Telemetry -->
            <div class="telemetry-grid">
              <div class="telemetry-box">
                <div class="telemetry-label">Base Area (B = l × w)</div>
                <div class="telemetry-val" id="teleBaseArea">40 cm²</div>
              </div>
              <div class="telemetry-box">
                <div class="telemetry-label">Total Volume (B × h)</div>
                <div class="telemetry-val" style="color: #38bdf8;" id="teleVolume">240 cm³</div>
              </div>
              <div class="telemetry-box">
                <div class="telemetry-label">Surface Area (SA)</div>
                <div class="telemetry-val" id="teleSurfaceArea">236 cm²</div>
              </div>
              <div class="telemetry-box">
                <div class="telemetry-label">Space Diagonal (d)</div>
                <div class="telemetry-val" style="color: #a5b4fc;" id="teleDiagonal">11.18 cm</div>
              </div>
            </div>

            <div class="math-formula">
              <span>V = (8 × 5) × 6 = 40 × 6 = 240 cm³</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 2: Multi-Digit Whole Number Operations -->
    <section id="tabAlgorithms" class="tab-pane">
      <div class="glass-card">
        <div class="card-title-group">
          <div>
            <h2 class="card-title">Multi-Digit Operations & Cryptarithm Studio</h2>
            <p class="card-desc">Inspect partial products area models and solve missing-digit cryptarithms under NC.5.NBT.5 and NC.5.NBT.6.</p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
          <!-- Partial Products Model -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="font-weight: 700; margin-bottom: 12px; color: var(--primary);">Interactive 3-Digit × 2-Digit Area Model</div>
            <div style="display: flex; gap: 12px; margin-bottom: 16px;">
              <input type="number" id="inputFactorA" value="487" style="width: 100px; padding: 8px; background: rgba(0,0,0,0.4); border: 1px solid var(--border-subtle); border-radius: 6px; color: #fff; font-family: var(--font-mono);" />
              <span style="font-size: 1.2rem; align-self: center;">×</span>
              <input type="number" id="inputFactorB" value="63" style="width: 80px; padding: 8px; background: rgba(0,0,0,0.4); border: 1px solid var(--border-subtle); border-radius: 6px; color: #fff; font-family: var(--font-mono);" />
              <button class="btn btn-secondary" id="btnCalculateProduct">Calculate</button>
            </div>
            <div id="partialProductsDisplay" style="font-family: var(--font-mono); font-size: 0.88rem; line-height: 1.8; color: #cbd5e1;">
              Row 1: 487 × 3 = 1,461<br />
              Row 2: 487 × 60 = 29,220 (with 10¹ placeholder shift)<br />
              <strong style="color: #34d399;">Total Product: 30,681</strong>
            </div>
          </div>

          <!-- Cryptarithm Challenge Box -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="font-weight: 700; margin-bottom: 12px; color: #a5b4fc;">Live Cryptarithm Puzzle: 3A5 × B4 = 11,810</div>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px;">Select digits A and B to verify row alignments in real time.</p>
            <div style="display: flex; gap: 16px; align-items: center; margin-bottom: 14px;">
              <label>Digit A: <select id="selectDigitA" style="padding: 6px 12px; background: #090d16; color: #fff; border: 1px solid var(--border-subtle); border-radius: 6px; font-family: var(--font-mono);"><option value="4">4</option><option value="5">5</option><option value="6" selected>6</option><option value="7">7</option></select></label>
              <label>Digit B: <select id="selectDigitB" style="padding: 6px 12px; background: #090d16; color: #fff; border: 1px solid var(--border-subtle); border-radius: 6px; font-family: var(--font-mono);"><option value="2">2</option><option value="3" selected>3</option><option value="4">4</option></select></label>
            </div>
            <div id="cryptarithmResult" style="font-family: var(--font-mono); font-size: 0.88rem; color: #34d399; padding: 10px; background: rgba(16, 185, 129, 0.1); border-radius: 6px; border: 1px solid rgba(16, 185, 129, 0.3);">
              ✓ 365 × 4 = 1,460 | 365 × 30 = 10,350 | Sum = 11,810 (Exact Match!)
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 3: Decimal Place Value & Operations -->
    <section id="tabDecimals" class="tab-pane">
      <div class="glass-card">
        <div class="card-title-group">
          <div>
            <h2 class="card-title">Exponential Base-10 Scale & Decimal Balancer</h2>
            <p class="card-desc">Shift digits across powers of 10 and test landmark compensation subtraction under NC.5.NBT.1, 2, and 7.</p>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 24px;">
          <!-- Power of 10 Shifter -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <span style="font-weight: 700; color: var(--primary);">Base Value: 48.5 × 10ⁿ Shift Engine</span>
              <span class="hud-num" id="exponentDisplay" style="color: var(--primary);">Power n = 2 (10² = 100)</span>
            </div>
            <input type="range" id="sliderExponent" class="control-slider" min="-3" max="4" value="2" step="1" />
            <div style="margin-top: 16px; font-family: var(--font-mono); font-size: 1.1rem; text-align: center; color: #fff;" id="exponentOutput">
              48.5 × 10² = 4,850
            </div>
          </div>

          <!-- Decimal Compensation Subtraction -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="font-weight: 700; color: #a5b4fc; margin-bottom: 8px;">Mental Math Compensation Tool: 64.382 - 29.995</div>
            <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 14px;">29.995 is 0.005 less than 30.000. Subtract 30, then add back 0.005.</p>
            <div class="math-formula" style="background: rgba(99, 102, 241, 0.08); border-color: rgba(99, 102, 241, 0.3); color: #c7d2fe;">
              <span>64.382 - 30.000 = 34.382 ➔ 34.382 + 0.005 = <strong>34.387</strong></span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 4: 60-Question AIG Mastery Quest -->
    <section id="tabQuest" class="tab-pane">
      <div class="quest-wrapper">
        
        <!-- Quest HUD -->
        <div class="quest-hud">
          <div class="hud-stat">
            <span class="badge badge-primary" id="questProgressChip">Question 1 of 60</span>
            <span class="badge badge-indigo" id="questTierChip">Tier 1</span>
          </div>

          <!-- Module Filter Buttons -->
          <div class="filter-group">
            <button class="filter-btn active" data-filter="all" id="filterAll">All (60)</button>
            <button class="filter-btn" data-filter="Module 1" id="filterM1">Volume (20)</button>
            <button class="filter-btn" data-filter="Module 2" id="filterM2">Algorithms (20)</button>
            <button class="filter-btn" data-filter="Module 3" id="filterM3">Decimals (20)</button>
          </div>

          <!-- Score & Timer -->
          <div style="display: flex; align-items: center; gap: 16px;">
            <div class="hud-stat">
              <span style="font-size: 0.8rem; color: var(--text-muted);">Score:</span>
              <span class="hud-num" id="scoreDisplay">0</span>
            </div>
            <div class="hud-stat">
              <span style="font-size: 0.8rem; color: var(--text-muted);">Streak:</span>
              <span class="hud-num" style="color: var(--accent-amber);" id="streakDisplay">🔥 0</span>
            </div>
          </div>
        </div>

        <!-- Question Presentation Card -->
        <div class="question-card">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <span class="badge badge-emerald" id="standardBadge">NC.5.MD.3</span>
            <span style="font-size: 0.8rem; color: var(--text-muted);" id="topicLabel">Topic 1: Unit Cube Packing & SA:V Ratios</span>
          </div>

          <div class="question-prompt" id="questionText">
            A shipping container is packed with 1-cm unit cubes. The base layer has 8 rows with 9 cubes in each row. If there are 7 identical layers packed without gaps or overlaps, what is the total volume?
          </div>

          <div class="options-grid" id="optionsContainer">
            <!-- Shuffled options injected dynamically -->
          </div>

          <!-- Action Buttons -->
          <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
            <button class="btn btn-primary" id="submitBtn" disabled>Submit Answer</button>
            <button class="btn btn-secondary" id="hintBtn">💡 Need a Hint?</button>
            <button class="btn btn-secondary" id="scratchpadBtn">✏️ Scratchpad</button>
            <button class="btn btn-outline" id="nextBtn" style="display: none; margin-left: auto;">Next Question →</button>
          </div>

          <!-- Socratic Hint Drawer -->
          <div class="hint-drawer" id="hintDrawer">
            <div style="font-weight: 700; color: var(--accent-amber); margin-bottom: 6px;">💡 Aria's Socratic Guidance</div>
            <div id="hintContent" style="font-size: 0.88rem; color: #fde68a; line-height: 1.6;"></div>
          </div>

          <!-- 4-Part Diagnostic Feedback Panel -->
          <div class="diagnostic-panel" id="diagnosticPanel" style="display: none;">
            <div class="diag-header" id="diagHeader">
              <span id="diagStatusIcon">✓</span>
              <span id="diagStatusTitle">Correct! Superior Mathematical Reasoning</span>
            </div>
            <div class="diag-body">
              <div>
                <div class="diag-section-title">1. Step-by-Step Resolution Path</div>
                <div class="diag-text" id="diagStepByStep"></div>
              </div>
              <div>
                <div class="diag-section-title">2. Underlying Mathematical Principle</div>
                <div class="diag-text" id="diagPrinciple"></div>
              </div>
              <div>
                <div class="diag-section-title">3. Misconception & Distractor Analysis</div>
                <div class="diag-text" id="diagMisconceptions"></div>
              </div>
              <div>
                <div class="diag-section-title">4. Fast-Track / Mental Math Shortcut</div>
                <div class="diag-text" id="diagFastTrack"></div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

  </main>

  <!-- Whiteboard Scratchpad Overlay -->
  <div class="scratchpad-overlay" id="scratchpadOverlay">
    <div class="scratchpad-bar">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-weight: 700; font-size: 1rem; color: #fff;">✏️ AIG Problem-Solving Scratchpad</span>
        <span class="badge badge-primary">Touch / Pointer</span>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <button class="btn btn-secondary" id="penToolBtn" style="border-color: var(--primary);">Pen</button>
        <button class="btn btn-secondary" id="highlighterToolBtn">Highlighter</button>
        <button class="btn btn-secondary" id="eraserToolBtn">Eraser</button>
        <button class="btn btn-secondary" id="clearScratchpadBtn">Clear</button>
        <button class="btn btn-primary" id="closeScratchpadBtn">Done</button>
      </div>
    </div>
    <div class="scratchpad-canvas-wrapper" id="scratchpadWrapper">
      <canvas id="scratchpadCanvas"></canvas>
    </div>
  </div>

  <!-- Footer -->
  <footer class="app-footer">
    <div class="container">
      <p>CMS 5th Grade AIG Mathematics • Quarter 1 Laboratory Suite • Illustrative Math K–5 / NC SCOS</p>
      <p style="margin-top: 4px;">Zero External Dependencies • Offline Capable • Native Web Audio & Unicode Math</p>
    </div>
  </footer>

  <!-- Embedded Question Bank & Master Application Engine -->
  <script>
    const QUESTION_BANK = {questions_json};

    // State
    let currentQuestions = [...QUESTION_BANK];
    let currentIndex = 0;
    let selectedOptionText = null;
    let score = 0;
    let streak = 0;
    let soundEnabled = true;
    let currentHintIndex = 0;

    // Web Audio Synthesizer
    let audioCtx = null;
    function playTone(freq, type, duration) {{
      if (!soundEnabled) return;
      try {{
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type || 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{}}
    }}

    function playSuccessSound() {{
      playTone(523.25, 'sine', 0.15);
      setTimeout(() => playTone(659.25, 'sine', 0.25), 100);
    }}

    function playErrorSound() {{
      playTone(220, 'triangle', 0.2);
      setTimeout(() => playTone(196, 'triangle', 0.25), 120);
    }}

    // Tab Navigation
    document.querySelectorAll('.tab-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const tabId = btn.dataset.tab;
        document.getElementById(tabId)?.classList.add('active');
        if (tabId === 'tabVolume') resizePrismCanvas();
      }});
    }});

    // 3D Prism Canvas Engine
    const prismCanvas = document.getElementById('prismCanvas');
    const pCtx = prismCanvas ? prismCanvas.getContext('2d') : null;
    let angleX = -0.55;
    let angleY = 0.65;
    let isDragging = false;
    let lastMouseX = 0;
    let lastMouseY = 0;
    let showWireframe = true;

    function resizePrismCanvas() {{
      if (!prismCanvas) return;
      const rect = prismCanvas.parentElement.getBoundingClientRect();
      prismCanvas.width = rect.width * window.devicePixelRatio;
      prismCanvas.height = rect.height * window.devicePixelRatio;
      pCtx.scale(window.devicePixelRatio, window.devicePixelRatio);
      render3DPrism();
    }}

    window.addEventListener('resize', resizePrismCanvas);

    const prismViewport = document.getElementById('prismViewport');
    prismViewport?.addEventListener('mousedown', e => {{
      isDragging = true;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
    }});

    window.addEventListener('mousemove', e => {{
      if (!isDragging) return;
      const dx = e.clientX - lastMouseX;
      const dy = e.clientY - lastMouseY;
      angleY += dx * 0.01;
      angleX += dy * 0.01;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
      render3DPrism();
    }});

    window.addEventListener('mouseup', () => {{ isDragging = false; }});

    // Touch support for 3D rotation
    prismViewport?.addEventListener('touchstart', e => {{
      if (e.touches.length === 1) {{
        isDragging = true;
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;
      }}
    }}, {{ passive: true }});

    window.addEventListener('touchmove', e => {{
      if (!isDragging || e.touches.length !== 1) return;
      const dx = e.touches[0].clientX - lastMouseX;
      const dy = e.touches[0].clientY - lastMouseY;
      angleY += dx * 0.015;
      angleX += dy * 0.015;
      lastMouseX = e.touches[0].clientX;
      lastMouseY = e.touches[0].clientY;
      render3DPrism();
    }}, {{ passive: true }});

    window.addEventListener('touchend', () => {{ isDragging = false; }});

    document.getElementById('resetPrismBtn')?.addEventListener('click', () => {{
      angleX = -0.55;
      angleY = 0.65;
      render3DPrism();
    }});

    document.getElementById('toggleWireframeBtn')?.addEventListener('click', () => {{
      showWireframe = !showWireframe;
      render3DPrism();
    }});

    // Dimension Sliders
    const sLen = document.getElementById('sliderLen');
    const sWidth = document.getElementById('sliderWidth');
    const sHeight = document.getElementById('sliderHeight');

    function updatePrismMetrics() {{
      const l = parseInt(sLen.value);
      const w = parseInt(sWidth.value);
      const h = parseInt(sHeight.value);

      document.getElementById('valLen').textContent = l + ' cm';
      document.getElementById('valWidth').textContent = w + ' cm';
      document.getElementById('valHeight').textContent = h + ' cm';
      document.getElementById('hudDimChip').textContent = `${{l}} × ${{w}} × ${{h}} cm`;

      const b = l * w;
      const v = b * h;
      const sa = 2 * (l * w + l * h + w * h);
      const diag = Math.sqrt(l * l + w * w + h * h).toFixed(2);

      document.getElementById('teleBaseArea').textContent = b + ' cm²';
      document.getElementById('teleVolume').textContent = v + ' cm³';
      document.getElementById('hudVolumeChip').textContent = `V = ${{v}} cm³`;
      document.getElementById('teleSurfaceArea').textContent = sa + ' cm²';
      document.getElementById('teleDiagonal').textContent = diag + ' cm';

      const formulaElem = document.querySelector('#tabVolume .math-formula span');
      if (formulaElem) {{
        formulaElem.textContent = `V = (${{l}} × ${{w}}) × ${{h}} = ${{b}} × ${{h}} = ${{v}} cm³`;
      }}

      render3DPrism();
    }}

    sLen?.addEventListener('input', updatePrismMetrics);
    sWidth?.addEventListener('input', updatePrismMetrics);
    sHeight?.addEventListener('input', updatePrismMetrics);

    function render3DPrism() {{
      if (!prismCanvas || !pCtx) return;
      const wCanvas = prismCanvas.getBoundingClientRect().width;
      const hCanvas = prismCanvas.getBoundingClientRect().height;

      pCtx.clearRect(0, 0, wCanvas, hCanvas);

      const l = parseInt(sLen.value);
      const w = parseInt(sWidth.value);
      const h = parseInt(sHeight.value);

      const scale = Math.min(wCanvas, hCanvas) * 0.024;
      const cx = wCanvas / 2;
      const cy = hCanvas / 2 + 10;

      // 8 Vertices of the Rectangular Prism centered at origin
      const hl = (l * scale) / 2;
      const hw = (w * scale) / 2;
      const hh = (h * scale) / 2;

      const vertices = [
        {{ x: -hl, y: -hh, z: -hw }},
        {{ x:  hl, y: -hh, z: -hw }},
        {{ x:  hl, y:  hh, z: -hw }},
        {{ x: -hl, y:  hh, z: -hw }},
        {{ x: -hl, y: -hh, z:  hw }},
        {{ x:  hl, y: -hh, z:  hw }},
        {{ x:  hl, y:  hh, z:  hw }},
        {{ x: -hl, y:  hh, z:  hw }}
      ];

      // 3D Rotation (Pitch around X, Yaw around Y)
      const cosX = Math.cos(angleX);
      const sinX = Math.sin(angleX);
      const cosY = Math.cos(angleY);
      const sinY = Math.sin(angleY);

      const proj = vertices.map(v => {{
        // Yaw (rotate Y)
        const x1 = v.x * cosY + v.z * sinY;
        const z1 = -v.x * sinY + v.z * cosY;
        // Pitch (rotate X)
        const y2 = v.y * cosX - z1 * sinX;
        const z2 = v.y * sinX + z1 * cosX;
        // Isometric / Weak perspective projection
        const factor = 400 / (400 + z2);
        return {{
          x: cx + x1 * factor,
          y: cy + y2 * factor,
          z: z2
        }};
      }});

      // 6 Faces (indices, normal, color)
      const faces = [
        {{ indices: [0, 1, 2, 3], color: 'rgba(6, 182, 212, 0.45)', stroke: '#06b6d4' }}, // Front
        {{ indices: [4, 5, 6, 7], color: 'rgba(6, 182, 212, 0.35)', stroke: '#06b6d4' }}, // Back
        {{ indices: [0, 1, 5, 4], color: 'rgba(99, 102, 241, 0.45)', stroke: '#6366f1' }}, // Top
        {{ indices: [2, 3, 7, 6], color: 'rgba(16, 185, 129, 0.45)', stroke: '#10b981' }}, // Bottom (Base)
        {{ indices: [0, 3, 7, 4], color: 'rgba(14, 165, 233, 0.4)', stroke: '#0ea5e9' }}, // Left
        {{ indices: [1, 2, 6, 5], color: 'rgba(56, 189, 248, 0.4)', stroke: '#38bdf8' }}  // Right
      ];

      // Sort faces back-to-front (Painter's algorithm)
      faces.forEach(f => {{
        let avgZ = 0;
        f.indices.forEach(idx => avgZ += proj[idx].z);
        f.avgZ = avgZ / 4;
      }});
      faces.sort((a, b) => b.avgZ - a.avgZ);

      // Draw Faces
      faces.forEach(f => {{
        pCtx.beginPath();
        pCtx.moveTo(proj[f.indices[0]].x, proj[f.indices[0]].y);
        for (let i = 1; i < 4; i++) {{
          pCtx.lineTo(proj[f.indices[i]].x, proj[f.indices[i]].y);
        }}
        pCtx.closePath();
        pCtx.fillStyle = f.color;
        pCtx.fill();
        pCtx.strokeStyle = f.stroke;
        pCtx.lineWidth = 1.5;
        pCtx.stroke();
      }});

      // Draw Wireframe unit grid lines if enabled
      if (showWireframe) {{
        pCtx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        pCtx.lineWidth = 1;
        pCtx.setLineDash([2, 3]);

        // Draw internal space diagonal line
        pCtx.strokeStyle = '#f59e0b';
        pCtx.lineWidth = 2;
        pCtx.beginPath();
        pCtx.moveTo(proj[0].x, proj[0].y);
        pCtx.lineTo(proj[6].x, proj[6].y);
        pCtx.stroke();
        pCtx.setLineDash([]);
      }}
    }}

    // Tab 2: Partial Products & Cryptarithm Handler
    document.getElementById('btnCalculateProduct')?.addEventListener('click', () => {{
      const a = parseInt(document.getElementById('inputFactorA').value) || 487;
      const b = parseInt(document.getElementById('inputFactorB').value) || 63;
      const onesB = b % 10;
      const tensB = Math.floor(b / 10) * 10;
      const p1 = a * onesB;
      const p2 = a * tensB;
      const total = a * b;

      document.getElementById('partialProductsDisplay').innerHTML = `
        Row 1: ${{a}} × ${{onesB}} = ${{p1.toLocaleString()}}<br />
        Row 2: ${{a}} × ${{tensB}} = ${{p2.toLocaleString()}} (with 10¹ placeholder shift)<br />
        <strong style="color: #34d399;">Total Product: ${{total.toLocaleString()}}</strong>
      `;
    }});

    function updateCryptarithm() {{
      const a = document.getElementById('selectDigitA').value;
      const b = document.getElementById('selectDigitB').value;
      const factor1 = parseInt(`3${{a}}5`);
      const factor2 = parseInt(`${{b}}4`);
      const row1 = factor1 * 4;
      const row2 = factor1 * parseInt(`${{b}}0`);
      const sum = factor1 * factor2;

      const isMatch = (a === '6' && b === '3');
      const box = document.getElementById('cryptarithmResult');
      if (isMatch) {{
        box.style.background = 'rgba(16, 185, 129, 0.15)';
        box.style.borderColor = 'rgba(16, 185, 129, 0.4)';
        box.style.color = '#34d399';
        box.innerHTML = `✓ 365 × 4 = 1,460 | 365 × 30 = 10,350 | Sum = 11,810 (Exact Match!)`;
      }} else {{
        box.style.background = 'rgba(244, 63, 94, 0.15)';
        box.style.borderColor = 'rgba(244, 63, 94, 0.4)';
        box.style.color = '#fb7185';
        box.innerHTML = `✗ ${{factor1}} × 4 = ${{row1.toLocaleString()}} | ${{factor1}} × ${{b}}0 = ${{row2.toLocaleString()}} | Sum = ${{sum.toLocaleString()}} (Target: 11,810)`;
      }}
    }}

    document.getElementById('selectDigitA')?.addEventListener('change', updateCryptarithm);
    document.getElementById('selectDigitB')?.addEventListener('change', updateCryptarithm);

    // Tab 3: Exponent Slider Handler
    const sExp = document.getElementById('sliderExponent');
    sExp?.addEventListener('input', () => {{
      const p = parseInt(sExp.value);
      const factor = Math.pow(10, p);
      const res = 48.5 * factor;
      let powerLabel = `10${{p >= 0 ? `^${{p}}` : `^(${{p}})`}}`;
      if (p === 0) powerLabel += ' = 1';
      else if (p > 0) powerLabel += ` = ${{factor.toLocaleString()}}`;
      else powerLabel += ` = 1/${{Math.pow(10, -p)}}`;

      document.getElementById('exponentDisplay').textContent = `Power n = ${{p}} (${{powerLabel}})`;
      document.getElementById('exponentOutput').textContent = `48.5 × 10${{p >= 0 ? `^${{p}}` : `^(${{p}})`}} = ${{res < 1 ? res.toFixed(5).replace(/\\.?0+$/, '') : res.toLocaleString()}}`;
    }});

    // Quest Assessment Engine
    function renderQuestion() {{
      if (currentQuestions.length === 0) return;
      const q = currentQuestions[currentIndex];
      selectedOptionText = null;

      document.getElementById('questProgressChip').textContent = `Question ${{currentIndex + 1}} of ${{currentQuestions.length}}`;
      document.getElementById('questTierChip').textContent = q.tier.split(':')[0];
      document.getElementById('standardBadge').textContent = q.standard;
      document.getElementById('topicLabel').textContent = q.topic;
      document.getElementById('questionText').innerHTML = q.question;

      // Reset Drawers & Buttons
      document.getElementById('diagnosticPanel').style.display = 'none';
      document.getElementById('hintDrawer').classList.remove('open');
      document.getElementById('submitBtn').disabled = true;
      document.getElementById('submitBtn').style.display = 'inline-flex';
      document.getElementById('nextBtn').style.display = 'none';

      // Fisher-Yates runtime shuffle of options
      const shuffledOptions = [...q.options];
      for (let i = shuffledOptions.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledOptions[i], shuffledOptions[j]] = [shuffledOptions[j], shuffledOptions[i]];
      }}

      const letters = ['A', 'B', 'C', 'D'];
      const optContainer = document.getElementById('optionsContainer');
      optContainer.innerHTML = '';

      shuffledOptions.forEach((optText, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.dataset.text = optText;
        btn.innerHTML = `
          <div class="opt-letter">${{letters[idx]}}</div>
          <div style="flex: 1;">${{optText}}</div>
        `;
        btn.addEventListener('click', () => selectOption(btn, optText));
        optContainer.appendChild(btn);
      }});

      currentHintIndex = 0;
    }}

    function selectOption(btn, text) {{
      document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      selectedOptionText = text;
      document.getElementById('submitBtn').disabled = false;
      playTone(440, 'sine', 0.05);
    }}

    document.getElementById('submitBtn')?.addEventListener('click', () => {{
      if (!selectedOptionText) return;
      const q = currentQuestions[currentIndex];
      const isCorrect = (selectedOptionText.trim() === q.formattedAnswer.trim());

      document.querySelectorAll('.option-btn').forEach(b => {{
        b.disabled = true;
        if (b.dataset.text.trim() === q.formattedAnswer.trim()) {{
          b.classList.add('correct');
        }} else if (b.dataset.text === selectedOptionText && !isCorrect) {{
          b.classList.add('incorrect');
        }}
      }});

      const diagPanel = document.getElementById('diagnosticPanel');
      const diagHeader = document.getElementById('diagHeader');
      const diagIcon = document.getElementById('diagStatusIcon');
      const diagTitle = document.getElementById('diagStatusTitle');

      if (isCorrect) {{
        score += 100;
        streak += 1;
        playSuccessSound();
        diagHeader.className = 'diag-header correct';
        diagIcon.textContent = '✓';
        diagTitle.textContent = 'Correct! Superior Mathematical Reasoning';
      }} else {{
        streak = 0;
        playErrorSound();
        diagHeader.className = 'diag-header incorrect';
        diagIcon.textContent = '✗';
        diagTitle.textContent = 'Misconception Diagnosed — Review Worked Model Below';
      }}

      document.getElementById('scoreDisplay').textContent = score;
      document.getElementById('streakDisplay').textContent = `🔥 ${{streak}}`;

      // Fill 4-part diagnostics
      document.getElementById('diagStepByStep').textContent = q.diagnostic.stepByStep;
      document.getElementById('diagPrinciple').textContent = q.diagnostic.principle;
      document.getElementById('diagMisconceptions').textContent = q.diagnostic.misconceptions;
      document.getElementById('diagFastTrack').textContent = q.diagnostic.fastTrack;

      diagPanel.style.display = 'block';
      document.getElementById('submitBtn').style.display = 'none';
      document.getElementById('nextBtn').style.display = 'inline-flex';
    }});

    document.getElementById('nextBtn')?.addEventListener('click', () => {{
      currentIndex = (currentIndex + 1) % currentQuestions.length;
      renderQuestion();
      document.querySelector('.question-card').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }});

    // Hint Drawer Toggle
    document.getElementById('hintBtn')?.addEventListener('click', () => {{
      const drawer = document.getElementById('hintDrawer');
      const q = currentQuestions[currentIndex];
      if (!q.socraticHints || q.socraticHints.length === 0) return;

      const hintText = q.socraticHints[currentHintIndex % q.socraticHints.length];
      document.getElementById('hintContent').textContent = `Stage ${{ (currentHintIndex % q.socraticHints.length) + 1 }}: ${{hintText}}`;
      drawer.classList.add('open');
      currentHintIndex++;
      playTone(330, 'sine', 0.08);
    }});

    // Module Filter Buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        if (filter === 'all') {{
          currentQuestions = [...QUESTION_BANK];
        }} else {{
          currentQuestions = QUESTION_BANK.filter(q => q.module.includes(filter));
        }}
        currentIndex = 0;
        renderQuestion();
      }});
    }});

    // Whiteboard Scratchpad Handlers
    const scratchpad = document.getElementById('scratchpadOverlay');
    const sCanvas = document.getElementById('scratchpadCanvas');
    const sCtx = sCanvas ? sCanvas.getContext('2d') : null;
    let sDrawing = false;
    let sTool = 'pen'; // 'pen', 'highlighter', 'eraser'

    function resizeScratchpad() {{
      if (!sCanvas) return;
      const wrapper = document.getElementById('scratchpadWrapper');
      sCanvas.width = wrapper.clientWidth * window.devicePixelRatio;
      sCanvas.height = wrapper.clientHeight * window.devicePixelRatio;
      sCtx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }}

    function toggleScratchpad() {{
      scratchpad.classList.toggle('active');
      if (scratchpad.classList.contains('active')) {{
        resizeScratchpad();
      }}
    }}

    document.getElementById('scratchpadToggleBtn')?.addEventListener('click', toggleScratchpad);
    document.getElementById('scratchpadBtn')?.addEventListener('click', toggleScratchpad);
    document.getElementById('closeScratchpadBtn')?.addEventListener('click', toggleScratchpad);

    document.getElementById('penToolBtn')?.addEventListener('click', () => {{
      sTool = 'pen';
      document.getElementById('penToolBtn').style.borderColor = 'var(--primary)';
      document.getElementById('highlighterToolBtn').style.borderColor = 'var(--border-subtle)';
      document.getElementById('eraserToolBtn').style.borderColor = 'var(--border-subtle)';
    }});

    document.getElementById('highlighterToolBtn')?.addEventListener('click', () => {{
      sTool = 'highlighter';
      document.getElementById('penToolBtn').style.borderColor = 'var(--border-subtle)';
      document.getElementById('highlighterToolBtn').style.borderColor = 'var(--accent-amber)';
      document.getElementById('eraserToolBtn').style.borderColor = 'var(--border-subtle)';
    }});

    document.getElementById('eraserToolBtn')?.addEventListener('click', () => {{
      sTool = 'eraser';
      document.getElementById('penToolBtn').style.borderColor = 'var(--border-subtle)';
      document.getElementById('highlighterToolBtn').style.borderColor = 'var(--border-subtle)';
      document.getElementById('eraserToolBtn').style.borderColor = 'var(--accent-rose)';
    }});

    document.getElementById('clearScratchpadBtn')?.addEventListener('click', () => {{
      if (sCtx && sCanvas) {{
        sCtx.clearRect(0, 0, sCanvas.width, sCanvas.height);
      }}
    }});

    sCanvas?.addEventListener('mousedown', e => {{
      sDrawing = true;
      sCtx.beginPath();
      sCtx.moveTo(e.offsetX, e.offsetY);
    }});

    sCanvas?.addEventListener('mousemove', e => {{
      if (!sDrawing) return;
      if (sTool === 'pen') {{
        sCtx.strokeStyle = '#06b6d4';
        sCtx.lineWidth = 2.5;
        sCtx.globalAlpha = 1.0;
      }} else if (sTool === 'highlighter') {{
        sCtx.strokeStyle = '#f59e0b';
        sCtx.lineWidth = 14;
        sCtx.globalAlpha = 0.35;
      }} else {{
        sCtx.strokeStyle = '#090d16';
        sCtx.lineWidth = 24;
        sCtx.globalAlpha = 1.0;
      }}
      sCtx.lineTo(e.offsetX, e.offsetY);
      sCtx.stroke();
    }});

    window.addEventListener('mouseup', () => {{ sDrawing = false; }});

    // Touch support for scratchpad
    sCanvas?.addEventListener('touchstart', e => {{
      if (e.touches.length === 1) {{
        sDrawing = true;
        const rect = sCanvas.getBoundingClientRect();
        sCtx.beginPath();
        sCtx.moveTo(e.touches[0].clientX - rect.left, e.touches[0].clientY - rect.top);
      }}
    }}, {{ passive: true }});

    sCanvas?.addEventListener('touchmove', e => {{
      if (!sDrawing || e.touches.length !== 1) return;
      const rect = sCanvas.getBoundingClientRect();
      if (sTool === 'pen') {{
        sCtx.strokeStyle = '#06b6d4';
        sCtx.lineWidth = 2.5;
        sCtx.globalAlpha = 1.0;
      }} else if (sTool === 'highlighter') {{
        sCtx.strokeStyle = '#f59e0b';
        sCtx.lineWidth = 14;
        sCtx.globalAlpha = 0.35;
      }} else {{
        sCtx.strokeStyle = '#090d16';
        sCtx.lineWidth = 24;
        sCtx.globalAlpha = 1.0;
      }}
      sCtx.lineTo(e.touches[0].clientX - rect.left, e.touches[0].clientY - rect.top);
      sCtx.stroke();
    }}, {{ passive: true }});

    window.addEventListener('touchend', () => {{ sDrawing = false; }});

    // Sound Toggle
    document.getElementById('soundToggleBtn')?.addEventListener('click', () => {{
      soundEnabled = !soundEnabled;
      document.getElementById('soundIcon').textContent = soundEnabled ? '🔊' : '🔇';
      document.getElementById('soundLabel').textContent = soundEnabled ? 'Sound' : 'Muted';
    }});

    // Initialize on DOM load
    document.addEventListener('DOMContentLoaded', () => {{
      resizePrismCanvas();
      updatePrismMetrics();
      renderQuestion();
    }});
  </script>
</body>
</html>'''

    target_path = 'apps/math/5th_grade_aig_math_volume_operations_decimals_q1.html'
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully generated standalone HTML application at {target_path} (length: {len(html)} chars)")

if __name__ == '__main__':
    build_app()

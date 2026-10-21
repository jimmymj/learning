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
  <meta name="description" content="Elite, interactive mathematical learning suite for CMS 5th Grade AIG students (Weeks 1–9 / NC SCOS / IM Units 1, 4, 5). Features 9 manipulatives, 3D rotatable volume sandbox, algorithm cryptarithm solver, 10-topic navigator, and 60-question adaptive quest." />

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
      background: rgba(9, 13, 22, 0.85);
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

    .btn-sm {{
      padding: 6px 12px;
      font-size: 0.8rem;
      border-radius: var(--radius-sm);
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

    .btn-accent {{
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #fff;
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.25);
    }}

    .btn-accent:hover {{
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

    /* Topic Quick Navigation Bar */
    .topic-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(14px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 10px 16px;
      margin: 18px 0 10px;
      flex-wrap: wrap;
    }}

    .topic-nav-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      flex: 1;
      min-width: 280px;
    }}

    .topic-selector-container {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 5px 12px;
      flex: 1;
      min-width: 250px;
    }}

    .topic-nav-icon {{
      font-size: 1.1rem;
    }}

    .topic-select {{
      background: transparent;
      border: none;
      color: #fff;
      font-family: var(--font-heading);
      font-size: 0.88rem;
      font-weight: 600;
      width: 100%;
      outline: none;
      cursor: pointer;
    }}

    .topic-select option, .topic-select optgroup {{
      background: #0f172a;
      color: #f8fafc;
      font-family: var(--font-body);
      font-size: 0.86rem;
    }}

    .topic-stepper-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .topic-nav-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    /* Horizontal Topic Pills Bar */
    .topic-pills-bar {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: thin;
      padding-bottom: 8px;
      margin-bottom: 18px;
    }}

    .topic-pills-bar::-webkit-scrollbar {{
      height: 4px;
    }}
    .topic-pills-bar::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-full);
    }}

    .topic-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.76rem;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      transition: var(--transition);
    }}

    .topic-pill:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
      border-color: rgba(255, 255, 255, 0.2);
    }}

    .topic-pill.active {{
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--primary);
      color: #38bdf8;
      box-shadow: 0 0 10px rgba(6, 182, 212, 0.2);
    }}

    .pill-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .pill-dot.m1 {{ background: var(--primary); }}
    .pill-dot.m2 {{ background: var(--accent-indigo); }}
    .pill-dot.m3 {{ background: var(--accent-emerald); }}

    /* Main Tab Navigation */
    .tab-bar {{
      display: flex;
      gap: 6px;
      background: rgba(15, 23, 42, 0.6);
      padding: 6px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      margin-bottom: 24px;
      overflow-x: auto;
      scrollbar-width: none;
    }}

    .tab-bar::-webkit-scrollbar {{
      display: none;
    }}

    .tab-btn {{
      flex: 1;
      min-width: 170px;
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
      align-items: center;
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

    /* Question Matrix Panel in Quest */
    .question-matrix-panel {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      margin-bottom: 8px;
    }}

    .matrix-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .matrix-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(34px, 1fr));
      gap: 6px;
    }}

    .matrix-chip {{
      height: 34px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }}

    .matrix-chip:hover {{
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border-color: rgba(255, 255, 255, 0.25);
    }}

    .matrix-chip.current {{
      border-color: var(--primary);
      background: rgba(6, 182, 212, 0.25);
      color: #38bdf8;
      box-shadow: 0 0 10px rgba(6, 182, 212, 0.4);
    }}

    .matrix-chip.correct {{
      border-color: var(--accent-emerald);
      background: rgba(16, 185, 129, 0.25);
      color: #34d399;
    }}

    .matrix-chip.incorrect {{
      border-color: var(--accent-rose);
      background: rgba(244, 63, 94, 0.25);
      color: #fb7185;
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

    /* Topic Directory Modal */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(10px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-overlay.active {{
      display: flex;
    }}

    .modal-container {{
      background: #0f172a;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 980px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
      overflow: hidden;
      animation: fadeIn 0.25s ease-out;
    }}

    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-subtle);
      background: rgba(15, 23, 42, 0.95);
    }}

    .modal-body {{
      padding: 24px;
      overflow-y: auto;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 16px;
    }}

    .topic-directory-card {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: var(--transition);
    }}

    .topic-directory-card:hover {{
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(6, 182, 212, 0.4);
      transform: translateY(-2px);
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
        <button id="soundToggleBtn" class="btn btn-secondary btn-sm" title="Toggle Sound">
          <span id="soundIcon">🔊</span>
          <span id="soundLabel">Sound</span>
        </button>
        <button id="scratchpadToggleBtn" class="btn btn-secondary btn-sm">
          <span>✏️ Whiteboard</span>
        </button>
        <button id="btnOpenTopicDirectoryHeader" class="btn btn-secondary btn-sm">
          <span>🗺️ Topics Index</span>
        </button>
        <a href="../../index.html" class="btn btn-outline btn-sm">
          <span>← LearningHub</span>
        </a>
      </div>
    </div>
  </header>

  <main class="container" style="padding-bottom: 40px;">

    <!-- TOPIC QUICK NAVIGATION BAR (SIMPLE & EASY) -->
    <div class="topic-nav-bar" id="topicNavBar">
      <div class="topic-nav-left">
        <div class="topic-selector-container">
          <span class="topic-nav-icon">📚</span>
          <select id="globalTopicSelect" class="topic-select" aria-label="Select Learning Topic">
            <optgroup label="Module 1: Spatial Volume Reasoning & 3D Geometry (NC.5.MD)">
              <option value="1">Topic 1: Unit Cube Packing & SA:V Ratios (NC.5.MD.3/4)</option>
              <option value="2">Topic 2: Volume Fluency & Layering V = B × h (NC.5.MD.5a/b)</option>
              <option value="3">Topic 3: Additive Volume & Composite Solids (NC.5.MD.5c)</option>
              <option value="4">Topic 4: Real-World Dimension Constraints (NC.5.MD.5b)</option>
            </optgroup>
            <optgroup label="Module 2: Multi-Digit Algorithms & Logic (NC.5.NBT)">
              <option value="5">Topic 5: Standard Algorithm Mechanics (NC.5.NBT.5)</option>
              <option value="6">Topic 6: Division & Remainder Models (NC.5.NBT.6)</option>
              <option value="7">Topic 7: Algorithmic Cryptarithms & Error Analysis (NC.5.NBT.5/6)</option>
            </optgroup>
            <optgroup label="Module 3: Decimal Place Value & Exponents (NC.5.NBT)">
              <option value="8">Topic 8: Base-Ten Patterns & Exponential Powers (NC.5.NBT.1/2)</option>
              <option value="9">Topic 9: Thousandths Inequalities & Value Density (NC.5.NBT.3a/b)</option>
              <option value="10">Topic 10: High-Precision Decimal Operations & Mental Math (NC.5.NBT.7)</option>
            </optgroup>
          </select>
        </div>

        <!-- Stepper Buttons -->
        <div class="topic-stepper-group">
          <button id="prevTopicBtn" class="btn btn-sm btn-secondary" title="Previous Topic">◀ Prev</button>
          <span id="topicCounterChip" class="badge badge-primary">Topic 1 / 10</span>
          <button id="nextTopicBtn" class="btn btn-sm btn-secondary" title="Next Topic">Next ▶</button>
        </div>
      </div>

      <!-- Direct 1-Click Action Launchers for Selected Topic -->
      <div class="topic-nav-right">
        <button id="btnOpenTopicLab" class="btn btn-sm btn-primary" title="Launch Interactive Manipulative for this topic">
          <span>🔬 Open Lab</span>
        </button>
        <button id="btnOpenTopicQuest" class="btn btn-sm btn-accent" title="Practice Questions for this topic">
          <span>🎯 Practice Quest</span>
          <span class="badge" id="topicQCountChip" style="background: rgba(0,0,0,0.35); font-size: 0.68rem; color: #fff;">5 Qs</span>
        </button>
        <button id="btnOpenTopicDirectory" class="btn btn-sm btn-secondary" title="View All 10 Topics Index">
          <span>🗺️ All Topics</span>
        </button>
      </div>
    </div>

    <!-- Quick Topic Pills (Horizontal Scrollable Strip) -->
    <div class="topic-pills-bar" id="topicPillsBar">
      <button class="topic-pill active" data-topic="1"><span class="pill-dot m1"></span>T1: Cube Packing</button>
      <button class="topic-pill" data-topic="2"><span class="pill-dot m1"></span>T2: Layering V=B×h</button>
      <button class="topic-pill" data-topic="3"><span class="pill-dot m1"></span>T3: Composite Solids</button>
      <button class="topic-pill" data-topic="4"><span class="pill-dot m1"></span>T4: Dimension Limits</button>
      <button class="topic-pill" data-topic="5"><span class="pill-dot m2"></span>T5: Multi-Digit Multiply</button>
      <button class="topic-pill" data-topic="6"><span class="pill-dot m2"></span>T6: Division & Remainders</button>
      <button class="topic-pill" data-topic="7"><span class="pill-dot m2"></span>T7: Cryptarithms</button>
      <button class="topic-pill" data-topic="8"><span class="pill-dot m3"></span>T8: Powers of 10</button>
      <button class="topic-pill" data-topic="9"><span class="pill-dot m3"></span>T9: Thousandths Values</button>
      <button class="topic-pill" data-topic="10"><span class="pill-dot m3"></span>T10: Decimal Operations</button>
    </div>

    <!-- Tab Navigation Bar -->
    <nav class="tab-bar" role="tablist">
      <button class="tab-btn active" data-tab="tabVolume" id="tabBtnVolume">
        <span>🏛️ 1. 3D Volume Lab</span>
        <span class="badge badge-primary">NC.5.MD</span>
      </button>
      <button class="tab-btn" data-tab="tabAlgorithms" id="tabBtnAlgorithms">
        <span>⚙️ 2. Multi-Digit Algorithms</span>
        <span class="badge badge-indigo">NC.5.NBT.5/6</span>
      </button>
      <button class="tab-btn" data-tab="tabDecimals" id="tabBtnDecimals">
        <span>🔢 3. Decimal Systems</span>
        <span class="badge badge-emerald">NC.5.NBT.1/2/7</span>
      </button>
      <button class="tab-btn" data-tab="tabQuest" id="tabBtnQuest">
        <span>🏆 4. 60-Q AIG Quest</span>
        <span class="badge badge-amber" id="questCountBadge">60 Qs</span>
      </button>
    </nav>

    <!-- Tab 1: 3D Volume & Spatial Reasoning Lab -->
    <section id="tabVolume" class="tab-pane active">
      <div class="glass-card">
        <div class="card-title-group">
          <div>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span class="badge badge-primary">Module 1 • Topics 1–4</span>
              <span style="font-size: 0.8rem; color: var(--text-muted);">NC.5.MD.3 • NC.5.MD.4 • NC.5.MD.5a-c • NC.5.OA.2</span>
            </div>
            <h2 class="card-title">Interactive 3D Rectangular Prism Sandbox</h2>
            <p class="card-desc">Drag to rotate the prism in 3D. Manipulate dimensions to investigate base area layering (V = B × h), discrete unit cube packing, and the 3D space diagonal.</p>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-secondary btn-sm" id="resetPrismBtn">↺ Reset View</button>
            <button class="btn btn-secondary btn-sm" id="toggleWireframeBtn">🔲 Toggle Mesh</button>
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
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span class="badge badge-indigo">Module 2 • Topics 5–7</span>
              <span style="font-size: 0.8rem; color: var(--text-muted);">NC.5.NBT.5 • NC.5.NBT.6</span>
            </div>
            <h2 class="card-title">Multi-Digit Operations & Cryptarithm Studio</h2>
            <p class="card-desc">Inspect partial products area models and solve missing-digit cryptarithms under NC.5.NBT.5 and NC.5.NBT.6.</p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
          <!-- Partial Products Model -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="font-weight: 700; margin-bottom: 12px; color: var(--primary);">Interactive 3-Digit × 2-Digit Area Model</div>
            <div style="display: flex; gap: 12px; margin-bottom: 16px; flex-wrap: wrap;">
              <input type="number" id="inputFactorA" value="487" style="width: 100px; padding: 8px; background: rgba(0,0,0,0.4); border: 1px solid var(--border-subtle); border-radius: 6px; color: #fff; font-family: var(--font-mono);" />
              <span style="font-size: 1.2rem; align-self: center;">×</span>
              <input type="number" id="inputFactorB" value="63" style="width: 80px; padding: 8px; background: rgba(0,0,0,0.4); border: 1px solid var(--border-subtle); border-radius: 6px; color: #fff; font-family: var(--font-mono);" />
              <button class="btn btn-secondary btn-sm" id="btnCalculateProduct">Calculate</button>
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
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px;">Select digits A and B to reconstruct the multiplication problem.</p>
            
            <div style="display: flex; gap: 16px; align-items: center; margin-bottom: 16px; flex-wrap: wrap;">
              <label style="font-size: 0.85rem; display: flex; align-items: center; gap: 6px;">
                Digit A:
                <select id="selectDigitA" style="padding: 6px 12px; background: rgba(0,0,0,0.5); border: 1px solid var(--border-subtle); border-radius: 6px; color: #fff; font-family: var(--font-mono);">
                  <option value="0">0</option><option value="1">1</option><option value="2">2</option><option value="3">3</option>
                  <option value="4" selected>4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option>
                </select>
              </label>

              <label style="font-size: 0.85rem; display: flex; align-items: center; gap: 6px;">
                Digit B:
                <select id="selectDigitB" style="padding: 6px 12px; background: rgba(0,0,0,0.5); border: 1px solid var(--border-subtle); border-radius: 6px; color: #fff; font-family: var(--font-mono);">
                  <option value="1">1</option><option value="2">2</option><option value="3" selected>3</option><option value="4">4</option>
                  <option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option>
                </select>
              </label>
            </div>

            <div id="cryptarithmResultBox" style="font-family: var(--font-mono); font-size: 0.85rem; padding: 12px; border-radius: 6px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); color: #34d399;">
              ✓ 345 × 4 = 1,380 | 345 × 30 = 10,350 | Sum = 11,730 (Keep testing!)
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 3: Decimal Place Value & Exponents -->
    <section id="tabDecimals" class="tab-pane">
      <div class="glass-card">
        <div class="card-title-group">
          <div>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span class="badge badge-emerald">Module 3 • Topics 8–10</span>
              <span style="font-size: 0.8rem; color: var(--text-muted);">NC.5.NBT.1 • NC.5.NBT.2 • NC.5.NBT.3a-b • NC.5.NBT.7</span>
            </div>
            <h2 class="card-title">Decimal Place Value & Exponential Shifter</h2>
            <p class="card-desc">Slide to multiply and divide by powers of 10 from 10⁻³ to 10⁶. Observe decimal point shifts and metric unit transitions.</p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
          <!-- Exponent Slider -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
              <span style="font-weight: 700; color: var(--primary);">Base Value: 48.5</span>
              <span id="exponentDisplay" style="font-family: var(--font-mono); font-size: 0.9rem; color: var(--accent-amber);">Power n = 2 (10² = 100)</span>
            </div>

            <input type="range" id="sliderExponent" class="control-slider" min="-3" max="6" value="2" style="margin: 16px 0;" />

            <div class="telemetry-box" style="margin-top: 14px;">
              <div class="telemetry-label">Shifted Decimal Value</div>
              <div id="exponentOutput" class="telemetry-val" style="color: #38bdf8;">48.5 × 10² = 4,850</div>
            </div>
          </div>

          <!-- Decimal Compensation Subtraction -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); padding: 20px; border-radius: var(--radius-md);">
            <div style="font-weight: 700; margin-bottom: 10px; color: #a5b4fc;">Landmark Compensation: 64.382 - 29.995</div>
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

          <!-- Module & Topic Filter Controls -->
          <div class="filter-group">
            <button class="filter-btn active" data-filter="all" id="filterAll">All (60)</button>
            <button class="filter-btn" data-filter="Module 1" id="filterM1">Volume (20)</button>
            <button class="filter-btn" data-filter="Module 2" id="filterM2">Algorithms (20)</button>
            <button class="filter-btn" data-filter="Module 3" id="filterM3">Decimals (20)</button>
            
            <!-- Quick Question Grid Toggle -->
            <button class="btn btn-sm btn-secondary" id="toggleMatrixBtn" title="Toggle 1-60 Question Matrix">
              <span>🔢 Jump Matrix</span>
            </button>
          </div>

          <!-- Score & Streak -->
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

        <!-- Collapsible 60-Question Matrix Jump Grid -->
        <div class="question-matrix-panel" id="questionMatrixPanel" style="display: none;">
          <div class="matrix-header">
            <span><strong>Quick Jump Matrix:</strong> Click any number to jump directly to that question.</span>
            <span style="font-size: 0.75rem;">🟢 Correct • 🔴 Misconception • 🔵 Active</span>
          </div>
          <div class="matrix-grid" id="matrixGridContainer">
            <!-- 60 matrix chips injected via JS -->
          </div>
        </div>

        <!-- Question Presentation Card -->
        <div class="question-card">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="badge badge-emerald" id="standardBadge">NC.5.MD.3</span>
              <span class="badge badge-primary" id="topicBadge">Topic 1</span>
            </div>
            <span style="font-size: 0.85rem; color: var(--text-muted);" id="topicLabel">Topic 1: Unit Cube Packing & SA:V Ratios</span>
          </div>

          <div class="question-prompt" id="questionText">
            A shipping container is packed with 1-cm unit cubes. The base layer has 8 rows with 9 cubes in each row. If there are 7 identical layers packed without gaps or overlaps, what is the total volume?
          </div>

          <div class="options-grid" id="optionsContainer">
            <!-- Shuffled options injected dynamically -->
          </div>

          <!-- Action Buttons -->
          <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
            <button class="btn btn-primary" id="submitBtn" disabled>Submit Answer</button>
            <button class="btn btn-secondary" id="hintBtn">💡 Need a Hint?</button>
            <button class="btn btn-secondary" id="scratchpadBtn">✏️ Scratchpad</button>
            <div style="margin-left: auto; display: flex; gap: 8px;">
              <button class="btn btn-outline" id="prevBtn">← Previous</button>
              <button class="btn btn-outline" id="nextBtn">Next →</button>
            </div>
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

  <!-- All 10 Topics Directory Modal -->
  <div class="modal-overlay" id="topicDirectoryModal">
    <div class="modal-container">
      <div class="modal-header">
        <div>
          <div style="font-weight: 700; font-size: 1.15rem; color: #fff;">🗺️ Curriculum Topic Directory</div>
          <div style="font-size: 0.8rem; color: var(--text-muted);">CMS 5th Grade AIG Math Q1 • All 10 Core Topics</div>
        </div>
        <button id="closeTopicDirectoryBtn" class="btn btn-sm btn-secondary" style="font-size: 1rem; width: 32px; height: 32px; padding: 0;">✕</button>
      </div>
      <div class="modal-body" id="topicDirectoryBody">
        <!-- 10 Topic Cards injected via JS -->
      </div>
    </div>
  </div>

  <!-- Whiteboard Scratchpad Overlay -->
  <div class="scratchpad-overlay" id="scratchpadOverlay">
    <div class="scratchpad-bar">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-weight: 700; font-size: 1rem; color: #fff;">✏️ AIG Problem-Solving Scratchpad</span>
        <span class="badge badge-primary">Touch / Pointer</span>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <button id="penToolBtn" class="btn btn-secondary btn-sm" style="border-color: var(--primary);">🖊️ Pen</button>
        <button id="highlighterToolBtn" class="btn btn-secondary btn-sm">🖍️ Highlighter</button>
        <button id="eraserToolBtn" class="btn btn-secondary btn-sm">🧹 Eraser</button>
        <button id="clearScratchpadBtn" class="btn btn-secondary btn-sm">Clear</button>
        <button id="closeScratchpadBtn" class="btn btn-secondary btn-sm">✕ Close</button>
      </div>
    </div>
    <div class="scratchpad-canvas-wrapper" id="scratchpadWrapper">
      <canvas id="scratchpadCanvas"></canvas>
    </div>
  </div>

  <!-- Footer -->
  <footer class="app-footer">
    <div class="container">
      <p>CMS 5th Grade AIG Mathematics • Quarter 1 Accelerated Curriculum Lab</p>
      <p style="margin-top: 6px; color: var(--text-muted);">Aligned to NC SCOS (NC.5.MD, NC.5.NBT, NC.5.OA) • Standalone Single-File Architecture</p>
    </div>
  </footer>

  <!-- Embedded Question Bank & Master Application Engine -->
  <script>
    const QUESTION_BANK = {questions_json};

    // Metadata for the 10 Curriculum Topics
    const TOPICS_META = [
      {{ id: 1, module: "Module 1", tab: "tabVolume", name: "Topic 1: Unit Cube Packing & SA:V Ratios", standard: "NC.5.MD.3/4", qCount: 5, qStart: 0, desc: "Packing 1-cm & 1-inch unit cubes, floor base layer counts, and surface-area-to-volume ratio optimization." }},
      {{ id: 2, module: "Module 1", tab: "tabVolume", name: "Topic 2: Volume Fluency & Layering V = B × h", standard: "NC.5.MD.5a/b", qCount: 5, qStart: 5, desc: "Base area layering (V = B × h), associative property V = (l × w) × h, and 3D internal space diagonal." }},
      {{ id: 3, module: "Module 1", tab: "tabVolume", name: "Topic 3: Additive Volume & Composite Solids", standard: "NC.5.MD.5c", qCount: 5, qStart: 10, desc: "Non-overlapping L-shaped decomposition, hollow-core cavity void subtraction, and nested bracket operations." }},
      {{ id: 4, module: "Module 1", tab: "tabVolume", name: "Topic 4: Real-World Dimension Constraints", standard: "NC.5.MD.5b", qCount: 5, qStart: 15, desc: "Fixed volume dimension factorizations, perimeter and height constraints, and minimal material packaging." }},
      {{ id: 5, module: "Module 2", tab: "tabAlgorithms", name: "Topic 5: Standard Algorithm Mechanics", standard: "NC.5.NBT.5", qCount: 5, qStart: 20, desc: "3-digit × 2-digit multiplication, partial products area models, and zero placeholder shifts." }},
      {{ id: 6, module: "Module 2", tab: "tabAlgorithms", name: "Topic 6: Division & Remainder Models", standard: "NC.5.NBT.6", qCount: 5, qStart: 25, desc: "4-digit ÷ 2-digit partial quotients division, interpreting remainders in real-world contexts." }},
      {{ id: 7, module: "Module 2", tab: "tabAlgorithms", name: "Topic 7: Algorithmic Cryptarithms & Error Analysis", standard: "NC.5.NBT.5/6", qCount: 10, qStart: 30, desc: "Reconstructing missing digits in multi-digit products (3A5 × B4 = 11,810) and carry propagation logic." }},
      {{ id: 8, module: "Module 3", tab: "tabDecimals", name: "Topic 8: Base-Ten Patterns & Exponential Powers", standard: "NC.5.NBT.1/2", qCount: 5, qStart: 40, desc: "Base-10 exponential powers (10⁻³ to 10⁶), metric prefix shifts (milli, centi, kilo), and decimal place migration." }},
      {{ id: 9, module: "Module 3", tab: "tabDecimals", name: "Topic 9: Thousandths Inequalities & Value Density", standard: "NC.5.NBT.3a/b", qCount: 5, qStart: 45, desc: "Comparing decimal magnitudes to thousandths, decimal sandwich density, and unit fraction expanded form." }},
      {{ id: 10, module: "Module 3", tab: "tabDecimals", name: "Topic 10: High-Precision Decimal Operations & Mental Math", standard: "NC.5.NBT.7", qCount: 10, qStart: 50, desc: "Compensation subtraction (64.382 - 29.995 = 34.387), decimal multiplication, and mental math shortcuts." }}
    ];

    // State
    let currentQuestions = [...QUESTION_BANK];
    let currentIndex = 0;
    let currentTopicId = 1;
    let selectedOptionText = null;
    let score = 0;
    let streak = 0;
    let soundEnabled = true;
    let currentHintIndex = 0;
    const userAnswers = {{}}; // qId -> boolean (correct/incorrect)

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
    function switchTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(b => {{
        b.classList.toggle('active', b.dataset.tab === tabId);
      }});
      document.querySelectorAll('.tab-pane').forEach(p => {{
        p.classList.toggle('active', p.id === tabId);
      }});
      if (tabId === 'tabVolume') {{
        setTimeout(resizePrismCanvas, 50);
      }}
    }}

    document.querySelectorAll('.tab-btn').forEach(btn => {{
      btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    }});

    // Central Topic Navigation Function
    function activateTopic(topicId, navigateTo) {{
      topicId = parseInt(topicId);
      if (isNaN(topicId) || topicId < 1 || topicId > 10) topicId = 1;
      currentTopicId = topicId;

      const meta = TOPICS_META.find(t => t.id === topicId) || TOPICS_META[0];

      // Update Select Dropdown
      const sel = document.getElementById('globalTopicSelect');
      if (sel) sel.value = String(topicId);

      // Update Stepper Counter & Chips
      const chip = document.getElementById('topicCounterChip');
      if (chip) chip.textContent = `Topic ${{topicId}} / 10`;

      const qChip = document.getElementById('topicQCountChip');
      if (qChip) qChip.textContent = `${{meta.qCount}} Qs`;

      // Update Pills Bar
      document.querySelectorAll('.topic-pill').forEach(pill => {{
        const isAct = parseInt(pill.dataset.topic) === topicId;
        pill.classList.toggle('active', isAct);
        if (isAct) {{
          pill.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
        }}
      }});

      // Route Navigation
      if (navigateTo === 'lab') {{
        switchTab(meta.tab);
        const targetElem = document.getElementById(meta.tab);
        if (targetElem) {{
          targetElem.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }}
      }} else if (navigateTo === 'quest') {{
        switchTab('tabQuest');
        filterQuestByTopic(topicId);
      }}
    }}

    function filterQuestByTopic(topicId) {{
      topicId = parseInt(topicId);
      currentQuestions = QUESTION_BANK.filter(q => q.topic.startsWith(`Topic ${{topicId}}:`));
      if (currentQuestions.length === 0) {{
        currentQuestions = [...QUESTION_BANK];
      }}
      currentIndex = 0;

      // Update module filter buttons
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));

      renderQuestion();
      renderQuestionMatrix();

      const qCard = document.querySelector('.question-card');
      if (qCard) qCard.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}

    // Topic Bar Event Listeners
    document.getElementById('globalTopicSelect')?.addEventListener('change', e => {{
      activateTopic(e.target.value);
    }});

    document.getElementById('prevTopicBtn')?.addEventListener('click', () => {{
      const prevId = currentTopicId > 1 ? currentTopicId - 1 : 10;
      activateTopic(prevId);
    }});

    document.getElementById('nextTopicBtn')?.addEventListener('click', () => {{
      const nextId = currentTopicId < 10 ? currentTopicId + 1 : 1;
      activateTopic(nextId);
    }});

    document.querySelectorAll('.topic-pill').forEach(pill => {{
      pill.addEventListener('click', () => {{
        activateTopic(pill.dataset.topic);
      }});
    }});

    document.getElementById('btnOpenTopicLab')?.addEventListener('click', () => {{
      activateTopic(currentTopicId, 'lab');
    }});

    document.getElementById('btnOpenTopicQuest')?.addEventListener('click', () => {{
      activateTopic(currentTopicId, 'quest');
    }});

    // Topic Directory Modal
    const topicModal = document.getElementById('topicDirectoryModal');
    function openTopicDirectory() {{
      renderTopicDirectoryCards();
      topicModal?.classList.add('active');
    }}
    function closeTopicDirectory() {{
      topicModal?.classList.remove('active');
    }}

    document.getElementById('btnOpenTopicDirectory')?.addEventListener('click', openTopicDirectory);
    document.getElementById('btnOpenTopicDirectoryHeader')?.addEventListener('click', openTopicDirectory);
    document.getElementById('closeTopicDirectoryBtn')?.addEventListener('click', closeTopicDirectory);
    topicModal?.addEventListener('click', e => {{
      if (e.target === topicModal) closeTopicDirectory();
    }});

    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape' && topicModal?.classList.contains('active')) {{
        closeTopicDirectory();
      }}
    }});

    function renderTopicDirectoryCards() {{
      const body = document.getElementById('topicDirectoryBody');
      if (!body) return;
      body.innerHTML = '';

      TOPICS_META.forEach(t => {{
        const card = document.createElement('div');
        card.className = 'topic-directory-card';
        card.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 8px;">
            <span class="badge ${{t.module === 'Module 1' ? 'badge-primary' : (t.module === 'Module 2' ? 'badge-indigo' : 'badge-emerald')}}">${{t.standard}}</span>
            <span class="badge" style="background: rgba(255,255,255,0.06); font-size: 0.7rem;">${{t.qCount}} Graded Qs</span>
          </div>
          <div style="font-weight: 700; font-size: 0.95rem; color: #fff;">${{t.name}}</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); flex: 1; line-height: 1.5;">${{t.desc}}</p>
          <div style="display: flex; gap: 8px; margin-top: 6px;">
            <button class="btn btn-sm btn-secondary" style="flex: 1;" onclick="closeTopicDirectory(); activateTopic(${{t.id}}, 'lab');">
              🔬 Open Lab
            </button>
            <button class="btn btn-sm btn-primary" style="flex: 1;" onclick="closeTopicDirectory(); activateTopic(${{t.id}}, 'quest');">
              🎯 Practice
            </button>
          </div>
        `;
        body.appendChild(card);
      }});
    }}

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

      const projected = vertices.map(v => {{
        const x1 = v.x * cosY - v.z * sinY;
        const z1 = v.x * sinY + v.z * cosY;

        const y2 = v.y * cosX - z1 * sinX;
        const z2 = v.y * sinX + z1 * cosX;

        return {{
          x: cx + x1,
          y: cy + y2,
          z: z2
        }};
      }});

      // 6 Faces defined by vertex indices
      const faces = [
        [0, 1, 2, 3], // back
        [4, 5, 6, 7], // front
        [0, 1, 5, 4], // top
        [3, 2, 6, 7], // bottom
        [0, 3, 7, 4], // left
        [1, 2, 6, 5]  // right
      ];

      // Draw bottom face highlight (base area B = l × w)
      pCtx.fillStyle = 'rgba(6, 182, 212, 0.22)';
      pCtx.beginPath();
      pCtx.moveTo(projected[3].x, projected[3].y);
      pCtx.lineTo(projected[2].x, projected[2].y);
      pCtx.lineTo(projected[6].x, projected[6].y);
      pCtx.lineTo(projected[7].x, projected[7].y);
      pCtx.closePath();
      pCtx.fill();

      // Draw Edges
      const edges = [
        [0,1], [1,2], [2,3], [3,0],
        [4,5], [5,6], [6,7], [7,4],
        [0,4], [1,5], [2,6], [3,7]
      ];

      pCtx.strokeStyle = showWireframe ? '#06b6d4' : 'rgba(6, 182, 212, 0.4)';
      pCtx.lineWidth = 1.8;
      edges.forEach(([i, j]) => {{
        pCtx.beginPath();
        pCtx.moveTo(projected[i].x, projected[i].y);
        pCtx.lineTo(projected[j].x, projected[j].y);
        pCtx.stroke();
      }});

      // Draw Internal Space Diagonal (connecting vertex 3 [bottom-left-back] to vertex 5 [top-right-front])
      pCtx.strokeStyle = '#f59e0b';
      pCtx.lineWidth = 2.2;
      pCtx.setLineDash([5, 4]);
      pCtx.beginPath();
      pCtx.moveTo(projected[3].x, projected[3].y);
      pCtx.lineTo(projected[5].x, projected[5].y);
      pCtx.stroke();
      pCtx.setLineDash([]);

      // Glow nodes on space diagonal ends
      pCtx.fillStyle = '#fbbf24';
      [projected[3], projected[5]].forEach(pt => {{
        pCtx.beginPath();
        pCtx.arc(pt.x, pt.y, 4.5, 0, Math.PI * 2);
        pCtx.fill();
      }});
    }}

    // Tab 2: Partial Products & Cryptarithm Engine
    document.getElementById('btnCalculateProduct')?.addEventListener('click', () => {{
      const a = parseInt(document.getElementById('inputFactorA').value) || 0;
      const b = parseInt(document.getElementById('inputFactorB').value) || 0;
      const ones = b % 10;
      const tens = Math.floor(b / 10) * 10;
      const p1 = a * ones;
      const p2 = a * tens;
      const total = a * b;

      document.getElementById('partialProductsDisplay').innerHTML = `
        Row 1: ${{a}} × ${{ones}} = ${{p1.toLocaleString()}}<br />
        Row 2: ${{a}} × ${{tens}} = ${{p2.toLocaleString()}} (with 10¹ placeholder shift)<br />
        <strong style="color: #34d399;">Total Product: ${{total.toLocaleString()}}</strong>
      `;
      playTone(587.33, 'sine', 0.1);
    }});

    function updateCryptarithm() {{
      const a = parseInt(document.getElementById('selectDigitA').value);
      const b = parseInt(document.getElementById('selectDigitB').value);
      const factor1 = 300 + a * 10 + 5;
      const factor2 = b * 10 + 4;
      const row1 = factor1 * 4;
      const row2 = factor1 * (b * 10);
      const sum = factor1 * factor2;

      const box = document.getElementById('cryptarithmResultBox');
      if (sum === 11810) {{
        playSuccessSound();
        box.style.background = 'rgba(16, 185, 129, 0.15)';
        box.style.borderColor = 'rgba(16, 185, 129, 0.4)';
        box.style.color = '#34d399';
        box.innerHTML = `✓ 345 × 4 = 1,380 | 345 × 30 = 10,350 | Sum = 11,810 (Exact Match!)`;
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
      document.getElementById('topicBadge').textContent = q.topic.split(':')[0];
      document.getElementById('topicLabel').textContent = q.topic;
      document.getElementById('questionText').innerHTML = q.question;

      // Synchronize active topic navigator bar
      const matchedMeta = TOPICS_META.find(t => q.topic.startsWith(t.name.split(':')[0] + ':'));
      if (matchedMeta) {{
        currentTopicId = matchedMeta.id;
        const sel = document.getElementById('globalTopicSelect');
        if (sel) sel.value = String(matchedMeta.id);
        const chip = document.getElementById('topicCounterChip');
        if (chip) chip.textContent = `Topic ${{matchedMeta.id}} / 10`;
        const qChip = document.getElementById('topicQCountChip');
        if (qChip) qChip.textContent = `${{matchedMeta.qCount}} Qs`;
        document.querySelectorAll('.topic-pill').forEach(pill => {{
          pill.classList.toggle('active', parseInt(pill.dataset.topic) === matchedMeta.id);
        }});
      }}

      // Reset Drawers & Buttons
      document.getElementById('diagnosticPanel').style.display = 'none';
      document.getElementById('hintDrawer').classList.remove('open');
      document.getElementById('submitBtn').disabled = true;
      document.getElementById('submitBtn').style.display = 'inline-flex';

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
      updateMatrixCurrentHighlight();
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

      userAnswers[q.id] = isCorrect;

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

      renderQuestionMatrix();
    }});

    // Next & Previous Question Steppers
    document.getElementById('nextBtn')?.addEventListener('click', () => {{
      currentIndex = (currentIndex + 1) % currentQuestions.length;
      renderQuestion();
      document.querySelector('.question-card').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }});

    document.getElementById('prevBtn')?.addEventListener('click', () => {{
      currentIndex = (currentIndex - 1 + currentQuestions.length) % currentQuestions.length;
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

    // Module Filter Buttons in Quest HUD
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
        renderQuestionMatrix();
      }});
    }});

    // Question Jump Matrix (1-60)
    const toggleMatrixBtn = document.getElementById('toggleMatrixBtn');
    const matrixPanel = document.getElementById('questionMatrixPanel');
    toggleMatrixBtn?.addEventListener('click', () => {{
      const isVisible = matrixPanel.style.display !== 'none';
      matrixPanel.style.display = isVisible ? 'none' : 'block';
      if (!isVisible) renderQuestionMatrix();
    }});

    function renderQuestionMatrix() {{
      const container = document.getElementById('matrixGridContainer');
      if (!container) return;
      container.innerHTML = '';

      currentQuestions.forEach((q, idx) => {{
        const chip = document.createElement('div');
        chip.className = 'matrix-chip';
        chip.textContent = idx + 1;

        if (idx === currentIndex) {{
          chip.classList.add('current');
        }}

        if (userAnswers[q.id] === true) {{
          chip.classList.add('correct');
        }} else if (userAnswers[q.id] === false) {{
          chip.classList.add('incorrect');
        }}

        chip.addEventListener('click', () => {{
          currentIndex = idx;
          renderQuestion();
          document.querySelector('.question-card').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }});

        container.appendChild(chip);
      }});
    }}

    function updateMatrixCurrentHighlight() {{
      const chips = document.querySelectorAll('.matrix-chip');
      chips.forEach((c, idx) => {{
        c.classList.toggle('current', idx === currentIndex);
      }});
    }}

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
      activateTopic(1);
      renderQuestion();
      renderQuestionMatrix();
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

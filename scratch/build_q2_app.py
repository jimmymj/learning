# Master HTML App Builder for CMS 4th Grade Math: Quarter 2
import sys
import json
import os
sys.path.insert(0, '.')
from scratch.q2_questions import ALL_Q2_QUESTIONS, CLUSTER1_QUESTIONS, CLUSTER2_QUESTIONS, CLUSTER3_QUESTIONS

print(f"Loaded {len(ALL_Q2_QUESTIONS)} Quarter 2 questions total ({len(CLUSTER1_QUESTIONS)} C1, {len(CLUSTER2_QUESTIONS)} C2, {len(CLUSTER3_QUESTIONS)} C3)")

def build_app():
    questions_json = json.dumps(ALL_Q2_QUESTIONS, indent=2)

    # Begin constructing the master standalone HTML
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CMS 4th Grade Math: Decimals, Operations & Measurement Lab (Quarter 2)</title>
  <meta name="description" content="Interactive 4th Grade Math suite aligned with CMS Quarter 2 / NC SCOS (NC.4.NF, NC.4.NBT, NC.4.OA, NC.4.MD). Features 9 dynamic manipulatives, Pip the Math Fox mascot, whiteboard scratchpad, and a 60-question adaptive quest with misconception remediation drawers." />
  
  <!-- Tailwind CSS & Google Fonts -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-heading: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --color-primary: #0284c7;
      --color-primary-glow: rgba(14, 165, 233, 0.35);
      --color-accent: #10b981;
      --color-accent-amber: #f59e0b;
      --color-accent-rose: #f43f5e;
      --color-accent-purple: #8b5cf6;
    }}

    body {{
      font-family: var(--font-main);
      touch-action: manipulation;
    }}
    h1, h2, h3, h4, .font-heading {{
      font-family: var(--font-heading);
    }}
    .mono {{
      font-family: var(--font-mono);
    }}

    /* Dyslexia-friendly Font Mode */
    body.dyslexia-mode {{
      font-family: 'Comic Sans MS', 'Trebuchet MS', 'Noto Sans', sans-serif !important;
      letter-spacing: 0.05em;
      word-spacing: 0.1em;
      line-height: 1.8 !important;
    }}

    /* Light Mode Overrides */
    body.theme-light {{
      background-color: #f8fafc !important;
      color: #0f172a !important;
    }}
    body.theme-light .bg-slate-900 {{
      background-color: #ffffff !important;
      color: #0f172a !important;
    }}
    body.theme-light .bg-slate-950 {{
      background-color: #f1f5f9 !important;
      color: #0f172a !important;
    }}
    body.theme-light .bg-slate-800 {{
      background-color: #e2e8f0 !important;
      color: #0f172a !important;
    }}
    body.theme-light .border-slate-800, body.theme-light .border-slate-700 {{
      border-color: #cbd5e1 !important;
    }}
    body.theme-light .text-slate-200, body.theme-light .text-slate-300 {{
      color: #1e293b !important;
    }}
    body.theme-light .text-slate-400 {{
      color: #475569 !important;
    }}

    /* Custom Scrollbars */
    ::-webkit-scrollbar {{
      width: 7px;
      height: 7px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(15, 23, 42, 0.7);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #334155;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #475569;
    }}

    /* Glassmorphism Classes */
    .glass-card {{
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(51, 65, 85, 0.7);
    }}
    .glass-card-subtle {{
      background: rgba(30, 41, 59, 0.5);
      border: 1px solid rgba(51, 65, 85, 0.4);
    }}

    /* Active Tab Styling */
    .tab-active {{
      background: linear-gradient(135deg, #0284c7, #2563eb) !important;
      color: #ffffff !important;
      border-color: rgba(56, 189, 248, 0.6) !important;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4) !important;
    }}

    /* Interactive Scratchpad Canvas */
    #scratchpadCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 9998;
      pointer-events: none;
      cursor: crosshair;
    }}
    #scratchpadCanvas.active {{
      pointer-events: auto;
    }}

    #scratchpadToolbar {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.4);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(14, 165, 233, 0.2);
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: none;
    }}
    #scratchpadToolbar.visible {{
      display: flex;
    }}

    /* Misconception Drawer Animation */
    #misconceptionDrawer {{
      transform: translateY(105%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    #misconceptionDrawer.open {{
      transform: translateY(0);
    }}

    /* Pulse animation */
    @keyframes pulseGlow {{
      0%, 100% {{ box-shadow: 0 0 15px rgba(14, 165, 233, 0.2); }}
      50% {{ box-shadow: 0 0 30px rgba(14, 165, 233, 0.5); }}
    }}
    .glow-pulse {{
      animation: pulseGlow 2.5s infinite;
    }}

    /* Micro-grid preview tile */
    .grid-tenth-col {{
      transition: background-color 0.15s ease;
    }}
    .grid-tenth-col:hover {{
      background-color: rgba(56, 189, 248, 0.3);
    }}
    .grid-hundredth-sq {{
      transition: background-color 0.1s ease;
    }}
    .grid-hundredth-sq:hover {{
      background-color: rgba(245, 158, 11, 0.4);
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-sky-500 selection:text-white">

  <!-- Whiteboard Overlay Canvas -->
  <canvas id="scratchpadCanvas"></canvas>
  
  <!-- Floating Whiteboard Toolbar -->
  <div id="scratchpadToolbar" class="rounded-2xl p-2.5 flex items-center gap-2">
    <div class="flex items-center gap-1.5 px-2 py-1 bg-slate-800/80 rounded-xl border border-slate-700/80">
      <span class="text-xs font-bold text-amber-400">✏️ Scratchpad</span>
    </div>
    <div class="h-5 w-px bg-slate-700"></div>
    <button id="wbPenBtn" onclick="setWbTool('pen')" class="px-2.5 py-1.5 rounded-lg text-xs font-semibold bg-blue-600 text-white transition shadow-sm">
      🖊️ Pen
    </button>
    <button id="wbHighlighterBtn" onclick="setWbTool('highlighter')" class="px-2.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">
      🖍️ Highlighter
    </button>
    <button id="wbEraserBtn" onclick="setWbTool('eraser')" class="px-2.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">
      🧹 Eraser
    </button>
    <div class="h-5 w-px bg-slate-700"></div>
    <!-- Color picks -->
    <button onclick="setWbColor('#38bdf8')" class="w-6 h-6 rounded-full bg-sky-400 border-2 border-white/80 transition hover:scale-110" title="Sky Blue"></button>
    <button onclick="setWbColor('#fbbf24')" class="w-6 h-6 rounded-full bg-amber-400 border-2 border-transparent hover:border-white/80 transition hover:scale-110" title="Amber"></button>
    <button onclick="setWbColor('#34d399')" class="w-6 h-6 rounded-full bg-emerald-400 border-2 border-transparent hover:border-white/80 transition hover:scale-110" title="Emerald"></button>
    <button onclick="setWbColor('#f43f5e')" class="w-6 h-6 rounded-full bg-rose-500 border-2 border-transparent hover:border-white/80 transition hover:scale-110" title="Rose"></button>
    <div class="h-5 w-px bg-slate-700"></div>
    <button onclick="clearScratchpad()" class="px-2.5 py-1.5 rounded-lg text-xs font-semibold bg-rose-500/20 text-rose-300 hover:bg-rose-500/30 transition">
      Clear All
    </button>
    <button onclick="toggleScratchpad()" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-200 hover:bg-slate-700 transition">
      ✕ Close
    </button>
  </div>

  <!-- Header -->
  <header class="border-b border-slate-800/90 bg-slate-900/90 backdrop-blur sticky top-0 z-40 shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex flex-col xl:flex-row xl:items-center xl:justify-between gap-3">
      
      <!-- Brand & Grade Alignment -->
      <div class="flex items-center gap-3">
        <a href="../../index.html" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 hover:text-white border border-slate-700/80 transition-all shadow-sm group" title="Return to Learning Hub">
          <svg class="w-3.5 h-3.5 group-hover:-translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span>Hub</span>
        </a>
        
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 via-sky-600 to-emerald-500 flex items-center justify-center font-extrabold text-base shadow-lg shadow-sky-500/25 text-white mono">
          4Q2
        </div>
        
        <div>
          <div class="flex items-center gap-2 flex-wrap">
            <h1 class="text-base sm:text-lg font-bold tracking-tight text-white flex items-center gap-1.5">
              <span>Decimals, Operations & Measurement Lab</span>
              <span class="text-sm">🦊</span>
            </h1>
            <span class="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30">CMS 4th Grade Math Q2</span>
            <span class="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">NC.4.NF • NBT • OA • MD</span>
          </div>
          <p class="text-[11px] sm:text-xs text-slate-400">Quarter 2 Standard Course of Study: Decimals, 10x Place Value, Multi-Digit Multiplication & Division, Rectilinear Area & Line Plots</p>
        </div>
      </div>

      <!-- Navigation & Utility Controls -->
      <div class="flex items-center gap-2 flex-wrap justify-between xl:justify-end">
        <nav class="flex flex-wrap gap-1 bg-slate-950 p-1.5 rounded-xl border border-slate-800/90 shadow-inner">
          <button onclick="switchTab('concept')" id="tab-concept" class="tab-btn px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-400 hover:text-white">
            💡 1. Concept Hub
          </button>
          <button onclick="switchTab('decimals')" id="tab-decimals" class="tab-btn tab-active px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-semibold transition-all">
            🔢 2. Decimal Grids & Slider
          </button>
          <button onclick="switchTab('operations')" id="tab-operations" class="tab-btn px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-400 hover:text-white">
            ✖️ 3. Operations & 10x Place Value
          </button>
          <button onclick="switchTab('measurement')" id="tab-measurement" class="tab-btn px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-400 hover:text-white">
            📐 4. Measurement & Line Plots
          </button>
          <button onclick="switchTab('challenge')" id="tab-challenge" class="tab-btn text-emerald-400 hover:text-white px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 border border-emerald-500/30 bg-emerald-500/10">
            <span>🎯 5. 60-Q Mastery Quest</span>
            <span id="navScoreBadge" class="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/30 text-emerald-200 mono">0/60</span>
          </button>
          <button onclick="switchTab('dashboard')" id="tab-dashboard" class="tab-btn px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-400 hover:text-white">
            📊 6. Radar & Analytics
          </button>
        </nav>

        <!-- Utility Buttons -->
        <div class="flex items-center gap-1.5">
          <button onclick="toggleScratchpad()" id="scratchpadToggleBtn" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-medium text-amber-300 border border-slate-700 flex items-center gap-1 transition" title="Toggle Interactive Whiteboard Scratchpad">
            <span>✏️</span>
            <span class="hidden sm:inline">Scratchpad</span>
          </button>
          <button onclick="toggleAudioMute()" id="audioMuteBtn" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-200 border border-slate-700 transition" title="Toggle Sound Feedback">
            <span id="audioMuteIcon">🔊</span>
          </button>
          <button onclick="toggleTheme()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-200 border border-slate-700 transition" title="Toggle Light/Dark Theme">
            🌓
          </button>
          <button onclick="toggleDyslexiaMode()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-200 border border-slate-700 transition" title="Toggle Dyslexia-Friendly Typography">
            🔤
          </button>
          <button onclick="downloadStandaloneApp()" class="px-2.5 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-xs font-medium text-white shadow-md flex items-center gap-1 transition" title="Save offline standalone single-file app">
            <span>💾</span>
            <span class="hidden sm:inline">Download App</span>
          </button>
        </div>

      </div>
    </div>
  </header>

  <!-- Mascot Pip Banner -->
  <aside class="bg-gradient-to-r from-slate-900 via-sky-950/40 to-slate-900 border-b border-slate-800/80 px-4 py-2.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <div class="relative cursor-pointer group" onclick="speakMascotMessage()">
          <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-600 to-amber-400 p-0.5 shadow-md group-hover:scale-105 transition-transform">
            <div class="w-full h-full bg-slate-900 rounded-[14px] flex items-center justify-center text-xl">
              🦊
            </div>
          </div>
          <span class="absolute -bottom-1 -right-1 flex h-3.5 w-3.5">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-emerald-500 border border-slate-950"></span>
          </span>
        </div>
        
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold text-amber-400">Pip the Math Fox</span>
            <span class="text-[10px] px-1.5 py-0.2 rounded bg-sky-500/20 text-sky-300 font-mono">Q2 Coach</span>
          </div>
          <p id="mascotSpeechText" class="text-xs text-slate-300 italic">
            "Welcome to Quarter 2! We will explore how tenths become hundredths, discover 10× place-value patterns, multiply multi-digit numbers, and measure rectilinear spaces!"
          </p>
        </div>
      </div>

      <button onclick="speakMascotMessage()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-[11px] font-semibold text-slate-300 hover:text-white flex items-center gap-1.5 border border-slate-700/80 transition shrink-0" title="Listen to Pip">
        <span>🗣️ Listen</span>
      </button>
    </div>
  </aside>

  <!-- Main Work Area -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">

    <!-- TAB 1: CONCEPT HUB (3-TIER SCAFFOLDING) -->
    <section id="panel-concept" class="tab-panel hidden space-y-6">
      
      <div class="flex items-center justify-between flex-wrap gap-4 border-b border-slate-800 pb-4">
        <div>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white">Curriculum Concept Hub</h2>
          <p class="text-xs sm:text-sm text-slate-400">3-Tier Progressive Scaffolding aligned with Charlotte-Mecklenburg Schools Q2 Illustrative Mathematics</p>
        </div>
        
        <!-- Scaffolding Tier Switches -->
        <div class="flex items-center gap-1.5 p-1 bg-slate-900 rounded-xl border border-slate-800">
          <button onclick="setConceptTier(1)" id="tierBtn1" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-sky-600 text-white shadow-sm transition">
            Level 1: Visual Intuition
          </button>
          <button onclick="setConceptTier(2)" id="tierBtn2" class="px-3 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition">
            Level 2: Core Operations
          </button>
          <button onclick="setConceptTier(3)" id="tierBtn3" class="px-3 py-1.5 rounded-lg text-xs font-bold text-slate-400 hover:text-white transition">
            Level 3: Applied Mastery
          </button>
        </div>
      </div>

      <div id="conceptTierContainer" class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Injected via renderConceptHub() -->
      </div>

    </section>

    <!-- TAB 2: DECIMAL GRIDS & SLIDER (CLUSTER 1) -->
    <section id="panel-decimals" class="tab-panel space-y-6">
      
      <div class="flex items-center justify-between flex-wrap gap-4 border-b border-slate-800 pb-4">
        <div>
          <span class="text-xs font-bold text-sky-400 tracking-wider uppercase">Cluster 1 Laboratory • NC.4.NF.6 & NC.4.NF.7</span>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white">Dual 10×10 Decimal Grids & Synchronized Slider</h2>
          <p class="text-xs sm:text-sm text-slate-400">Explore how 1 tenth equals 10 hundredths, add tenths and hundredths, and compare decimal magnitudes relative to 1 whole.</p>
        </div>
        <button onclick="resetDecimalLab()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition">
          ↺ Reset Lab
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Left: Side-by-Side Dual 10x10 Grids -->
        <div class="lg:col-span-7 glass-card rounded-2xl p-5 space-y-5">
          <div class="flex items-center justify-between">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>Dual Synchronized Decimal Grids</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 mono">Interactive Visual Model</span>
            </h3>
            <span class="text-xs text-slate-400">Click columns or squares to shade</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            
            <!-- Tenths Grid (10 Columns) -->
            <div class="p-3.5 bg-slate-900 rounded-xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-sky-300">Tenths Grid (10 Columns)</span>
                <span id="tenthsReadout" class="text-xs font-mono font-bold text-sky-400">4/10 = 0.4</span>
              </div>
              <div id="tenthsGridContainer" class="w-full aspect-square border-2 border-sky-500/50 rounded-lg grid grid-cols-10 gap-0.5 p-1 bg-slate-950">
                <!-- 10 columns injected via JS -->
              </div>
              <div class="flex items-center justify-between text-[11px] text-slate-400">
                <span>Shaded: <strong id="tenthsCountText" class="text-white">4</strong> / 10 columns</span>
                <button onclick="shadeTenths(0)" class="text-sky-400 hover:underline">Clear</button>
              </div>
            </div>

            <!-- Hundredths Grid (100 Squares) -->
            <div class="p-3.5 bg-slate-900 rounded-xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-amber-300">Hundredths Grid (100 Squares)</span>
                <span id="hundredthsReadout" class="text-xs font-mono font-bold text-amber-400">40/100 = 0.40</span>
              </div>
              <div id="hundredthsGridContainer" class="w-full aspect-square border-2 border-amber-500/50 rounded-lg grid grid-cols-10 gap-0.5 p-1 bg-slate-950">
                <!-- 100 squares injected via JS -->
              </div>
              <div class="flex items-center justify-between text-[11px] text-slate-400">
                <span>Shaded: <strong id="hundredthsCountText" class="text-white">40</strong> / 100 squares</span>
                <button onclick="shadeHundredths(0)" class="text-amber-400 hover:underline">Clear</button>
              </div>
            </div>

          </div>

          <!-- Equivalence Telemetry Banner -->
          <div class="p-4 bg-gradient-to-r from-sky-950/60 via-slate-900 to-amber-950/60 rounded-xl border border-slate-700/80 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-3">
              <span class="text-2xl">⚖️</span>
              <div>
                <span class="text-xs font-bold text-slate-300">Visual Decimal Equivalence Engine</span>
                <p id="equivalenceEquation" class="text-sm font-mono font-bold text-white">
                  4/10 = 40/100 ↔ 0.4 = 0.40
                </p>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <button onclick="applyPresetDecimal(0.5)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300">0.5 = 1/2</button>
              <button onclick="applyPresetDecimal(0.75)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300">0.75 = 3/4</button>
              <button onclick="applyPresetDecimal(0.25)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300">0.25 = 1/4</button>
            </div>
          </div>

        </div>

        <!-- Right: Continuous Number Line Slider & Snapping -->
        <div class="lg:col-span-5 glass-card rounded-2xl p-5 space-y-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>Fraction-Decimal Number Line</span>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 mono">0 to 1</span>
              </h3>
              <span id="sliderValueBadge" class="text-xs font-mono font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30">0.50</span>
            </div>

            <!-- Number Line Display SVG -->
            <div class="w-full bg-slate-900 rounded-xl p-4 border border-slate-800">
              <svg id="decimalNumberLineSvg" viewBox="0 0 400 120" class="w-full h-auto">
                <!-- Rendered dynamically via renderDecimalNumberLine() -->
              </svg>
            </div>

            <!-- Interactive Slider Controls -->
            <div class="mt-4 space-y-2">
              <div class="flex items-center justify-between text-xs text-slate-400">
                <span>0.00 (0/10)</span>
                <span class="text-amber-400 font-semibold">Drag handle to snap to benchmarks</span>
                <span>1.00 (10/10)</span>
              </div>
              <input type="range" id="decimalSlider" min="0" max="100" value="50" step="1" oninput="onDecimalSliderInput(this.value)" class="w-full accent-sky-400 cursor-pointer h-2 bg-slate-800 rounded-lg" />
            </div>

            <!-- Benchmark Snapping Cards -->
            <div class="grid grid-cols-3 gap-2 mt-4">
              <button onclick="setSliderBenchmark(0.25)" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-800 text-center transition">
                <span class="text-[11px] block text-slate-400">Quarter</span>
                <span class="text-xs font-bold text-sky-400 mono">0.25 = 1/4</span>
              </button>
              <button onclick="setSliderBenchmark(0.50)" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-800 text-center transition">
                <span class="text-[11px] block text-slate-400">Halfway</span>
                <span class="text-xs font-bold text-emerald-400 mono">0.50 = 1/2</span>
              </button>
              <button onclick="setSliderBenchmark(0.75)" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-800 text-center transition">
                <span class="text-[11px] block text-slate-400">Three-Quarters</span>
                <span class="text-xs font-bold text-purple-400 mono">0.75 = 3/4</span>
              </button>
            </div>
          </div>

          <!-- Misconception Callout Alert -->
          <div class="p-3.5 bg-amber-500/10 rounded-xl border border-amber-500/30 text-xs text-amber-200 flex items-start gap-2.5">
            <span class="text-base shrink-0">💡</span>
            <div>
              <strong class="font-bold text-amber-300">Watch Out for Whole-Number Bias!</strong>
              <p class="text-[11px] text-amber-200/90 mt-0.5">
                Students often think 0.17 > 0.9 because 17 > 9. But 0.9 is 9 full columns (90 hundredths), while 0.17 is only 17 little squares. 0.9 > 0.17!
              </p>
            </div>
          </div>

        </div>

      </div>

    </section>

    <!-- TAB 3: OPERATIONS & PLACE VALUE (CLUSTER 2) -->
    <section id="panel-operations" class="tab-panel hidden space-y-6">
      
      <div class="flex items-center justify-between flex-wrap gap-4 border-b border-slate-800 pb-4">
        <div>
          <span class="text-xs font-bold text-emerald-400 tracking-wider uppercase">Cluster 2 Laboratory • NC.4.NBT.1, 5, 6 & NC.4.OA</span>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white">Place Value 10× Magnifier & Partial Products Studio</h2>
          <p class="text-xs sm:text-sm text-slate-400">Understand that shifting one place left multiplies value by 10, solve multi-digit multiplication with area models, and explore division with remainders.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Top/Left: 10x Place Value Chart with Magnification Animation -->
        <div class="lg:col-span-12 glass-card rounded-2xl p-5 space-y-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>Interactive 10× Place Value Magnifier</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 mono">NC.4.NBT.1</span>
            </h3>
            <span class="text-xs text-slate-400">Click any digit box to trigger 10× left shift animation</span>
          </div>

          <div class="grid grid-cols-5 gap-2 sm:gap-3 text-center">
            <div onclick="shiftPlaceValue(4)" id="pvCol4" class="p-3 bg-slate-900 rounded-xl border border-slate-800 hover:border-sky-400 transition cursor-pointer">
              <span class="text-[11px] text-slate-400 block font-semibold">Ten-Thousands</span>
              <span id="pvVal4" class="text-lg sm:text-2xl font-extrabold text-indigo-400 mono block my-1">40,000</span>
              <span class="text-[10px] text-slate-500">10,000s place</span>
            </div>
            <div onclick="shiftPlaceValue(3)" id="pvCol3" class="p-3 bg-slate-900 rounded-xl border border-sky-500/60 bg-sky-950/20 transition cursor-pointer">
              <span class="text-[11px] text-slate-400 block font-semibold">Thousands</span>
              <span id="pvVal3" class="text-lg sm:text-2xl font-extrabold text-sky-400 mono block my-1">4,000</span>
              <span class="text-[10px] text-slate-500">1,000s place</span>
            </div>
            <div onclick="shiftPlaceValue(2)" id="pvCol2" class="p-3 bg-slate-900 rounded-xl border border-slate-800 hover:border-emerald-400 transition cursor-pointer">
              <span class="text-[11px] text-slate-400 block font-semibold">Hundreds</span>
              <span id="pvVal2" class="text-lg sm:text-2xl font-extrabold text-emerald-400 mono block my-1">400</span>
              <span class="text-[10px] text-slate-500">100s place</span>
            </div>
            <div onclick="shiftPlaceValue(1)" id="pvCol1" class="p-3 bg-slate-900 rounded-xl border border-slate-800 hover:border-amber-400 transition cursor-pointer">
              <span class="text-[11px] text-slate-400 block font-semibold">Tens</span>
              <span id="pvVal1" class="text-lg sm:text-2xl font-extrabold text-amber-400 mono block my-1">40</span>
              <span class="text-[10px] text-slate-500">10s place</span>
            </div>
            <div onclick="shiftPlaceValue(0)" id="pvCol0" class="p-3 bg-slate-900 rounded-xl border border-slate-800 hover:border-rose-400 transition cursor-pointer">
              <span class="text-[11px] text-slate-400 block font-semibold">Ones</span>
              <span id="pvVal0" class="text-lg sm:text-2xl font-extrabold text-rose-400 mono block my-1">4</span>
              <span class="text-[10px] text-slate-500">1s place</span>
            </div>
          </div>

          <!-- Interactive Magnification Zoom Display -->
          <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-sky-500/20 border border-sky-500/40 flex items-center justify-center text-lg">🔍</div>
              <div>
                <span class="text-xs font-bold text-sky-300">Positional Shift Rule (10× Relationship)</span>
                <p id="pvShiftExplanation" class="text-sm text-slate-200 font-mono mt-0.5">
                  4 in Thousands place (4,000) = 4 in Hundreds place (400) × 10
                </p>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <button onclick="shiftDigitLeft()" class="px-3 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-xs font-bold text-white transition flex items-center gap-1">
                <span>← Shift Left (×10)</span>
              </button>
              <button onclick="shiftDigitRight()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 transition flex items-center gap-1">
                <span>Shift Right (÷10) →</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Dynamic Area Model Generator for Multiplication -->
        <div class="lg:col-span-7 glass-card rounded-2xl p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>Dynamic Area Model Generator</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 mono">NC.4.NBT.5</span>
            </h3>
            <div class="flex items-center gap-2">
              <button onclick="setAreaModelMode('4x1')" id="btn4x1" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white transition">4-Digit × 1-Digit</button>
              <button onclick="setAreaModelMode('2x2')" id="btn2x2" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:text-white transition">2-Digit × 2-Digit (Q3 Extension)</button>
            </div>
          </div>

          <!-- Factor Inputs -->
          <div class="flex items-center gap-3 p-3 bg-slate-900 rounded-xl border border-slate-800">
            <div class="flex items-center gap-2">
              <label class="text-xs text-slate-400 font-semibold">Factor 1:</label>
              <input type="number" id="areaFactor1" value="312" min="10" max="9999" onchange="updateAreaModelVisual()" class="w-24 px-2 py-1 bg-slate-950 border border-slate-700 rounded-lg text-xs font-mono font-bold text-white" />
            </div>
            <span class="text-slate-500 font-bold">×</span>
            <div class="flex items-center gap-2">
              <label class="text-xs text-slate-400 font-semibold">Factor 2:</label>
              <input type="number" id="areaFactor2" value="4" min="1" max="99" onchange="updateAreaModelVisual()" class="w-16 px-2 py-1 bg-slate-950 border border-slate-700 rounded-lg text-xs font-mono font-bold text-white" />
            </div>
            <button onclick="updateAreaModelVisual()" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white rounded-lg transition ml-auto">
              Calculate Model
            </button>
          </div>

          <!-- Dynamic SVG Area Model Canvas -->
          <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <svg id="areaModelSvg" viewBox="0 0 500 200" class="w-full h-auto">
              <!-- Rendered via renderAreaModelSvg() -->
            </svg>
          </div>

          <div id="areaModelSumBreakdown" class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300">
            Total Product: (300 × 4 = 1,200) + (10 × 4 = 40) + (2 × 4 = 8) = 1,248
          </div>
        </div>

        <!-- Partial Quotients & Remainder Visualizer -->
        <div class="lg:col-span-5 glass-card rounded-2xl p-5 space-y-4 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>Partial Quotients & Remainders</span>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 mono">NC.4.NBT.6</span>
              </h3>
              <span class="text-xs font-mono text-purple-400 font-bold">158 ÷ 4</span>
            </div>

            <!-- Division Workspace Interactive Card -->
            <div class="p-4 bg-slate-900 rounded-xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Dividend: <strong class="text-white mono">158</strong></span>
                <span>Divisor: <strong class="text-purple-400 mono">4</strong></span>
              </div>

              <!-- Step 1 Chunk -->
              <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 flex items-center justify-between text-xs font-mono">
                <div>
                  <span class="text-slate-400">Step 1: 4 × 30</span>
                  <span class="text-rose-400 block">- 120</span>
                </div>
                <div class="text-right">
                  <span class="text-slate-400">Remaining</span>
                  <span class="text-white font-bold block">38</span>
                </div>
                <span class="px-2 py-1 bg-purple-500/20 text-purple-300 rounded font-bold">+30</span>
              </div>

              <!-- Step 2 Chunk -->
              <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 flex items-center justify-between text-xs font-mono">
                <div>
                  <span class="text-slate-400">Step 2: 4 × 9</span>
                  <span class="text-rose-400 block">- 36</span>
                </div>
                <div class="text-right">
                  <span class="text-slate-400">Remaining</span>
                  <span class="text-amber-400 font-bold block">2</span>
                </div>
                <span class="px-2 py-1 bg-purple-500/20 text-purple-300 rounded font-bold">+9</span>
              </div>

              <!-- Final Quotient Result -->
              <div class="p-3 bg-purple-950/40 rounded-xl border border-purple-500/40 flex items-center justify-between">
                <span class="text-xs font-bold text-purple-200">Total Quotient:</span>
                <span class="text-sm font-mono font-extrabold text-white">39 with Remainder 2 (39 R 2)</span>
              </div>
            </div>
          </div>

          <div class="p-3 bg-purple-500/10 rounded-xl border border-purple-500/30 text-xs text-purple-200">
            <strong>Contextual Remainder Tip:</strong> In real-world problems like renting 8-passenger vans for 125 students, 125 ÷ 8 = 15 R 5. You must round UP to 16 vans so no student is left behind!
          </div>
        </div>

      </div>

    </section>

    <!-- TAB 4: MEASUREMENT & LINE PLOTS (CLUSTER 3) -->
    <section id="panel-measurement" class="tab-panel hidden space-y-6">
      
      <div class="flex items-center justify-between flex-wrap gap-4 border-b border-slate-800 pb-4">
        <div>
          <span class="text-xs font-bold text-amber-400 tracking-wider uppercase">Cluster 3 Laboratory • NC.4.MD.1, 2, 3, 4</span>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white">Rectilinear Decomposer & Fractional Line Plot Studio</h2>
          <p class="text-xs sm:text-sm text-slate-400">Decompose L-shaped rooms into non-overlapping rectangles, analyze fractional measurement data on line plots, and calculate elapsed time across hour marks.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Left: Rectilinear Decomposition & Area/Perimeter Grid -->
        <div class="lg:col-span-6 glass-card rounded-2xl p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>L-Shaped Rectilinear Decomposition</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 mono">NC.4.MD.3</span>
            </h3>
            <button onclick="toggleRectilinearDecomp()" id="btnDecompToggle" class="px-2.5 py-1 bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white rounded-lg transition">
              Slice into Rect A & B
            </button>
          </div>

          <!-- Rectilinear Interactive SVG -->
          <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <svg id="rectilinearSvg" viewBox="0 0 400 220" class="w-full h-auto">
              <!-- Rendered dynamically via renderRectilinearSvg() -->
            </svg>
          </div>

          <div id="rectilinearReadout" class="p-3.5 bg-slate-900 rounded-xl border border-slate-800 space-y-2 text-xs">
            <div class="flex items-center justify-between">
              <span class="text-slate-400">Rectangle A (Top/Left):</span>
              <span class="text-white font-mono font-bold">6 m × 4 m = 24 m²</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-slate-400">Rectangle B (Right):</span>
              <span class="text-white font-mono font-bold">3 m × 2 m = 6 m²</span>
            </div>
            <div class="border-t border-slate-800 pt-2 flex items-center justify-between text-sm font-bold text-amber-300 font-mono">
              <span>Total Combined Area:</span>
              <span>24 + 6 = 30 m²</span>
            </div>
          </div>
        </div>

        <!-- Right: Fractional Line Plot Builder (NC.4.MD.4) -->
        <div class="lg:col-span-6 glass-card rounded-2xl p-5 space-y-4 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>Fractional Line Plot Studio</span>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 mono">Eighths (1/8 in)</span>
              </h3>
              <button onclick="resetLinePlotData()" class="text-xs text-sky-400 hover:underline">Reset Data</button>
            </div>

            <!-- Line Plot SVG -->
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
              <svg id="fractionalLinePlotSvg" viewBox="0 0 400 160" class="w-full h-auto">
                <!-- Rendered dynamically via renderLinePlotSvg() -->
              </svg>
            </div>

            <!-- Seedling Data Interactive Buttons -->
            <div class="mt-4 space-y-2">
              <span class="text-xs font-bold text-slate-300 block">Tap to Add Measurement Data Point (X):</span>
              <div class="flex flex-wrap gap-1.5">
                <button onclick="addLinePlotPoint(0.125)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 1/8 in</button>
                <button onclick="addLinePlotPoint(0.25)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 2/8 (1/4)</button>
                <button onclick="addLinePlotPoint(0.375)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 3/8 in</button>
                <button onclick="addLinePlotPoint(0.5)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 4/8 (1/2)</button>
                <button onclick="addLinePlotPoint(0.625)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 5/8 in</button>
                <button onclick="addLinePlotPoint(0.75)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 6/8 (3/4)</button>
                <button onclick="addLinePlotPoint(0.875)" class="px-2 py-1 bg-slate-900 hover:bg-slate-800 text-[11px] font-mono rounded border border-slate-700 text-sky-300">+ 7/8 in</button>
              </div>
            </div>
          </div>

          <div id="linePlotDifferenceReadout" class="p-3 bg-emerald-950/40 rounded-xl border border-emerald-500/40 text-xs text-emerald-200 flex items-center justify-between">
            <span>Range Analysis:</span>
            <span class="font-mono font-bold text-white">Longest (7/8) - Shortest (2/8) = 5/8 inch</span>
          </div>
        </div>

        <!-- Bottom: Elapsed Time Timeline Jumper (10:45 AM -> 1:15 PM) -->
        <div class="lg:col-span-12 glass-card rounded-2xl p-5 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>Open Timeline Elapsed Time Jumper</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-rose-500/20 text-rose-300 mono">Base-60 Hours</span>
            </h3>
            <span class="text-xs text-slate-400">Practice: 10:45 AM to 1:15 PM</span>
          </div>

          <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <svg id="elapsedTimeSvg" viewBox="0 0 600 130" class="w-full h-auto">
              <!-- Rendered dynamically via renderElapsedTimeSvg() -->
            </svg>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center">
            <div class="p-2.5 bg-slate-900 rounded-xl border border-slate-800">
              <span class="text-[11px] text-slate-400 block font-semibold">Jump 1 (To next hour)</span>
              <span class="text-sm font-bold text-sky-400 mono block mt-0.5">+15 minutes</span>
              <span class="text-[10px] text-slate-500">10:45 AM -> 11:00 AM</span>
            </div>
            <div class="p-2.5 bg-slate-900 rounded-xl border border-slate-800">
              <span class="text-[11px] text-slate-400 block font-semibold">Jump 2 (Hour interval)</span>
              <span class="text-sm font-bold text-emerald-400 mono block mt-0.5">+2 full hours</span>
              <span class="text-[10px] text-slate-500">11:00 AM -> 1:00 PM</span>
            </div>
            <div class="p-2.5 bg-slate-900 rounded-xl border border-slate-800">
              <span class="text-[11px] text-slate-400 block font-semibold">Jump 3 (Remaining)</span>
              <span class="text-sm font-bold text-amber-400 mono block mt-0.5">+15 minutes</span>
              <span class="text-[10px] text-slate-500">1:00 PM -> 1:15 PM</span>
            </div>
          </div>

          <div class="p-3 bg-rose-950/40 rounded-xl border border-rose-500/40 text-xs flex items-center justify-between text-rose-200">
            <span>Total Duration Calculation:</span>
            <span class="font-mono font-bold text-white text-sm">2 hours + 15 min + 15 min = 2 hours 30 minutes (150 minutes)</span>
          </div>
        </div>

      </div>

    </section>

    <!-- TAB 5: 60-QUESTION MASTERY QUEST -->
    <section id="panel-challenge" class="tab-panel hidden space-y-6">
      
      <!-- Quest Top Navigation HUD -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">CMS Q2 Adaptive Quest</span>
            <span id="currentClusterBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 font-mono">Cluster 1</span>
            <span id="currentTierBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-mono">Easy Tier</span>
          </div>
          <div class="flex items-center gap-3 mt-1">
            <h2 id="qNumberHeading" class="text-lg sm:text-xl font-extrabold text-white">Question 1 of 60</h2>
            <span id="qStandardTag" class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono border border-slate-700">NC.4.NF.6</span>
          </div>
        </div>

        <!-- Telemetry Gauges -->
        <div class="flex items-center gap-3 sm:gap-4 flex-wrap">
          
          <!-- Timer -->
          <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800">
            <span class="text-sm">⏱️</span>
            <div>
              <span class="text-[10px] block text-slate-400">Time</span>
              <span id="timerDisplay" class="text-xs font-mono font-bold text-white">45s</span>
            </div>
            <button onclick="toggleTimerPause()" id="pauseTimerBtn" class="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 hover:text-white" title="Pause / Zen Mode">⏸</button>
          </div>

          <!-- Streak Multiplier -->
          <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800">
            <span class="text-sm">🔥</span>
            <div>
              <span class="text-[10px] block text-slate-400">Streak</span>
              <span id="streakDisplay" class="text-xs font-mono font-bold text-amber-400">0× (1.0x)</span>
            </div>
          </div>

          <!-- Score -->
          <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800">
            <span class="text-sm">⭐</span>
            <div>
              <span class="text-[10px] block text-slate-400">Score</span>
              <span id="scoreDisplay" class="text-xs font-mono font-bold text-emerald-400">0 pts</span>
            </div>
          </div>

        </div>

      </div>

      <!-- Question Main Presentation Card -->
      <div class="glass-card rounded-2xl p-5 sm:p-7 space-y-6">
        
        <!-- Question Prompt Text -->
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <span id="qFormatTag" class="text-[11px] font-semibold text-slate-400 uppercase tracking-wide">Multiple Choice</span>
            <button onclick="readActiveQuestionAloud()" class="text-xs font-semibold text-sky-400 hover:text-sky-300 flex items-center gap-1">
              <span>🔊 Read Aloud</span>
            </button>
          </div>
          <p id="questionPromptText" class="text-base sm:text-lg font-medium text-slate-100 leading-relaxed">
            Loading question...
          </p>
        </div>

        <!-- Interactive Question Workspace Container (MC, Visual, Numberline, Drag-and-Drop) -->
        <div id="questionWorkspaceContainer" class="p-4 bg-slate-950/70 rounded-2xl border border-slate-800/80 min-h-[160px]">
          <!-- Rendered dynamically by format -->
        </div>

        <!-- Action Controls -->
        <div class="flex items-center justify-between flex-wrap gap-3 pt-3 border-t border-slate-800/80">
          <div class="flex items-center gap-2">
            <button onclick="requestSocraticHint()" id="btnSocraticHint" class="px-3 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-xs font-bold text-amber-300 border border-amber-500/40 flex items-center gap-1.5 transition">
              <span>💡 Socratic Hint</span>
              <span id="hintsRemainingBadge" class="text-[10px] px-1.5 py-0.2 rounded bg-amber-500/30 text-amber-200">3 left</span>
            </button>
            <button onclick="toggleScratchpad()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 flex items-center gap-1.5 transition">
              <span>✏️ Whiteboard</span>
            </button>
          </div>

          <div class="flex items-center gap-2">
            <button onclick="submitActiveAnswer()" id="btnSubmitAnswer" class="px-6 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs sm:text-sm font-bold text-white shadow-lg shadow-emerald-500/25 transition hover:scale-[1.02] flex items-center gap-2">
              <span>Check Answer</span>
              <span>✓</span>
            </button>
          </div>
        </div>

        <!-- Progressive Hint Drawer Inline Box -->
        <div id="hintDisplayBox" class="hidden p-4 bg-amber-950/30 rounded-xl border border-amber-500/40 space-y-1.5 text-xs text-amber-200">
          <div class="flex items-center gap-2 font-bold text-amber-300">
            <span>💡 Pip's Socratic Nudge:</span>
            <span id="hintStageBadge" class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/30 font-mono">Hint 1/3</span>
          </div>
          <p id="hintTextContent">Think about place values...</p>
        </div>

        <!-- 4-Step Solution Breakdown (Displayed upon answer commit) -->
        <div id="solutionBreakdownBox" class="hidden p-5 bg-slate-900 rounded-2xl border border-slate-700 space-y-4">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
              <span id="solutionResultIcon" class="text-xl">✅</span>
              <h3 id="solutionResultTitle" class="text-sm font-extrabold text-white">Verified 4-Step Solution Model</h3>
            </div>
            <span id="solutionStandardLabel" class="text-xs font-mono text-slate-400">NC.4.NF.6</span>
          </div>

          <!-- Verified Answer Display Card (Replaces raw JSON) -->
          <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/40 flex items-start gap-3">
            <span class="text-lg">🎯</span>
            <div>
              <span class="text-[11px] font-bold text-emerald-300 block uppercase tracking-wider">Verified Correct Answer:</span>
              <span id="verifiedAnswerText" class="text-sm font-bold text-white block mt-0.5 font-mono">
                0.7 (7 tenths)
              </span>
            </div>
          </div>

          <!-- Visual Solution Model SVG Diagram -->
          <div id="visualSolutionModelContainer" class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <!-- Dynamic SVG diagram rendered by renderVisualSolutionModel() -->
          </div>

          <!-- 4-Step Pedagogical Logic -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
              <span class="font-bold text-sky-400 block mb-1">Step 1: Understand the Goal</span>
              <p id="solStep1Text" class="text-slate-300">Identify the required rational or operational target.</p>
            </div>
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
              <span class="font-bold text-amber-400 block mb-1">Step 2: Construct the Visual Model</span>
              <p id="solStep2Text" class="text-slate-300">Partition by place-value grids, partial products, or intervals.</p>
            </div>
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
              <span class="font-bold text-emerald-400 block mb-1">Step 3: Solve with Operation</span>
              <p id="solStep3Text" class="text-slate-300">Execute calculation ensuring common denominators or place values.</p>
            </div>
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
              <span class="font-bold text-purple-400 block mb-1">Step 4: Verify & Check Real Reasonableness</span>
              <p id="solStep4Text" class="text-slate-300">Compare with benchmarks and check real-world validity.</p>
            </div>
          </div>

          <div class="flex justify-end pt-2">
            <button onclick="advanceToNextQuestion()" class="px-6 py-2.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-xs sm:text-sm font-bold text-white shadow-lg shadow-sky-500/25 transition hover:scale-[1.02] flex items-center gap-2">
              <span>Next Question</span>
              <span>→</span>
            </button>
          </div>
        </div>

      </div>

    </section>

    <!-- TAB 6: RADAR & DASHBOARD -->
    <section id="panel-dashboard" class="tab-panel hidden space-y-6">
      
      <div class="flex items-center justify-between flex-wrap gap-4 border-b border-slate-800 pb-4">
        <div>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white">Mastery Analytics & Performance Radar</h2>
          <p class="text-xs sm:text-sm text-slate-400">Real-time mastery tracking across CMS Quarter 2 Standards and Misconception Remediation History</p>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="retryMissedQuestions()" id="btnRetryMissed" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white transition flex items-center gap-1.5 shadow-sm">
            <span>↺ Retry Missed Items</span>
            <span id="missedCountBadge" class="text-[10px] px-1.5 py-0.2 rounded bg-amber-900/60 mono">0</span>
          </button>
          <button onclick="restartChallenge()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition">
            Restart Quest
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Score & Completion Card -->
        <div class="glass-card rounded-2xl p-5 space-y-4 text-center flex flex-col justify-center">
          <div class="w-20 h-20 mx-auto rounded-full bg-gradient-to-tr from-sky-500 to-emerald-400 p-1 flex items-center justify-center shadow-lg">
            <div class="w-full h-full bg-slate-900 rounded-full flex flex-col items-center justify-center">
              <span id="dashAccuracyPercent" class="text-2xl font-extrabold text-white mono">0%</span>
              <span class="text-[10px] text-slate-400">Accuracy</span>
            </div>
          </div>
          <div>
            <h3 class="text-base font-bold text-white">Quarter 2 Assessment Status</h3>
            <p id="dashCompletionText" class="text-xs text-slate-400 mt-1">0 of 60 questions completed</p>
          </div>
        </div>

        <!-- Cluster Mastery Breakdown -->
        <div class="glass-card rounded-2xl p-5 space-y-3 md:col-span-2">
          <h3 class="text-sm font-bold text-white">Cluster Mastery Breakdown</h3>
          
          <div class="space-y-3">
            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="text-sky-300 font-semibold">Cluster 1: Fractions Continuation & Decimals (NC.4.NF.1, 2, 3, 6, 7)</span>
                <span id="c1PercentText" class="mono text-slate-400">0%</span>
              </div>
              <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden border border-slate-800">
                <div id="c1ProgressBar" class="h-full bg-sky-500 transition-all duration-500" style="width: 0%"></div>
              </div>
            </div>

            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="text-emerald-300 font-semibold">Cluster 2: Multi-Digit Operations & 10× Place Value (NC.4.NBT & OA)</span>
                <span id="c2PercentText" class="mono text-slate-400">0%</span>
              </div>
              <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden border border-slate-800">
                <div id="c2ProgressBar" class="h-full bg-emerald-500 transition-all duration-500" style="width: 0%"></div>
              </div>
            </div>

            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="text-amber-300 font-semibold">Cluster 3: Area, Perimeter, Measurement & Data (NC.4.MD)</span>
                <span id="c3PercentText" class="mono text-slate-400">0%</span>
              </div>
              <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden border border-slate-800">
                <div id="c3ProgressBar" class="h-full bg-amber-500 transition-all duration-500" style="width: 0%"></div>
              </div>
            </div>
          </div>
        </div>

      </div>

    </section>

  </main>

  <!-- MISCONCEPTION REMEDIATION SLIDE-UP DRAWER -->
  <div id="misconceptionDrawer" class="fixed bottom-0 left-0 right-0 z-50 bg-slate-900/95 backdrop-blur-xl border-t-2 border-amber-500 shadow-2xl p-5 sm:p-6 max-h-[85vh] overflow-y-auto">
    <div class="max-w-4xl mx-auto space-y-4">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-lg">💡</div>
          <div>
            <h3 class="text-sm font-bold text-amber-300">Targeted Conceptual Remediation Drawer</h3>
            <span id="drawerMisconceptionTitle" class="text-xs text-slate-300 font-mono">Misconception: Decimal Bias</span>
          </div>
        </div>
        <button onclick="closeMisconceptionDrawer()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 transition">
          ✕ Return to Quest
        </button>
      </div>

      <!-- Interactive Mini-Intervention Diagram -->
      <div id="drawerVisualCanvas" class="p-3 bg-slate-950 rounded-xl border border-slate-800">
        <!-- Injected diagram -->
      </div>

      <div class="p-4 bg-amber-950/20 rounded-xl border border-amber-500/30 text-xs text-amber-200 space-y-1">
        <strong class="font-bold text-amber-300">Why this happens:</strong>
        <p id="drawerDiagnosticExplanation" class="text-slate-300 leading-relaxed">
          Students frequently compare decimals using whole-number rules...
        </p>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 bg-slate-950 py-4 text-center text-xs text-slate-500">
    CMS Quarter 2 Mathematics Laboratory • Aligned with NC Standard Course of Study & Illustrative Mathematics
  </footer>

  <!-- Application Logic & State Engine -->
  <script>
    // 60 Graded Questions embedded
    const ALL_QUESTIONS = {questions_json};

    // State Variables
    let currentTab = 'decimals';
    let currentTier = 1;
    let activeChallengeQuestions = [...ALL_QUESTIONS];
    let currentQuestionIndex = 0;
    let selectedAnswerState = null;
    let userScore = 0;
    let userStreak = 0;
    let timerSeconds = 45;
    let timerInterval = null;
    let timerPaused = false;
    let questionsAnsweredCount = 0;
    let missedQuestions = [];
    let audioMuted = false;
    let audioCtx = null;
    let hintsUsedForActiveQ = 0;

    // Web Audio API Synthesizer
    function getAudioContext() {{
      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }}
      return audioCtx;
    }}

    function playSound(type) {{
      if (audioMuted) return;
      try {{
        const ctx = getAudioContext();
        if (ctx.state === 'suspended') ctx.resume();

        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        const now = ctx.currentTime;

        if (type === 'click') {{
          osc.type = 'sine';
          osc.frequency.setValueAtTime(440, now);
          osc.frequency.exponentialRampToValueAtTime(880, now + 0.05);
          gain.gain.setValueAtTime(0.15, now);
          gain.gain.linearRampToValueAtTime(0.01, now + 0.05);
          osc.start(now);
          osc.stop(now + 0.05);
        }} else if (type === 'correct') {{
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(523.25, now); // C5
          osc.frequency.setValueAtTime(659.25, now + 0.08); // E5
          osc.frequency.setValueAtTime(783.99, now + 0.16); // G5
          osc.frequency.setValueAtTime(1046.50, now + 0.24); // C6
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.linearRampToValueAtTime(0.01, now + 0.35);
          osc.start(now);
          osc.stop(now + 0.35);
        }} else if (type === 'incorrect') {{
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, now);
          osc.frequency.linearRampToValueAtTime(160, now + 0.2);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.linearRampToValueAtTime(0.01, now + 0.25);
          osc.start(now);
          osc.stop(now + 0.25);
        }}
      }} catch (e) {{
        console.warn('Audio synthesis note:', e);
      }}
    }}

    function toggleAudioMute() {{
      audioMuted = !audioMuted;
      document.getElementById('audioMuteIcon').textContent = audioMuted ? '🔇' : '🔊';
    }}

    // Text to Speech
    function speakText(text) {{
      if ('speechSynthesis' in window) {{
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 0.95;
        utterance.pitch = 1.05;
        window.speechSynthesis.speak(utterance);
      }}
    }}

    function speakMascotMessage() {{
      const msg = document.getElementById('mascotSpeechText').textContent;
      speakText(msg);
    }}

    function readActiveQuestionAloud() {{
      const q = activeChallengeQuestions[currentQuestionIndex];
      if (q) speakText(q.question);
    }}

    // Tab Switching
    function switchTab(tabId) {{
      playSound('click');
      currentTab = tabId;

      document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('tab-active'));

      const targetPanel = document.getElementById('panel-' + tabId);
      if (targetPanel) targetPanel.classList.remove('hidden');

      const targetBtn = document.getElementById('tab-' + tabId);
      if (targetBtn) targetBtn.classList.add('tab-active');

      if (tabId === 'concept') renderConceptHub();
      if (tabId === 'challenge') loadQuestion(currentQuestionIndex);
      if (tabId === 'dashboard') updateDashboard();
    }}

    // Theme & Accessibility Toggles
    function toggleTheme() {{
      document.body.classList.toggle('theme-light');
    }}
    function toggleDyslexiaMode() {{
      document.body.classList.toggle('dyslexia-mode');
    }}

    // Interactive Whiteboard Scratchpad
    let wbCanvas, wbCtx, isDrawing = false, wbTool = 'pen', wbColor = '#38bdf8', wbActive = false;

    function initScratchpad() {{
      wbCanvas = document.getElementById('scratchpadCanvas');
      wbCtx = wbCanvas.getContext('2d');
      resizeWbCanvas();
      window.addEventListener('resize', resizeWbCanvas);

      wbCanvas.addEventListener('mousedown', startDrawing);
      wbCanvas.addEventListener('mousemove', draw);
      wbCanvas.addEventListener('mouseup', stopDrawing);
      wbCanvas.addEventListener('mouseout', stopDrawing);

      wbCanvas.addEventListener('touchstart', (e) => {{
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousedown', {{ clientX: touch.clientX, clientY: touch.clientY }});
        wbCanvas.dispatchEvent(mouseEvent);
      }}, {{ passive: false }});

      wbCanvas.addEventListener('touchmove', (e) => {{
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousemove', {{ clientX: touch.clientX, clientY: touch.clientY }});
        wbCanvas.dispatchEvent(mouseEvent);
      }}, {{ passive: false }});

      wbCanvas.addEventListener('touchend', () => {{
        const mouseEvent = new MouseEvent('mouseup', {{}});
        wbCanvas.dispatchEvent(mouseEvent);
      }});
    }}

    function resizeWbCanvas() {{
      if (!wbCanvas) return;
      wbCanvas.width = window.innerWidth;
      wbCanvas.height = window.innerHeight;
    }}

    function toggleScratchpad() {{
      wbActive = !wbActive;
      const toolbar = document.getElementById('scratchpadToolbar');
      if (wbActive) {{
        wbCanvas.classList.add('active');
        toolbar.classList.add('visible');
      }} else {{
        wbCanvas.classList.remove('active');
        toolbar.classList.remove('visible');
      }}
    }}

    function setWbTool(tool) {{
      wbTool = tool;
      document.getElementById('wbPenBtn').classList.remove('bg-blue-600', 'text-white');
      document.getElementById('wbHighlighterBtn').classList.remove('bg-blue-600', 'text-white');
      document.getElementById('wbEraserBtn').classList.remove('bg-blue-600', 'text-white');

      if (tool === 'pen') document.getElementById('wbPenBtn').classList.add('bg-blue-600', 'text-white');
      if (tool === 'highlighter') document.getElementById('wbHighlighterBtn').classList.add('bg-blue-600', 'text-white');
      if (tool === 'eraser') document.getElementById('wbEraserBtn').classList.add('bg-blue-600', 'text-white');
    }}

    function setWbColor(color) {{
      wbColor = color;
      if (wbTool === 'eraser') setWbTool('pen');
    }}

    function clearScratchpad() {{
      if (wbCtx) wbCtx.clearRect(0, 0, wbCanvas.width, wbCanvas.height);
    }}

    function startDrawing(e) {{
      if (!wbActive) return;
      isDrawing = true;
      wbCtx.beginPath();
      wbCtx.moveTo(e.clientX, e.clientY);
    }}

    function draw(e) {{
      if (!isDrawing || !wbActive) return;
      if (wbTool === 'eraser') {{
        wbCtx.clearRect(e.clientX - 12, e.clientY - 12, 24, 24);
      }} else if (wbTool === 'highlighter') {{
        wbCtx.strokeStyle = wbColor + '55'; // Alpha transparency
        wbCtx.lineWidth = 16;
        wbCtx.lineCap = 'round';
        wbCtx.lineTo(e.clientX, e.clientY);
        wbCtx.stroke();
      }} else {{
        wbCtx.strokeStyle = wbColor;
        wbCtx.lineWidth = 3;
        wbCtx.lineCap = 'round';
        wbCtx.lineTo(e.clientX, e.clientY);
        wbCtx.stroke();
      }}
    }}

    function stopDrawing() {{
      isDrawing = false;
    }}

    // MANIPULATIVE 1: DUAL 10x10 DECIMAL GRIDS (CLUSTER 1)
    let shadedTenthsCount = 4;
    let shadedHundredthsCount = 40;

    function buildDecimalGrids() {{
      const tenthsContainer = document.getElementById('tenthsGridContainer');
      const hundredthsContainer = document.getElementById('hundredthsGridContainer');
      if (!tenthsContainer || !hundredthsContainer) return;

      tenthsContainer.innerHTML = '';
      hundredthsContainer.innerHTML = '';

      // 10 Columns
      for (let c = 0; c < 10; c++) {{
        const col = document.createElement('div');
        col.className = 'grid-tenth-col h-full rounded cursor-pointer border border-sky-500/20';
        col.id = 'tenthCol_' + c;
        col.onclick = () => onTenthColClick(c);
        tenthsContainer.appendChild(col);
      }}

      // 100 Squares
      for (let s = 0; s < 100; s++) {{
        const sq = document.createElement('div');
        sq.className = 'grid-hundredth-sq w-full h-full rounded-[2px] cursor-pointer border border-amber-500/20';
        sq.id = 'hundredthSq_' + s;
        sq.onclick = () => onHundredthSqClick(s);
        hundredthsContainer.appendChild(sq);
      }}

      updateDecimalGridsVisual();
    }}

    function onTenthColClick(colIndex) {{
      playSound('click');
      shadedTenthsCount = colIndex + 1;
      shadedHundredthsCount = shadedTenthsCount * 10;
      updateDecimalGridsVisual();
    }}

    function onHundredthSqClick(sqIndex) {{
      playSound('click');
      shadedHundredthsCount = sqIndex + 1;
      shadedTenthsCount = Math.floor(shadedHundredthsCount / 10);
      updateDecimalGridsVisual();
    }}

    function shadeTenths(n) {{
      shadedTenthsCount = n;
      shadedHundredthsCount = n * 10;
      updateDecimalGridsVisual();
    }}

    function shadeHundredths(n) {{
      shadedHundredthsCount = n;
      shadedTenthsCount = Math.floor(n / 10);
      updateDecimalGridsVisual();
    }}

    function applyPresetDecimal(val) {{
      playSound('click');
      shadedHundredthsCount = Math.round(val * 100);
      shadedTenthsCount = Math.floor(shadedHundredthsCount / 10);
      updateDecimalGridsVisual();
      setSliderBenchmark(val);
    }}

    function updateDecimalGridsVisual() {{
      for (let c = 0; c < 10; c++) {{
        const col = document.getElementById('tenthCol_' + c);
        if (col) {{
          if (c < shadedTenthsCount) {{
            col.style.backgroundColor = 'rgba(56, 189, 248, 0.7)';
          }} else {{
            col.style.backgroundColor = 'transparent';
          }}
        }}
      }}

      for (let s = 0; s < 100; s++) {{
        const sq = document.getElementById('hundredthSq_' + s);
        if (sq) {{
          if (s < shadedHundredthsCount) {{
            sq.style.backgroundColor = 'rgba(245, 158, 11, 0.7)';
          }} else {{
            sq.style.backgroundColor = 'transparent';
          }}
        }}
      }}

      const tDec = (shadedTenthsCount / 10).toFixed(1);
      const hDec = (shadedHundredthsCount / 100).toFixed(2);

      document.getElementById('tenthsReadout').textContent = `${{shadedTenthsCount}}/10 = ${{tDec}}`;
      document.getElementById('tenthsCountText').textContent = shadedTenthsCount;
      document.getElementById('hundredthsReadout').textContent = `${{shadedHundredthsCount}}/100 = ${{hDec}}`;
      document.getElementById('hundredthsCountText').textContent = shadedHundredthsCount;

      document.getElementById('equivalenceEquation').textContent = 
        `${{shadedTenthsCount}}/10 = ${{shadedTenthsCount * 10}}/100 ↔ ${{tDec}} = ${{(shadedTenthsCount * 10 / 100).toFixed(2)}} (Active Squares: ${{shadedHundredthsCount}})`;
    }}

    // MANIPULATIVE 2: NUMBER LINE SLIDER (CLUSTER 1)
    let currentSliderValue = 0.50;

    function renderDecimalNumberLine(val) {{
      const svg = document.getElementById('decimalNumberLineSvg');
      if (!svg) return;

      const w = 400, h = 120;
      const margin = 35;
      const lineY = 60;
      const lineW = w - margin * 2;

      let html = `
        <defs>
          <linearGradient id="nlGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#0284c7" />
            <stop offset="100%" stop-color="#10b981" />
          </linearGradient>
        </defs>
        <!-- Main Line -->
        <line x1="${{margin}}" y1="${{lineY}}" x2="${{w - margin}}" y2="${{lineY}}" stroke="#475569" stroke-width="3" stroke-linecap="round" />
      `;

      // 10 Tenths Marks
      for (let t = 0; t <= 10; t++) {{
        const x = margin + (t / 10) * lineW;
        html += `
          <line x1="${{x}}" y1="${{lineY - 14}}" x2="${{x}}" y2="${{lineY + 14}}" stroke="#94a3b8" stroke-width="1.8" />
          <text x="${{x}}" y="${{lineY - 20}}" fill="#38bdf8" font-size="9" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{t}}/10</text>
          <text x="${{x}}" y="${{lineY + 28}}" fill="#94a3b8" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">${{(t / 10).toFixed(1)}}</text>
        `;
      }}

      // Active Point P Handle
      const px = margin + val * lineW;
      html += `
        <!-- Shaded fill segment -->
        <line x1="${{margin}}" y1="${{lineY}}" x2="${{px}}" y2="${{lineY}}" stroke="url(#nlGrad)" stroke-width="4" />
        <!-- Point P Pin -->
        <circle cx="${{px}}" cy="${{lineY}}" r="7" fill="#fbbf24" stroke="#0f172a" stroke-width="2" />
        <rect x="${{px - 24}}" y="${{lineY - 45}}" width="48" height="20" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1.2" />
        <text x="${{px}}" y="${{lineY - 31}}" fill="#fbbf24" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">P: ${{val.toFixed(2)}}</text>
      `;

      svg.innerHTML = html;
    }}

    function onDecimalSliderInput(sliderVal) {{
      currentSliderValue = sliderVal / 100;
      document.getElementById('sliderValueBadge').textContent = currentSliderValue.toFixed(2);
      renderDecimalNumberLine(currentSliderValue);
    }}

    function setSliderBenchmark(val) {{
      currentSliderValue = val;
      const slider = document.getElementById('decimalSlider');
      if (slider) slider.value = Math.round(val * 100);
      document.getElementById('sliderValueBadge').textContent = val.toFixed(2);
      renderDecimalNumberLine(val);
    }}

    function resetDecimalLab() {{
      playSound('click');
      shadedTenthsCount = 4;
      shadedHundredthsCount = 40;
      updateDecimalGridsVisual();
      setSliderBenchmark(0.50);
    }}

    // MANIPULATIVE 3: 10x PLACE VALUE MAGNIFIER (CLUSTER 2)
    let activePvDigit = 4;
    let activePvCol = 3; // Thousands

    function shiftPlaceValue(colIndex) {{
      playSound('click');
      activePvCol = colIndex;
      updatePlaceValueDisplay();
    }}

    function shiftDigitLeft() {{
      if (activePvCol < 4) {{
        playSound('click');
        activePvCol++;
        updatePlaceValueDisplay();
      }}
    }}

    function shiftDigitRight() {{
      if (activePvCol > 0) {{
        playSound('click');
        activePvCol--;
        updatePlaceValueDisplay();
      }}
    }}

    function updatePlaceValueDisplay() {{
      const cols = ['Ones', 'Tens', 'Hundreds', 'Thousands', 'Ten-Thousands'];
      const values = [4, 40, 400, 4000, 40000];

      for (let i = 0; i <= 4; i++) {{
        const colEl = document.getElementById('pvCol' + i);
        if (colEl) {{
          if (i === activePvCol) {{
            colEl.classList.add('border-sky-400', 'bg-sky-950/40');
            colEl.classList.remove('border-slate-800');
          }} else {{
            colEl.classList.remove('border-sky-400', 'bg-sky-950/40');
            colEl.classList.add('border-slate-800');
          }}
        }}
      }}

      const currentVal = values[activePvCol];
      const prevVal = activePvCol > 0 ? values[activePvCol - 1] : 0.4;
      const colName = cols[activePvCol];
      const prevName = activePvCol > 0 ? cols[activePvCol - 1] : 'Tenths';

      document.getElementById('pvShiftExplanation').textContent = 
        `${{activePvDigit}} in ${{colName}} (${{currentVal.toLocaleString()}}) = ${{activePvDigit}} in ${{prevName}} (${{prevVal.toLocaleString()}}) × 10`;
    }}

    // MANIPULATIVE 4: DYNAMIC AREA MODEL MULTIPLICATION (CLUSTER 2)
    let areaModelMode = '4x1';

    function setAreaModelMode(mode) {{
      playSound('click');
      areaModelMode = mode;
      document.getElementById('btn4x1').classList.toggle('bg-emerald-600', mode === '4x1');
      document.getElementById('btn4x1').classList.toggle('bg-slate-800', mode !== '4x1');
      document.getElementById('btn2x2').classList.toggle('bg-emerald-600', mode === '2x2');
      document.getElementById('btn2x2').classList.toggle('bg-slate-800', mode !== '2x2');

      if (mode === '4x1') {{
        document.getElementById('areaFactor1').value = 312;
        document.getElementById('areaFactor2').value = 4;
      }} else {{
        document.getElementById('areaFactor1').value = 24;
        document.getElementById('areaFactor2').value = 13;
      }}
      updateAreaModelVisual();
    }}

    function updateAreaModelVisual() {{
      const f1 = parseInt(document.getElementById('areaFactor1').value) || 24;
      const f2 = parseInt(document.getElementById('areaFactor2').value) || 13;
      renderAreaModelSvg(f1, f2, areaModelMode);
    }}

    function renderAreaModelSvg(f1, f2, mode) {{
      const svg = document.getElementById('areaModelSvg');
      if (!svg) return;

      if (mode === '4x1') {{
        // Decompose f1 by hundreds, tens, ones (e.g. 300 + 10 + 2)
        const h = Math.floor(f1 / 100) * 100;
        const rem = f1 % 100;
        const t = Math.floor(rem / 10) * 10;
        const o = rem % 10;

        const p1 = h * f2;
        const p2 = t * f2;
        const p3 = o * f2;
        const total = p1 + p2 + p3;

        svg.innerHTML = `
          <!-- Width / Length Labels -->
          <text x="100" y="24" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{h}}</text>
          <text x="250" y="24" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{t}}</text>
          <text x="390" y="24" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{o}}</text>
          
          <text x="16" y="115" fill="#f59e0b" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold">${{f2}}</text>

          <!-- 3 Sub-rectangles -->
          <rect x="35" y="35" width="150" height="130" fill="rgba(14, 165, 233, 0.2)" stroke="#38bdf8" stroke-width="1.8" rx="4" />
          <text x="110" y="90" fill="#ffffff" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{h}} × ${{f2}}</text>
          <text x="110" y="115" fill="#38bdf8" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">= ${{p1.toLocaleString()}}</text>

          <rect x="195" y="35" width="130" height="130" fill="rgba(16, 185, 129, 0.2)" stroke="#34d399" stroke-width="1.8" rx="4" />
          <text x="260" y="90" fill="#ffffff" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{t}} × ${{f2}}</text>
          <text x="260" y="115" fill="#34d399" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">= ${{p2.toLocaleString()}}</text>

          <rect x="335" y="35" width="130" height="130" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="1.8" rx="4" />
          <text x="400" y="90" fill="#ffffff" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{o}} × ${{f2}}</text>
          <text x="400" y="115" fill="#fbbf24" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">= ${{p3.toLocaleString()}}</text>
        `;

        document.getElementById('areaModelSumBreakdown').textContent = 
          `Total Product: (${{h}} × ${{f2}} = ${{p1}}) + (${{t}} × ${{f2}} = ${{p2}}) + (${{o}} × ${{f2}} = ${{p3}}) = ${{total.toLocaleString()}}`;
      }} else {{
        // 2x2 Area Model (e.g. 24 x 13 -> (20 + 4) x (10 + 3))
        const t1 = Math.floor(f1 / 10) * 10;
        const o1 = f1 % 10;
        const t2 = Math.floor(f2 / 10) * 10;
        const o2 = f2 % 10;

        const p11 = t1 * t2, p12 = o1 * t2;
        const p21 = t1 * o2, p22 = o1 * o2;
        const total = p11 + p12 + p21 + p22;

        svg.innerHTML = `
          <!-- Top labels -->
          <text x="145" y="20" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold">${{t1}}</text>
          <text x="325" y="20" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold">${{o1}}</text>

          <!-- Left labels -->
          <text x="12" y="75" fill="#f59e0b" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold">${{t2}}</text>
          <text x="12" y="145" fill="#f59e0b" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold">${{o2}}</text>

          <!-- 4 Boxes -->
          <rect x="40" y="30" width="220" height="70" fill="rgba(14, 165, 233, 0.2)" stroke="#38bdf8" stroke-width="1.5" />
          <text x="150" y="70" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{t1}} × ${{t2}} = ${{p11}}</text>

          <rect x="270" y="30" width="150" height="70" fill="rgba(16, 185, 129, 0.2)" stroke="#34d399" stroke-width="1.5" />
          <text x="345" y="70" fill="#34d399" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{o1}} × ${{t2}} = ${{p12}}</text>

          <rect x="40" y="110" width="220" height="70" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="1.5" />
          <text x="150" y="150" fill="#fbbf24" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{t1}} × ${{o2}} = ${{p21}}</text>

          <rect x="270" y="110" width="150" height="70" fill="rgba(139, 92, 246, 0.2)" stroke="#a78bfa" stroke-width="1.5" />
          <text x="345" y="150" fill="#a78bfa" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{o1}} × ${{o2}} = ${{p22}}</text>
        `;

        document.getElementById('areaModelSumBreakdown').textContent = 
          `Total Product: ${{p11}} + ${{p12}} + ${{p21}} + ${{p22}} = ${{total.toLocaleString()}}`;
      }}
    }}

    // MANIPULATIVE 6: RECTILINEAR AREA & DECOMPOSITION (CLUSTER 3)
    let isRectDecomposed = true;

    function toggleRectilinearDecomp() {{
      playSound('click');
      isRectDecomposed = !isRectDecomposed;
      document.getElementById('btnDecompToggle').textContent = isRectDecomposed ? 'Combine into Single L-Shape' : 'Slice into Rect A & B';
      renderRectilinearSvg();
    }}

    function renderRectilinearSvg() {{
      const svg = document.getElementById('rectilinearSvg');
      if (!svg) return;

      if (isRectDecomposed) {{
        svg.innerHTML = `
          <!-- Rectangle A -->
          <rect x="40" y="30" width="180" height="120" fill="rgba(245, 158, 11, 0.25)" stroke="#fbbf24" stroke-width="2" rx="4" />
          <text x="130" y="20" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">6 meters</text>
          <text x="20" y="95" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">4 m</text>
          <text x="130" y="90" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Rectangle A</text>
          <text x="130" y="110" fill="#fbbf24" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">Area = 24 m²</text>

          <!-- Dotted Divider Line -->
          <line x1="220" y1="90" x2="220" y2="150" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4" />

          <!-- Rectangle B -->
          <rect x="220" y="90" width="120" height="60" fill="rgba(16, 185, 129, 0.25)" stroke="#34d399" stroke-width="2" rx="4" />
          <text x="280" y="80" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">3 meters</text>
          <text x="355" y="125" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold">2 m</text>
          <text x="280" y="125" fill="#34d399" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">Area = 6 m²</text>
        `;
      }} else {{
        svg.innerHTML = `
          <!-- Combined L-Shape polygon -->
          <polygon points="40,30 220,30 220,90 340,90 340,150 40,150" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="2.5" />
          <text x="130" y="20" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">6 meters</text>
          <text x="20" y="95" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">4 m</text>
          <text x="280" y="80" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">3 m</text>
          <text x="355" y="125" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold">2 m</text>
          <text x="180" y="105" fill="#ffffff" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">Total Area = ? (Slice to solve!)</text>
        `;
      }}
    }}

    // MANIPULATIVE 7: FRACTIONAL LINE PLOT (CLUSTER 3)
    let linePlotPoints = [0.25, 0.25, 0.375, 0.375, 0.375, 0.5, 0.75, 0.875];

    function addLinePlotPoint(val) {{
      playSound('click');
      linePlotPoints.push(val);
      renderLinePlotSvg();
    }}

    function resetLinePlotData() {{
      playSound('click');
      linePlotPoints = [0.25, 0.25, 0.375, 0.375, 0.375, 0.5, 0.75, 0.875];
      renderLinePlotSvg();
    }}

    function renderLinePlotSvg() {{
      const svg = document.getElementById('fractionalLinePlotSvg');
      if (!svg) return;

      const w = 400, h = 160;
      const margin = 35;
      const axisY = 125;
      const axisW = w - margin * 2;

      let html = `
        <!-- Title -->
        <text x="200" y="18" fill="#94a3b8" font-size="11" font-family="'Inter', sans-serif" font-weight="bold" text-anchor="middle">Seedling Lengths (Inches)</text>
        <!-- Horizontal Axis -->
        <line x1="${{margin}}" y1="${{axisY}}" x2="${{w - margin}}" y2="${{axisY}}" stroke="#475569" stroke-width="2.5" />
      `;

      // 8 Eighths Ticks
      const labels = ['0', '1/8', '1/4', '3/8', '1/2', '5/8', '3/4', '7/8', '1'];
      for (let i = 0; i <= 8; i++) {{
        const x = margin + (i / 8) * axisW;
        html += `
          <line x1="${{x}}" y1="${{axisY - 8}}" x2="${{x}}" y2="${{axisY + 8}}" stroke="#64748b" stroke-width="1.8" />
          <text x="${{x}}" y="${{axisY + 22}}" fill="#94a3b8" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">${{labels[i]}}</text>
        `;
      }}

      // Group points by value to stack 'X' markers
      const counts = {{}};
      linePlotPoints.forEach(p => {{
        counts[p] = (counts[p] || 0) + 1;
        const stackIndex = counts[p];
        const px = margin + p * axisW;
        const py = axisY - 14 - (stackIndex - 1) * 16;
        html += `
          <text x="${{px}}" y="${{py}}" fill="#38bdf8" font-size="13" font-family="'Outfit', sans-serif" font-weight="extrabold" text-anchor="middle">✕</text>
        `;
      }});

      svg.innerHTML = html;
    }}

    // MANIPULATIVE 9: ELAPSED TIME TIMELINE SVG (CLUSTER 3)
    function renderElapsedTimeSvg() {{
      const svg = document.getElementById('elapsedTimeSvg');
      if (!svg) return;

      svg.innerHTML = `
        <!-- Base Timeline -->
        <line x1="40" y1="85" x2="560" y2="85" stroke="#475569" stroke-width="2.5" />
        
        <!-- Markers -->
        <circle cx="60" cy="85" r="5" fill="#f43f5e" />
        <text x="60" y="105" fill="#f43f5e" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">10:45 AM</text>

        <circle cx="160" cy="85" r="5" fill="#38bdf8" />
        <text x="160" y="105" fill="#38bdf8" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">11:00 AM</text>

        <circle cx="440" cy="85" r="5" fill="#10b981" />
        <text x="440" y="105" fill="#10b981" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">1:00 PM</text>

        <circle cx="540" cy="85" r="5" fill="#fbbf24" />
        <text x="540" y="105" fill="#fbbf24" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">1:15 PM</text>

        <!-- Jump Arcs -->
        <path d="M 60 80 Q 110 30 160 80" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2" />
        <text x="110" y="45" fill="#38bdf8" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">+15m</text>

        <path d="M 160 80 Q 300 10 440 80" fill="none" stroke="#10b981" stroke-width="2.5" />
        <text x="300" y="30" fill="#10b981" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="extrabold" text-anchor="middle">+2 Hours</text>

        <path d="M 440 80 Q 490 30 540 80" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,2" />
        <text x="490" y="45" fill="#fbbf24" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">+15m</text>
      `;
    }}

    // CONCEPT HUB RENDERING (3 TIERS)
    function setConceptTier(tier) {{
      playSound('click');
      currentTier = tier;
      document.getElementById('tierBtn1').classList.toggle('bg-sky-600', tier === 1);
      document.getElementById('tierBtn1').classList.toggle('text-white', tier === 1);
      document.getElementById('tierBtn1').classList.toggle('text-slate-400', tier !== 1);

      document.getElementById('tierBtn2').classList.toggle('bg-sky-600', tier === 2);
      document.getElementById('tierBtn2').classList.toggle('text-white', tier === 2);
      document.getElementById('tierBtn2').classList.toggle('text-slate-400', tier !== 2);

      document.getElementById('tierBtn3').classList.toggle('bg-sky-600', tier === 3);
      document.getElementById('tierBtn3').classList.toggle('text-white', tier === 3);
      document.getElementById('tierBtn3').classList.toggle('text-slate-400', tier !== 3);

      renderConceptHub();
    }}

    function renderConceptHub() {{
      const container = document.getElementById('conceptTierContainer');
      if (!container) return;

      if (currentTier === 1) {{
        // Level 1: Visual Intuition
        container.innerHTML = `
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block">Cluster 1: Decimals</span>
            <h3 class="text-base font-bold text-white">Visual Grids: 1 Tenth = 10 Hundredths</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Think of decimals like money: 1 whole dollar has 10 dimes (tenths) or 100 pennies (hundredths). Shading 4 dimes is the exact same amount of money as shading 40 pennies: <strong>4/10 = 40/100 ↔ 0.4 = 0.40</strong>.
            </p>
          </div>
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">Cluster 2: Place Value</span>
            <h3 class="text-base font-bold text-white">The 10× Zoom Secret</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Every time a digit hops one column to the left, it multiplies its value by 10! A digit 4 in the thousands place is 4,000—which is 10 times bigger than 4 in the hundreds place (400).
            </p>
          </div>
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block">Cluster 3: Geometry & Time</span>
            <h3 class="text-base font-bold text-white">Border vs Carpet (P vs A)</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              <strong>Perimeter</strong> is like a fence walking around the outside boundary (add all sides). <strong>Area</strong> is like carpet tiles covering the inside surface (multiply length × width).
            </p>
          </div>
        `;
      }} else if (currentTier === 2) {{
        // Level 2: Core Operations
        container.innerHTML = `
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block">Equivalence & Decimal Addition</span>
            <h3 class="text-base font-bold text-white">Adding Tenths to Hundredths</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              To calculate <strong>3/10 + 25/100</strong>, first scale 3/10 to 30/100: <code class="mono text-sky-300">30/100 + 25/100 = 55/100 = 0.55</code>. Never add denominators together!
            </p>
          </div>
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">Multi-Digit Partial Products</span>
            <h3 class="text-base font-bold text-white">Area Model Multiplication</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Decompose factors by place value: <code class="mono text-emerald-300">312 × 4 = (300 × 4) + (10 × 4) + (2 × 4) = 1,200 + 40 + 8 = 1,248</code>. Summing sub-areas guarantees zero omitted place values.
            </p>
          </div>
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block">Decomposition & Units</span>
            <h3 class="text-base font-bold text-white">Rectilinear Area & Metric Rules</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Slice L-shaped rooms into separate non-overlapping boxes A and B, then sum: <code class="mono text-amber-300">A_total = A₁ + A₂</code>. For metrics, multiply by 1,000 (<code class="mono text-amber-300">1 km = 1,000 m</code>).
            </p>
          </div>
        `;
      }} else {{
        // Level 3: Applied Mastery
        container.innerHTML = `
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block">Decimal Reasoning</span>
            <h3 class="text-base font-bold text-white">Comparing Decimals of Unequal Length</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Pad with trailing zeros to compare accurately: <strong>0.8 = 0.80</strong>. Because 80 hundredths is greater than 74 hundredths, <code class="mono text-sky-300">0.8 > 0.74</code> despite 74 looking bigger!
            </p>
          </div>
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">Contextual Division</span>
            <h3 class="text-base font-bold text-white">Interpreting Real-World Remainders</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              When 125 students ride 8-passenger vans: <code class="mono text-emerald-300">125 ÷ 8 = 15 R 5</code>. 15 vans leave 5 kids behind! You must round up to <strong>16 vans</strong> so every student rides.
            </p>
          </div>
          <div class="glass-card rounded-2xl p-5 space-y-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block">Optimization & Time</span>
            <h3 class="text-base font-bold text-white">Fixed Area Minimum Perimeter</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              For a fixed 36 sq ft area, a square (6 ft × 6 ft, P = 24 ft) yields the minimum perimeter fence compared to longer rectangles (1×36, P = 74 ft; 4×9, P = 26 ft).
            </p>
          </div>
        `;
      }}
    }}

    // QUEST LOGIC (60 QUESTIONS ADAPTIVE)
    function loadQuestion(index) {{
      clearInterval(timerInterval);
      currentQuestionIndex = index;
      selectedAnswerState = null;
      hintsUsedForActiveQ = 0;

      const q = activeChallengeQuestions[index];
      if (!q) {{
        renderQuestComplete();
        return;
      }}

      // Reset UI elements
      document.getElementById('hintDisplayBox').classList.add('hidden');
      document.getElementById('solutionBreakdownBox').classList.add('hidden');
      document.getElementById('btnSubmitAnswer').classList.remove('hidden');

      // Update Top HUD
      document.getElementById('qNumberHeading').textContent = `Question ${{index + 1}} of ${{activeChallengeQuestions.length}}`;
      document.getElementById('qStandardTag').textContent = q.standard || 'NC.4.NF';
      document.getElementById('currentClusterBadge').textContent = q.clusterTitle || 'Cluster';
      document.getElementById('currentTierBadge').textContent = (q.tier ? q.tier.toUpperCase() : 'MEDIUM') + ' TIER';
      document.getElementById('questionPromptText').textContent = q.question;
      document.getElementById('qFormatTag').textContent = q.format.toUpperCase();

      // Render workspace by format
      const workspace = document.getElementById('questionWorkspaceContainer');
      workspace.innerHTML = '';

      if (q.format === 'mc') {{
        renderMCWorkspace(workspace, q);
      }} else if (q.format === 'visual') {{
        renderVisualWorkspace(workspace, q);
      }} else if (q.format === 'numberline') {{
        renderNumberlineWorkspace(workspace, q);
      }} else if (q.format === 'dragdrop') {{
        renderDragDropWorkspace(workspace, q);
      }}

      // Start timer
      timerSeconds = (q.tier === 'easy' ? 45 : (q.tier === 'hard' ? 60 : 50));
      document.getElementById('timerDisplay').textContent = timerSeconds + 's';
      timerPaused = false;
      document.getElementById('pauseTimerBtn').textContent = '⏸';

      timerInterval = setInterval(() => {{
        if (!timerPaused) {{
          timerSeconds--;
          document.getElementById('timerDisplay').textContent = timerSeconds + 's';
          if (timerSeconds <= 0) {{
            clearInterval(timerInterval);
            submitActiveAnswer(true);
          }}
        }}
      }}, 1000);
    }}

    // Format 1: Multiple Choice with Runtime Fisher-Yates Shuffling
    function renderMCWorkspace(container, q) {{
      const letters = ['A', 'B', 'C', 'D'];
      if (!q._shuffledOptions || q._shuffledQId !== q.id) {{
        const shuffled = [...q.options].map(opt => ({{ ...opt }}));
        for (let i = shuffled.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }}
        shuffled.forEach((opt, idx) => {{
          opt.displayLetter = letters[idx] || (idx + 1);
        }});
        q._shuffledOptions = shuffled;
        q._shuffledQId = q.id;
      }}

      let html = '<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">';
      q._shuffledOptions.forEach((opt, idx) => {{
        html += `
          <button onclick="selectMCOption(${{idx}})" id="mcOpt_${{idx}}" class="mc-option-btn p-3.5 rounded-xl bg-slate-900 border border-slate-700/80 hover:border-sky-400 text-left transition flex items-center justify-between group">
            <span class="text-xs font-semibold text-slate-200 group-hover:text-white">${{opt.text}}</span>
            <span class="w-6 h-6 rounded-full border border-slate-700 flex items-center justify-center text-[10px] text-slate-400 group-hover:border-sky-400 group-hover:text-sky-300 mono">${{opt.displayLetter}}</span>
          </button>
        `;
      }});
      html += '</div>';
      container.innerHTML = html;
    }}

    function selectMCOption(optIndex) {{
      playSound('click');
      const q = activeChallengeQuestions[currentQuestionIndex];
      const opt = q._shuffledOptions ? q._shuffledOptions[optIndex] : q.options[optIndex];
      selectedAnswerState = opt;

      document.querySelectorAll('.mc-option-btn').forEach(btn => {{
        btn.classList.remove('border-sky-400', 'bg-sky-500/20');
        btn.classList.add('border-slate-700/80', 'bg-slate-900');
      }});
      const selectedBtn = document.getElementById('mcOpt_' + optIndex);
      if (selectedBtn) {{
        selectedBtn.classList.remove('border-slate-700/80', 'bg-slate-900');
        selectedBtn.classList.add('border-sky-400', 'bg-sky-500/20');
      }}
    }}

    // Format 2: Visual Selection
    function renderVisualWorkspace(container, q) {{
      const letters = ['A', 'B', 'C', 'D'];
      if (!q._shuffledVisualCards || q._shuffledQId !== q.id) {{
        const shuffled = [...q.visualCards].map(c => ({{
          ...c,
          correct: (c.id === q.answerKey || c.correct === true)
        }}));
        for (let i = shuffled.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }}
        shuffled.forEach((card, idx) => {{
          card.displayLetter = letters[idx] || (idx + 1);
          card.dynamicLabel = `Option ${{letters[idx]}}: ${{card.desc || card.label}}`;
        }});
        q._shuffledVisualCards = shuffled;
        q._shuffledQId = q.id;
      }}

      let html = '<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">';
      q._shuffledVisualCards.forEach((card, idx) => {{
        html += `
          <button onclick="selectVisualCard(${{idx}})" id="visCard_${{idx}}" class="visual-card-btn p-3.5 bg-slate-900 rounded-xl border border-slate-700/80 hover:border-amber-400 text-left transition flex flex-col justify-between group">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-amber-300">${{card.dynamicLabel}}</span>
              <span class="w-6 h-6 rounded-full border border-slate-700 flex items-center justify-center text-[10px] text-slate-400 group-hover:border-amber-400 mono">${{card.displayLetter}}</span>
            </div>
            <div class="w-full bg-slate-950 p-2 rounded-lg border border-slate-800 flex items-center justify-center">
              ${{renderVisualCardSvg(card)}}
            </div>
          </button>
        `;
      }});
      html += '</div>';
      container.innerHTML = html;
    }}

    function renderVisualCardSvg(card) {{
      if (card.svgType === 'tenths_grid') {{
        const shaded = card.shaded || 4;
        let cols = '';
        for (let c = 0; c < 10; c++) {{
          const fill = c < shaded ? '#38bdf8' : 'rgba(51, 65, 85, 0.4)';
          cols += `<rect x="${{c * 14 + 4}}" y="4" width="11" height="50" fill="${{fill}}" rx="1" />`;
        }}
        return `<svg viewBox="0 0 150 58" class="w-full h-12">${{cols}}</svg>`;
      }} else if (card.svgType === 'hundredths_grid') {{
        const shaded = card.shaded || 30;
        let sqs = '';
        for (let s = 0; s < 100; s++) {{
          const fill = s < shaded ? '#fbbf24' : 'rgba(51, 65, 85, 0.3)';
          const r = Math.floor(s / 10), c = s % 10;
          sqs += `<rect x="${{c * 6 + 4}}" y="${{r * 5 + 4}}" width="4.5" height="3.8" fill="${{fill}}" rx="0.5" />`;
        }}
        return `<svg viewBox="0 0 70 58" class="w-full h-12">${{sqs}}</svg>`;
      }} else if (card.svgType === 'rect_perimeter') {{
        return `
          <svg viewBox="0 0 160 58" class="w-full h-12">
            <rect x="25" y="10" width="110" height="38" fill="none" stroke="#34d399" stroke-width="2.5" />
            <text x="80" y="8" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">8 ft</text>
            <text x="12" y="33" fill="#34d399" font-size="9" font-weight="bold">5 ft</text>
            <text x="80" y="34" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">P = 26 ft</text>
          </svg>
        `;
      }} else if (card.svgType === 'rect_area') {{
        return `
          <svg viewBox="0 0 160 58" class="w-full h-12">
            <rect x="25" y="10" width="110" height="38" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="1.8" />
            <text x="80" y="34" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Area = 40 sq ft</text>
          </svg>
        `;
      }} else {{
        return `<div class="text-xs font-mono text-slate-300 py-2">${{card.desc || card.label}}</div>`;
      }}
    }}

    function selectVisualCard(idx) {{
      playSound('click');
      const q = activeChallengeQuestions[currentQuestionIndex];
      const card = q._shuffledVisualCards[idx];
      selectedAnswerState = card;

      document.querySelectorAll('.visual-card-btn').forEach(btn => {{
        btn.classList.remove('border-amber-400', 'bg-amber-500/20');
        btn.classList.add('border-slate-700/80', 'bg-slate-900');
      }});
      const selectedBtn = document.getElementById('visCard_' + idx);
      if (selectedBtn) {{
        selectedBtn.classList.remove('border-slate-700/80', 'bg-slate-900');
        selectedBtn.classList.add('border-amber-400', 'bg-amber-500/20');
      }}
    }}

    // Format 3: Interactive Numberline
    function renderNumberlineWorkspace(container, q) {{
      const min = q.nlMin !== undefined ? q.nlMin : 0;
      const max = q.nlMax !== undefined ? q.nlMax : 1;
      const step = q.step !== undefined ? q.step : 0.05;
      const initial = (min + max) / 2;
      selectedAnswerState = initial;

      container.innerHTML = `
        <div class="space-y-4">
          <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Minimum: <strong class="text-white">${{min}}</strong></span>
            <span class="text-emerald-400 font-bold">Selected Coordinate: <span id="qNlValueBadge" class="text-white font-mono font-bold">${{initial.toFixed(2)}}</span></span>
            <span>Maximum: <strong class="text-white">${{max}}</strong></span>
          </div>
          
          <svg id="qNumberlineSvg" viewBox="0 0 500 80" class="w-full h-auto bg-slate-900 rounded-xl p-2 border border-slate-800">
            <!-- Rendered below -->
          </svg>

          <input type="range" id="qNlSlider" min="${{min}}" max="${{max}}" step="${{step}}" value="${{initial}}" oninput="updateQNumberline(this.value)" class="w-full accent-emerald-400 cursor-pointer h-2.5 bg-slate-800 rounded-lg" />
        </div>
      `;

      updateQNumberline(initial);
    }}

    function updateQNumberline(val) {{
      const numVal = parseFloat(val);
      selectedAnswerState = numVal;
      const badge = document.getElementById('qNlValueBadge');
      if (badge) badge.textContent = numVal.toFixed(2);

      const q = activeChallengeQuestions[currentQuestionIndex];
      const min = q.nlMin !== undefined ? q.nlMin : 0;
      const max = q.nlMax !== undefined ? q.nlMax : 1;

      const svg = document.getElementById('qNumberlineSvg');
      if (!svg) return;

      const w = 500, lineY = 40, margin = 40;
      const lineW = w - margin * 2;
      const ratio = (numVal - min) / (max - min);
      const px = margin + ratio * lineW;

      let ticksHtml = '';
      const steps = 10;
      for (let i = 0; i <= steps; i++) {{
        const tx = margin + (i / steps) * lineW;
        const tickVal = min + (i / steps) * (max - min);
        ticksHtml += `
          <line x1="${{tx}}" y1="${{lineY - 8}}" x2="${{tx}}" y2="${{lineY + 8}}" stroke="#64748b" stroke-width="1.5" />
          <text x="${{tx}}" y="${{lineY + 22}}" fill="#94a3b8" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">${{tickVal.toFixed(tickVal % 1 === 0 ? 0 : 2)}}</text>
        `;
      }}

      svg.innerHTML = `
        <line x1="${{margin}}" y1="${{lineY}}" x2="${{w - margin}}" y2="${{lineY}}" stroke="#475569" stroke-width="2.5" />
        ${{ticksHtml}}
        <circle cx="${{px}}" cy="${{lineY}}" r="7" fill="#10b981" stroke="#ffffff" stroke-width="2" />
        <text x="${{px}}" y="${{lineY - 14}}" fill="#10b981" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">P: ${{numVal.toFixed(2)}}</text>
      `;
    }}

    // Format 4: Drag & Drop
    let activeDragState = {{}};

    function renderDragDropWorkspace(container, q) {{
      activeDragState = {{}};
      const d = q.dragData;

      let html = '<div class="space-y-4">';
      
      // Source Tray (Randomized)
      const trayItems = [...d.items];
      for (let i = trayItems.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [trayItems[i], trayItems[j]] = [trayItems[j], trayItems[i]];
      }}

      html += '<div class="space-y-1.5"><span class="text-xs font-bold text-slate-400">Available Cards (Drag or Tap to slot):</span>';
      html += '<div id="dragCardTray" class="flex flex-wrap gap-2 p-3 bg-slate-950 rounded-xl border border-slate-800 min-h-[56px]">';
      trayItems.forEach(item => {{
        html += `
          <div id="dragItem_${{item.id}}" onclick="onDragItemTap('${{item.id}}')" class="drag-chip px-3 py-1.5 rounded-lg bg-sky-600/30 border border-sky-500/50 text-xs font-semibold text-sky-200 cursor-pointer hover:bg-sky-600 hover:text-white transition shadow-sm">
            ${{item.text}}
          </div>
        `;
      }});
      html += '</div></div>';

      // Target Slots
      html += '<div class="space-y-2"><span class="text-xs font-bold text-slate-400">Target Containers:</span>';
      html += '<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">';
      d.slots.forEach(slot => {{
        html += `
          <div id="dropSlot_${{slot.id}}" onclick="onDropSlotTap('${{slot.id}}')" class="drop-target-slot p-3 rounded-xl bg-slate-900 border-2 border-dashed border-slate-700 hover:border-sky-400 transition min-h-[72px] flex flex-col justify-between cursor-pointer">
            <span class="text-xs font-bold text-slate-400">${{slot.label}}</span>
            <div id="slotContent_${{slot.id}}" class="flex flex-wrap gap-1.5 mt-2 min-h-[28px]"></div>
          </div>
        `;
      }});
      html += '</div></div></div>';

      container.innerHTML = html;
      selectedAnswerState = activeDragState;
    }}

    let tappedSourceItemId = null;

    function onDragItemTap(itemId) {{
      playSound('click');
      tappedSourceItemId = itemId;
      document.querySelectorAll('.drag-chip').forEach(el => el.classList.remove('ring-2', 'ring-amber-400'));
      const itemEl = document.getElementById('dragItem_' + itemId);
      if (itemEl) itemEl.classList.add('ring-2', 'ring-amber-400');
    }}

    function onDropSlotTap(slotId) {{
      if (!tappedSourceItemId) return;
      playSound('click');

      const q = activeChallengeQuestions[currentQuestionIndex];
      const itemObj = q.dragData.items.find(i => i.id === tappedSourceItemId);
      if (!itemObj) return;

      // Assign to slot
      if (!activeDragState[slotId]) activeDragState[slotId] = [];
      if (!activeDragState[slotId].includes(tappedSourceItemId)) {{
        activeDragState[slotId].push(tappedSourceItemId);
      }}

      // Hide from tray
      const itemEl = document.getElementById('dragItem_' + tappedSourceItemId);
      if (itemEl) itemEl.style.display = 'none';

      // Render into slot
      const slotContent = document.getElementById('slotContent_' + slotId);
      if (slotContent) {{
        const chip = document.createElement('span');
        chip.className = 'px-2.5 py-1 rounded-md bg-emerald-600/30 border border-emerald-500/50 text-xs font-mono font-bold text-emerald-200 cursor-pointer';
        chip.textContent = itemObj.text;
        chip.onclick = (e) => {{
          e.stopPropagation();
          // Return to tray
          activeDragState[slotId] = activeDragState[slotId].filter(id => id !== itemObj.id);
          chip.remove();
          if (itemEl) itemEl.style.display = 'block';
        }};
        slotContent.appendChild(chip);
      }}

      tappedSourceItemId = null;
      document.querySelectorAll('.drag-chip').forEach(el => el.classList.remove('ring-2', 'ring-amber-400'));
      selectedAnswerState = activeDragState;
    }}

    // SUBMIT & VALIDATE ANSWER
    function submitActiveAnswer(isTimeout = false) {{
      const q = activeChallengeQuestions[currentQuestionIndex];
      if (!q) return;

      clearInterval(timerInterval);
      questionsAnsweredCount++;

      let isCorrect = false;

      if (!isTimeout && selectedAnswerState !== null && selectedAnswerState !== undefined) {{
        if (q.format === 'mc' || q.format === 'visual') {{
          if (selectedAnswerState && typeof selectedAnswerState === 'object') {{
            isCorrect = !!(selectedAnswerState.correct || selectedAnswerState.id === q.answerKey);
          }} else {{
            isCorrect = (selectedAnswerState === q.answerKey);
          }}
        }} else if (q.format === 'numberline') {{
          isCorrect = Math.abs(selectedAnswerState - q.answerKey) < (q.step ? q.step * 0.75 : 0.05);
        }} else if (q.format === 'dragdrop') {{
          // Validate container placement
          let allMatched = true;
          for (let slotId in q.answerKey) {{
            const expected = q.answerKey[slotId];
            const placed = activeDragState[slotId] || [];
            if (Array.isArray(expected)) {{
              const hasAll = expected.every(item => placed.includes(item));
              if (!hasAll || placed.length !== expected.length) allMatched = false;
            }} else {{
              if (!placed.includes(expected)) allMatched = false;
            }}
          }}
          isCorrect = allMatched;
        }}
      }}

      if (isCorrect) {{
        playSound('correct');
        userStreak++;
        userScore += Math.round(100 * (1 + userStreak * 0.1));
      }} else {{
        playSound('incorrect');
        userStreak = 0;
        missedQuestions.push(q);
        showMisconceptionDrawer(q);
      }}

      updateHUD();
      revealSolutionBreakdown(q, isCorrect);
    }}

    function revealSolutionBreakdown(q, isCorrect) {{
      document.getElementById('btnSubmitAnswer').classList.add('hidden');
      const box = document.getElementById('solutionBreakdownBox');
      box.classList.remove('hidden');

      const icon = document.getElementById('solutionResultIcon');
      const title = document.getElementById('solutionResultTitle');

      if (isCorrect) {{
        icon.textContent = '🎉';
        title.textContent = 'Correct! Mastered Solution';
        title.className = 'text-sm font-extrabold text-emerald-400';
      }} else {{
        icon.textContent = '🧐';
        title.textContent = 'Review & Learn Solution Model';
        title.className = 'text-sm font-extrabold text-amber-400';
      }}

      document.getElementById('solutionStandardLabel').textContent = q.standard || 'NC.4.NF';
      document.getElementById('verifiedAnswerText').textContent = getHumanReadableAnswer(q);

      renderVisualSolutionModel(q);

      document.getElementById('solStep1Text').textContent = `Target standard: ${{q.standard}}. Identify the core values and relationship.`;
      document.getElementById('solStep2Text').textContent = `Visualize using place value grids, partial products, or fractional intervals.`;
      document.getElementById('solStep3Text').textContent = q.explanation;
      document.getElementById('solStep4Text').textContent = `Verify by comparing place value sizes and checking mathematical reasonableness.`;
    }}

    function getHumanReadableAnswer(q) {{
      if (q.formattedAnswer) return q.formattedAnswer;
      if (q.format === 'mc') {{
        const correctOpt = q.options.find(o => o.correct || o.id === q.answerKey);
        return correctOpt ? correctOpt.text : String(q.answerKey);
      }} else if (q.format === 'visual') {{
        const correctCard = q.visualCards.find(c => c.id === q.answerKey);
        return correctCard ? `${{correctCard.label}} - ${{correctCard.desc}}` : String(q.answerKey);
      }} else if (q.format === 'numberline') {{
        return `Point at coordinate ${{q.answerKey}}`;
      }} else {{
        return 'Correct container placement verified.';
      }}
    }}

    function renderVisualSolutionModel(q) {{
      const container = document.getElementById('visualSolutionModelContainer');
      if (!container) return;

      if (q.cluster === 'c1') {{
        // Fractions & Decimals SVG diagram
        container.innerHTML = `
          <svg viewBox="0 0 450 70" class="w-full h-16">
            <rect x="20" y="10" width="180" height="40" fill="rgba(14, 165, 233, 0.2)" stroke="#38bdf8" stroke-width="1.8" rx="4" />
            <text x="110" y="34" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Tenths: 1/10 = 0.1</text>
            
            <text x="225" y="35" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">↔</text>

            <rect x="250" y="10" width="180" height="40" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="1.8" rx="4" />
            <text x="340" y="34" fill="#fbbf24" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Hundredths: 10/100 = 0.10</text>
          </svg>
        `;
      }} else if (q.cluster === 'c2') {{
        // Multi-Digit Operations SVG
        container.innerHTML = `
          <svg viewBox="0 0 450 70" class="w-full h-16">
            <rect x="20" y="10" width="120" height="40" fill="rgba(16, 185, 129, 0.2)" stroke="#34d399" stroke-width="1.8" rx="4" />
            <text x="80" y="34" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Thousands (×10)</text>

            <line x1="145" y1="30" x2="165" y2="30" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />

            <rect x="170" y="10" width="120" height="40" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="1.8" rx="4" />
            <text x="230" y="34" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Hundreds (×10)</text>

            <line x1="295" y1="30" x2="315" y2="30" stroke="#94a3b8" stroke-width="2" />

            <rect x="320" y="10" width="110" height="40" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="1.8" rx="4" />
            <text x="375" y="34" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Tens (×10)</text>
          </svg>
        `;
      }} else {{
        // Measurement & Line Plot SVG
        container.innerHTML = `
          <svg viewBox="0 0 450 70" class="w-full h-16">
            <rect x="30" y="10" width="160" height="40" fill="rgba(16, 185, 129, 0.2)" stroke="#34d399" stroke-width="1.8" rx="4" />
            <text x="110" y="34" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Rect A (Sub-Area 1)</text>

            <text x="215" y="35" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">+</text>

            <rect x="235" y="10" width="180" height="40" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="1.8" rx="4" />
            <text x="325" y="34" fill="#fbbf24" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">Rect B (Sub-Area 2)</text>
          </svg>
        `;
      }}
    }}

    function advanceToNextQuestion() {{
      playSound('click');
      if (currentQuestionIndex < activeChallengeQuestions.length - 1) {{
        loadQuestion(currentQuestionIndex + 1);
      }} else {{
        renderQuestComplete();
      }}
    }}

    function requestSocraticHint() {{
      const q = activeChallengeQuestions[currentQuestionIndex];
      if (!q || !q.hints || q.hints.length === 0) return;

      playSound('click');
      hintsUsedForActiveQ++;
      const hintIdx = Math.min(hintsUsedForActiveQ - 1, q.hints.length - 1);

      const box = document.getElementById('hintDisplayBox');
      box.classList.remove('hidden');
      document.getElementById('hintStageBadge').textContent = `Hint ${{hintIdx + 1}}/${{q.hints.length}}`;
      document.getElementById('hintTextContent').textContent = q.hints[hintIdx];

      const remaining = Math.max(0, q.hints.length - hintsUsedForActiveQ);
      document.getElementById('hintsRemainingBadge').textContent = `${{remaining}} left`;
    }}

    function toggleTimerPause() {{
      timerPaused = !timerPaused;
      document.getElementById('pauseTimerBtn').textContent = timerPaused ? '▶' : '⏸';
    }}

    function updateHUD() {{
      document.getElementById('scoreDisplay').textContent = `${{userScore}} pts`;
      document.getElementById('streakDisplay').textContent = `${{userStreak}}× (${{(1 + userStreak * 0.1).toFixed(1)}}x)`;
      document.getElementById('navScoreBadge').textContent = `${{questionsAnsweredCount}}/${{activeChallengeQuestions.length}}`;
    }}

    // MISCONCEPTION DRAWER
    function showMisconceptionDrawer(q) {{
      const drawer = document.getElementById('misconceptionDrawer');
      drawer.classList.add('open');

      document.getElementById('drawerMisconceptionTitle').textContent = q.misconception || 'Conceptual Misconception Intercepted';
      document.getElementById('drawerDiagnosticExplanation').textContent = q.explanation;

      const canvas = document.getElementById('drawerVisualCanvas');
      if (q.cluster === 'c1') {{
        canvas.innerHTML = `
          <div class="text-xs text-slate-300 font-mono p-2 text-center">
            Remember: 0.8 occupies 8 full columns (80 hundredths). 0.74 occupies 74 hundredths. Because 80 > 74, 0.8 > 0.74!
          </div>
        `;
      }} else if (q.cluster === 'c2') {{
        canvas.innerHTML = `
          <div class="text-xs text-slate-300 font-mono p-2 text-center">
            Remember: Shifting 1 column left multiplies by 10! Multiplicative comparison uses multiplication: 4 times as many means 4 × n.
          </div>
        `;
      }} else {{
        canvas.innerHTML = `
          <div class="text-xs text-slate-300 font-mono p-2 text-center">
            Remember: Perimeter is boundary fence (2l + 2w). Area is surface carpet (l × w). Hours are base-60, not base-100!
          </div>
        `;
      }}
    }}

    function closeMisconceptionDrawer() {{
      playSound('click');
      document.getElementById('misconceptionDrawer').classList.remove('open');
    }}

    // DASHBOARD & ANALYTICS
    function updateDashboard() {{
      const total = activeChallengeQuestions.length || 60;
      const answered = questionsAnsweredCount || 0;
      const missed = missedQuestions.length;
      const correct = Math.max(0, answered - missed);
      const acc = answered > 0 ? Math.round((correct / answered) * 100) : 0;

      document.getElementById('dashAccuracyPercent').textContent = `${{acc}}%`;
      document.getElementById('dashCompletionText').textContent = `${{answered}} of ${{total}} questions completed (${{missed}} flagged for review)`;
      document.getElementById('missedCountBadge').textContent = missed;

      // Cluster Breakdown
      const c1 = ALL_QUESTIONS.filter(q => q.cluster === 'c1');
      const c2 = ALL_QUESTIONS.filter(q => q.cluster === 'c2');
      const c3 = ALL_QUESTIONS.filter(q => q.cluster === 'c3');

      const c1Correct = c1.filter(q => !missedQuestions.some(m => m.id === q.id)).length;
      const c2Correct = c2.filter(q => !missedQuestions.some(m => m.id === q.id)).length;
      const c3Correct = c3.filter(q => !missedQuestions.some(m => m.id === q.id)).length;

      const p1 = Math.round((c1Correct / c1.length) * 100);
      const p2 = Math.round((c2Correct / c2.length) * 100);
      const p3 = Math.round((c3Correct / c3.length) * 100);

      document.getElementById('c1ProgressBar').style.width = p1 + '%';
      document.getElementById('c1PercentText').textContent = p1 + '%';

      document.getElementById('c2ProgressBar').style.width = p2 + '%';
      document.getElementById('c2PercentText').textContent = p2 + '%';

      document.getElementById('c3ProgressBar').style.width = p3 + '%';
      document.getElementById('c3PercentText').textContent = p3 + '%';
    }}

    function retryMissedQuestions() {{
      if (missedQuestions.length === 0) {{
        alert('Zero missed questions! Outstanding mastery!');
        return;
      }}
      playSound('click');
      activeChallengeQuestions = [...missedQuestions];
      missedQuestions = [];
      currentQuestionIndex = 0;
      switchTab('challenge');
    }}

    function restartChallenge() {{
      playSound('click');
      activeChallengeQuestions = [...ALL_QUESTIONS];
      currentQuestionIndex = 0;
      userScore = 0;
      userStreak = 0;
      questionsAnsweredCount = 0;
      missedQuestions = [];
      updateHUD();
      switchTab('challenge');
    }}

    function renderQuestComplete() {{
      clearInterval(timerInterval);
      const workspace = document.getElementById('questionWorkspaceContainer');
      workspace.innerHTML = `
        <div class="text-center py-8 space-y-4">
          <span class="text-5xl block animate-bounce">🏆</span>
          <h3 class="text-xl font-extrabold text-emerald-400">Mastery Quest Complete!</h3>
          <p class="text-xs sm:text-sm text-slate-300 max-w-md mx-auto">
            You have journeyed through all CMS Quarter 2 Standards: Fractions to Decimals, 10× Place Value, Multi-Digit Operations, and Spatial Measurement!
          </p>
          <div class="flex items-center justify-center gap-3 pt-3">
            <button onclick="switchTab('dashboard')" class="px-5 py-2.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-xs font-bold text-white transition">
              View Mastery Radar & Report
            </button>
            <button onclick="restartChallenge()" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 transition">
              Restart Full Quest
            </button>
          </div>
        </div>
      `;
    }}

    // DOWNLOAD OFFLINE SINGLE FILE
    function downloadStandaloneApp() {{
      const blob = new Blob([document.documentElement.outerHTML], {{ type: 'text/html' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'CMS_4th_Grade_Math_Quarter_2_Decimals_Operations_Measurement_Lab.html';
      a.click();
      URL.revokeObjectURL(url);
    }}

    // INITIAL BOOTSTRAP
    document.addEventListener('DOMContentLoaded', () => {{
      initScratchpad();
      buildDecimalGrids();
      renderDecimalNumberLine(0.50);
      updatePlaceValueDisplay();
      updateAreaModelVisual();
      renderRectilinearSvg();
      renderLinePlotSvg();
      renderElapsedTimeSvg();
      renderConceptHub();
      loadQuestion(0);
    }});
  </script>
</body>
</html>
'''

    out_path = r'c:\Antygravity\learning\apps\math\4th_grade_math_decimals_multi_digit_measurement_q2.html'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Flawlessly created {out_path} ({len(html_content)} bytes)")

if __name__ == '__main__':
    build_app()

// Portal Interactivity & Dynamic Canvas Visualizer

document.addEventListener('DOMContentLoaded', () => {
  initMiniCanvas();
  initFunctionsMiniCanvas();
  initGrade4MiniCanvas();
  initGrade4Q2MiniCanvas();
  initSearchAndFilter();
  initModalRunner();
});

// 1. Dynamic Mini Canvas Animation for Dilation Featured Card
function initMiniCanvas() {
  const canvas = document.getElementById('previewCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  let angle = 0;

  function render() {
    const width = canvas.getBoundingClientRect().width;
    const height = canvas.getBoundingClientRect().height;

    ctx.clearRect(0, 0, width, height);

    // Grid lines
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    const step = 25;
    for (let x = 0; x <= width; x += step) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (let y = 0; y <= height; y += step) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Origin / Center of Dilation (cx, cy)
    const cx = width * 0.28;
    const cy = height * 0.72;

    // Draw Coordinate Axes
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.25)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cx - 50, cy);
    ctx.lineTo(width - 20, cy);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(cx, height - 20);
    ctx.lineTo(cx, 20);
    ctx.stroke();

    // Scale factor oscillating smoothly between 0.7 and 2.4
    const k = 1.35 + 0.75 * Math.sin(angle);

    // Original Triangle vertices relative to center
    const origPoints = [
      { x: 30, y: -20 },
      { x: 90, y: -20 },
      { x: 30, y: -70 }
    ];

    // Projection ray lines from center of dilation
    ctx.strokeStyle = 'rgba(245, 158, 11, 0.35)';
    ctx.setLineDash([4, 4]);
    origPoints.forEach(p => {
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + p.x * 2.3, cy + p.y * 2.3);
      ctx.stroke();
    });
    ctx.setLineDash([]);

    // Draw Original Triangle (Pre-image)
    ctx.fillStyle = 'rgba(59, 130, 246, 0.2)';
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(cx + origPoints[0].x, cy + origPoints[0].y);
    ctx.lineTo(cx + origPoints[1].x, cy + origPoints[1].y);
    ctx.lineTo(cx + origPoints[2].x, cy + origPoints[2].y);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    // Draw Dilated Triangle (Image)
    ctx.fillStyle = 'rgba(236, 72, 153, 0.18)';
    ctx.strokeStyle = '#ec4899';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(cx + origPoints[0].x * k, cy + origPoints[0].y * k);
    ctx.lineTo(cx + origPoints[1].x * k, cy + origPoints[1].y * k);
    ctx.lineTo(cx + origPoints[2].x * k, cy + origPoints[2].y * k);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    // Center of dilation point
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(cx, cy, 4, 0, Math.PI * 2);
    ctx.fill();

    // Slope line demonstration
    ctx.strokeStyle = 'rgba(16, 185, 129, 0.6)';
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    ctx.moveTo(cx + origPoints[0].x * k, cy + origPoints[0].y * k);
    ctx.lineTo(cx + origPoints[2].x * k, cy + origPoints[2].y * k);
    ctx.stroke();

    // Text labels
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Scale Factor k = ${k.toFixed(2)}`, 20, 30);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Center (cx, cy)', cx - 40, cy + 18);

    angle += 0.02;
    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// 1b. Dynamic Mini Canvas for Functions Featured Card
function initFunctionsMiniCanvas() {
  const canvas = document.getElementById('previewCanvasFunctions');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  let t = 0;

  function render() {
    const width = canvas.getBoundingClientRect().width;
    const height = canvas.getBoundingClientRect().height;

    ctx.clearRect(0, 0, width, height);

    // Subtle Grid
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    const step = 24;
    for (let x = 0; x <= width; x += step) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (let y = 0; y <= height; y += step) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Origin
    const ox = width * 0.35;
    const oy = height * 0.65;

    // Axes
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.3)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(15, oy);
    ctx.lineTo(width - 15, oy);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(ox, height - 15);
    ctx.lineTo(ox, 15);
    ctx.stroke();

    const scaleX = 22;
    const scaleY = 18;

    // 1. Linear Curve: f(x) = mx + b
    const m = 0.8 + 0.4 * Math.sin(t);
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let px = 20; px <= width - 20; px += 4) {
      const mx = (px - ox) / scaleX;
      const my = m * mx;
      const py = oy - my * scaleY;
      if (px === 20) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 2. Quadratic Curve: f(x) = a * x²
    const a = 0.28 + 0.12 * Math.cos(t * 0.8);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let px = 20; px <= width - 20; px += 4) {
      const mx = (px - ox) / scaleX;
      const my = a * mx * mx - 1.5;
      const py = oy - my * scaleY;
      if (px === 20) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 3. Exponential Curve: f(x) = 1.5^x
    ctx.strokeStyle = '#ec4899';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = 20; px <= width - 20; px += 4) {
      const mx = (px - ox) / scaleX;
      const my = Math.pow(1.5, mx);
      const py = oy - my * scaleY;
      if (px === 20) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 4. Moving Secant Line & Slope Triangle on Quadratic
    const secX1 = 0.5 + 0.6 * Math.sin(t * 1.2);
    const secX2 = secX1 + 1.8;
    const secY1 = a * secX1 * secX1 - 1.5;
    const secY2 = a * secX2 * secX2 - 1.5;

    const sx1 = ox + secX1 * scaleX;
    const sy1 = oy - secY1 * scaleY;
    const sx2 = ox + secX2 * scaleX;
    const sy2 = oy - secY2 * scaleY;

    // Slope Triangle
    ctx.strokeStyle = 'rgba(6, 182, 212, 0.7)';
    ctx.setLineDash([3, 3]);
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(sx1, sy1);
    ctx.lineTo(sx2, sy1);
    ctx.lineTo(sx2, sy2);
    ctx.stroke();
    ctx.setLineDash([]);

    // Secant Segment
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(sx1 - 15, sy1 + (sy1 - sy2) * 0.2);
    ctx.lineTo(sx2 + 15, sy2 - (sy1 - sy2) * 0.2);
    ctx.stroke();

    // Endpoint dots
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(sx1, sy1, 3.5, 0, Math.PI * 2);
    ctx.arc(sx2, sy2, 3.5, 0, Math.PI * 2);
    ctx.fill();

    // Telemetry text
    const aroc = (secY2 - secY1) / (secX2 - secX1);
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Δy/Δx (AROC) = ${aroc.toFixed(2)}`, 20, 30);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Linear • Quadratic • Exponential', 20, height - 16);

    t += 0.025;
    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// 1c. Dynamic Mini Canvas for 4th Grade Math Featured Card
function initGrade4MiniCanvas() {
  const canvas = document.getElementById('previewCanvasGrade4');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  let frame = 0;

  function render() {
    const width = canvas.getBoundingClientRect().width;
    const height = canvas.getBoundingClientRect().height;

    ctx.clearRect(0, 0, width, height);

    // Background Grid
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 22) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 22) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    // 1. Dynamic Factor Array (oscillating between 3x4 and 2x6)
    const arrayPhase = Math.sin(frame * 0.03);
    const cols = (arrayPhase > 0) ? 4 : 6;
    const rows = (arrayPhase > 0) ? 3 : 2;
    const tileSize = 16;
    const startX = 24;
    const startY = 40;

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const tx = startX + c * tileSize;
        const ty = startY + r * tileSize;
        ctx.fillStyle = ((r + c) % 2 === 0) ? 'rgba(245, 158, 11, 0.35)' : 'rgba(217, 119, 6, 0.2)';
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 1.2;
        ctx.fillRect(tx, ty, tileSize - 2, tileSize - 2);
        ctx.strokeRect(tx, ty, tileSize - 2, tileSize - 2);
      }
    }

    // Array label
    ctx.font = 'bold 11px "JetBrains Mono", monospace';
    ctx.fillStyle = '#fbbf24';
    ctx.fillText(`${rows} × ${cols} = 12 Array`, startX, startY - 8);

    // 2. Aligned Stacked Fraction Strips (2/3 and 4/6)
    const stripX = width * 0.52;
    const stripW = width * 0.42;
    const stripH = 18;

    // Top Strip: 2/3
    const strip1Y = 36;
    ctx.strokeStyle = '#38bdf8';
    ctx.strokeRect(stripX, strip1Y, stripW, stripH);
    for (let i = 0; i < 3; i++) {
      const partW = stripW / 3;
      const px = stripX + i * partW;
      if (i < 2) {
        ctx.fillStyle = 'rgba(14, 165, 233, 0.4)';
        ctx.fillRect(px, strip1Y, partW, stripH);
      }
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(px, strip1Y, partW, stripH);
    }
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('2/3', stripX + stripW + 8, strip1Y + 13);

    // Bottom Strip: 4/6
    const strip2Y = strip1Y + stripH + 8;
    ctx.strokeStyle = '#10b981';
    ctx.strokeRect(stripX, strip2Y, stripW, stripH);
    for (let i = 0; i < 6; i++) {
      const partW = stripW / 6;
      const px = stripX + i * partW;
      if (i < 4) {
        ctx.fillStyle = 'rgba(16, 185, 129, 0.4)';
        ctx.fillRect(px, strip2Y, partW, stripH);
      }
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(px, strip2Y, partW, stripH);
    }
    ctx.fillStyle = '#34d399';
    ctx.fillText('4/6', stripX + stripW + 8, strip2Y + 13);

    // Equivalence indicator
    ctx.font = '10px "Inter", sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Aligned: 2/3 = 4/6', stripX, strip2Y + stripH + 16);

    // Bottom Telemetry
    ctx.font = '11px "JetBrains Mono", monospace';
    ctx.fillStyle = '#a78bfa';
    ctx.fillText('Factors • Equivalence • Operations', 20, height - 16);

    frame++;
    requestAnimationFrame(render);
  }

}

// 1d. Dynamic Mini Canvas for 4th Grade Math Q2 Featured Card
function initGrade4Q2MiniCanvas() {
  const canvas = document.getElementById('previewCanvasGrade4Q2');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  let frame = 0;

  function render() {
    const width = canvas.getBoundingClientRect().width;
    const height = canvas.getBoundingClientRect().height;

    ctx.clearRect(0, 0, width, height);

    // Subtle background grid
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 22) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 22) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    // Left Visualizer: 10x10 Decimal Hundredths Grid (Tenths Equivalence)
    const gridX = 22;
    const gridY = 32;
    const gridSide = Math.min(84, height - 60);
    const cellSize = gridSide / 10;

    // Oscillation between 3 tenths (30 hundredths) and 5 tenths (50 hundredths)
    const tenthsCount = 3 + Math.floor(((Math.sin(frame * 0.025) + 1) / 2) * 3); // 3, 4, or 5
    const shadedHundredths = tenthsCount * 10;

    // Draw 10x10 Hundredths Grid
    for (let row = 0; row < 10; row++) {
      for (let col = 0; col < 10; col++) {
        const cx = gridX + col * cellSize;
        const cy = gridY + row * cellSize;
        const isShaded = col < tenthsCount;

        if (isShaded) {
          ctx.fillStyle = ((row + col) % 2 === 0) ? 'rgba(16, 185, 129, 0.45)' : 'rgba(5, 150, 105, 0.35)';
        } else {
          ctx.fillStyle = 'rgba(15, 23, 42, 0.5)';
        }
        ctx.fillRect(cx, cy, cellSize, cellSize);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.07)';
        ctx.strokeRect(cx, cy, cellSize, cellSize);
      }
    }

    // Outer grid border & tenths columns divider
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(gridX, gridY, gridSide, gridSide);

    for (let col = 1; col < 10; col++) {
      ctx.strokeStyle = (col === tenthsCount) ? '#34d399' : 'rgba(16, 185, 129, 0.3)';
      ctx.lineWidth = (col === tenthsCount) ? 2 : 1;
      ctx.beginPath();
      ctx.moveTo(gridX + col * cellSize, gridY);
      ctx.lineTo(gridX + col * cellSize, gridY + gridSide);
      ctx.stroke();
    }

    // Left Label
    ctx.font = 'bold 10px "JetBrains Mono", monospace';
    ctx.fillStyle = '#34d399';
    ctx.fillText(`${tenthsCount}/10 = ${shadedHundredths}/100 = 0.${tenthsCount}`, gridX, gridY - 8);

    // Right Visualizer: Rectilinear L-Shaped Area Decomposition
    const polyLeft = width * 0.48;
    const polyTop = 32;
    const unitScale = Math.min(10, (width * 0.45) / 10);

    // Box A: 6m wide x 4m high -> Area 24 m²
    const wA = 6 * unitScale;
    const hA = 4 * unitScale;
    // Box B: 2m wide x 3m high attached underneath -> Area 6 m²
    const wB = 3 * unitScale;
    const hB = 3 * unitScale;

    // Draw Box A
    ctx.fillStyle = 'rgba(14, 165, 233, 0.35)';
    ctx.fillRect(polyLeft, polyTop, wA, hA);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(polyLeft, polyTop, wA, hA);

    // Draw Box B
    ctx.fillStyle = 'rgba(168, 85, 247, 0.35)';
    ctx.fillRect(polyLeft, polyTop + hA, wB, hB);
    ctx.strokeStyle = '#c084fc';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(polyLeft, polyTop + hA, wB, hB);

    // Dashed internal decomposition line
    ctx.strokeStyle = '#fbbf24';
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(polyLeft, polyTop + hA);
    ctx.lineTo(polyLeft + wB, polyTop + hA);
    ctx.stroke();
    ctx.setLineDash([]);

    // Area labels inside boxes
    ctx.font = 'bold 9px "Inter", sans-serif';
    ctx.fillStyle = '#bae6fd';
    ctx.fillText('A = 24 m²', polyLeft + 8, polyTop + hA / 2 + 3);
    ctx.fillStyle = '#f3e8ff';
    ctx.fillText('B = 9 m²', polyLeft + 4, polyTop + hA + hB / 2 + 3);

    // Total area computation label
    ctx.font = 'bold 10px "JetBrains Mono", monospace';
    ctx.fillStyle = '#22d3ee';
    ctx.fillText('24 + 9 = 33 m²', polyLeft, polyTop - 8);

    // Bottom Telemetry
    ctx.font = '11px "JetBrains Mono", monospace';
    ctx.fillStyle = '#34d399';
    ctx.fillText('Decimals • Partial Products • Area & Line Plots', 20, height - 16);

    frame++;
    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// 2. Search & Subject Filter
function initSearchAndFilter() {
  const searchInput = document.getElementById('appSearchInput');
  const filterPills = document.querySelectorAll('.filter-pill');
  const cards = document.querySelectorAll('.app-item-card');

  function filterCards() {
    const rawQuery = (searchInput?.value || '').toLowerCase().trim();
    const query = rawQuery;
    const normalizedQuery = rawQuery.replace(/[_-\s]+/g, ' ').trim();
    const activePill = document.querySelector('.filter-pill.active')?.dataset.category || 'all';

    cards.forEach(card => {
      const title = card.querySelector('.searchable-title')?.textContent.toLowerCase() || '';
      const desc = card.querySelector('.searchable-desc')?.textContent.toLowerCase() || '';
      const filename = (card.dataset.filename || '').toLowerCase();
      const keywords = (card.dataset.keywords || '').toLowerCase();
      const cardText = card.textContent.toLowerCase();
      const category = card.dataset.category || '';

      const combinedText = `${title} ${desc} ${filename} ${keywords} ${cardText}`;
      const normalizedCombined = combinedText.replace(/[_-\s]+/g, ' ');

      const matchesQuery = !query || 
        combinedText.includes(query) || 
        (normalizedQuery && normalizedCombined.includes(normalizedQuery)) ||
        filename.includes(query);

      const matchesCategory = activePill === 'all' || category === activePill;

      if (matchesQuery && matchesCategory) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  }

  searchInput?.addEventListener('input', filterCards);

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      filterCards();
    });
  });
}

// 3. Modal Runner
function initModalRunner() {
  const modal = document.getElementById('labModal');
  const iframe = document.getElementById('labIframe');
  const modalTitle = document.getElementById('modalLabTitle');
  const openBtns = document.querySelectorAll('.open-modal-btn');
  const closeBtn = document.getElementById('closeModalBtn');
  const reloadBtn = document.getElementById('reloadModalBtn');
  const newTabBtn = document.getElementById('newTabModalBtn');

  if (!modal || !iframe) return;

  openBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetUrl = btn.dataset.url;
      const title = btn.dataset.title || 'Interactive Lab';
      if (modalTitle) modalTitle.textContent = title;
      iframe.src = targetUrl;
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
      if (newTabBtn) newTabBtn.href = targetUrl;
    });
  });

  function closeModal() {
    modal.classList.remove('active');
    iframe.src = 'about:blank';
    document.body.style.overflow = '';
  }

  closeBtn?.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  reloadBtn?.addEventListener('click', () => {
    if (iframe.contentWindow) {
      iframe.contentWindow.location.reload();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
}

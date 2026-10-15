// Portal Interactivity & Dynamic Canvas Visualizer

document.addEventListener('DOMContentLoaded', () => {
  initMiniCanvas();
  initFunctionsMiniCanvas();
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

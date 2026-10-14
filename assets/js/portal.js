// Portal Interactivity & Dynamic Canvas Visualizer

document.addEventListener('DOMContentLoaded', () => {
  initMiniCanvas();
  initSearchAndFilter();
  initModalRunner();
});

// 1. Dynamic Mini Canvas Animation for Featured Card
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

// 2. Search & Subject Filter
function initSearchAndFilter() {
  const searchInput = document.getElementById('appSearchInput');
  const filterPills = document.querySelectorAll('.filter-pill');
  const cards = document.querySelectorAll('.app-item-card');

  function filterCards() {
    const query = (searchInput?.value || '').toLowerCase().trim();
    const activePill = document.querySelector('.filter-pill.active')?.dataset.category || 'all';

    cards.forEach(card => {
      const title = card.querySelector('.searchable-title')?.textContent.toLowerCase() || '';
      const desc = card.querySelector('.searchable-desc')?.textContent.toLowerCase() || '';
      const category = card.dataset.category || '';

      const matchesQuery = !query || title.includes(query) || desc.includes(query);
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

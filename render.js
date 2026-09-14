/* ========================================
   1000 HILLS GROUP - CONTENT RENDERER
   Fetches content.json and injects it into
   whichever containers exist on the page.
   ======================================== */

(function () {

  function esc(str) {
    if (str === undefined || str === null) return '';
    const div = document.createElement('div');
    div.textContent = String(str);
    return div.innerHTML;
  }

  function renderTeam(team, container) {
    if (!container || !Array.isArray(team)) return;
    container.innerHTML = team.map((m, i) => `
      <div class="team-card" data-aos="flip-up" data-aos-delay="${i * 100}">
        <div class="team-image">
          <img src="${esc(m.image)}" alt="${esc(m.name)}" loading="lazy" />
          ${m.badge ? `<span class="team-badge"><i class="${esc(m.badgeIcon || 'fas fa-star')}"></i> ${esc(m.badge)}</span>` : ''}
          <div class="team-socials">
            ${m.socials && m.socials.length ? m.socials.map(s => `
              <a href="${esc(s.url)}" target="_blank"><i class="${esc(s.icon)}"></i></a>
            `).join('') : ''}
          </div>
        </div>
        <div class="team-info">
          <h4>${esc(m.name)}</h4>
          <p class="team-role">${esc(m.role)}</p>
          <p class="team-bio">${esc(m.bio)}</p>
          <div class="team-skills">
            ${(m.skills || []).map(s => `<span>${esc(s)}</span>`).join('')}
          </div>
        </div>
      </div>
    `).join('');
  }

  function renderServicesPreview(services, container) {
    if (!container || !Array.isArray(services)) return;
    container.innerHTML = services.map((s, i) => `
      <div class="service-card" data-aos="flip-up" data-aos-delay="${i * 50}">
        <div class="service-icon"><i class="${esc(s.icon)}"></i></div>
        <h4>${esc(s.title)}</h4>
        <p>${esc(s.shortDesc)}</p>
        <a href="services.html#${esc(s.anchor)}" class="service-link">Learn More <i class="fas fa-arrow-right"></i></a>
      </div>
    `).join('');
  }

  function renderServicesFull(services, container) {
    if (!container || !Array.isArray(services)) return;
    container.innerHTML = services.map((s, i) => `
      <div class="service-full-card" id="${esc(s.anchor)}" data-aos="fade-up" data-aos-delay="${i * 50}">
        <div class="service-full-icon"><i class="${esc(s.icon)}"></i></div>
        <div class="service-full-content">
          <h3>${esc(s.title)}</h3>
          <p class="service-short">${esc(s.shortDesc)}</p>
          <div class="service-expanded" id="exp-${esc(s.anchor)}">
            <p>${esc(s.detailsParagraph)}</p>
            <ul>
              ${(s.detailsList || []).map(li => `<li><i class="fas fa-check"></i> ${esc(li)}</li>`).join('')}
            </ul>
          </div>
          <button class="read-more-btn" aria-expanded="false" aria-controls="exp-${esc(s.anchor)}" onclick="toggleReadMore('${esc(s.anchor)}', this)">Read More <i class="fas fa-chevron-down"></i></button>
        </div>
      </div>
    `).join('');
  }

  function renderClients(clients, container) {
    if (!container || !Array.isArray(clients)) return;
    container.innerHTML = clients.map(c => `
      <div class="client-item">
        <img src="${esc(c.logo)}" alt="${esc(c.name)}" loading="lazy" />
      </div>
    `).join('');
  }

  function renderPortfolio(portfolio, container) {
    if (!container || !Array.isArray(portfolio)) return;
    const cards = portfolio.map((p, i) => {
      const isLive = p.status === 'live';
      return `
      <div class="company-card" data-aos="flip-up" data-aos-delay="${i * 100}">
        <div class="company-logo-wrapper">
          <img src="${esc(p.logo)}" alt="${esc(p.name)}" loading="lazy" />
        </div>
        <h3>${esc(p.name)}</h3>
        <p>${esc(p.description)}</p>
        <span class="company-status ${isLive ? 'live' : 'coming'}">
          <i class="fas fa-${isLive ? 'circle' : 'clock'}"></i> ${isLive ? 'Live' : 'Coming Soon'}
        </span>
        ${isLive && p.url
          ? `<a href="${esc(p.url)}" target="_blank" rel="noopener noreferrer" class="btn-company">Visit Website <i class="fas fa-arrow-right"></i></a>`
          : `<span class="btn-company disabled">Launching Soon</span>`}
      </div>`;
    }).join('');
    container.innerHTML = cards;
  }

  function renderTestimonials(testimonials, container) {
    if (!container || !Array.isArray(testimonials)) return;
    if (testimonials.length === 0) {
      container.closest('section')?.style.setProperty('display', 'none');
      return;
    }
    container.innerHTML = testimonials.map((t, i) => `
      <div class="testimonial-card" data-aos="zoom-in" data-aos-delay="${i * 100}">
        <i class="fas fa-quote-left testimonial-quote-icon"></i>
        <p class="testimonial-text">${esc(t.text)}</p>
        <div class="testimonial-author">
          <h4>${esc(t.company || t.name)}</h4>
          <span>${esc(t.role || 'Client')}</span>
        </div>
      </div>
    `).join('');
  }

  function toggleReadMore(serviceId, btn) {
    const expanded = document.getElementById('exp-' + serviceId);
    if (!expanded) return;
    const isOpen = expanded.classList.toggle('show');
    btn.classList.toggle('active', isOpen);
    btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    btn.innerHTML = isOpen
      ? 'Read Less <i class="fas fa-chevron-up"></i>'
      : 'Read More <i class="fas fa-chevron-down"></i>';
  }

  /* Containers that render.js is responsible for filling. */
  const CONTENT_IDS = [
    'teamGrid', 'servicesGrid', 'servicesGridFull',
    'clientsGrid', 'companiesGrid', 'testimonialsGrid'
  ];

  /* If content.json cannot be fetched (404, opened straight from disk via
     file:// where fetch is blocked, offline, blocked by an extension...) the
     grids would sit there saying "Loading..." forever. Replace those
     placeholders with a real message instead of a fake loading state. */
  function showFallback() {
    const message = 'Content is temporarily unavailable. Please refresh the page, or ' +
      '<a href="contact.html" style="color:#C9A96E;">get in touch</a>.';
    CONTENT_IDS.forEach(function (id) {
      const el = document.getElementById(id);
      if (!el) return;
      if (el.querySelector('.team-card, .service-card, .service-full-card, .client-item, .company-card, .testimonial-card')) return;
      const text = (el.textContent || '').trim();
      if (!text || /loading/i.test(text)) {
        el.innerHTML = '<p style="text-align:center;color:#888;grid-column:1/-1;">' + message + '</p>';
      }
    });
  }

  async function init() {
    let data;
    try {
      const res = await fetch('content.json');
      if (!res.ok) throw new Error('content.json responded ' + res.status);
      data = await res.json();
    } catch (err) {
      console.error('Could not load content.json — falling back to the content already in the HTML.', err);
      showFallback();
      return;
    }

    renderTeam(data.team, document.getElementById('teamGrid'));
    renderServicesPreview(data.services, document.getElementById('servicesGrid'));
    renderServicesFull(data.services, document.getElementById('servicesGridFull'));
    renderClients(data.clients, document.getElementById('clientsGrid'));
    renderPortfolio(data.portfolio, document.getElementById('companiesGrid'));
    renderTestimonials(data.testimonials, document.getElementById('testimonialsGrid'));

    /* Anything still showing a "Loading..." placeholder gets a real message. */
    showFallback();

    if (window.AOS) {
      setTimeout(() => window.AOS.refresh(), 50);
    }
  }

  document.addEventListener('DOMContentLoaded', init);
})();
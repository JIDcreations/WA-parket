/* W&A Parket: hifi V1 interactie */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* ── Header: rand na scrollen, verbergen bij naar beneden scrollen ── */
  const header = $('.header');
  let lastY = window.scrollY, ticking = false;
  const menuOpen = () => !!$('.mega.is-open') || !!$('.drawer.is-open');
  const onScroll = () => {
    const y = window.scrollY;
    header.classList.toggle('is-scrolled', y > 8);
    if (!menuOpen()) header.classList.toggle('is-hidden', y > lastY && y > 240);
    lastY = y; ticking = false;
  };
  if (header) {
    onScroll();
    window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
    header.addEventListener('focusin', () => header.classList.remove('is-hidden'));
  }

  /* ── Menu: dropdowns ─────────────────────────
     Hover opent na een korte pauze (geen per-ongeluk-open), klik en toetsenbord werken altijd.
     Focus die het menu-item verlaat, sluit het paneel. */
  const triggers = $$('.nav__link[aria-controls]');
  const backdrop = $('.mega-backdrop');
  const panelOf = t => $('#' + t.getAttribute('aria-controls'));
  let openTimer, closeTimer;
  const closeAll = () => {
    clearTimeout(openTimer);
    triggers.forEach(t => { t.setAttribute('aria-expanded', 'false'); panelOf(t).classList.remove('is-open'); });
    backdrop && backdrop.classList.remove('is-open');
  };
  const open = t => {
    clearTimeout(closeTimer);
    triggers.forEach(o => { if (o !== t) { o.setAttribute('aria-expanded', 'false'); panelOf(o).classList.remove('is-open'); } });
    t.setAttribute('aria-expanded', 'true');
    panelOf(t).classList.add('is-open');
    backdrop && backdrop.classList.add('is-open');
    header && header.classList.remove('is-hidden');
  };
  const anyOpen = () => triggers.some(t => t.getAttribute('aria-expanded') === 'true');
  const hoverable = window.matchMedia('(hover: hover)').matches;
  triggers.forEach(t => {
    const item = t.parentElement;
    t.addEventListener('click', () => t.getAttribute('aria-expanded') === 'true' ? closeAll() : open(t));
    t.addEventListener('keydown', e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); open(t); panelOf(t).querySelector('a')?.focus(); }
    });
    item.addEventListener('focusout', e => { if (!item.contains(e.relatedTarget)) { t.setAttribute('aria-expanded', 'false'); panelOf(t).classList.remove('is-open'); if (!anyOpen()) backdrop.classList.remove('is-open'); } });
    if (hoverable) {
      item.addEventListener('mouseenter', () => { clearTimeout(closeTimer); clearTimeout(openTimer); openTimer = setTimeout(() => open(t), anyOpen() ? 0 : 90); });
      item.addEventListener('mouseleave', () => { clearTimeout(openTimer); closeTimer = setTimeout(closeAll, 180); });
    }
  });
  document.addEventListener('click', e => { if (!e.target.closest('.nav__item')) closeAll(); });
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    const openT = triggers.find(t => t.getAttribute('aria-expanded') === 'true');
    closeAll(); openT && openT.focus();
    closeDrawer(); closeFilters();
  });

  /* ── Menu: toon waar je bent op de homepage ── */
  const spyLinks = $$('.nav__link[href^="index.html#"]');
  if (spyLinks.length && 'IntersectionObserver' in window) {
    const map = new Map();
    spyLinks.forEach(l => { const sec = document.getElementById(l.hash.slice(1)); if (sec) map.set(sec, l); });
    const io = new IntersectionObserver(entries => entries.forEach(en => map.get(en.target)?.classList.toggle('is-current', en.isIntersecting)), { rootMargin: '-45% 0px -45% 0px' });
    map.forEach((_, sec) => io.observe(sec));
  }

  /* ── Mobiel menu ─────────────────────────────── */
  const drawer = $('#drawer');
  const burger = $('.burger');
  function closeDrawer() {
    if (!drawer || !drawer.classList.contains('is-open')) return;
    drawer.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = ''; burger.focus();
  }
  burger && burger.addEventListener('click', () => {
    drawer.classList.add('is-open'); burger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden'; $('.drawer__close', drawer).focus();
  });
  drawer && $('.drawer__close', drawer).addEventListener('click', closeDrawer);
  drawer && $$('a', drawer).forEach(a => a.addEventListener('click', closeDrawer));
  $$('.drawer__group > button').forEach(b => b.addEventListener('click', () => {
    const on = b.getAttribute('aria-expanded') !== 'true';
    b.setAttribute('aria-expanded', String(on));
    $('#' + b.getAttribute('aria-controls')).classList.toggle('is-open', on);
  }));

  /* ── Openingsuren: vandaag ───────────────────── */
  const day = new Date().getDay(); // 0 = zondag
  const hrs = new Date().getHours();
  $$('[data-hours] [data-day]').forEach(el => {
    if (el.dataset.day.split(' ').includes(String(day))) el.classList.add('is-today');
  });
  const today = $('[data-open-today]');
  if (today) {
    const slots = { 2: [13, 18], 3: [13, 18], 4: [13, 18], 5: [13, 18], 6: [10, 18] };
    const s = slots[day];
    if (s && hrs < s[1]) today.textContent = hrs >= s[0] ? `Toonzaal nu open, tot ${s[1]}u` : `Toonzaal vandaag open van ${s[0]}u tot ${s[1]}u`;
    else today.textContent = day === 6 || day === 0 || (day === 1) ? 'Toonzaal weer open op dinsdag vanaf 13u' : 'Toonzaal morgen open vanaf ' + (day === 5 ? '10u' : '13u');
  }

  /* ── Collectie: filters ──────────────────────── */
  const form = $('#filter-form');
  let closeFilters = () => {};
  if (form) {
    const cards = $$('.card[data-type]', $('[data-grid]'));
    const grid = $('[data-grid]');
    const chips = $('[data-chips]');
    const empty = $('[data-empty]');
    const countEls = $$('[data-count], [data-count-label], [data-shown]');
    const quick = $$('[data-quick]');
    const activeN = $('[data-active-n]');
    const sheet = $('#filters');
    const opener = $('.filter-open');
    const labelFor = input => input.closest('label').querySelector('span:nth-of-type(2)').textContent;

    const selected = () => {
      const sel = {};
      $$('input:checked', form).forEach(i => (sel[i.name] ||= []).push(i.value));
      return sel;
    };
    const matches = (card, sel, skip) => Object.entries(sel).every(([k, vals]) => k === skip || vals.includes(card.dataset[k]));

    const apply = (push = true) => {
      const sel = selected();
      let n = 0;
      cards.forEach(c => { const ok = matches(c, sel); c.hidden = !ok; if (ok) n++; });
      countEls.forEach(el => (el.textContent = n));
      empty.hidden = n !== 0;

      // aantallen per optie, rekening houdend met de andere groepen
      $$('.check', form).forEach(l => {
        const i = $('input', l);
        const c = cards.filter(card => matches(card, sel, i.name) && card.dataset[i.name] === i.value).length;
        $('.check__count', l).textContent = c;
        l.classList.toggle('is-empty', c === 0 && !i.checked);
      });

      // chips
      chips.innerHTML = '';
      const checked = $$('input:checked', form);
      checked.forEach(i => {
        const b = document.createElement('button');
        b.type = 'button'; b.className = 'chip';
        b.innerHTML = `${labelFor(i)} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg>`;
        b.setAttribute('aria-label', `Filter ${labelFor(i)} verwijderen`);
        b.addEventListener('click', () => { i.checked = false; apply(); });
        chips.appendChild(b);
      });
      if (checked.length) {
        const r = document.createElement('button');
        r.type = 'button'; r.className = 'link'; r.textContent = 'Wis alle filters';
        r.addEventListener('click', reset);
        chips.appendChild(r);
      }
      activeN.textContent = checked.length ? `(${checked.length})` : '';
      const more = $('.more'); if (more) more.hidden = checked.length > 0;

      // snelkeuze synchroniseren
      const types = sel.type || [];
      quick.forEach(q => q.setAttribute('aria-pressed', String(q.dataset.quick === '' ? types.length === 0 : types.length === 1 && types[0] === q.dataset.quick)));

      if (push) {
        const p = new URLSearchParams();
        Object.entries(sel).forEach(([k, v]) => p.set(k, v.join(',')));
        history.replaceState(null, '', p.toString() ? '?' + p : location.pathname);
      }
    };
    function reset() { $$('input', form).forEach(i => (i.checked = false)); apply(); }

    form.addEventListener('change', () => apply());
    $$('[data-reset]').forEach(b => b.addEventListener('click', reset));
    quick.forEach(q => q.addEventListener('click', () => {
      $$('input[name="type"]', form).forEach(i => (i.checked = i.value === q.dataset.quick));
      apply();
    }));
    $$('.fgroup__toggle').forEach(t => t.addEventListener('click', () => {
      const on = t.getAttribute('aria-expanded') !== 'true';
      t.setAttribute('aria-expanded', String(on));
      $('#' + t.getAttribute('aria-controls')).hidden = !on;
    }));

    // sorteren
    const order = cards.slice();
    $('#sort').addEventListener('change', e => {
      const v = e.target.value;
      const sorted = order.slice();
      if (v === 'promo') sorted.sort((a, b) => b.dataset.promo - a.dataset.promo);
      if (v === 'az') sorted.sort((a, b) => $('h3', a).textContent.localeCompare($('h3', b).textContent, 'nl'));
      sorted.forEach(c => grid.insertBefore(c, empty));
    });

    // mobiele bottom sheet
    closeFilters = () => {
      if (!sheet.classList.contains('is-open')) return;
      sheet.classList.remove('is-open'); opener.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = ''; opener.focus();
    };
    opener.addEventListener('click', () => {
      sheet.classList.add('is-open'); opener.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    });
    $$('.filters__close, [data-close-filters]').forEach(b => b.addEventListener('click', closeFilters));

    // URL → filters (links uit het megamenu)
    new URLSearchParams(location.search).forEach((v, k) => v.split(',').forEach(val => {
      const i = $(`input[name="${k}"][value="${val}"]`, form);
      if (i) i.checked = true;
    }));
    apply(false);
  }

  /* ── Productgalerij ──────────────────────────── */
  const gal = $('[data-gallery]');
  if (gal) {
    const main = $('[data-main]', gal);
    const idx = $('[data-idx]', gal);
    const thumbs = $$('.gallery__thumbs button', gal);
    thumbs.forEach((b, n) => b.addEventListener('click', () => {
      thumbs.forEach(t => t.setAttribute('aria-current', 'false'));
      b.setAttribute('aria-current', 'true');
      main.src = b.dataset.src; main.alt = b.dataset.alt; idx.textContent = n + 1;
    }));
  }

  /* ── Afspraakformulier (prototype: geen verzending) ── */
  const bf = $('#booking-form');
  if (bf) {
    const q = new URLSearchParams(location.search);
    const intent = q.get('intent');
    if (intent) { const r = $(`input[name="intent"][value="${intent}"]`, bf); if (r) r.checked = true; }
    if (q.get('product')) $('#f-msg').value = `Interesse in: ${q.get('product')}\n`;
    bf.addEventListener('submit', e => {
      e.preventDefault();
      const bad = $$('[required]', bf).filter(f => !f.checkValidity());
      $$('.field', bf).forEach(f => f.querySelector('.field__err')?.remove());
      bad.forEach(f => {
        f.setAttribute('aria-invalid', 'true');
        const m = document.createElement('p');
        m.className = 'field__err small'; m.style.color = 'var(--wa-rood)';
        m.textContent = f.type === 'email' && f.value ? 'Vul een geldig e-mailadres in, bijvoorbeeld naam@voorbeeld.be.' : 'Vul dit veld in zodat we u kunnen bereiken.';
        f.after(m);
      });
      if (bad.length) { bad[0].focus(); return; }
      bf.classList.add('is-sent');
      $('.form__done', bf).focus();
    });
  }
})();

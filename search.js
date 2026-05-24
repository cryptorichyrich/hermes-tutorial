// Hermes Tutorial — Client-side search with smooth scroll navigation
(function() {
    'use strict';

    const IDX_URL = 'search-index.json';
    let searchData = null;
    let activeIdx = -1;

    const bar = document.getElementById('searchToggle');
    const input = document.getElementById('searchInput');
    const dropdown = document.getElementById('searchDropdown');

    if (!bar || !input || !dropdown) return;

    // Load index on first focus
    async function loadIndex() {
        if (searchData) return;
        try {
            const res = await fetch(IDX_URL);
            searchData = await res.json();
        } catch (e) {
            console.error('Failed to load search index:', e);
            searchData = [];
        }
    }

    // Toggle search open/closed
    function openSearch() {
        bar.classList.add('open');
        input.focus();
        loadIndex();
    }

    function closeSearch() {
        bar.classList.remove('open');
        input.value = '';
        dropdown.classList.remove('open');
        dropdown.innerHTML = '';
        activeIdx = -1;
    }

    bar.addEventListener('click', function(e) {
        // If clicking the input itself, don't toggle closed
        if (e.target === input) return;
        if (bar.classList.contains('open')) {
            closeSearch();
        } else {
            openSearch();
        }
    });

    // Also open on direct input focus
    input.addEventListener('focus', function() {
        if (!bar.classList.contains('open')) openSearch();
    });

    // Keyboard shortcut: Ctrl+K or Cmd+K
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            openSearch();
        }
        if (e.key === 'Escape') {
            closeSearch();
        }
    });

    // Close on outside click
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.nav-search')) {
            closeSearch();
        }
    });

    // Search logic
    input.addEventListener('input', function() {
        const query = this.value.trim().toLowerCase();
        if (query.length < 2) {
            dropdown.classList.remove('open');
            dropdown.innerHTML = '';
            activeIdx = -1;
            return;
        }

        if (!searchData) return;

        const terms = query.split(/\s+/).filter(t => t.length > 0);

        const scored = searchData.map(function(section) {
            const text = (section.heading + ' ' + section.content).toLowerCase();
            let score = 0;
            terms.forEach(function(term) {
                if (text.includes(term)) score += 1;
                if (section.heading.toLowerCase().includes(term)) score += 3;
            });
            return { section: section, score: score };
        }).filter(function(r) { return r.score > 0; })
          .sort(function(a, b) { return b.score - a.score; })
          .slice(0, 12);

        dropdown.innerHTML = '';
        activeIdx = -1;

        if (scored.length === 0) {
            dropdown.innerHTML = '<div class="sr-empty">No results found</div>';
            dropdown.classList.add('open');
            return;
        }

        // Group by chapter
        const groups = {};
        scored.forEach(function(r) {
            const ch = r.section.chapter;
            if (!groups[ch]) groups[ch] = [];
            groups[ch].push(r.section);
        });

        Object.keys(groups).forEach(function(ch) {
            const label = document.createElement('div');
            label.className = 'sr-label';
            label.textContent = ch;
            dropdown.appendChild(label);

            groups[ch].forEach(function(section) {
                const item = document.createElement('a');
                item.className = 'sr-item';
                item.href = section.url;

                let html = '<div class="sr-item-heading">' + escHtml(section.heading) + '</div>';
                if (section.content) {
                    const snippet = getSnippet(section.content, terms[0]);
                    html += '<div class="sr-item-snippet">' + highlightTerms(escHtml(snippet), terms) + '</div>';
                }
                item.innerHTML = html;

                item.addEventListener('click', function(e) {
                    // If same page, smooth scroll
                    const hash = section.url.split('#')[1];
                    if (hash && isSamePage(section.url)) {
                        e.preventDefault();
                        const target = document.getElementById(hash);
                        if (target) {
                            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                            closeSearch();
                        }
                    }
                });

                dropdown.appendChild(item);
            });
        });

        dropdown.classList.add('open');
    });

    // Keyboard navigation in dropdown
    input.addEventListener('keydown', function(e) {
        const items = dropdown.querySelectorAll('.sr-item');
        if (!items.length) return;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            activeIdx = Math.min(activeIdx + 1, items.length - 1);
            updateActive(items);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            activeIdx = Math.max(activeIdx - 1, 0);
            updateActive(items);
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (activeIdx >= 0 && items[activeIdx]) {
                items[activeIdx].click();
            }
        }
    });

    function updateActive(items) {
        items.forEach(function(it, i) {
            it.classList.toggle('active', i === activeIdx);
            if (i === activeIdx) it.scrollIntoView({ block: 'nearest' });
        });
    }

    function escHtml(str) {
        return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function getSnippet(text, term) {
        const idx = text.toLowerCase().indexOf(term);
        if (idx === -1) return text.slice(0, 120);
        const start = Math.max(0, idx - 40);
        const end = Math.min(text.length, idx + 80);
        let s = text.slice(start, end);
        if (start > 0) s = '…' + s;
        if (end < text.length) s += '…';
        return s;
    }

    function highlightTerms(html, terms) {
        terms.forEach(function(term) {
            const re = new RegExp('(' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
            html = html.replace(re, '<mark>$1</mark>');
        });
        return html;
    }

    function isSamePage(url) {
        const path = url.split('#')[0];
        return path === '' || path === location.pathname.split('/').pop();
    }
})();

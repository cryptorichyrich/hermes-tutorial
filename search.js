// Hermes Tutorial — Client-side search with smooth scroll navigation
(function() {
    'use strict';

    const IDX_URL = 'search-index.json';
    let searchData = null;
    let activeIdx = -1;

    const input = document.getElementById('searchInput');
    const toggle = document.getElementById('searchToggle');
    const dropdown = document.getElementById('searchDropdown');

    if (!input || !dropdown) return;

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
        input.classList.add('open');
        input.focus();
        loadIndex();
    }

    function closeSearch() {
        input.classList.remove('open');
        input.value = '';
        dropdown.classList.remove('open');
        dropdown.innerHTML = '';
        activeIdx = -1;
    }

    toggle.addEventListener('click', function() {
        if (input.classList.contains('open')) {
            closeSearch();
        } else {
            openSearch();
        }
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
        const results = [];

        for (const entry of searchData) {
            const text = (entry.heading + ' ' + entry.text).toLowerCase();
            let score = 0;
            let allMatch = true;

            for (const term of terms) {
                if (text.includes(term)) {
                    // Heading match scores higher
                    if (entry.heading.toLowerCase().includes(term)) score += 10;
                    // Count occurrences in text
                    const matches = text.split(term).length - 1;
                    score += matches;
                } else {
                    allMatch = false;
                }
            }

            if (allMatch && score > 0) {
                results.push({ ...entry, score });
            }
        }

        // Sort by score descending
        results.sort((a, b) => b.score - a.score);

        // Take top 8
        const top = results.slice(0, 8);
        activeIdx = -1;

        if (top.length === 0) {
            dropdown.innerHTML = '<div class="sr-empty">No results for "' + escapeHtml(query) + '"</div>';
            dropdown.classList.add('open');
            return;
        }

        let html = '<div class="sr-label">Results</div>';
        top.forEach((r, i) => {
            const snippet = highlightSnippet(r.text, terms);
            html += '<div class="sr-item" data-idx="' + i + '" data-url="' + r.slug + '.html#' + r.headingId + '">' +
                '<div class="sr-item-chapter">Ch ' + r.ch + ' · ' + escapeHtml(r.chTitle.split('—')[0].trim()) + '</div>' +
                '<div class="sr-item-heading">' + highlightText(r.heading, terms) + '</div>' +
                '<div class="sr-item-snippet">' + snippet + '</div>' +
            '</div>';
        });

        dropdown.innerHTML = html;
        dropdown.classList.add('open');

        // Click handler for results
        dropdown.querySelectorAll('.sr-item').forEach(function(item) {
            item.addEventListener('click', function() {
                navigateTo(this.dataset.url);
            });
        });
    });

    // Keyboard navigation within dropdown
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
        } else if (e.key === 'Enter' && activeIdx >= 0) {
            e.preventDefault();
            navigateTo(items[activeIdx].dataset.url);
        }
    });

    function updateActive(items) {
        items.forEach(function(el, i) {
            el.classList.toggle('active', i === activeIdx);
        });
        if (activeIdx >= 0 && items[activeIdx]) {
            items[activeIdx].scrollIntoView({ block: 'nearest' });
        }
    }

    // Navigate to page and smooth-scroll to section
    function navigateTo(url) {
        const [page, hash] = url.split('#');
        const currentPage = location.pathname.split('/').pop() || 'index.html';

        if (page === currentPage) {
            // Same page — scroll directly
            scrollToHash(hash);
            closeSearch();
        } else {
            // Different page — navigate with hash
            location.href = url;
        }
    }

    function scrollToHash(hash) {
        if (!hash || hash === 'top') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
            return;
        }
        // Try to find the heading by ID
        let target = document.getElementById(hash);
        if (!target) {
            // Try matching heading text content
            const headings = document.querySelectorAll('h1, h2, h3');
            const slugify = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
            for (const h of headings) {
                if (slugify(h.textContent) === hash) {
                    target = h;
                    break;
                }
            }
        }
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            // Flash highlight
            target.style.transition = 'background 0.3s';
            target.style.background = '#eef2ff';
            target.style.borderRadius = '4px';
            setTimeout(function() {
                target.style.background = '';
            }, 1500);
        }
    }

    // On page load, if there's a hash, smooth scroll to it
    if (location.hash) {
        setTimeout(function() {
            scrollToHash(location.hash.slice(1));
        }, 300);
    }

    // Highlight matching text
    function highlightText(text, terms) {
        let result = escapeHtml(text);
        for (const term of terms) {
            const re = new RegExp('(' + escapeRegex(term) + ')', 'gi');
            result = result.replace(re, '<mark>$1</mark>');
        }
        return result;
    }

    function highlightSnippet(text, terms) {
        // Find the best 120-char window containing the most terms
        const lower = text.toLowerCase();
        let bestPos = 0;
        let bestCount = 0;

        for (let i = 0; i < text.length - 40; i += 20) {
            const window = lower.slice(i, i + 140);
            let count = 0;
            for (const t of terms) {
                const idx = window.indexOf(t);
                if (idx >= 0) count++;
            }
            if (count > bestCount) {
                bestCount = count;
                bestPos = i;
            }
        }

        let snippet = text.slice(bestPos, bestPos + 140);
        if (bestPos > 0) snippet = '…' + snippet;
        if (bestPos + 140 < text.length) snippet += '…';

        return highlightText(snippet, terms);
    }

    function escapeHtml(s) {
        return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function escapeRegex(s) {
        return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }
})();

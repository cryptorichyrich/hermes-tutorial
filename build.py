#!/usr/bin/env python3
"""
Build static HTML pages for Hermes Tutorial.
Pre-renders markdown with Mermaid diagrams, full SEO, and biotama.cv links.
"""
import os
import re
import json
import markdown
from pathlib import Path

BASE_DIR = Path(__file__).parent
SITE_URL = "https://cryptorichyrich.github.io/hermes-tutorial"
AUTHOR_URL = "https://biotama.cv"
AUTHOR_NAME = "Bio"
AUTHOR_TITLE = "System Architect · Fintech Engineer"

CHAPTERS = [
    {
        "num": 1,
        "file": "ch01-hello-hermes.md",
        "slug": "ch01-hello-hermes",
        "title": "Hello Hermes — Install, First Run, and Your 5-Minute Win",
        "description": "Get started with Hermes Agent in 5 minutes. Install, configure, and run your first AI agent task. Covers the Harness Framework, Three Tools Three Jobs, and system requirements.",
        "keywords": "Hermes Agent install, AI agent setup, Harness Engineering, Hermes vs Claude Code, Hermes vs OpenClaw, AI agent tutorial",
    },
    {
        "num": 2,
        "file": "ch02-core-concepts.md",
        "slug": "ch02-core-concepts",
        "title": "Core Concepts — Agent Loop, Models, and Tools",
        "description": "Understand how Hermes Agent works internally. The Agent Loop, model selection (GPT-4, Claude, Gemini, DeepSeek, local LLMs), 40+ built-in tools, and execution pipeline explained.",
        "keywords": "Hermes Agent loop, LLM model selection, AI agent tools, agent execution pipeline, OpenRouter, Hermes architecture",
    },
    {
        "num": 3,
        "file": "ch03-messaging-gateway.md",
        "slug": "ch03-messaging-gateway",
        "title": "Messaging Gateway — AI Everywhere, Always Online",
        "description": "Connect Hermes Agent to Telegram, Discord, Slack, WhatsApp, and 14 platforms. Voice messages, slash commands, deployment costs, and production hardening.",
        "keywords": "Hermes Telegram bot, AI agent Discord, messaging gateway, voice transcription, Hermes deployment cost, VPS setup",
    },
    {
        "num": 4,
        "file": "ch04-skills-memory.md",
        "slug": "ch04-skills-memory",
        "title": "Skills & Memory — How Hermes Gets Smarter Over Time",
        "description": "The Learning Loop that makes Hermes self-improving. Skills system, memory architecture, session search, and the Curator that maintains your skill library automatically.",
        "keywords": "Hermes skills, AI agent memory, self-improving agent, Learning Loop, skill curator, session search, agentskills.io",
    },
    {
        "num": 5,
        "file": "ch05-automation-scheduling.md",
        "slug": "ch05-automation-scheduling",
        "title": "Automation — Cron Jobs, Webhooks, and Background Tasks",
        "description": "Automate everything with Hermes. Cron scheduling, webhook integrations, background processes, job chaining, and the zero-cost gateway heartbeat that keeps your agent alive 24/7.",
        "keywords": "Hermes cron jobs, AI automation, webhook integration, background tasks, gateway heartbeat, zero-token watchdog",
    },
    {
        "num": 6,
        "file": "ch06-multi-agent.md",
        "slug": "ch06-multi-agent",
        "title": "Multi-Agent Orchestration — An Army of One",
        "description": "Delegate tasks to subagents running in parallel. Kanban workflows, agent orchestration, and building multi-agent pipelines that scale your productivity.",
        "keywords": "Hermes multi-agent, AI delegation, subagent orchestration, Kanban workflow, parallel AI agents",
    },
    {
        "num": 7,
        "file": "ch07-advanced-config.md",
        "slug": "ch07-advanced-config",
        "title": "Advanced Configuration — Security, MCP, and Local Models",
        "description": "Master Hermes configuration. 4-layer security model, MCP integration for 6000+ apps, profiles, local LLMs with Ollama, and running Hermes on Android.",
        "keywords": "Hermes security, MCP integration, Ollama local LLM, Hermes profiles, Android AI agent, Hermes advanced config",
    },
    {
        "num": 8,
        "file": "ch08-power-techniques.md",
        "slug": "ch08-power-techniques",
        "title": "Power Techniques — YOLO Mode, Goals, and Self-Debugging",
        "description": "Expert techniques for power users. YOLO mode for autonomous execution, goal-driven conversations, steering mid-task, model switching, context management, and self-debugging.",
        "keywords": "Hermes YOLO mode, AI agent goals, self-debugging AI, context window management, model switching, power user techniques",
    },
    {
        "num": 9,
        "file": "ch09-business-use-cases.md",
        "slug": "ch09-business-use-cases",
        "title": "Real Business Use Cases — 10 Scenarios with ROI Numbers",
        "description": "10 real business scenarios automated with Hermes Agent, complete with ROI calculations. Content marketing, code review, e-commerce, SaaS monitoring, and lead generation.",
        "keywords": "Hermes business use cases, AI agent ROI, automated content marketing, AI code review, SaaS monitoring agent",
    },
    {
        "num": 10,
        "file": "ch10-business-around-hermes.md",
        "slug": "ch10-business-around-hermes",
        "title": "Building a Business Around Hermes — Pricing, White-Label, and Scaling",
        "description": "Turn Hermes Agent into a business. Pricing models, white-label solutions, agency setup, scaling strategies, and cost optimization for AI agent services.",
        "keywords": "Hermes business model, AI agent pricing, white-label AI, AI agency, Hermes scaling, AI agent costs",
    },
]


def render_markdown(md_text: str) -> str:
    """Convert markdown to HTML, preserving mermaid blocks."""
    # Extract mermaid blocks before markdown processing
    mermaid_blocks = {}
    counter = [0]
    def replace_mermaid(match):
        key = f"MERMAID_BLOCK_{counter[0]}"
        mermaid_blocks[key] = match.group(1).strip()
        counter[0] += 1
        return f"\n\n{key}\n\n"

    md_text = re.sub(r"```mermaid\n([\s\S]*?)```", replace_mermaid, md_text)

    # Render markdown
    html = markdown.markdown(
        md_text,
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
            "attr_list",
            "md_in_html",
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": True},
        },
    )

    # Add IDs to h2/h3 headings for search scroll targets
    def add_heading_ids(html):
        import hashlib
        def replacer(match):
            tag = match.group(1)
            attrs = match.group(2) or ''
            text = match.group(3)
            # Generate slug from text
            slug = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', text).lower()).strip('-')
            if not slug:
                slug = 'section-' + hashlib.md5(text.encode()).hexdigest()[:6]
            if 'id=' not in attrs:
                return f'<{tag}{attrs} id="{slug}">{text}'
            return match.group(0)
        return re.sub(r'<(h[1-3])(\s[^>]*)?>(.+?)</h[1-3]>', replacer, html)

    html = add_heading_ids(html)

    # Restore mermaid blocks as divs
    for key, code in mermaid_blocks.items():
        html = html.replace(f"<p>{key}</p>", f'<div class="mermaid">{code}</div>')
        html = html.replace(key, f'<div class="mermaid">{code}</div>')

    return html


def build_page(chapter: dict, prev_ch: dict | None, next_ch: dict | None) -> str:
    """Build a full HTML page for a chapter."""
    md_path = BASE_DIR / chapter["file"]
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    content_html = render_markdown(md_text)
    ch = chapter["num"]
    url = f"{SITE_URL}/{chapter['slug']}.html"

    # Breadcrumbs
    breadcrumbs = f"""
    <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="sep">›</span>
        <span>Chapter {ch}</span>
    </nav>
    """

    # Chapter navigation
    nav_html = '<nav class="chapter-nav" aria-label="Chapter navigation">'
    if prev_ch:
        nav_html += f'<a href="{prev_ch["slug"]}.html" class="prev">← Ch {prev_ch["num"]}: {prev_ch["title"].split("—")[0].strip()}</a>'
    else:
        nav_html += '<span></span>'
    if next_ch:
        nav_html += f'<a href="{next_ch["slug"]}.html" class="next">Ch {next_ch["num"]}: {next_ch["title"].split("—")[0].strip()} →</a>'
    nav_html += '</nav>'

    # Author bio (subtle, end of page)
    author_bio = f"""
    <aside class="author-bio">
        <div class="author-avatar">B</div>
        <div class="author-info">
            <strong>{AUTHOR_NAME}</strong> · <a href="{AUTHOR_URL}" target="_blank" rel="noopener">{AUTHOR_TITLE}</a>
            <p>Building AI-powered systems in production. More at <a href="{AUTHOR_URL}" target="_blank" rel="noopener">biotama.cv</a></p>
        </div>
    </aside>
    """

    # Schema.org JSON-LD
    schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": chapter["title"],
        "description": chapter["description"],
        "author": {
            "@type": "Person",
            "name": AUTHOR_NAME,
            "url": AUTHOR_URL,
            "jobTitle": AUTHOR_TITLE,
        },
        "publisher": {
            "@type": "Person",
            "name": AUTHOR_NAME,
            "url": AUTHOR_URL,
        },
        "url": url,
        "mainEntityOfPage": url,
        "isPartOf": {
            "@type": "TechArticle",
            "name": "Hermes Agent — The Complete Tutorial",
            "url": SITE_URL,
        },
        "programmingLanguage": "Python",
        "about": {
            "@type": "SoftwareApplication",
            "name": "Hermes Agent",
            "url": "https://github.com/nousresearch/hermes-agent",
            "applicationCategory": "DeveloperApplication",
        },
    }

    # Build nav links
    nav_links = ""
    for c in CHAPTERS:
        active = ' class="active"' if c["num"] == ch else ""
        nav_links += f'<a href="{c["slug"]}.html"{active}>Ch {c["num"]}</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter["title"]} | Hermes Agent Tutorial</title>
    <meta name="description" content="{chapter["description"]}">
    <meta name="keywords" content="{chapter["keywords"]}">
    <meta name="author" content="{AUTHOR_NAME}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{chapter["title"]}">
    <meta property="og:description" content="{chapter["description"]}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Hermes Agent Tutorial">
    <meta property="article:author" content="{AUTHOR_URL}">
    <meta property="article:section" content="Chapter {ch}">
    <meta property="article:tag" content="Hermes Agent">
    <meta property="article:tag" content="AI Agent">
    <meta property="article:tag" content="Nous Research">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{chapter["title"]}">
    <meta name="twitter:description" content="{chapter["description"]}">

    <!-- Schema.org -->
    <script type="application/ld+json">{json.dumps(schema, indent=2)}</script>

    <!-- Styles -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@300&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-light.min.css">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
    <style>
        :root {{
            --primary: #292524;
            --primary-active: #0c0a09;
            --ink: #0c0a09;
            --body: #4e4e4e;
            --body-strong: #292524;
            --muted: #777169;
            --muted-soft: #a8a29e;
            --hairline: #e7e5e4;
            --hairline-soft: #f0efed;
            --hairline-strong: #d6d3d1;
            --canvas: #f5f5f5;
            --canvas-soft: #fafafa;
            --surface-card: #ffffff;
            --gradient-mint: #a7e5d3;
            --gradient-peach: #f4c5a8;
            --gradient-lavender: #c8b8e0;
            --gradient-sky: #a8c8e8;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--canvas);
            color: var(--body);
            line-height: 1.5;
            letter-spacing: 0.16px;
        }}

        /* Top bar */
        .nav {{
            position: fixed; top: 0; left: 0; right: 0; height: 64px;
            background: rgba(250,250,250,0.95); backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--hairline);
            display: flex; align-items: center; padding: 0 20px; z-index: 100;
        }}
        .nav-brand {{
            font-family: 'Inter', sans-serif;
            font-weight: 500; font-size: 15px; color: var(--ink);
            text-decoration: none; display: flex; align-items: center; gap: 6px;
            letter-spacing: 0;
        }}
        .nav-brand span {{ 
            font-family: 'EB Garamond', 'Times New Roman', serif;
            font-weight: 300; font-size: 24px; letter-spacing: -0.32px;
        }}
        .nav-links {{
            display: flex; gap: 2px; margin-left: 24px; overflow-x: auto;
        }}
        .nav-links a {{
            padding: 4px 12px; border-radius: 9999px; color: var(--muted);
            text-decoration: none; font-size: 15px; font-weight: 500;
            white-space: nowrap; transition: all 0.2s; letter-spacing: 0;
        }}
        .nav-links a:hover, .nav-links a.active {{
            background: var(--primary); color: white;
        }}

        /* Search — integrated bar */
        .nav-search {{ margin-left: auto; position: relative; }}
        .nav-search-bar {{
            display: flex; align-items: center; gap: 8px;
            background: var(--surface-card); border: 1px solid var(--hairline);
            border-radius: 9999px; padding: 6px 14px;
            cursor: pointer; transition: all 0.25s ease; min-width: 44px;
        }}
        .nav-search-bar:hover, .nav-search-bar.open {{ border-color: var(--ink); }}
        .nav-search-bar.open {{ min-width: 260px; }}
        .nav-search-bar svg {{
            width: 16px; height: 16px; stroke: var(--muted); fill: none;
            stroke-width: 2; flex-shrink: 0; transition: stroke 0.2s;
        }}
        .nav-search-bar:hover svg, .nav-search-bar.open svg {{ stroke: var(--ink); }}
        .nav-search-bar input {{
            border: none; outline: none; background: transparent;
            color: var(--ink); font-size: 14px; font-family: inherit;
            letter-spacing: 0; width: 0; padding: 0;
            transition: width 0.25s ease;
        }}
        .nav-search-bar.open input {{ width: 200px; }}
        .nav-search-bar input::placeholder {{ color: var(--muted); }}

        /* Search dropdown */
        .search-dropdown {{
            position: absolute; top: 44px; right: 0; width: 420px;
            max-height: 480px; overflow-y: auto;
            background: var(--surface-card); border-radius: 16px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04), 0 0 0 1px var(--hairline);
            z-index: 200; display: none;
        }}
        .search-dropdown.open {{ display: block; }}
        .search-dropdown .sr-label {{
            padding: 10px 16px 6px; font-size: 12px; font-weight: 600;
            text-transform: uppercase; letter-spacing: 0.96px;
            color: var(--muted); border-bottom: 1px solid var(--hairline);
        }}
        .search-dropdown .sr-item {{
            display: block; padding: 10px 16px; text-decoration: none;
            color: var(--ink); transition: background 0.15s; cursor: pointer;
            border-bottom: 1px solid var(--hairline-soft);
        }}
        .search-dropdown .sr-item:hover, .search-dropdown .sr-item.active {{
            background: var(--canvas);
        }}
        .search-dropdown .sr-item:last-child {{ border-bottom: none; }}
        .sr-item-chapter {{
            font-size: 12px; font-weight: 600; color: var(--primary);
            margin-bottom: 2px; text-transform: uppercase; letter-spacing: 0.96px;
        }}
        .sr-item-heading {{
            font-weight: 500; font-size: 16px; margin-bottom: 2px; color: var(--ink);
        }}
        .sr-item-snippet {{
            font-size: 15px; color: var(--body); line-height: 1.4; letter-spacing: 0.15px;
        }}
        .sr-item-snippet mark {{
            background: #fef08a; color: var(--ink); padding: 0 2px;
            border-radius: 2px;
        }}
        .sr-empty {{
            padding: 24px 16px; text-align: center; color: var(--muted);
            font-size: 15px; letter-spacing: 0.15px;
        }}
        .sr-kbd {{
            display: inline-block; padding: 1px 6px; border-radius: 9999px;
            background: var(--canvas); border: 1px solid var(--hairline);
            font-size: 12px; font-family: monospace; color: var(--muted);
        }}

        .container {{
            max-width: 860px; margin: 96px auto 60px; padding: 0 20px;
        }}

        /* Breadcrumbs */
        .breadcrumbs {{
            font-size: 15px; color: var(--muted); margin-bottom: 16px; letter-spacing: 0.15px;
        }}
        .breadcrumbs a {{ color: var(--ink); text-decoration: none; font-weight: 500; }}
        .breadcrumbs a:hover {{ text-decoration: underline; }}
        .breadcrumbs .sep {{ margin: 0 8px; }}

        /* Content */
        .markdown-body {{
            background: var(--surface-card); border-radius: 16px; padding: 48px 52px;
            box-shadow: 0 0 0 1px var(--hairline);
        }}

        .markdown-body h1 {{
            font-family: 'EB Garamond', 'Times New Roman', serif;
            font-size: 48px; font-weight: 300; margin-bottom: 8px;
            padding-bottom: 24px; border-bottom: 1px solid var(--hairline);
            line-height: 1.08; letter-spacing: -0.96px; color: var(--ink);
        }}
        .markdown-body h2 {{
            font-family: 'EB Garamond', 'Times New Roman', serif;
            font-size: 36px; font-weight: 300; margin-top: 48px; margin-bottom: 16px;
            padding-left: 16px; border-left: 1px solid var(--hairline);
            line-height: 1.17; letter-spacing: -0.36px; color: var(--ink);
        }}
        .markdown-body h3 {{
            font-family: 'EB Garamond', 'Times New Roman', serif;
            font-size: 24px; font-weight: 300; margin-top: 32px; margin-bottom: 12px;
            line-height: 1.2; color: var(--ink);
        }}
        .markdown-body p {{ margin-bottom: 16px; line-height: 1.5; }}

        .markdown-body blockquote {{
            border-left: 1px solid var(--hairline-strong); background: var(--canvas);
            padding: 16px 20px; border-radius: 0 16px 16px 0; margin: 24px 0;
        }}
        .markdown-body blockquote p {{ margin-bottom: 0; }}

        .markdown-body code {{
            background: var(--canvas); padding: 2px 7px; border-radius: 4px;
            font-size: 0.88em; font-family: 'JetBrains Mono', 'Fira Code', monospace;
        }}
        .markdown-body pre {{
            background: #0c0a09; border-radius: 16px; padding: 18px 22px;
            overflow-x: auto; margin: 24px 0;
        }}
        .markdown-body pre code {{
            background: none; padding: 0; color: #cdd6f4;
            font-size: 0.82rem; line-height: 1.6;
        }}

        .markdown-body table {{
            border-collapse: separate; border-spacing: 0;
            margin: 0; border-radius: 16px;
            min-width: 100%;
        }}
        .markdown-body th {{
            background: var(--primary); color: white; font-weight: 500;
            text-align: left; padding: 12px 16px; font-size: 15px;
        }}
        .markdown-body td {{ padding: 10px 16px; border-top: 1px solid var(--hairline); font-size: 15px; }}
        .markdown-body tr:nth-child(even) td {{ background: var(--canvas); }}

        .markdown-body ul, .markdown-body ol {{ padding-left: 24px; margin-bottom: 16px; }}
        .markdown-body li {{ margin-bottom: 6px; line-height: 1.5; }}

        .markdown-body hr {{
            border: none; height: 1px;
            background: var(--hairline);
            margin: 48px 0;
        }}

        .markdown-body img {{
            max-width: 100%; border-radius: 16px;
            box-shadow: 0 0 0 1px var(--hairline);
        }}

        .markdown-body a {{
            color: var(--primary); text-decoration: none; font-weight: 500;
            border-bottom: 1px solid var(--hairline); transition: all 0.2s;
        }}
        .markdown-body a:hover {{ color: var(--primary-active); border-bottom-color: var(--primary-active); }}

        /* Mermaid — enlarged + zoomable */
        .mermaid {{
            margin: 48px auto; text-align: center;
            cursor: zoom-in; position: relative;
            padding: 24px; background: var(--surface-card);
            border-radius: 16px; border: 1px solid var(--hairline);
            overflow-x: auto; -webkit-overflow-scrolling: touch;
        }}
        .mermaid svg {{
            max-width: none; height: auto; min-width: 700px;
            display: block; margin: 0 auto;
        }}
        .mermaid-zoom-overlay {{
            display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(12,10,9,0.7); backdrop-filter: blur(6px);
            z-index: 1000; justify-content: center; align-items: center;
        }}
        .mermaid-zoom-overlay.active {{ display: flex; }}
        .mermaid-zoom-overlay .mermaid-zoom-content {{
            background: var(--surface-card); border-radius: 16px;
            padding: 40px; max-width: 96vw; max-height: 92vh;
            overflow: auto; box-shadow: 0 8px 40px rgba(0,0,0,0.2);
            border: 1px solid var(--hairline); cursor: grab;
            -webkit-overflow-scrolling: touch;
        }}
        .mermaid-zoom-overlay svg {{
            min-width: 1200px; max-width: none; height: auto;
        }}

        /* Chapter nav */
        .chapter-nav {{
            display: flex; justify-content: space-between; margin-top: 48px;
            padding-top: 24px; border-top: 1px solid var(--hairline);
        }}
        .chapter-nav a {{
            display: inline-flex; align-items: center; gap: 8px;
            padding: 10px 20px; border-radius: 9999px; background: var(--primary);
            color: white; font-weight: 500; border: none;
            transition: all 0.2s; text-decoration: none; font-size: 15px; height: 40px;
            letter-spacing: 0;
        }}
        .chapter-nav a:hover {{
            background: var(--primary-active);
        }}
        .chapter-nav .prev, .chapter-nav .next {{ border: 1px solid var(--hairline); background: var(--surface-card); color: var(--ink); }}
        .chapter-nav .prev:hover, .chapter-nav .next:hover {{ background: var(--primary); color: white; border-color: var(--primary); }}

        /* Author bio — subtle */
        .author-bio {{
            display: flex; align-items: center; gap: 16px; margin-top: 48px;
            padding: 24px; background: var(--canvas); border-radius: 16px;
            border: 1px solid var(--hairline);
        }}
        .author-avatar {{
            width: 40px; height: 40px; border-radius: 50%;
            background: var(--primary); color: white;
            display: flex; align-items: center; justify-content: center;
            font-weight: 600; font-size: 15px; flex-shrink: 0;
        }}
        .author-info {{ font-size: 15px; line-height: 1.5; letter-spacing: 0.15px; }}
        .author-info strong {{ color: var(--ink); font-weight: 500; }}
        .author-info a {{
            color: var(--primary); text-decoration: none;
            border-bottom: 1px solid var(--hairline);
        }}
        .author-info a:hover {{ text-decoration: underline; }}
        .author-info p {{ margin: 2px 0 0; color: var(--muted); font-size: 15px; }}

        /* Footer */
        footer {{
            text-align: center; padding: 24px 20px; color: var(--muted);
            font-size: 15px; margin-top: 24px; letter-spacing: 0.15px;
        }}
        footer a {{ color: var(--ink); text-decoration: none; font-weight: 500; }}
        footer a:hover {{ text-decoration: underline; }}

        @media (max-width: 768px) {{
            .markdown-body {{ padding: 24px 18px; }}
            .markdown-body h1 {{ font-size: 32px; letter-spacing: -0.32px; }}
            .markdown-body h2 {{ font-size: 24px; letter-spacing: 0; }}
            .nav-links {{ display: none; }}
            .container {{ padding: 0 12px; }}
            .chapter-nav {{ flex-direction: column; gap: 12px; }}
            .chapter-nav a {{ text-align: center; justify-content: center; }}
        }}
    </style>
</head>
<body>
    <nav class="nav">
        <a href="index.html" class="nav-brand"><span>Hermes Tutorial</span></a>
        <div class="nav-links">{nav_links}</div>
        <div class="nav-search">
            <div class="nav-search-bar" id="searchToggle" role="button" tabindex="0" aria-label="Search">
                <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                <input id="searchInput" type="text" placeholder="Search tutorial…" autocomplete="off">
            </div>
            <div class="search-dropdown" id="searchDropdown"></div>
        </div>
    </nav>

    <div class="container">
        {breadcrumbs}
        <article class="markdown-body">
            {content_html}
            {nav_html}
            {author_bio}
        </article>
        <footer>
            <p>Hermes Agent Tutorial by <a href="{AUTHOR_URL}" target="_blank" rel="noopener">{AUTHOR_NAME}</a> ·
            <a href="https://github.com/cryptorichyrich/hermes-tutorial">Source on GitHub</a></p>
        </footer>
    </div>

    <script src="search.js"></script>
    <script>
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'base',
            themeVariables: {{
                primaryColor: '#fafafa',
                primaryTextColor: '#0c0a09',
                primaryBorderColor: '#e7e5e4',
                lineColor: '#292524',
                secondaryColor: '#f5f5f5',
                tertiaryColor: '#ffffff',
                fontSize: '15px',
                fontFamily: 'Inter'
            }},
            flowchart: {{ curve: 'basis', padding: 16 }}
        }});
        // Wrap tables in scrollable containers
        document.querySelectorAll('.markdown-body table').forEach(function(t) {{
            if (!t.parentElement.classList.contains('table-scroll-wrap')) {{
                var wrap = document.createElement('div');
                wrap.className = 'table-scroll-wrap';
                wrap.style.cssText = 'overflow-x:auto;-webkit-overflow-scrolling:touch;margin:24px 0;border-radius:16px;box-shadow:0 0 0 1px var(--hairline);';
                t.parentNode.insertBefore(wrap, t);
                wrap.appendChild(t);
            }}
        }});
        // Mermaid zoom with pan/drag
        document.querySelectorAll('.mermaid').forEach(function(m) {{
            m.addEventListener('click', function() {{
                var overlay = document.createElement('div');
                overlay.className = 'mermaid-zoom-overlay active';
                var content = document.createElement('div');
                content.className = 'mermaid-zoom-content';
                content.innerHTML = m.innerHTML;
                overlay.appendChild(content);
                document.body.appendChild(overlay);

                // Pan state
                var isPanning = false, startX = 0, startY = 0, scrollL = 0, scrollT = 0;
                content.addEventListener('mousedown', function(e) {{
                    isPanning = true;
                    startX = e.pageX - content.offsetLeft;
                    startY = e.pageY - content.offsetTop;
                    scrollL = content.scrollLeft;
                    scrollT = content.scrollTop;
                    content.style.cursor = 'grabbing';
                    e.preventDefault();
                }});
                overlay.addEventListener('mousemove', function(e) {{
                    if (!isPanning) return;
                    var x = e.pageX - content.offsetLeft;
                    var y = e.pageY - content.offsetTop;
                    content.scrollLeft = scrollL - (x - startX);
                    content.scrollTop = scrollT - (y - startY);
                }});
                overlay.addEventListener('mouseup', function() {{
                    isPanning = false;
                    content.style.cursor = 'grab';
                }});

                // Close on click outside content or Escape
                overlay.addEventListener('click', function(e) {{
                    if (e.target === overlay) overlay.remove();
                }});
                document.addEventListener('keydown', function handler(e) {{
                    if (e.key === 'Escape') {{ overlay.remove(); document.removeEventListener('keydown', handler); }}
                }});
            }});
        }});
    </script>
</body>
</html>"""


def build_index() -> str:
    """Build the homepage."""
    schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "name": "Hermes Agent — The Complete Tutorial",
        "description": "The first comprehensive English tutorial for Hermes Agent. 10 chapters covering installation, skills, automation, multi-agent orchestration, and business use cases.",
        "author": {"@type": "Person", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "url": SITE_URL,
        "about": {
            "@type": "SoftwareApplication",
            "name": "Hermes Agent",
            "url": "https://github.com/nousresearch/hermes-agent",
        },
    }

    toc_items = ""
    for ch in CHAPTERS:
        toc_items += f"""
            <a href="{ch['slug']}.html" class="toc-card">
                <span class="toc-num">Ch {ch['num']}</span>
                <span class="toc-title">{ch['title']}</span>
                <span class="toc-arrow">→</span>
            </a>"""

    nav_links = ""
    for c in CHAPTERS:
        nav_links += f'<a href="{c["slug"]}.html">Ch {c["num"]}</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hermes Agent — The Complete Tutorial (10 Chapters)</title>
    <meta name="description" content="The first comprehensive English tutorial for Hermes Agent by Nous Research. 10 chapters, production-tested code examples, Mermaid diagrams. From first install to expert workflows.">
    <meta name="keywords" content="Hermes Agent tutorial, AI agent guide, Nous Research, self-improving AI agent, Harness Engineering, Hermes Agent install">
    <meta name="author" content="{AUTHOR_NAME}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE_URL}/">

    <meta property="og:type" content="website">
    <meta property="og:title" content="Hermes Agent — The Complete Tutorial">
    <meta property="og:description" content="The first comprehensive English tutorial for Hermes Agent. 10 chapters, production-tested code examples, Mermaid diagrams.">
    <meta property="og:url" content="{SITE_URL}/">
    <meta property="og:site_name" content="Hermes Agent Tutorial">

    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Hermes Agent — The Complete Tutorial">
    <meta name="twitter:description" content="The first comprehensive English tutorial for Hermes Agent. 10 chapters.">

    <script type="application/ld+json">{json.dumps(schema, indent=2)}</script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@300&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #292524;
            --primary-active: #0c0a09;
            --ink: #0c0a09;
            --body: #4e4e4e;
            --muted: #777169;
            --hairline: #e7e5e4;
            --canvas: #f5f5f5;
            --canvas-soft: #fafafa;
            --surface-card: #ffffff;
            --gradient-mint: #a7e5d3;
            --gradient-peach: #f4c5a8;
            --gradient-lavender: #c8b8e0;
            --gradient-sky: #a8c8e8;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--canvas); color: var(--body); line-height: 1.5; letter-spacing: 0.16px;
        }}
        .nav {{
            position: fixed; top: 0; left: 0; right: 0; height: 64px;
            background: rgba(250,250,250,0.95); backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--hairline);
            display: flex; align-items: center; padding: 0 20px; z-index: 100;
        }}
        .nav-brand {{
            font-family: 'Inter', sans-serif;
            font-weight: 500; font-size: 15px; color: var(--ink);
            text-decoration: none; display: flex; align-items: center; gap: 6px; letter-spacing: 0;
        }}
        .nav-brand span {{ 
            font-family: 'EB Garamond', 'Times New Roman', serif;
            font-weight: 300; font-size: 24px; letter-spacing: -0.32px;
        }}
        .nav-links {{
            display: flex; gap: 2px; margin-left: 24px; overflow-x: auto;
        }}
        .nav-links a {{
            padding: 4px 12px; border-radius: 9999px; color: var(--muted);
            text-decoration: none; font-size: 15px; font-weight: 500;
            white-space: nowrap; transition: all 0.2s; letter-spacing: 0;
        }}
        .nav-links a:hover {{ background: var(--primary); color: white; }}

        /* Search — integrated bar */
        .nav-search {{ margin-left: auto; position: relative; }}
        .nav-search-bar {{
            display: flex; align-items: center; gap: 8px;
            background: var(--surface-card); border: 1px solid var(--hairline);
            border-radius: 9999px; padding: 6px 14px;
            cursor: pointer; transition: all 0.25s ease; min-width: 44px;
        }}
        .nav-search-bar:hover, .nav-search-bar.open {{ border-color: var(--ink); }}
        .nav-search-bar.open {{ min-width: 260px; }}
        .nav-search-bar svg {{
            width: 16px; height: 16px; stroke: var(--muted); fill: none;
            stroke-width: 2; flex-shrink: 0; transition: stroke 0.2s;
        }}
        .nav-search-bar:hover svg, .nav-search-bar.open svg {{ stroke: var(--ink); }}
        .nav-search-bar input {{
            border: none; outline: none; background: transparent;
            color: var(--ink); font-size: 14px; font-family: inherit;
            letter-spacing: 0; width: 0; padding: 0;
            transition: width 0.25s ease;
        }}
        .nav-search-bar.open input {{ width: 200px; }}
        .nav-search-bar input::placeholder {{ color: var(--muted); }}
        .search-dropdown {{
            position: absolute; top: 44px; right: 0; width: 420px;
            max-height: 480px; overflow-y: auto;
            background: var(--surface-card); border-radius: 16px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04), 0 0 0 1px var(--hairline);
            z-index: 200; display: none;
        }}
        .search-dropdown.open {{ display: block; }}
        .search-dropdown .sr-label {{
            padding: 10px 16px 6px; font-size: 12px; font-weight: 600;
            text-transform: uppercase; letter-spacing: 0.96px;
            color: var(--muted); border-bottom: 1px solid var(--hairline);
        }}
        .search-dropdown .sr-item {{
            display: block; padding: 10px 16px; text-decoration: none;
            color: var(--ink); transition: background 0.15s; cursor: pointer;
            border-bottom: 1px solid var(--hairline-soft);
        }}
        .search-dropdown .sr-item:hover {{ background: var(--canvas); }}
        .search-dropdown .sr-item:last-child {{ border-bottom: none; }}
        .sr-item-chapter {{ font-size: 12px; font-weight: 600; color: var(--primary); margin-bottom: 2px; text-transform: uppercase; letter-spacing: 0.96px; }}
        .sr-item-heading {{ font-weight: 500; font-size: 16px; margin-bottom: 2px; color: var(--ink); }}
        .sr-item-snippet {{ font-size: 15px; color: var(--body); line-height: 1.4; letter-spacing: 0.15px; }}
        .sr-item-snippet mark {{ background: #fef08a; color: var(--ink); padding: 0 2px; border-radius: 2px; }}
        .sr-empty {{ padding: 24px 16px; text-align: center; color: var(--muted); font-size: 15px; letter-spacing: 0.15px; }}

        /* Hero section with gradient orb */
        .hero {{
            position: relative;
            text-align: center; padding: 96px 20px 48px;
            max-width: 700px; margin: 0 auto;
        }}
        .hero::before {{
            content: '';
            position: absolute;
            top: -100px;
            left: 50%;
            transform: translateX(-50%);
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, var(--gradient-mint) 0%, transparent 70%);
            opacity: 0.4;
            pointer-events: none;
            z-index: -1;
        }}
        .hero::after {{
            content: '';
            position: absolute;
            top: 50px;
            right: -100px;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, var(--gradient-peach) 0%, transparent 70%);
            opacity: 0.3;
            pointer-events: none;
            z-index: -1;
        }}
        .hero h1 {{
            font-family: 'EB Garamond', 'Times New Roman', serif;
            font-size: 64px; font-weight: 300; margin-bottom: 16px;
            line-height: 1.05; letter-spacing: -1.92px; color: var(--ink);
        }}
        .hero p {{ color: var(--body); font-size: 18px; margin-bottom: 8px; letter-spacing: 0.18px; }}

        .toc {{
            max-width: 700px; margin: 0 auto 48px; padding: 0 20px;
            display: flex; flex-direction: column; gap: 12px;
        }}
        .toc-card {{
            display: flex; align-items: center; gap: 16px;
            padding: 20px 24px; background: var(--surface-card);
            border-radius: 16px; border: 1px solid var(--hairline);
            text-decoration: none; color: var(--ink);
            transition: all 0.2s;
        }}
        .toc-card:hover {{
            border-color: var(--hairline-strong); box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            transform: translateY(-2px);
        }}
        .toc-num {{
            font-weight: 600; color: var(--primary); font-size: 14px;
            min-width: 60px; text-transform: uppercase; letter-spacing: 0.96px;
        }}
        .toc-title {{
            flex: 1; font-weight: 500; font-size: 16px; letter-spacing: 0.16px;
        }}
        .toc-arrow {{
            color: var(--muted); font-size: 20px; transition: transform 0.2s;
        }}
        .toc-card:hover .toc-arrow {{ transform: translateX(4px); color: var(--ink); }}

        .bottom-bar {{
            text-align: center; padding: 48px 20px 64px; color: var(--muted);
            font-size: 15px; letter-spacing: 0.15px;
        }}
        .bottom-bar a {{ color: var(--ink); text-decoration: none; font-weight: 500; }}
        .bottom-bar a:hover {{ text-decoration: underline; }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 48px; letter-spacing: -0.96px; }}
            .hero::before {{ width: 250px; height: 250px; top: -50px; }}
            .hero::after {{ width: 200px; height: 200px; right: -50px; }}
            .nav-links {{ display: none; }}
        }}
    </style>
</head>
<body>
    <nav class="nav">
        <a href="index.html" class="nav-brand"><span>Hermes Tutorial</span></a>
        <div class="nav-links">{nav_links}</div>
        <div class="nav-search">
            <div class="nav-search-bar" id="searchToggle" role="button" tabindex="0" aria-label="Search">
                <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                <input id="searchInput" type="text" placeholder="Search tutorial…" autocomplete="off">
            </div>
            <div class="search-dropdown" id="searchDropdown"></div>
        </div>
    </nav>

    <div class="hero">
        <h1>Hermes Agent — The Complete Tutorial</h1>
        <p>The AI Agent that ships with reins built in.</p>
        <p style="margin-top:12px;">
            By <a href="{AUTHOR_URL}" style="color:var(--ink);font-weight:500;">{AUTHOR_NAME}</a> ·
            {AUTHOR_TITLE}
        </p>
    </div>

    <div class="toc">
        {toc_items}
    </div>

    <div class="bottom-bar">
        <p>
            Open source ·
            <a href="https://github.com/cryptorichyrich/hermes-tutorial">GitHub</a> ·
            <a href="https://github.com/nousresearch/hermes-agent">Hermes Agent</a> ·
            <a href="{AUTHOR_URL}">biotama.cv</a>
        </p>
    </div>
    <script src="search.js"></script>
</body>
</html>"""


def build_search_index() -> list:
    """Build a search index JSON from all chapter markdown files."""
    index = []
    for ch in CHAPTERS:
        md_path = BASE_DIR / ch["file"]
        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        current_heading = ch["title"]
        current_id = None
        buffer = []

        for line in lines:
            # Detect headings
            heading_match = re.match(r"^(#{1,3})\s+(.+)$", line)
            if heading_match:
                # Flush previous section
                if buffer:
                    text = " ".join(buffer).strip()
                    if len(text) > 10:
                        index.append({
                            "ch": ch["num"],
                            "slug": ch["slug"],
                            "chTitle": ch["title"],
                            "heading": current_heading,
                            "headingId": current_id,
                            "text": text[:500],
                        })
                    buffer = []

                level = len(heading_match.group(1))
                current_heading = heading_match.group(2).strip()
                # Generate a slug-like ID
                current_id = re.sub(r"[^a-z0-9]+", "-", current_heading.lower()).strip("-")
                if level == 1:
                    current_id = "top"
                continue

            # Skip code blocks markers but include code content for search
            stripped = line.strip()
            if stripped.startswith("```"):
                continue
            if stripped.startswith("|") or stripped.startswith(">"):
                buffer.append(stripped.lstrip(">|"))
                continue
            if stripped:
                buffer.append(stripped)

        # Flush last section
        if buffer:
            text = " ".join(buffer).strip()
            if len(text) > 10:
                index.append({
                    "ch": ch["num"],
                    "slug": ch["slug"],
                    "chTitle": ch["title"],
                    "heading": current_heading,
                    "headingId": current_id,
                    "text": text[:500],
                })

    return index


def build_sitemap() -> str:
    """Generate sitemap.xml."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Homepage
    lines.append(f"""  <url>
    <loc>{SITE_URL}/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>""")

    for ch in CHAPTERS:
        lines.append(f"""  <url>
    <loc>{SITE_URL}/{ch["slug"]}.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    lines.append('</urlset>')
    return '\n'.join(lines)


def build_robots() -> str:
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def main():
    print("Building static pages...")

    # Build index
    index_html = build_index()
    out = BASE_DIR / "index.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"  ✓ index.html")

    # Build chapter pages
    for i, ch in enumerate(CHAPTERS):
        prev = CHAPTERS[i - 1] if i > 0 else None
        nxt = CHAPTERS[i + 1] if i < len(CHAPTERS) - 1 else None
        html = build_page(ch, prev, nxt)
        out = BASE_DIR / f"{ch['slug']}.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✓ {ch['slug']}.html")

    # Build sitemap
    sitemap = build_sitemap()
    out = BASE_DIR / "sitemap.xml"
    with open(out, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"  ✓ sitemap.xml")

    # Build robots.txt
    robots = build_robots()
    out = BASE_DIR / "robots.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(robots)
    print(f"  ✓ robots.txt")

    # Build search index
    search_idx = build_search_index()
    out = BASE_DIR / "search-index.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(search_idx, f, ensure_ascii=False)
    print(f"  ✓ search-index.json ({len(search_idx)} sections)")

    print(f"\nDone. {len(CHAPTERS) + 1} pages + sitemap + robots + search")


if __name__ == "__main__":
    main()

# 📘 Hermes Agent Complete Tutorial — Master Outline

> **Last updated:** May 24, 2026
> **Location:** `~/hermes-tutorial/`
> **Status:** Chapters 1-6 written, Chapters 7-10 + Appendices pending

---

## Structure Overview

**10 Chapters, 3 Parts, 8 Appendices**

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  PART 1 — UP & RUNNING (Chapters 1-3)          ✅ COMPLETE   │
│                                                              │
│  PART 2 — GETTING PRODUCTIVE (Chapters 4-7)    🔄 Ch 7 next  │
│                                                              │
│  PART 3 — EXPERT & BUSINESS (Chapters 8-10)    ⬜ PENDING    │
│                                                              │
│  APPENDICES                                    ⬜ PENDING    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## PART 1 — UP & RUNNING

> Goal: Go from zero to a working Hermes on Telegram in 30 minutes.

### Chapter 1: Hello Hermes — Install, First Run, 5-Minute Win ✅

**File:** `ch01-hello-hermes.md` (371 lines, ~1,750 words)

- 1.1 The Problem Hermes Solves
- 1.2 What Makes Hermes Different (Three Tools Three Jobs + Harness Framework)
- 1.3 System Requirements & Installation
- 1.4 Installation (Linux, macOS, Windows, Docker)
- 1.5 First Run & Setup Wizard
- 1.7 Your First Conversation — 5-minute win

### Chapter 2: Core Concepts — Agent Loop, Models, Tools ✅

**File:** `ch02-core-concepts.md` (535 lines, ~2,181 words)

- 2.1 The Agent Loop — How Hermes Thinks (think → act → observe cycle)
- 2.2 Models & Providers (OpenRouter, Anthropic, OpenAI, DeepSeek, etc.)
- 2.3 Toolsets — What Hermes Can Do (20+ tool bundles)
- 2.4 Sessions — Conversation Management (lifecycle, resume, storage)
- 2.5 Configuration — config.yaml & .env
- 2.6 How It All Fits Together (full architecture diagram)

### Chapter 3: Messaging Gateway — Telegram, Voice, Slash Commands ✅

**File:** `ch03-messaging-gateway.md` (665 lines, ~2,450 words)

- 3.1 What is the Gateway?
- 3.2 Setting Up Telegram Bot (step-by-step with BotFather)
- 3.3 Gateway Lifecycle (run, install, start, stop, restart)
- 3.4 Slash Commands in Chat (`/new`, `/model`, `/tools`, `/yolo`, etc.)
- 3.5 Voice Mode (`/voice on`, STT/TTS providers)
- 3.6 Command Approval (`/approve`, `/deny`, approval modes)
- 3.7 Other Platforms (Discord, Slack, WhatsApp, Signal, etc.)
- 3.8 Running the Gateway — Production Tips

---

## PART 2 — GETTING PRODUCTIVE

> Goal: Build a daily workflow with automation, skills, and multi-agent coordination.

### Chapter 4: Skills & Memory — Making Hermes Smarter Over Time ✅

**File:** `ch04-skills-memory.md` (658 lines, ~2,600 words)

- 4.1 The Learning Loop — How Hermes Improves Itself (5-step causal chain)
- 4.2 Skills — Reusable Procedures (SKILL.md structure, frontmatter)
- 4.3 The Skills Hub — 88+ Pre-Built Skills (browse, install, search)
- 4.4 Loading & Creating Custom Skills
- 4.5 The Curator — Automatic Skill Maintenance (lifecycle: active → stale → archived)
- 4.6 Memory — Persistent Knowledge Across Sessions (user profile + agent notes)
- 4.7 Session Search — Recalling the Past (FTS5 full-text search, 3 modes)
- 4.8 Context Compression — Staying Within Limits
- 4.9 Skills + Memory in Practice (real workflow scenarios)

### Chapter 5: Automation — Cron, Webhooks, Background Tasks ✅

**File:** `ch05-automation-scheduling.md` (644 lines, ~2,800 words)

- 5.1 Why Automation Matters (the automation spectrum: manual → scheduled → event-driven)
- 5.2 Cron Jobs — Scheduled Intelligence (anatomy, 4 schedule formats, delivery, model override)
- 5.3 Script-Only Jobs — Lightweight Watchdogs (zero-token, silent-unless-alert design)
- 5.4 Job Chaining — Output Pipelines (`context_from` architecture)
- 5.5 Webhooks — Event-Driven Automation (subscribe, list, test, remove)
- 5.6 Background Tasks — Long-Running Work (lifecycle, process management actions)
- 5.7 Cron Safety & Best Practices (safety checklist, cost awareness table)
- 5.8 Three Real Workflows (content engine, server watchdog, PR auto-review)

### Chapter 6: Multi-Agent — Delegation, Kanban, Parallel Workflows ✅

**File:** `ch06-multi-agent.md` (717 lines, ~2,498 words)

- 6.1 Why Multi-Agent? (sequential vs parallel, four mechanisms overview)
- 6.2 Delegation — `delegate_task` (single, batch, leaf vs orchestrator, anatomy)
- 6.3 Spawning Independent Agents (one-shot, tmux interactive, multi-agent coordination)
- 6.4 Kanban Board — Multi-Agent Work Queue (lifecycle, dispatcher, dependencies, profiles)
- 6.5 External Coding Agents (KiloCode, Claude Code, Codex comparison)
- 6.6 Coordination Patterns (research+write, backend+frontend, project pipeline, daily ops)
- 6.7 Multi-Agent Best Practices (right-size tooling, isolate edits, verify results)

### Chapter 7: Advanced Config — Security, MCP, Profiles, Credential Pools ✅

**File:** `ch07-advanced-config.md` (711 lines, ~2,650 words)

- 7.1 Security & Privacy (secret redaction, PII, approval modes)
- 7.2 MCP Servers — Extending Hermes with External Tools
  ```
  hermes mcp add gitnexus --url http://localhost:3000
  ```
- 7.3 Custom Providers & Base URLs (self-hosted models, local endpoints)
- 7.4 Profiles — Isolated Hermes Instances (work/personal/client separation)
  ```
  hermes profile create work --clone
  hermes profile use work
  ```
- 7.5 Credential Pools — Rate Limit Busting (multi-key rotation)
  ```
  hermes auth add
  hermes auth list openrouter
  ```
- 7.6 Context Window Optimization (compression tuning, toolset pruning)
- 7.7 Debugging Hermes (`hermes doctor`, `/debug`, log inspection)
- 7.8 Windows-Specific Tips (Ctrl+Enter, BOM fix, WSL, path conventions)

---

## PART 3 — EXPERT & BUSINESS

> Goal: Master every power-user technique and turn Hermes into a profit engine.

### Chapter 8: Power Techniques — Goal, Checkpoints, Steer, Compression ⬜

**File:** `ch08-power-techniques.md` (pending)

- 8.1 YOLO Mode — Skip Approvals for Speed (`--yolo`, `/yolo`)
- 8.2 `/goal` — Standing Objectives Across Turns (set, pause, resume, clear)
- 8.3 `/steer` — Inject Context Mid-Task Without Interrupting
- 8.4 `/queue` — Stack Commands While Hermes Works
- 8.5 `/branch` — Fork Conversations for Exploration
- 8.6 Checkpoints & Rollback (`--checkpoints`, `/rollback`)
- 8.7 Session Snapshots (`/snapshot`)
- 8.8 Fast Mode (`/fast`) — Priority Processing
- 8.9 Reasoning Control (`/reasoning high|xhigh`)
- 8.10 Busy Mode (`/busy queue|steer|interrupt`)
- 8.11 Background Prompts (`/background`)
- 8.12 Pipe Tricks (stdin, heredoc, Unix tool chaining)
- 8.13 Model Mid-Task Switching (change models without losing context)
- 8.14 Compression Tricks (manual `/compress`, threshold tuning)
- 8.15 Profile-Based Work/Personal/Lab Separation

### Chapter 9: Real Business Use Cases — 10 Scenarios with ROI Numbers ✅

**File:** `ch09-business-use-cases.md` (939 lines, ~4,734 words)

- 9.1 **Content Marketing Engine** — Automated Blog Pipeline
  - Cron: 2 articles/day, SEO-optimized, auto-publish
  - Skills: blog, marketing-copy, humanizer
  - ROI: save $2,000-5,000/mo on content writers
- 9.2 **Customer Support Automation** — 24/7 on Telegram/WhatsApp
  - Gateway setup + custom skills for FAQ routing
  - Escalation to human agents
  - ROI: reduce support staff costs by 60-80%
- 9.3 **Code Review & CI/CD Automation**
  - PR auto-review, security scanning, quality gates
  - Skills: github-code-review, requesting-code-review
  - ROI: catch bugs before production, save $10K+ per incident
- 9.4 **E-Commerce Operations**
  - Inventory monitoring, price comparison, order notifications
  - Cron jobs for daily stock checks
  - ROI: never miss a restock, optimize pricing
- 9.5 **Research & Competitive Intelligence**
  - Market monitoring, RSS feeds, paper tracking
  - Skills: blogwatcher, arxiv, polymarket
  - Cron: daily competitive digest
  - ROI: stay ahead of competition, discover opportunities first
- 9.6 **Freelancer/Agency Acceleration**
  - Delegate coding to subagents (parallel features)
  - Auto-generate project proposals, estimates
  - Skills: writing-plans, fullstack-web-architecture
  - ROI: 3-5x throughput increase
- 9.7 **SaaS Monitoring & Alerting**
  - Watchdog scripts with `no_agent=True`
  - Uptime checks, API health, threshold alerts
  - Webhook-triggered remediation
  - ROI: reduce downtime, prevent revenue loss
- 9.8 **Data Analysis & Reporting**
  - Jupyter kernel integration, automated reports
  - Cron: weekly analytics digest
  - Skills: jupyter-live-kernel
  - ROI: replace $3K/mo analyst for routine reports
- 9.9 **Email Management** — Triage & Respond
  - Himalaya CLI integration, auto-categorize
  - ROI: save 2+ hours/day on email
- 9.10 **Real Estate / Lead Generation**
  - Web scraping, market analysis, lead notifications
  - Browser automation for data collection
  - ROI: faster lead response = higher conversion

### Chapter 10: Building a Business Around Hermes ✅

**File:** `ch10-business-around-hermes.md` (694 lines, ~3,823 words)

- 10.1 Cost Analysis (API costs vs hiring, break-even points)
- 10.2 Pricing Your AI-Powered Services
- 10.3 Building Reusable Skill Packages to Sell
- 10.4 White-Label Hermes for Clients (profiles + custom skills)
- 10.5 Compliance & Data Privacy (PII redaction, local models)
- 10.6 Scaling: Multi-Profile Agency Setup
- 10.7 Future-Proofing (local models via llama.cpp, edge deployment)

---

## APPENDICES

### Appendix A: Complete CLI Quick Reference Card ⬜

**File:** `appendix-a-cli-reference.md`

- All `hermes` commands organized by category
- Flags, arguments, common patterns

### Appendix B: Provider Configuration Cheat Sheet ⬜

**File:** `appendix-b-providers.md`

- 20+ providers: auth method, env var, best use, pricing tier
- Custom endpoint configuration
- Credential pool setup

### Appendix C: Toolset Reference Table ⬜

**File:** `appendix-c-toolsets.md`

- All 20+ toolsets: description, tools included, requirements
- Enable/disable per platform

### Appendix D: Slash Command Reference ⬜

**File:** `appendix-d-slash-commands.md`

- All slash commands: syntax, description, availability (CLI/gateway)
- Organized by category (session, config, tools, utility, info)

### Appendix E: Environment Variables Reference ⬜

**File:** `appendix-e-env-vars.md`

- All env vars: name, provider/purpose, required/optional
- `.env` file structure

### Appendix F: Troubleshooting Decision Tree ⬜

**File:** `appendix-f-troubleshooting.md`

- Common problems → diagnosis → fix
- Platform-specific issues
- Error message lookup

### Appendix G: Skills Catalog ⬜

**File:** `appendix-g-skills-catalog.md`

- All 88+ skills: name, category, description
- Installation commands
- Custom skill authoring quick guide

### Appendix H: Glossary ⬜

**File:** `appendix-h-glossary.md`

- All terms defined in one place
- Cross-referenced with chapter numbers

---

## Progress Tracker

| # | Chapter | File | Lines | Words | Status |
|---|---------|------|-------|-------|--------|
| 1 | Hello Hermes | `ch01-hello-hermes.md` | 326 | ~1,539 | ✅ Done |
| 2 | Core Concepts | `ch02-core-concepts.md` | 535 | ~2,181 | ✅ Done |
| 3 | Messaging Gateway | `ch03-messaging-gateway.md` | 651 | ~2,274 | ✅ Done |
| 4 | Skills & Memory | `ch04-skills-memory.md` | 634 | ~2,440 | ✅ Done |
| 5 | Automation | `ch05-automation-scheduling.md` | 580 | ~2,454 | ✅ Done |
| 6 | Multi-Agent | `ch06-multi-agent.md` | 717 | ~2,498 | ✅ Done |
| 7 | Advanced Config | `ch07-advanced-config.md` | 711 | ~2,650 | ✅ Done |
| 8 | Power Techniques | `ch08-power-techniques.md` | 651 | ~3,295 | ✅ Done |
| 9 | Business Use Cases | `ch09-business-use-cases.md` | 939 | ~4,734 | ✅ Done |
| 10 | Business Around Hermes | `ch10-business-around-hermes.md` | 694 | ~3,823 | ✅ Done |
| A | CLI Reference | `appendix-a-cli-reference.md` | — | — | ⬜ |
| B | Providers | `appendix-b-providers.md` | — | — | ⬜ |
| C | Toolsets | `appendix-c-toolsets.md` | — | — | ⬜ |
| D | Slash Commands | `appendix-d-slash-commands.md` | — | — | ⬜ |
| E | Env Vars | `appendix-e-env-vars.md` | — | — | ⬜ |
| F | Troubleshooting | `appendix-f-troubleshooting.md` | — | — | ⬜ |
| G | Skills Catalog | `appendix-g-skills-catalog.md` | — | — | ⬜ |
| H | Glossary | `appendix-h-glossary.md` | — | — | ⬜ |

**Written so far:** ~4,154 lines, ~16,036 words, ~177KB
**Target:** ~15,000-20,000 words (10 chapters) + appendices

---

## Writing Conventions

- **Target per chapter:** 500-700 lines, ~2,000-2,500 words
- **Rich with:** ASCII diagrams, code blocks, real commands, comparison tables
- **Progressive:** each chapter builds on the last
- **Business-focused:** Part 3 shows ROI with real dollar value
- **Cross-platform:** Windows, macOS, Linux covered
- **Honest:** limitations and gotchas included alongside strengths
- **File naming:** `ch##-slug.md` for chapters, `appendix-?-slug.md` for appendices

# Hermes Agent — The Complete Tutorial

> **The AI Agent that ships with reins built in**
> A practical guide to Hermes Agent — from first install to expert workflows
>
> **Merged edition — all 10 chapters**

---

# Chapter 1: Hello Hermes

> **The AI agent that works while you sleep, chats where you chat, and gets smarter every time you use it.**

---

## 1.1 The Problem Hermes Solves

You've used ChatGPT. You've used Claude. Maybe Copilot, maybe Gemini. They're great at answering questions — but every time you open a new chat, you start from zero. No memory. No tools. No access to your files, your terminal, your workflow.

**Hermes Agent is different.**

Hermes is an **autonomous AI agent** that:

- **Remembers** — your preferences, your projects, your past conversations, across sessions
- **Acts** — reads files, writes code, runs terminal commands, searches the web, manages your schedule
- **Lives everywhere** — Telegram, Discord, Slack, WhatsApp, your terminal, your IDE
- **Improves** — learns from experience by saving reusable skills
- **Scales** — spawns parallel agents, schedules cron jobs, orchestrates multi-agent workflows

It's not a chatbot. It's an **AI employee** that works 24/7 across all your platforms with full system access.

---

## 1.2 What Makes Hermes Different

The AI agent space is crowded. Here's where Hermes sits:

```mermaid
flowchart LR
    subgraph Chatbots["💬 Chatbots"]
        direction TB
        C1["ChatGPT"]
        C2["Claude.ai"]
        C3["Gemini"]
        CT["❌ Q&A only · No tools · No memory"]
    end
    subgraph CodingAgents["💻 Coding Agents"]
        direction TB
        D1["Claude Code"]
        D2["GitHub Copilot"]
        D3["Cursor"]
        D4["Codex CLI"]
        DT["⚠️ Code only · IDE-bound · No scheduling"]
    end
    subgraph FullAgents["🚀 Full Agent Platforms"]
        direction TB
        F1["Hermes Agent"]
        F2["OpenHands"]
        F3["MetaGPT"]
        FT["✅ Everything + Memory · Multi-platform · Persistent context"]
    end
```

**Key differentiators:**

| Feature | ChatGPT | Claude Code | Hermes |
|---------|---------|-------------|--------|
| Persistent memory | ❌ | Partial | ✅ Cross-session |
| Messaging platforms | ❌ | ❌ | ✅ 10+ platforms |
| Skill system | ❌ | ❌ | ✅ Learns & improves |
| Cron scheduling | ❌ | ❌ | ✅ Built-in |
| Multi-agent orchestration | ❌ | Partial | ✅ Delegation + Kanban |
| Provider-agnostic | ❌ | ❌ Anthropic only | ✅ 20+ providers |
| Self-improvement | ❌ | ❌ | ✅ Curator system |

### Three Tools, Three Jobs

Hermes isn't here to replace your existing tools. It's the next step in the progression:

| Tool | Job | Analogy |
|------|-----|---------|
| **Claude Code** | Interactive pair programming | Sitting with a senior dev at the terminal |
| **OpenClaw** | Configuration-as-behavior | Raising a pet — you shape it with SOUL.md |
| **Hermes Agent** | Autonomous self-improvement | An employee who learns on the job, works while you sleep |

Each tool excels at its job. You don't choose one — you use all three for different needs. And here's the best part: all three use the **agentskills.io standard**, meaning Skills are portable. A Skill written for Claude Code works in Hermes, and vice versa.

> **💡 When to reach for Hermes:** If you want an AI that runs background tasks, schedules itself, remembers everything across sessions, and gets better without you feeding it — that's Hermes. If you need real-time pair coding, that's Claude Code.

### The Harness Framework

In early 2026, a consensus emerged in the AI world: **the bottleneck isn't the model — it's the environment around it.** Mitchell Hashimoto (creator of Terraform) named this **Harness Engineering** — the practice of wrapping AI in rules, memory, and tools so it performs reliably.

Hermes is the first agent that **ships with the harness built in**. Every component maps to a proven principle:

```mermaid
flowchart LR
    subgraph Harness["THE HARNESS BUILT INTO HERMES"]
        direction TB
        IL["📖 Instruction Layer<br/><i>Teach the AI</i>"] --> HS["⚙️ Skill System<br/><i>Auto-created + self-improving SKILL.md files</i>"]
        CL["🔒 Constraint Layer<br/><i>Keep it safe</i>"] --> TP["🛡️ Tool Permissions<br/><i>Sandbox + toolset enable/disable on demand</i>"]
        FL["🔁 Feedback Layer<br/><i>Learn from mistakes</i>"] --> LL["📊 Learning Loop<br/><i>Auto-retrospective after each task, skill patching</i>"]
        ML["💾 Memory Layer<br/><i>Don't forget</i>"] --> TM["🗂️ Three-layer Memory<br/><i>Session + persistent + skill + FTS5 recall</i>"]
        OL["🎼 Orchestration Layer<br/><i>Coordinate work</i>"] --> SA["🤖 Sub-Agent Delegation<br/><i>Cron scheduling + multi-platform gateway</i>"]
    end
```

Other tools require you to build this harness manually — writing config files, setting up hooks, managing memory by hand. Hermes does all five automatically, from your very first conversation.

---

## 1.3 System Requirements

Before we install, make sure you have:

**Required:**
- **Python 3.10+** — Hermes is a Python application
- **Git** — for installation and project management
- **4GB RAM minimum** — 8GB recommended for multi-agent workflows
- **Internet connection** — API calls to LLM providers

**Supported Operating Systems:**
- ✅ Linux (Ubuntu 20.04+, Fedora, Arch)
- ✅ macOS (Intel + Apple Silicon)
- ✅ Windows 10/11 (native, WSL2, or git-bash)
- ✅ Docker (any OS)

**One LLM provider API key** — pick one to start:
- OpenRouter (recommended — access to 200+ models)
- Anthropic (Claude models)
- OpenAI (GPT-4, GPT-4o)
- Google (Gemini)
- DeepSeek
- Or any of 15+ others

> **💡 Recommendation:** Start with OpenRouter. One API key gives you access to every major model, and you can switch between them freely. We'll cover provider setup in Section 1.5.

---

## 1.4 Installation

### Linux & macOS

```bash
# One-line install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

This script will:
1. Clone the Hermes Agent repository
2. Create a Python virtual environment
3. Install all dependencies
4. Add `hermes` to your PATH

### Windows

```bash
# Using git-bash (recommended)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

> **Windows users:** Hermes runs natively on Windows. Use git-bash, PowerShell, or Windows Terminal — all work. See [Appendix A: Windows Quirks] for platform-specific notes.

### Docker

```bash
docker pull ghcr.io/nousresearch/hermes-agent:latest
docker run -it --rm \
  -v ~/.hermes:/root/.hermes \
  -v ~/projects:/root/projects \
  ghcr.io/nousresearch/hermes-agent:latest
```

### Verify Installation

```bash
hermes --version
# Output: hermes x.x.x
```

If you see a version number, you're golden.

---

## 1.5 Your First Run — The Setup Wizard

```bash
hermes setup
```

Hermes launches an interactive wizard that walks you through:

**Step 1: Model Selection**
```
? Choose your default model:
  ❯ Anthropic Claude Sonnet 4 (recommended)
    OpenAI GPT-4o
    Google Gemini 2.5 Pro
    DeepSeek V3
    [100+ more via OpenRouter]
```

**Step 2: API Key**
```
? Enter your API key: sk-or-v1-xxxxx...
✓ Key validated. Provider: OpenRouter
```

**Step 3: Tool Configuration**
```
? Which toolsets would you like to enable?
  ❯ ◉ web (search + content extraction)
    ◉ terminal (shell commands)
    ◉ file (read/write/search)
    ◉ browser (web automation)
    ◯ image_gen (AI image generation)
    ◉ memory (persistent memory)
    ◉ delegation (subagent tasks)
    ◉ cronjob (scheduled tasks)
```

> **💡 Tip:** Enable `web`, `terminal`, `file`, `memory`, `delegation`, and `cronjob` at minimum. You can add more later with `hermes tools`.

**Step 4: Confirm**
```
✓ Setup complete!
  Model: openrouter/anthropic/claude-sonnet-4
  Provider: openrouter
  Tools: 6 toolsets enabled
  Config: ~/.hermes/config.yaml

Run 'hermes' to start chatting.
```

---

## 1.6 Your 5-Minute Win

Let's get you actual value right now. Start Hermes:

```bash
hermes
```

You'll see the welcome banner and a prompt:

```
╭──────────────────────────────────────────╮
│  Hermes Agent v2.x                       │
│  Model: claude-sonnet-4 (OpenRouter)     │
│  Tools: 42 loaded                        │
╰──────────────────────────────────────────╯

You: 
```

### Task 1: Ask It Anything

```
You: What are the top 5 most starred GitHub repos this week?
```

Hermes uses its web search tools, fetches live data, and gives you an answer with sources. Not cached — **live**.

### Task 2: Have It Do Real Work

```
You: Create a Python FastAPI project called "my-api" in ~/projects/ 
    with a health check endpoint, Dockerfile, and README
```

Watch what happens:

```
Hermes: I'll set up a FastAPI project with the requested structure.

  [terminal] mkdir -p ~/projects/my-api/app
  [write]   ~/projects/my-api/app/main.py (created)
  [write]   ~/projects/my-api/Dockerfile (created)
  [write]   ~/projects/my-api/README.md (created)
  [write]   ~/projects/my-api/requirements.txt (created)

  Done! Project created at ~/projects/my-api/

  Structure:
  my-api/
  ├── app/
  │   └── main.py          ← FastAPI app with GET /health
  ├── Dockerfile            ← Multi-stage Python 3.12 build
  ├── requirements.txt      ← fastapi, uvicorn
  └── README.md             ← Setup & run instructions

  Run it: cd ~/projects/my-api && python -m uvicorn app.main:app --reload
```

**That just happened.** Hermes created real files on your real filesystem, with working code, in seconds.

### Task 3: Make It Remember

```
You: Remember that my preferred Python framework is FastAPI and I use 
    4-space indentation.

Hermes: ✓ Saved to memory:
  - Preferred Python framework: FastAPI
  - Code style: 4-space indentation
```

Next session, next week, next month — Hermes will **still remember this**. No re-explaining.

---

## 1.7 The Big Picture — What You Just Unlocked

In 5 minutes, you've experienced three core capabilities:

```mermaid
flowchart TD
    MEM["🧠 MEMORY<br/><i>Learns & persists across sessions</i>"]
    TOOL["🔧 TOOLS<br/><i>Terminal, files, web, browser, code, cron</i>"]
    PLAT["💬 PLATFORMS<br/><i>Telegram, Discord, Slack, WhatsApp, CLI</i>"]

    MEM --- TOOL
    TOOL --- PLAT
    PLAT --- MEM

    DESC["<b>Together =</b> An AI that knows you, acts for you,<br/>and meets you where you already work."]
    MEM --> DESC
```

**What's next:** In Chapter 2, we'll dive into *how* Hermes works — the agent loop, model selection, toolsets, and configuration. You'll understand what's happening under the hood so you can bend Hermes to your will.

But first — if you want Hermes on your phone right now...

### Bonus: Connect to Telegram (2 minutes)

```bash
hermes gateway setup
```

Select Telegram, enter your bot token (from [@BotFather](https://t.me/BotFather)), and:

```
✓ Gateway running
✓ Telegram connected: @YourHermesBot

Message your bot on Telegram to start chatting.
Same agent, same memory, same tools — now in your pocket.
```

Now you have Hermes on your phone. **Every feature from the CLI is available through Telegram.** Send voice messages, images, files — Hermes handles them all.

---

## Chapter 1 Summary

| Concept | What You Learned |
|---------|-----------------|
| What Hermes is | Autonomous AI agent with memory, tools, and multi-platform presence |
| Installation | One command: `curl ... \| bash` then `hermes setup` |
| First interaction | `hermes` → chat, create projects, save memories |
| Quick win | Created a real FastAPI project in seconds |
| Telegram gateway | `hermes gateway setup` → AI in your pocket |
| Key insight | Hermes remembers, acts, and lives where you work |

**Next:** [Chapter 2: Core Concepts →](ch02-core-concepts.md)

---

<!-- SCREENSHOT: Hermes welcome banner in terminal -->
<!-- SCREENSHOT: Setup wizard model selection -->
<!-- SCREENSHOT: FastAPI project creation output -->
<!-- SCREENSHOT: Telegram bot first message -->


---

# Chapter 2: Core Concepts

> **Understand the engine before you drive the car. This chapter demystifies how Hermes thinks, acts, and remembers.**

---

## 2.1 The Agent Loop — How Hermes Thinks

Everything Hermes does follows one repeating pattern — the **agent loop**:

```mermaid
flowchart TD
    A["<b>1. BUILD PROMPT</b><br/>Assemble system prompt + context<br/><i>memory, skills, tools, history</i>"]
    B["<b>2. CALL LLM</b><br/>Send everything to the LLM<br/><i>Claude, GPT-4, Gemini, etc.</i>"]
    C{"<b>3. PARSE RESPONSE</b><br/>Tool call?"}
    D["YES: Run the tool"]
    E["DONE: Reply to user"]
    F["Append tool result"]

    A --> B --> C
    C -->|Tool call| D --> F --> A
    C -->|Text response| E
```

Here's what that looks like in practice:

```
You: Set up a Python project with pytest

Turn 1:
  LLM → "I'll create the project structure."
       Tool call: terminal("mkdir -p myproject/tests")
       Tool call: write_file("myproject/tests/__init__.py", "")
       
Turn 2:
  LLM → "Now I'll add the test configuration."
       Tool call: write_file("myproject/pyproject.toml", "[tool.pytest]...")
       
Turn 3:
  LLM → "Project created! Here's the structure:
       myproject/
       ├── src/
       ├── tests/
       │   └── __init__.py
       └── pyproject.toml
       
       Run tests with: pytest"
```

**Three things to notice:**

1. **Multiple turns** — Hermes doesn't do everything in one shot. Each LLM call is a "turn," and complex tasks take multiple turns
2. **Tool results feed back** — the output of one tool call becomes context for the next
3. **It stops when done** — the LLM decides when to respond with text instead of more tool calls

### Turn Limits

Hermes doesn't loop forever. The default is **90 turns per conversation turn** (configurable):

```yaml
# ~/.hermes/config.yaml
agent:
  max_turns: 90
```

Most tasks complete in 2-15 turns. If Hermes hits the limit, it summarizes what it accomplished and what's left.

### Context Compression

When the conversation gets long (near the model's token limit), Hermes automatically **compresses context** — summarizing older messages while keeping recent ones intact:

```yaml
compression:
  enabled: true
  threshold: 0.50    # Compress when 50% of context window used
  target_ratio: 0.20  # Compress down to 20% of original
```

You can also trigger it manually:

```
/compress
```

---

## 2.2 Models & Providers — The Brains

Hermes is **provider-agnostic** — it doesn't care which LLM powers it. You choose.

### Provider Overview

| Provider | Auth Method | Key Env Var | Best For |
|----------|-------------|-------------|----------|
| **OpenRouter** | API key | `OPENROUTER_API_KEY` | Access to 200+ models, one key |
| **Anthropic** | API key | `ANTHROPIC_API_KEY` | Claude models — best for coding |
| **OpenAI** | API key | `OPENAI_API_KEY` | GPT-4o, o3 |
| **Google Gemini** | API key | `GOOGLE_API_KEY` | Large context windows |
| **DeepSeek** | API key | `DEEPSEEK_API_KEY` | Budget-friendly coding |
| **xAI / Grok** | API key | `XAI_API_KEY` | Grok models |
| **Z.AI / GLM** | API key | `GLM_API_KEY` | GLM models |
| **GitHub Copilot** | OAuth | `hermes login` | Free with Copilot subscription |
| **Custom endpoint** | Config | `model.base_url` + `model.api_key` | Self-hosted, local models |

### Choosing Your Model

```bash
# Interactive model picker
hermes model

# Set directly
hermes config set model.default anthropic/claude-sonnet-4
hermes config set model.provider openrouter
```

**Model tiers for different tasks:**

```mermaid
flowchart LR
    subgraph Complex["🧠 Complex Reasoning"]
        CR1["Claude Sonnet 4"]
        CR2["GPT-4o"]
        CRD["<i>Architecture, debugging, multi-step planning</i>"]
    end
    subgraph Fast["⚡ Fast & Cheap"]
        FC1["Claude Haiku"]
        FC2["Gemini Flash"]
        FCD["<i>Simple tasks, quick questions, bulk operations</i>"]
    end
    subgraph Coding["💻 Deep Coding"]
        DC1["Claude Sonnet 4"]
        DC2["DeepSeek V3"]
        DCD["<i>Code generation, refactoring, PR reviews</i>"]
    end
    subgraph LongContext["📚 Long Context"]
        LC1["Gemini 2.5 Pro (1M tokens)"]
        LCD["<i>Large codebases, document analysis</i>"]
    end
    subgraph Budget["💰 Budget"]
        BU1["DeepSeek V3"]
        BU2["Gemini Flash"]
        BUD["<i>When cost matters more than peak quality</i>"]
    end
```

### Switching Models Mid-Conversation

You don't need to restart to change models:

```
/model anthropic/claude-sonnet-4    # Switch for this session
/model deepseek/deepseek-chat       # Switch to budget model
```

### Credential Pools

Running multiple API keys for the same provider? Hermes rotates them automatically:

```bash
# Add additional keys
hermes auth add

# View all keys
hermes auth list openrouter
```

When one key hits a rate limit, Hermes silently rotates to the next. No interruption.

---

## 2.3 Toolsets — The Hands

Models think. **Toolsets act.** Each toolset is a bundle of related capabilities:

```mermaid
flowchart LR
    subgraph Toolsets["HERMES TOOLSETS"]
        direction TB
        T1["🌐 web — Search engines + content extraction"]
        T2["🔍 search — Web search only"]
        T3["🖥️ terminal — Shell commands + process management"]
        T4["📁 file — Read, write, search, patch files"]
        T5["🌍 browser — Browser automation (Chromium)"]
        T6["🐍 code_exec — Sandboxed Python execution"]
        T7["👁️ vision — Image analysis"]
        T8["🎨 image_gen — AI image generation"]
        T9["🎬 video — Video analysis & generation"]
        T10["🔊 tts — Text-to-speech"]
        T11["🧠 memory — Persistent cross-session memory"]
        T12["🔎 session_search — Search past conversations"]
        T13["👥 delegation — Subagent task delegation"]
        T14["⏰ cronjob — Scheduled task management"]
        T15["❓ clarify — Ask user clarifying questions"]
        T16["📨 messaging — Cross-platform message sending"]
        T17["✅ todo — In-session task planning"]
        T18["📋 kanban — Multi-agent work queues"]
        T19["🎵 spotify — Spotify playback control"]
        T20["🏠 homeassistant — Smart home control"]
        T21["🔒 safe — Minimal toolset for locked sessions"]
    end
```

### Managing Toolsets

```bash
# Interactive curses UI — toggle toolsets on/off
hermes tools

# Command line
hermes tools enable browser
hermes tools disable spotify

# List all
hermes tools list
```

**Important:** Tool changes take effect on the **next session** (`/reset` or new `hermes` invocation), not mid-conversation. This preserves prompt caching.

### The Tools in Action

Here's what a typical tool-enabled workflow looks like:

```
You: Find the latest version of React and update my project

Hermes uses: web (search for latest React version)
Hermes uses: file (read package.json)
Hermes uses: file (patch package.json with new version)
Hermes uses: terminal (npm install)

✓ React updated from 19.0.0 to 19.1.0 in ~/my-project/
```

Each tool call is a separate turn in the agent loop. Hermes decides which tools to use, in what order, based on your request.

---

## 2.4 Sessions — The Conversations

Every chat you have with Hermes is a **session** — a self-contained conversation with its own history, context, and state.

### Session Lifecycle

```mermaid
flowchart LR
    NEW["🆕 NEW SESSION<br/><i>Fresh context · Full tools · No memory</i>"]
    ACTIVE["✅ ACTIVE SESSION<br/><i>Growing context · Full tools · Can save memory</i>"]
    COMPRESSED["📦 COMPRESSED SESSION<br/><i>Summarized context · Full tools · Memory preserved</i>"]
    CLOSED["🗄️ CLOSED (archived)"]

    NEW -->|Start| ACTIVE -->|Compress| COMPRESSED -->|End| CLOSED
```

### Session Commands

```bash
# CLI — start a new session
hermes

# Resume most recent session
hermes --continue

# Resume a specific session by ID
hermes --resume 20260101_143052_abc123

# Resume by name
hermes --continue my-project
```

Inside a session:

```
/new              # Start fresh (same process, clean context)
/title auth-work  # Name this session for easy resume later
/undo             # Remove last exchange (oops, wrong prompt)
/history          # See conversation history (CLI)
```

### Session Storage

Sessions are stored in a local SQLite database:

```bash
# Browse sessions interactively
hermes sessions browse

# List recent sessions
hermes sessions list

# Export a session
hermes sessions export session_2026.jsonl

# Clean up old sessions
hermes sessions prune --older-than 30
```

**Key insight:** Sessions are local and private. Your conversation history never leaves your machine (unless you explicitly export or share it).

---

## 2.5 Configuration — The Control Panel

Hermes is configured through one YAML file and one `.env` file:

```
~/.hermes/
├── config.yaml     ← All settings (model, tools, agent behavior)
├── .env            ← API keys and secrets (never committed to git)
├── skills/         ← Installed skills
├── sessions/       ← Session transcripts
├── state.db        ← Session store (SQLite)
└── logs/           ← Gateway and error logs
```

### config.yaml — The Main Config

```yaml
# ~/.hermes/config.yaml

# Model configuration
model:
  default: anthropic/claude-sonnet-4
  provider: openrouter
  context_length: 200000

# Agent behavior
agent:
  max_turns: 90
  tool_use_enforcement: true

# Terminal settings
terminal:
  backend: local       # local, docker, ssh
  timeout: 180         # seconds

# Context compression
compression:
  enabled: true
  threshold: 0.50
  target_ratio: 0.20

# Memory
memory:
  memory_enabled: true
  user_profile_enabled: true
  provider: builtin    # builtin, honcho, mem0

# Security
security:
  tirith_enabled: false
  redact_secrets: false

# Delegation (subagents)
delegation:
  max_iterations: 50
  max_spawn_depth: 1
  max_concurrent_children: 3
```

### .env — Secrets

```bash
# ~/.hermes/.env
OPENROUTER_API_KEY=sk-or-v1-xxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxx
GOOGLE_API_KEY=AIzaxxxxx
```

### Quick Config Commands

```bash
# View current config
hermes config

# Edit config in your editor
hermes config edit

# Set individual values
hermes config set model.default deepseek/deepseek-chat
hermes config set agent.max_turns 120
hermes config set terminal.timeout 300

# Check for issues
hermes doctor
```

### Profiles — Multiple Configurations

If you need different setups for different projects:

```bash
# Create a profile (clones current config)
hermes profile create work --clone

# Switch to it
hermes profile use work

# Use a profile for one command
hermes -p work chat -q "Check production logs"
```

Each profile gets its own:
- Config and .env
- Sessions and memory
- Skills and history

```
~/.hermes/
├── config.yaml              ← Default profile
├── .env
├── profiles/
│   ├── work/
│   │   ├── config.yaml      ← Work profile
│   │   └── .env
│   └── personal/
│       ├── config.yaml      ← Personal profile
│       └── .env
```

---

## 2.6 How It All Fits Together

Let's zoom out and see the complete picture:

```mermaid
flowchart TD
    subgraph Platforms["📱 Messaging Platforms"]
        TG["Telegram"]
        DC["Discord"]
        CLI["CLI"]
        MORE["..."]
    end

    Platforms --> GW

    subgraph Core["🔧 Core"]
        GW["🔀 GATEWAY<br/><i>Routes messages · Manages connections</i>"]
        AL["🔁 AGENT LOOP<br/><i>Builds prompt · Calls LLM · Dispatches tools · Manages context</i>"]

        subgraph Internal["Internal State"]
            MEM["🧠 Memory"]
            SKL["📋 Skills"]
            SES["💬 Sessions"]
        end
    end

    GW --> AL

    subgraph Tools["🛠️ Toolsets"]
        T1["Terminal"]
        T2["Files"]
        T3["Web"]
        T4["Browser"]
        T5["Cron"]
        T6["Delegation"]
    end

    AL --> Tools

    subgraph Providers["☁️ Providers — 20+ LLM APIs"]
        P1["OpenRouter"]
        P2["Anthropic"]
        P3["OpenAI"]
        P4["Google"]
        PM["..."]
    end

    AL --> Providers
```

**The flow:**
1. You send a message (Telegram, Discord, CLI, etc.)
2. Gateway receives it and routes to a session
3. Agent loop builds a prompt with your message + memory + skills + tool schemas
4. LLM processes the prompt and decides: respond with text, or call a tool
5. If tool call → execute it → feed result back → repeat
6. If text response → deliver back through the same platform

**All platforms share the same session, memory, and tools.** Start a conversation on Telegram, continue it on CLI — seamless.

---

## 2.7 Key Vocabulary

Before we move on, let's lock in the terminology:

| Term | Definition |
|------|-----------|
| **Agent loop** | The think → act → observe cycle Hermes repeats until done |
| **Turn** | One cycle of the agent loop (one LLM call) |
| **Session** | A complete conversation with its own history and context |
| **Provider** | The LLM API service (OpenRouter, Anthropic, etc.) |
| **Model** | The specific LLM (Claude Sonnet 4, GPT-4o, etc.) |
| **Toolset** | A bundle of related tools (web, terminal, file, etc.) |
| **Tool** | A single capability (web_search, terminal, read_file, etc.) |
| **Skill** | A reusable procedure Hermes learns and reloads |
| **Memory** | Persistent facts that survive across sessions |
| **Profile** | An isolated Hermes configuration (config + .env + sessions) |
| **Gateway** | The service connecting Hermes to messaging platforms |
| **Context** | Everything the LLM sees: system prompt + history + tool output |
| **Compression** | Summarizing old context to stay within token limits |
| **Delegation** | Spawning a subagent to handle a subtask in isolation |
| **Cron** | A scheduled task that runs automatically at set times |

---

## Chapter 2 Summary

| Concept | What You Learned |
|---------|-----------------|
| Agent loop | Think → Act → Observe cycle, max 90 turns, auto-compression |
| Models & providers | 20+ providers, switch freely, credential rotation |
| Toolsets | 20+ tool bundles, enable/disable per platform |
| Sessions | Self-contained conversations, resumable, stored locally |
| Configuration | config.yaml + .env, quick commands, profiles for isolation |
| Architecture | Platform → Gateway → Agent Loop → Tools → Provider |

**Next:** [Chapter 3: Messaging Gateway →](ch03-messaging-gateway.md)

---

<!-- SCREENSHOT: Agent loop terminal output showing multiple tool calls -->
<!-- SCREENSHOT: hermes model interactive picker -->
<!-- SCREENSHOT: hermes tools curses UI -->
<!-- SCREENSHOT: hermes sessions browse list -->
<!-- SCREENSHOT: config.yaml in editor -->


---

# Chapter 3: Messaging Gateway — AI Everywhere

> **Your AI agent shouldn't live in a terminal. The gateway connects Hermes to Telegram, Discord, Slack, and 10+ platforms — full tools, full memory, everywhere you chat.**

---

## 3.1 What is the Gateway?

The **gateway** is a long-running background process that connects your Hermes agent to messaging platforms. It's the bridge between your chat apps and the AI brain:

```mermaid
flowchart TD
    subgraph platforms["Messaging Platforms"]
        direction LR
        T["💬 Telegram"]
        D["💬 Discord"]
        S["💬 Slack"]
        W["💬 WhatsApp"]
    end

    platforms -->|"messages"| GW["🔄 GATEWAY<br/><b>Scheduler</b><br/>Routes messages<br/>Manages sessions<br/>Handles platform auth"]

    GW -->|"routes to"| AL["🧠 AGENT LOOP<br/>Same brain<br/>Same memory<br/>Same tools"]

    classDef platform fill:#4a9eff,color:#fff,stroke:#2d7dd2
    classDef gateway fill:#ff6b35,color:#fff,stroke:#cc5529
    classDef agent fill:#2ecc71,color:#fff,stroke:#25a25a
    class T,D,S,W platform
    class GW gateway
    class AL agent
```

*One session per conversation — switch platforms freely.*

**Key insight:** The gateway doesn't create a separate Hermes — it connects your existing agent to messaging platforms. Same memory, same tools, same sessions. Start a conversation on Telegram, continue on CLI — it's one agent.

### Supported Platforms

```mermaid
flowchart LR
    subgraph platforms["SUPPORTED MESSAGING PLATFORMS"]
        direction TB
        subgraph chat["💬 Chat Apps"]
            direction TB
            C1["Telegram"]
            C2["Discord"]
            C3["WhatsApp"]
            C4["WeChat (Weixin)"]
            C5["iMessage*"]
        end
        subgraph biz["🏢 Business"]
            direction TB
            B1["Slack"]
            B2["Microsoft Teams"]
            B3["DingTalk"]
            B4["Feishu (Lark)"]
            B5["WeCom"]
        end
        subgraph other["📱 Other"]
            direction TB
            O1["Signal"]
            O2["Matrix"]
            O3["Mattermost"]
            O4["SMS"]
            O5["Email"]
        end
        subgraph home["🏠 Smart Home"]
            direction TB
            H1["Home Assistant"]
        end
        subgraph integ["🔌 Integrations"]
            direction TB
            I1["API Server (REST)"]
            I2["Webhooks"]
            I3["Open WebUI"]
        end
    end

    classDef cat fill:#4a9eff,color:#fff,stroke:#2d7dd2
    class C1,C2,C3,C4,C5,B1,B2,B3,B4,B5,O1,O2,O3,O4,O5,H1,I1,I2,I3 cat
```

*\* iMessage via BlueBubbles (requires Mac)*

That's **17+ platforms** — and they all have access to the same tools (terminal, files, web search, browser automation, etc.).

---

## 3.2 Setting Up Telegram — The Deep Dive

Telegram is the most popular platform for Hermes. It supports text, voice, images, files, slash commands, topics, and inline keyboards — everything you need for a full AI agent experience.

### Step 1: Create Your Bot

1. Open Telegram, search for **@BotFather**
2. Send `/newbot`
3. Choose a name (e.g., "My Hermes Agent")
4. Choose a username (e.g., `my_hermes_agent_bot`)
5. BotFather responds with your **bot token** — it looks like:
   ```
   7123456789:AAHfG3k9dBz8vN2mX5pLqRtWyUiOoP0aBcD
   ```
   **Save this.** You'll need it in Step 2.

### Step 2: Configure Hermes

```bash
# Interactive setup — walks you through everything
hermes gateway setup

# Or set directly in config.yaml
hermes config set telegram.token "YOUR_BOT_TOKEN"
```

The interactive setup will ask:
- Which platforms to enable
- Bot tokens / OAuth credentials for each
- Whether to enable voice (STT/TTS)
- Home channel (which chat receives notifications)

### Step 3: Start the Gateway

```bash
# Run in foreground (good for testing)
hermes gateway run

# Install as a background service (production)
hermes gateway install
hermes gateway start

# Check it's running
hermes gateway status
```

Foreground mode shows you every message as it arrives — great for debugging. Once everything works, switch to the background service.

### Step 4: Verify

Send a message to your bot on Telegram:

```
You: Hello Hermes, what can you do?

Hermes: Hey! I'm your Hermes agent. I can:
• Read and write files on your machine
• Run terminal commands
• Search the web
• Manage your schedule with cron jobs
• Remember things across sessions
• ...and much more. Just ask!
```

**It's alive.** Same agent as your CLI, now in your pocket.

### Telegram-Specific Features

| Feature | How It Works |
|---------|-------------|
| **Voice messages** | Auto-transcribed via STT, Hermes responds with text or voice |
| **Images** | Send a photo → Hermes analyzes it with vision tools |
| **Files** | Send documents → Hermes reads, edits, and sends them back |
| **Topics** | Separate conversations per topic in group chats |
| **Group chats** | Mention `@YourBot` to trigger (or DM directly) |
| **Inline commands** | Slash command menu built into the chat input |

---

## 3.3 Slash Commands — Your In-Chat Control Panel

Slash commands work identically across all messaging platforms and the CLI. They're how you control Hermes without leaving the conversation.

### Essential Commands

```
/new (/reset)        Start a fresh session
/model [name]        Show or switch model
/tools               Manage enabled toolsets
/yolo                Toggle command approval bypass
/voice [on|off|tts]  Control voice mode
/compress            Manually compress context
/stop                Kill background processes
/status              Show session info
/help                Show all commands
```

### Workflow Commands

```
/background <prompt> Run a task in the background while you keep chatting
/queue <prompt>      Queue a task for the next turn
/steer <prompt>      Inject context mid-task without interrupting
/goal [text]         Set a standing objective across turns
/branch              Fork the conversation for exploration
```

### How `/background` Works

```
You: /background research the top 10 React state management libraries in 2026

Hermes: ✅ Background task started. I'll notify you when it's done.

[You keep chatting normally...]

Hermes: ✅ Background task complete
Prompt: "research the top 10 React state management libraries in 2026"
Result: Here's the research summary...
1. Zustand — Lightweight, TypeScript-first...
2. Jotai — Atomic state management...
[etc.]
```

**The key insight:** `/background` lets you fire off tasks without waiting. Keep working, get notified when it's done.

### How `/steer` Works

```
You: Build me a FastAPI project with auth

Hermes: [working on project structure...]

You: /steer Use SQLAlchemy 2.0 with async, not Tortoise ORM

Hermes: [receives the steer after the next tool call, adjusts course]
✓ Using SQLAlchemy 2.0 with async engine...
```

`/steer` injects your message *after* the next tool call completes — it doesn't interrupt the current operation, but course-corrects before the next one.

### Discovery Commands

```
/skills              Browse and install skills
/skill <name>        Load a skill into the current session
/curator status      Check skill maintenance status
/cron                Manage scheduled jobs
/plugins             List installed plugins
/kanban              Multi-agent work queue
```

### Info Commands

```
/usage               Token usage for this session
/insights [days]     Usage analytics over time
/debug               Upload debug report for support
/profile             Show active profile info
/platforms           Show all connected platforms
```

---

## 3.4 Voice Mode — Talk to Your Agent

Hermes can **listen** and **speak**. This turns Telegram (or any platform) into a voice-to-voice AI assistant.

### Enabling Voice

```
/voice on            # Voice input → text response (default voice mode)
/voice tts           # Voice input → voice response (full voice-to-voice)
/voice off           # Disable voice mode
```

Or configure permanently:

```bash
hermes config set stt.enabled true
hermes config set tts.provider edge     # Free, no API key needed
```

### STT — Speech to Text

When you send a voice message, Hermes transcribes it automatically:

```mermaid
flowchart TD
    VM["🎤 Voice message"] --> STT["STT Provider<br/><i>priority order:</i>"]

    STT --> P1["1. Local faster-whisper<br/><i>free</i>"]
    STT --> P2["2. Groq Whisper<br/><i>free tier</i>"]
    STT --> P3["3. OpenAI Whisper<br/><i>paid</i>"]
    STT --> P4["4. Mistral Voxtral<br/><i>paid</i>"]

    P1 & P2 & P3 & P4 --> RESULT["Transcribed text → Agent loop → Response"]

    classDef voice fill:#9b59b6,color:#fff,stroke:#7d3c98
    classDef provider fill:#3498db,color:#fff,stroke:#2d7dd2
    classDef result fill:#2ecc71,color:#fff,stroke:#25a25a
    class VM voice
    class P1,P2,P3,P4 provider
    class RESULT result
```

**Setup local transcription (free, recommended):**

```bash
pip install faster-whisper
hermes config set stt.provider local
```

No API key needed. Runs locally on your machine. Model sizes:

| Size | VRAM | Speed | Accuracy |
|------|------|-------|----------|
| `tiny` | ~1 GB | Fastest | Good |
| `base` | ~1 GB | Fast | Great |
| `small` | ~2 GB | Medium | Very good |
| `medium` | ~5 GB | Slower | Excellent |
| `large-v3` | ~10 GB | Slowest | Best |

### TTS — Text to Speech

Hermes can respond with voice messages instead of text:

```
You: /voice tts

You: [voice message] "Summarize my unread emails"

Hermes: 🔊 [voice message] "You have 12 unread emails. The most urgent is
from your client about the deployment timeline..."
```

**TTS providers:**

| Provider | Cost | Quality | Setup |
|----------|------|---------|-------|
| **Edge TTS** | Free | Good | No config needed (default) |
| ElevenLabs | Free tier | Excellent | Set `ELEVENLABS_API_KEY` |
| OpenAI | Paid | Great | Set `VOICE_TOOLS_OPENAI_KEY` |
| MiniMax | Paid | Great | Set `MINIMAX_API_KEY` |
| NeuTTS (local) | Free | Good | `pip install neutts[all]` + `espeak-ng` |

**Edge TTS is the zero-config default** — it's free and works immediately. Upgrade to ElevenLabs if you want natural-sounding voices.

---

## 3.5 Other Platforms — Quick Setup

While Telegram is the most feature-rich, Hermes works across all major platforms. Here's how to set up the most common ones:

### Discord

```bash
hermes gateway setup    # Select Discord
```

**Requirements:**
1. Create a bot at [discord.com/developers](https://discord.com/developers)
2. Enable **Message Content Intent** (Bot → Privileged Gateway Intents) — *this is the #1 reason Discord bots go silent*
3. Generate a bot token and paste during setup

```
⚠️  Discord gotcha: Without Message Content Intent enabled, your bot
    will receive events but can't read message content. It will appear
    online but never respond. Enable it in the Discord Developer Portal.
```

### Slack

```bash
hermes gateway setup    # Select Slack
```

**Requirements:**
1. Create a Slack App at [api.slack.com](https://api.slack.com)
2. Subscribe to `message.channels` event — *without this, the bot only works in DMs*
3. Install to your workspace and copy the bot token

### WhatsApp

Hermes supports WhatsApp via the WhatsApp Business API or third-party bridges. Setup varies by provider — `hermes gateway setup` will walk you through the options.

### Signal, Matrix, Email, SMS

All follow the same pattern: `hermes gateway setup` → select platform → enter credentials. Each has platform-specific requirements documented at:

```
https://hermes-agent.nousresearch.com/docs/user-guide/messaging/
```

### Multi-Platform Simultaneous Connections

You can connect **multiple platforms at once**:

```yaml
# config.yaml
telegram:
  token: "your-telegram-token"

discord:
  token: "your-discord-token"

slack:
  token: "xoxb-your-slack-token"
```

All platforms route to the same agent. One brain, many faces.

---

## 3.6 Gateway Lifecycle

The gateway is a persistent service. Here's how to manage it:

### Commands

```bash
hermes gateway run        # Foreground (testing, debugging)
hermes gateway install    # Install as system service
hermes gateway start      # Start the background service
hermes gateway stop       # Stop the background service
hermes gateway restart    # Restart (picks up config changes)
hermes gateway status     # Check running status + connected platforms
hermes gateway setup      # Reconfigure platforms
```

### In-Chat Gateway Commands

These work inside any connected messaging platform:

```
/restart              Restart the gateway (picks up config changes)
/sethome              Set this chat as the home channel
/update               Update Hermes to latest version
/platforms            Show all connected platforms
/approve              Approve a pending command
/deny                 Deny a pending command
```

### Checking Logs

When something goes wrong, check the gateway logs:

```bash
# View recent errors
grep -i "error\|failed" ~/.hermes/logs/gateway.log | tail -20

# Follow live
tail -f ~/.hermes/logs/gateway.log
```

### Restarting from Chat

No need to SSH into your server to restart:

```
You: /restart

Hermes: 🔄 Gateway restarting...
✓ Gateway restarted. All platforms reconnected.
```

---

## 3.7 The Approval System — Safety First

When Hermes wants to run a potentially dangerous command (like `rm -rf`, `git push --force`, or writing to system files), it asks for your permission first.

### How Approvals Work

```
Hermes: ⚠️ I need to run a potentially destructive command:
        rm -rf /tmp/old-builds/
        
        /approve to allow, /deny to reject

You: /approve

Hermes: ✓ Command executed. Removed /tmp/old-builds/
```

This only triggers for commands flagged as **destructive** — normal operations (reading files, searching, creating projects) run without approval.

### Approval Modes

```bash
# Manual — always ask (default)
hermes config set approvals.mode manual

# Smart — AI auto-approves low-risk, asks on high-risk
hermes config set approvals.mode smart

# Off — skip all approvals (use at your own risk)
hermes config set approvals.mode off
```

**Recommendation:** Use `smart` mode. It blocks dangerous operations but doesn't waste your time on safe ones.

### YOLO Mode — Skip Everything

For when you trust Hermes completely (or are in a rush):

```bash
# Per-session (in chat)
/yolo

# Per-invocation (CLI)
hermes --yolo

# Environment variable
export HERMES_YOLO_MODE=1
```

YOLO mode skips *all* approval prompts. Use it when you know what you're doing.

---

## 3.8 Practical Patterns

Here's how people actually use the gateway day-to-day:

### Pattern 1: Phone-Driven Development

```
[On the bus, Telegram]

You: What's the status of the auth module?

Hermes: The auth module is 80% complete. Remaining:
- JWT refresh token rotation
- Rate limiting on /login
- Unit tests for password reset

Want me to continue?

You: Yes, finish the JWT refresh tokens

Hermes: ✓ JWT refresh token rotation implemented.
Added to auth/routes.py and auth/tests/test_refresh.py.
3 tests passing.
```

### Pattern 2: Voice-Powered Research

```
[Driving, voice message]

You: 🔊 "What were our top 3 selling products last month?"

Hermes: 🔊 "Your top 3 sellers in April were:
1. Premium Widget — 2,340 units, $47K revenue
2. Standard Gadget — 1,890 units, $28K revenue  
3. Mega Pack Bundle — 670 units, $33K revenue"
```

### Pattern 3: Multi-Platform Workflow

```
[Morning: Telegram]
You: Start the daily blog pipeline

Hermes: ✓ Blog pipeline started. 2 articles queued.
Topic 1: "5 Python Patterns Every Senior Dev Should Know"
Topic 2: "Docker Multi-Stage Builds: A Practical Guide"

[Afternoon: CLI]
You: hermes
Hermes: Welcome back! Both blog articles are drafted and ready for review.
       Want me to show them?

[Evening: Telegram]
You: Publish both articles

Hermes: ✓ Both articles published to your blog.
```

**Same agent. Same context. Different platforms.**

### Deployment Cost Quick-Reference

How much does it actually cost to run Hermes 24/7?

| Option | Monthly Cost | RAM | Best For |
|--------|-------------|-----|----------|
| **$5 VPS** (Hetzner CX22, Vultr, DigitalOcean) | $4–6 | <500MB without local LLM | Most users — always-on Telegram bot |
| **Serverless** (Daytona, Modal) | ~$0 idle, pay-per-wake | Scales to zero | Infrequent use — hibernates between messages |
| **Privacy VPS** (local Ollama) | $15–30 (16GB+ RAM VPS) | 4–16GB | Zero API cost, full data privacy |

**Typical monthly total:** $5 VPS + $5 API calls = **~$10/month** for a personal 24/7 AI agent. Compare: Claude Code Pro is $20/mo, Max is $200/mo. Different tools, but the barrier to entry is remarkably low.

> **💡 Tip:** Start with the cheapest $5 VPS + OpenRouter. You can always scale up later. The gateway uses minimal resources — most of the cost is LLM API calls, not hosting.

---

## 3.9 Troubleshooting the Gateway

### Gateway won't start

```bash
hermes doctor           # Check dependencies and config
hermes gateway status   # See what's happening
tail -20 ~/.hermes/logs/gateway.log   # Check error logs
```

### Bot is silent on Telegram

1. Check gateway is running: `hermes gateway status`
2. Check logs for errors: `grep -i "telegram\|error" ~/.hermes/logs/gateway.log`
3. Verify bot token: `hermes config` → look for `telegram.token`
4. Make sure you're messaging the right bot

### Bot is silent on Discord

1. **Enable Message Content Intent** — this is the #1 cause
2. Check bot has permissions to read messages in the channel
3. Verify gateway is running

### Bot is silent on Slack

1. Subscribe to `message.channels` event — without it, bot only works in DMs
2. Check bot is invited to the channel
3. Verify token starts with `xoxb-`

### Voice not working

```bash
# Check STT is enabled
hermes config get stt.enabled

# Check provider
hermes config get stt.provider

# Install local transcription
pip install faster-whisper

# Restart gateway
hermes gateway restart
```

### Gateway dies on server logout

```bash
# Linux: enable linger so the service persists after logout
sudo loginctl enable-linger $USER

# WSL2: enable systemd in /etc/wsl.conf
[boot]
systemd=true
```

---

## Chapter 3 Key Vocabulary

| Term | Definition |
|------|-----------|
| **Gateway** | The background service connecting Hermes to messaging platforms |
| **Home channel** | The default chat where notifications and cron deliveries are sent |
| **Slash command** | An in-chat command prefixed with `/` (e.g., `/model`, `/yolo`) |
| **STT** | Speech-to-Text — transcribes voice messages into text |
| **TTS** | Text-to-Speech — converts responses into voice messages |
| **Approval** | Safety mechanism requiring user confirmation for dangerous commands |
| **YOLO mode** | Bypasses all approval prompts for faster execution |
| **Topic** | Telegram's thread-like feature for separate conversations in one group |
| `/background` | Runs a task asynchronously while you continue chatting |
| `/steer` | Injects context mid-task without interrupting the current operation |
| `/queue` | Stacks a command for the next agent turn |
| `/goal` | Sets a standing objective Hermes works on across multiple turns |

---

## Chapter 3 Summary

| Topic | What You Learned |
|-------|-----------------|
| Gateway architecture | Background service bridging platforms → agent loop |
| Telegram setup | BotFather → token → `hermes gateway setup` → live |
| Slash commands | 30+ commands for session control, config, and workflow |
| Voice mode | STT (faster-whisper free) + TTS (Edge TTS free) |
| Other platforms | Discord, Slack, WhatsApp, Signal, Matrix, 17+ total |
| Gateway lifecycle | `run`, `install`, `start`, `stop`, `restart`, `status` |
| Approval system | Manual / Smart / YOLO — safety vs speed tradeoff |
| Troubleshooting | Doctor, logs, platform-specific gotchas |

**Next:** [Chapter 4: Skills & Memory →](ch04-skills-memory.md)

---

<!-- SCREENSHOT: Gateway startup output in terminal -->
<!-- SCREENSHOT: Telegram bot conversation showing slash command menu -->
<!-- SCREENSHOT: Voice message transcription in Telegram -->
<!-- SCREENSHOT: /background task notification in Telegram -->
<!-- SCREENSHOT: Approval prompt with /approve / /deny buttons -->
<!-- SCREENSHOT: hermes gateway status output -->
<!-- SCREENSHOT: Discord bot responding in a channel -->


---

# Chapter 4: Skills & Memory — Making Hermes Smarter Over Time

> **Every conversation with Hermes makes it better. Skills teach it procedures. Memory gives it permanence. Together, they transform a general AI into your personal expert.**

---

## 4.1 The Learning Loop — How Hermes Improves Itself

The most surprising thing about Hermes isn't what it can do — it's that **it changes**. The more you use it, the better it gets. This isn't marketing. It's an observable, verifiable closed loop.

```mermaid
flowchart TD
    A["1️⃣ CURATE MEMORY<br/>After each task, decide what's worth<br/>remembering → save to persistent store"]
    B["2️⃣ CREATE SKILL<br/>If the solution is reusable, distill it<br/>into a SKILL.md with steps + pitfalls"]
    C["3️⃣ IMPROVE SKILL<br/>When a Skill fails or gets corrected,<br/>patch it — it never makes the same mistake twice"]
    D["4️⃣ RECALL via FTS5<br/>FTS5 full-text search finds the right<br/>skill/memory instantly on next task"]
    E["5️⃣ USER MODEL<br/>Over time, Hermes builds a model of<br/>who you are, what you prefer, how you work"]

    A --> B --> C --> D --> E

    classDef step fill:#3498db,color:#fff,stroke:#2980b9,rx:8,ry:8
    class A,B,C,D,E step
```

*Nobody teaches it any of this. It figures it out alone.*

**Step 1: Memory Curation** — After each conversation, Hermes actively decides what's worth remembering. Not brute-force chat history dumps — selective, indexed saves to a SQLite database with FTS5 full-text search. (Covered in §4.3)

**Step 2: Skill Creation** — When Hermes finishes a complex task, it asks: *will this solution be useful again?* If yes, it distills the approach into a standalone Skill file. (Covered in §4.2)

**Step 3: Skill Self-Improvement** — Creating a Skill isn't the end. Every time you correct Hermes or a Skill produces a suboptimal result, it patches the Skill itself. The longer you use it, the fewer mistakes it repeats. (Covered in §4.2, Curator section)

**Step 4: FTS5 Recall** — When a new task arrives, Hermes searches its skill library and memory with full-text search. It finds relevant experience in milliseconds, not by re-deriving solutions from scratch. (Covered in §4.3, Session Search)

**Step 5: User Modeling** — Over time, Hermes builds a picture of who you are — your stack, your style, your quirks. This is injected into every session automatically. (Covered in §4.3, Memory Architecture)

These five steps form a flywheel: **more use → more data → better skills → better results → more use.** The harness grows on its own.

---

## 4.2 Skills — Reusable Procedures

A **skill** is a structured document that teaches Hermes how to handle a specific type of task. Think of it as a playbook — step-by-step instructions, pitfalls, commands, and context that load into the agent's prompt when relevant.

### What Skills Look Like

Every skill is a `SKILL.md` file with YAML frontmatter and a markdown body:

```mermaid
flowchart TD
    subgraph skill["SKILL STRUCTURE"]
        FM["📋 YAML frontmatter<br/>name · description · version · author<br/>metadata → tags"]
        BODY["📝 Markdown Body<br/><br/># Skill Name<br/>## When to Use — trigger conditions<br/>## Steps — numbered with exact commands<br/>## Verification — confirm it worked"]
        OPT["📁 Optional Extras<br/>references/ · templates/ · scripts/"]
    end

    FM --> BODY --> OPT

    classDef yaml fill:#f39c12,color:#fff,stroke:#d68910
    classDef md fill:#2ecc71,color:#fff,stroke:#25a25a
    classDef opt fill:#95a5a6,color:#fff,stroke:#7f8c8d
    class FM yaml
    class BODY md
    class OPT opt
```

The YAML frontmatter provides metadata (name, description, tags, version). The markdown body is the actual knowledge — step-by-step procedures, commands, pitfalls, and verification steps.

### The Skills Hub — 88+ Pre-Built Skills

Hermes ships with a **skills hub** — a curated catalog of community-maintained skills across 17+ categories:

```bash
# Browse all available skills interactively
hermes skills browse

# Search by keyword
hermes skills search "docker"

# Preview without installing
hermes skills inspect github-code-review

# Install a skill
hermes skills install github-code-review

# Install from a direct URL
hermes skills install https://raw.githubusercontent.com/user/repo/main/SKILL.md
```

**Category highlights:**

```mermaid
flowchart LR
    subgraph cats["SKILL CATEGORIES — 88+ skills"]
        direction TB
        subgraph sw["🔧 Software Dev"]
            SW1["debugging · test-driven-dev<br/>writing-plans · spike"]
        end
        subgraph cr["🎨 Creative"]
            CR1["ascii-art · design-md<br/>excalidraw · sketch"]
        end
        subgraph wd["🌐 Web Dev"]
            WD1["blog · fullstack<br/>devcard · web-dkc"]
        end
        subgraph ai["🤖 AI Agents"]
            AI1["claude-code · codex<br/>kilocode · opencode"]
        end
        subgraph ds["📊 Data Science"]
            DS1["jupyter-live"]
        end
        subgraph pr["📝 Productivity"]
            PR1["notion · linear<br/>google-ws · powerpoint"]
        end
        subgraph gm["🎮 Gaming & Media"]
            GM1["youtube-content · gif-search<br/>spotify · songsee"]
        end
        subgraph rs["🔬 Research"]
            RS1["arxiv · blogwatcher<br/>polymarket · llm-wiki"]
        end
        subgraph sh["🏠 Smart Home"]
            SH1["openhue"]
        end
        subgraph rt["🔒 Red Teaming"]
            RT1["godmode"]
        end
        subgraph dv["🛠 DevOps"]
            DV1["webhook-subs · kanban"]
        end
        subgraph em["📧 Email"]
            EM1["himalaya"]
        end
        subgraph aa["🚀 Autonomous Agents"]
            AA1["hermes-agent<br/>kanban-worker · kanban-orchestrator"]
        end
    end

    classDef cat fill:#3498db,color:#fff,stroke:#2980b9
    class SW1,CR1,WD1,AI1,DS1,PR1,GM1,RS1,SH1,RT1,DV1,EM1,AA1 cat
```

### Loading Skills into a Session

Skills are loaded automatically when relevant, or manually when you need them:

```bash
# Preload skills at startup
hermes -s github-code-review,plan

# Load inside a session
/skill plan

# Browse and install from inside a session
/skills
```

**In cron jobs**, attach skills so the scheduled agent has the right knowledge:

```yaml
# A cron job that writes blog articles
skills: ["blog", "marketing-copy", "humanizer"]
prompt: "Write and publish today's blog article"
```

### Creating Your Own Skills

When Hermes solves a complex problem or discovers a non-trivial workflow, save it:

```
You: That debugging session was rough. Save it as a skill so you 
     never have to rediscover all this.

Hermes: ✓ Skill saved as "systematic-debugging"

  Covers:
  - 4-phase root cause analysis
  - Environment-specific pitfalls
  - Verification steps
  - Exact commands for each phase
```

**When to save a skill:**
- Complex task with 5+ tool calls that succeeded
- You corrected Hermes and the corrected approach worked
- Non-trivial workflow discovered (API integration, deployment pipeline, etc.)
- User asked you to remember a procedure

**What makes a good skill:**
- Clear trigger conditions ("Use when...")
- Numbered steps with exact commands
- Pitfalls section (what went wrong before)
- Verification steps (how to confirm it worked)

### The Curator — Automatic Skill Maintenance

Hermes has a built-in **curator** that automatically maintains skills over time:

```mermaid
flowchart LR
    ACTIVE["✅ ACTIVE<br/><i>in use</i>"] -->|"idle over time"| STALE["⏳ STALE<br/><i>idle</i>"]
    STALE -->|"further idle"| ARCHIVED["📦 ARCHIVED<br/><i>backed up</i>"]

    classDef active fill:#2ecc71,color:#fff,stroke:#25a25a
    classDef stale fill:#f39c12,color:#fff,stroke:#d68910
    classDef archived fill:#95a5a6,color:#fff,stroke:#7f8c8d
    class ACTIVE active
    class STALE stale
    class ARCHIVED archived
```

- Usage tracked via `.usage.json`
- Pinned skills are exempt from all auto-transitions
- Only agent-created skills are touched; hub/bundled skills are never modified
- Nothing is ever deleted — max action is archive

```bash
# Check curator status
hermes curator status
/curator status

# Pin a skill (protect from archive)
hermes curator pin my-critical-skill

# Force a maintenance run
hermes curator run

# Restore an archived skill
hermes curator restore my-old-skill
```

**The curator never deletes** — it archives with a backup. Pinned skills are completely protected.

---

## 4.3 Memory — Persistent Knowledge Across Sessions

While skills store *procedures*, **memory** stores *facts*. Memory survives across sessions — when you close a conversation and start a new one, Hermes still knows who you are, what you're working on, and what matters to you.

### Two Memory Stores

```mermaid
flowchart TD
    subgraph memory["MEMORY ARCHITECTURE"]
        UP["👤 USER PROFILE<br/><b>Who you are:</b><br/>• Name, role, timezone<br/>• Tech stack preferences<br/>• Communication style<br/>• Device info<br/><br/><i>\"Bio is a senior fullstack<br/>architect using React,<br/>TypeScript, Flutter...\"</i>"]
        AN["🤖 AGENT NOTES<br/><b>What Hermes has learned:</b><br/>• Environment facts<br/>• Project conventions<br/>• Tool quirks discovered<br/>• Lessons from mistakes<br/><br/><i>\"Hermes home is at<br/>C:\\Users\\bio\\AppData...\"</i>"]
    end

    UP & AN -->|"injected into<br/>every session"| SESSION["💬 Every Session"]

    classDef profile fill:#3498db,color:#fff,stroke:#2d7dd2
    classDef notes fill:#e74c3c,color:#fff,stroke:#c0392b
    classDef session fill:#2ecc71,color:#fff,stroke:#25a25a
    class UP profile
    class AN notes
    class SESSION session
```

*Both are injected into every session automatically. Memory is compact — only facts that persist.*

### How Memory Gets Saved

Memory is saved proactively — Hermes stores facts that will matter later:

**User profile** — saved when:
- User shares personal details (name, role, timezone)
- User corrects behavior or states preferences
- User's tech stack or workflow becomes clear

**Agent notes** — saved when:
- Environment facts discovered (OS, paths, tool versions)
- Project conventions identified
- Tool quirks or non-obvious behaviors found
- User corrects an approach

**What NOT to save to memory:**
- Task progress or session outcomes → use `session_search` instead
- Temporary TODO state → use the `todo` tool
- Raw data dumps → save to files
- Anything that will be stale in 7 days

### Memory Commands

```bash
# Check memory status
hermes memory status

# In-session memory management (Hermes does this automatically,
# but you can also request it)
```

Inside a session:
```
You: Remember that I always use pytest with xdist for testing

Hermes: ✓ Saved to memory: "User prefers pytest with xdist for 
        parallel test execution."
```

### Session Search — Recalling the Past

When you need to find something from a previous conversation, **session search** is your time machine. It uses FTS5 (full-text search) against the local SQLite session store — no LLM calls, instant results.

```bash
# Browse recent sessions
hermes sessions browse

# Search sessions by keyword
hermes sessions list --search "auth refactor"
```

Inside a session, Hermes uses session_search automatically when you reference past events:

```
You: What did we decide about the database schema last week?

Hermes: [searches session history]
        Last week in the "project-setup" session, we decided on:
        - PostgreSQL 16 with UUID primary keys
        - Async SQLAlchemy 2.0
        - Alembic for migrations
        - Separate read/write connection pools
```

**Three search modes:**

```mermaid
flowchart TD
    subgraph modes["SESSION SEARCH MODES"]
        M1["1️⃣ DISCOVERY — search by keyword<br/><code>session_search(query='docker networking')</code><br/>→ matching sessions + context windows"]
        M2["2️⃣ SCROLL — read inside a found session<br/><code>session_search(session_id='...', around_msg=42)</code><br/>→ ±5 messages around the match"]
        M3["3️⃣ BROWSE — recent sessions chronologically<br/><code>session_search()</code><br/>→ latest sessions with previews"]
    end

    classDef mode fill:#9b59b6,color:#fff,stroke:#7d3c98
    class M1,M2,M3 mode
```

### Memory Backends

Hermes supports pluggable memory backends:

| Backend | Setup | Best For |
|---------|-------|----------|
| **Built-in** (default) | No config needed | Most users — fast, local, private |
| **Honcho** | `hermes honcho setup` | Multi-agent memory sharing, cloud sync |
| **Mem0** | Set `MEM0_API_KEY` | Advanced memory with deduplication |

```bash
# Switch memory provider
hermes config set memory.provider honcho
hermes memory setup

# Disable memory entirely
hermes memory off
```

**Recommendation:** Stick with built-in unless you need multi-agent memory sharing or cloud sync.

---

## 4.4 Profiles — Isolated Hermes Instances

Profiles let you run multiple independent Hermes configurations on the same machine:

```mermaid
flowchart TD
    subgraph hermes["~/.hermes/"]
        CFG["📄 config.yaml<br/><i>← Default profile</i>"]
        ENV["🔐 .env"]
        SKILLS["📁 skills/"]
        SESSIONS["📁 sessions/"]
        STATE["🗄️ state.db<br/><i>← Shared session store</i>"]
        subgraph profiles["📁 profiles/"]
            subgraph work["🏢 work/ — Work profile"]
                WCFG["📄 config.yaml<br/><i>separate model, tools</i>"]
                WENV["🔐 .env<br/><i>separate API keys</i>"]
                WSKILLS["📁 skills/<br/><i>separate skills</i>"]
                WSESSIONS["📁 sessions/<br/><i>separate history</i>"]
            end
            subgraph personal["🏠 personal/ — Personal profile"]
                PCFG["📄 config.yaml"]
                PENV["🔐 .env"]
                PSKILLS["📁 skills/"]
                PSESSIONS["📁 sessions/"]
            end
        end
    end

    classDef file fill:#3498db,color:#fff,stroke:#2d7dd2
    classDef dir fill:#2ecc71,color:#fff,stroke:#25a25a
    classDef profile fill:#e74c3c,color:#fff,stroke:#c0392b
    class CFG,ENV,STATE,WCFG,WENV,PCFG,PENV file
    class SKILLS,SESSIONS,WSKILLS,WSESSIONS,PSKILLS,PSESSIONS dir
    class profiles,work,personal profile
```

**Each profile gets its own:** config, API keys, skills, sessions, and memory.

```bash
# Create a profile (clones current config)
hermes profile create work --clone

# Create with everything cloned (sessions, skills, memory)
hermes profile create work --clone-all

# Switch default profile
hermes profile use work

# Use a profile for one command
hermes -p work chat -q "Check production logs"

# List profiles
hermes profile list

# Export/import (share configs between machines)
hermes profile export work > work-profile.tar.gz
hermes profile import work-profile.tar.gz
```

**When to use profiles:**
- **Work vs personal** — different API keys, different projects, different memory
- **Client work** — each client gets isolated memory and sessions
- **Experimentation** — test new models/configs without risking your main setup
- **Multi-tenant** — run separate Hermes instances for different purposes

---

## 4.5 Credential Pools — Rate Limit Busting

Running into rate limits? Add multiple API keys for the same provider and Hermes rotates automatically:

```bash
# Add additional API keys interactively
hermes auth add

# View all keys for a provider
hermes auth list openrouter

# Remove a specific key
hermes auth remove openrouter 2

# Reset exhaustion status (if keys recover)
hermes auth reset openrouter
```

```mermaid
flowchart LR
    K1["🔑 Key 1"] -->|"Rate limited?"| R1["🔄 Rotate"]
    K2["🔑 Key 2"] -->|"Rate limited?"| R2["🔄 Rotate"]
    K3["🔑 Key 3"] -->|"Available!"| USE["✅ Use this"]

    R1 --> K2
    R2 --> K3

    classDef key fill:#3498db,color:#fff,stroke:#2d7dd2
    classDef rotate fill:#f39c12,color:#fff,stroke:#d68910
    classDef use fill:#2ecc71,color:#fff,stroke:#25a25a
    class K1,K2,K3 key
    class R1,R2 rotate
    class USE use
```

*Automatic, silent, zero interruption.*

**When this matters:**
- Heavy cron job schedules hitting the same provider
- Multiple concurrent agents sharing keys
- Free tier keys with low rate limits
- Batch processing large datasets

---

## 4.6 Context Compression — Staying Within Limits

When a conversation grows long (approaching the model's token limit), Hermes automatically **compresses context** — summarizing older messages while preserving recent ones:

```yaml
# config.yaml
compression:
  enabled: true
  threshold: 0.50    # Compress when 50% of context window used
  target_ratio: 0.20  # Compress down to 20% of original
```

```mermaid
flowchart TD
    subgraph lifecycle["CONTEXT LIFECYCLE"]
        direction LR
        NEW["📄 New session<br/><i>empty</i>"] -->|"messages arrive"| GROW["📈 Growing<br/><i>messages accumulating</i>"]
        GROW -->|"50% full"| NEAR["⚠️ Near limit"]
        NEAR -->|"auto-trigger"| COMP["📦 Compressed<br/><i>summarized</i>"]
    end

    subgraph before["Before compression"]
        B1["msg 1"] --- B2["msg 2"] --- BD["..."] --- B48["msg 48"] --- B49["msg 49"] --- BN["new"]
    end

    subgraph after["After compression"]
        SUM["📝 Summary of<br/>msgs 1-47"] --- A48["msg 48"] --- A49["msg 49"] --- AN["new"] --- AD["..."]
    end

    NEAR -.->|"shows"| before
    COMP -.->|"becomes"| after

    classDef phase fill:#3498db,color:#fff,stroke:#2d7dd2
    classDef old fill:#e74c3c,color:#fff,stroke:#c0392b
    classDef sum fill:#2ecc71,color:#fff,stroke:#25a25a
    class NEW,GROW,NEAR,COMP phase
    class B1,B2,BD,B48,B49,BN old
    class SUM,A48,A49,AN,AD sum
```

*Recent messages preserved verbatim. Older messages become a summary. You can also trigger manually: `/compress`*

---

## 4.7 Skills + Memory in Practice

Let's see how skills and memory work together in a real workflow:

### Scenario: Building a New Project

```
Day 1 — First time building a FastAPI project with auth:

You: Set up a FastAPI project with JWT auth and PostgreSQL

Hermes: [uses tools to create project structure]
        [hits a few snags with async SQLAlchemy setup]
        [eventually gets everything working]
        
        ✓ Project created. That async SQLAlchemy + Alembic 
        setup had some version-specific quirks.
        
You: Save this as a skill and remember the key facts.

Hermes: ✓ Skill saved: "fastapi-auth-setup"
        ✓ Memory saved: "User prefers FastAPI with SQLAlchemy 
          2.0 async, Alembic migrations, JWT auth via 
          python-jose"

──────────────────────────────────────────────────────

Day 15 — Building another API project:

You: Set up another FastAPI project, this time for inventory 
     management.

Hermes: [loads skill: fastapi-auth-setup]
        [loads memory: user's FastAPI preferences]
        [skips all the discovery from Day 1]
        
        ✓ Project created with your preferred stack:
        FastAPI + SQLAlchemy 2.0 async + Alembic + JWT.
        Used the same auth pattern from the skill.
        3 minutes instead of 15.
```

### Scenario: Cross-Session Continuity

```
Monday — You tell Hermes about your project:

You: I'm working on a fintech dashboard at ~/projects/dashboard.
     Stack is Next.js 15 with App Router, Tailwind, and tRPC.

Hermes: ✓ Saved to memory: project details, tech stack, path.

──────────────────────────────────────────────────────

Wednesday — New session, different platform:

You: [on Telegram] What was the tech stack for the dashboard 
     project?

Hermes: Your fintech dashboard at ~/projects/dashboard uses:
        Next.js 15 (App Router) + Tailwind CSS + tRPC.
        I remember from Monday.

──────────────────────────────────────────────────────

Friday — Yet another session:

You: Add a new route to the dashboard for transaction history.

Hermes: [loads memory, knows the project structure]
        [uses correct patterns: App Router, tRPC procedure]
        [follows project conventions automatically]
        
        ✓ Added /transactions route with tRPC router.
```

**Memory makes every session feel like a continuation, not a fresh start.**

---

## Chapter 4 Key Vocabulary

| Term | Definition |
|------|-----------|
| **Skill** | A reusable procedure document (SKILL.md) that teaches Hermes how to handle a task type |
| **Skill hub** | The curated catalog of 88+ community-maintained skills |
| **Frontmatter** | YAML metadata at the top of a skill (name, description, tags, version) |
| **Curator** | Automatic maintenance system that tracks skill usage and archives idle ones |
| **Memory** | Persistent facts (user profile + agent notes) that survive across sessions |
| **User profile** | Facts about the user (name, role, preferences, tech stack) |
| **Agent notes** | Facts Hermes discovers (environment, conventions, tool quirks) |
| **Session search** | FTS5-powered search across past conversation transcripts |
| **Profile** | An isolated Hermes configuration (config + .env + skills + sessions + memory) |
| **Credential pool** | Multiple API keys for the same provider, auto-rotated on rate limits |
| **Context compression** | Automatic summarization of old messages when approaching token limits |
| **Pin** | Protect a skill from curator auto-archival |

---

## Chapter 4 Summary

| Topic | What You Learned |
|-------|-----------------|
| Why skills & memory | The improvement flywheel — solve, save, reuse |
| Skill structure | YAML frontmatter + markdown body, stored as SKILL.md |
| Skills hub | 88+ skills across 17 categories, browse/install/search |
| Creating skills | Save after complex tasks, good skills have triggers + steps + pitfalls |
| Curator | Auto-maintenance lifecycle: active → stale → archived (never deleted) |
| Memory stores | User profile (who you are) + agent notes (what Hermes learned) |
| Session search | FTS5 full-text search across past conversations, instant recall |
| Profiles | Isolated configs for work/personal/client/experiment separation |
| Credential pools | Multiple API keys, auto-rotation on rate limits |
| Context compression | Auto-summarize old messages when approaching token limits |

**Next:** [Chapter 5: Automation & Scheduling →](ch05-automation-scheduling.md)

---

<!-- SCREENSHOT: hermes skills browse interactive UI -->
<!-- SCREENSHOT: Skill SKILL.md file in editor -->
<!-- SCREENSHOT: Memory injection in session startup -->
<!-- SCREENSHOT: hermes profile list output -->
<!-- SCREENSHOT: hermes auth list openrouter showing multiple keys -->
<!-- SCREENSHOT: Context compression notification in chat -->


---

# Chapter 5: Automation & Scheduling — Hermes Never Sleeps

> **The real power of an AI agent isn't in answering questions — it's in running tasks on autopilot. Cron jobs, webhooks, background processes, and job chaining turn Hermes from a chat partner into a 24/7 operations engine.**

---

## 5.1 Why Automation Matters

You've set up Hermes, connected it to Telegram, built up skills and memory. But you're still *driving* every interaction manually. Automation changes the game:

- **Consistency** — tasks run at the same time, every time, without you remembering
- **Speed** — Hermes reacts to events the moment they happen
- **Scale** — one Hermes can monitor 10 systems, write 2 blog posts a day, and review every PR
- **Freedom** — you sleep, Hermes works. You code, Hermes handles ops.

```mermaid
flowchart LR
    subgraph spectrum ["THE AUTOMATION SPECTRUM — LOW AUTONOMY → HIGH AUTONOMY"]
        M["MANUAL\n(you type)\nYou → Hermes\n\"Write this\""]
        S["SCHEDULED\n(cron jobs)\nScheduler → Hermes\n\"Every day at 9am\""]
        E["EVENT-DRIVEN\n(webhooks)\nHook → Hermes\n\"When PR is opened\""]
    end
    M --> S --> E
```

Hermes gives you four automation mechanisms, each with a different trigger:

| Mechanism | Trigger | Duration | Best For |
|-----------|---------|----------|----------|
| **Cron jobs** | Time-based schedule | Minutes to hours | Daily digests, periodic checks, content pipeline |
| **Script-only jobs** | Time-based schedule | Seconds | Watchdogs, health checks, threshold alerts |
| **Webhooks** | External HTTP event | Minutes | CI/CD, GitHub events, payment notifications |
| **Background tasks** | Manual kick-off | Minutes to hours | Long builds, test suites, data processing |

---

## 5.2 Cron Jobs — Scheduled Intelligence

Cron jobs are the backbone of Hermes automation. They run a full agent loop on a schedule — the same Hermes brain, same tools, same memory, just autonomous.

### Creating a Cron Job

```bash
# Interactive creation (recommended)
hermes cron create "0 9 * * *"

# Or use natural language
hermes cron create "every day at 9am"
hermes cron create "every 2 hours"
hermes cron create "30m"
```

During creation, Hermes walks you through the key settings:

```mermaid
flowchart TD
    subgraph anatomy ["CRON JOB ANATOMY"]
        direction TB
        S["Schedule: \"0 9 * * *\" — When it runs"]
        N["Name: \"morning-digest\" — Human label"]
        P["Prompt: \"Check emails...\" — What Hermes does"]
        SK["Skills: [email, summary] — Preloaded knowledge"]
        MO["Model: claude-sonnet-4 — Optional override"]
        D["Deliver: telegram — Where output goes"]
        W["Workdir: ~/projects/app — Project context"]
        E["Enabled: [x] — Active or paused"]
    end
    S --> N --> P --> SK --> MO --> D --> W --> E
    E -.->|"Result: Hermes wakes up at 9am,\nloads skills, checks inbox,\nwrites digest, delivers to Telegram"| R((📰 Digest))
```

### Schedule Formats

Hermes supports four schedule formats:

```bash
# 1. Duration — runs every N minutes/hours
"30m"           # Every 30 minutes
"2h"            # Every 2 hours

# 2. "Every" phrase — natural language
"every monday 9am"
"every weekday at 8:30"
"every 6 hours"

# 3. Standard cron — 5-field expression
"0 9 * * *"     # Every day at 9:00
"*/15 * * * *"  # Every 15 minutes
"0 9 * * 1-5"   # Weekdays at 9:00

# 4. One-shot — ISO timestamp
"2026-06-01T09:00:00"   # Once, at a specific time
```

### Managing Cron Jobs

```bash
# List all jobs
hermes cron list

# List including disabled/paused jobs
hermes cron list --all

# Pause a job (stop it from running)
hermes cron pause <job_id>

# Resume a paused job
hermes cron resume <job_id>

# Trigger a job manually (run on next tick)
hermes cron run <job_id>

# Edit a job's schedule, prompt, or delivery
hermes cron edit <job_id>

# Delete a job
hermes cron remove <job_id>

# Check scheduler status
hermes cron status
```

Inside a session, use `/cron` to manage jobs from chat.

### Delivery Targets

Cron job output needs to go somewhere. Hermes supports multiple delivery targets:

```bash
# Default: deliver back to the current chat
deliver: "origin"

# Deliver to all connected channels
deliver: "all"

# Deliver to a specific platform chat
deliver: "telegram"
deliver: "discord:#engineering"
deliver: "telegram:-1001234567890:17585"

# Combine targets
deliver: "origin,all"
```

### Model Overrides

Different jobs may need different models. Override per-job without changing your default:

```yaml
model:
  model: "anthropic/claude-sonnet-4"
  provider: "anthropic"
```

A daily digest might use a fast/cheap model, while a code review job needs the best reasoning. You control this per-job.

---

## 5.3 Script-Only Jobs — Lightweight Watchdogs

Not every scheduled task needs an LLM. **Script-only jobs** run a script and deliver its output verbatim — no agent loop, no tokens, no model call:

```mermaid
flowchart TD
    subgraph agent ["AGENT JOB (default)"]
        A1["Schedule tick"] --> A2["Load agent"]
        A2 --> A3["Load skills"]
        A3 --> A4["Run LLM prompt"]
        A4 --> A5["Deliver response"]
    end

    subgraph script ["SCRIPT-ONLY JOB (no_agent: true)"]
        B1["Schedule tick"] --> B2["Run script"]
        B2 --> B3["Capture stdout"]
        B3 --> B4{"stdout?"}
        B4 -->|"empty"| B5["SILENT — nothing sent"]
        B4 -->|"has text"| B6["SEND — deliver verbatim"]
        B4 -->|"exit non-zero"| B7["ERROR — alert sent"]
    end

    A5 -.- NOTE1["~5-50K tokens/job\nMinutes per run"]
    B5 -.- NOTE2["~0 tokens/job\nSeconds per run"]
```

**When to use script-only:**
- Server uptime checks (`curl -sf https://api.example.com/health`)
- Disk/memory/GPU threshold alerts
- Git repo status checks
- Any fixed-output health check where the script IS the message

```bash
# Example: a GPU memory watchdog
hermes cron create "5m" \
  --script scripts/gpu_watchdog.py \
  --no-agent \
  --deliver telegram
```

The script at `~/.hermes/scripts/gpu_watchdog.py` might look like:

```python
#!/usr/bin/env python3
import subprocess, sys
result = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                       capture_output=True, text=True)
used = int(result.stdout.strip().split("\n")[0])
if used > 90:
    print(f"⚠️ GPU memory at {used}% — over 90% threshold!")
# No output = silent (nothing sent)
```

**Key behavior:**
- Empty stdout → nothing sent (you won't even know it ran)
- Non-empty stdout → delivered verbatim as the message
- Non-zero exit → error alert sent
- Maximum efficiency — zero tokens, zero model cost

### Real-World Example: Gateway Heartbeat

The most important script-only job is one that keeps Hermes itself alive. System failures happen — Windows sleep/hibernate kills processes, OOM killers strike on Linux, unexpected crashes occur at 3 AM. Without a heartbeat, your gateway silently dies and you lose hours of coverage.

Hermes ships with a built-in heartbeat script at `~/.hermes/scripts/heartbeat.py`:

```bash
# Set up the gateway heartbeat — runs every 10 minutes, zero tokens
hermes cron create "every 10m" \
  --script scripts/heartbeat.py \
  --no-agent \
  --deliver origin
```

**How it works:**

```mermaid
flowchart TD
    A["GATEWAY HEARTBEAT\nevery 10 min"] --> B{"ALIVE?"}
    B -->|"YES"| C["Silent exit\n(nothing sent)"]
    B -->|"NO"| D["Kill zombie PIDs"]
    D --> E["Restart gateway"]
    E --> F["Notify you via Telegram"]

    style A fill:#e3f2fd
    style C fill:#e8f5e9
    style F fill:#fff3e0
```

**Key details:**
- **Zero tokens.** The heartbeat is a pure Python script (`no_agent: true`). It checks processes and log files locally — no API calls, no model involved. Your LLM bill is unaffected.
- **Silent when healthy.** If the gateway is running fine, the script prints nothing and exits with code 0. You never see a message. Only problems get reported.
- **Auto-restart.** When the gateway is down, the script kills any zombie processes and starts a fresh instance.
- **Survives sleep/hibernate.** On Windows, pair this with a Scheduled Task (every 10 min + at logon, with `StartWhenAvailable`). On Linux, use systemd timers. The watchdog catches up after wake.

**On Windows — add a Scheduled Task for extra reliability:**

```powershell
# Run as admin in PowerShell
$action = New-ScheduledTaskAction -Execute "python" `
  -Argument "$env:LOCALAPPDATA\hermes\scripts\heartbeat.py --restart"
$trigger1 = New-ScheduledTaskTrigger -Once -At (Get-Date) `
  -RepetitionInterval (New-Timespan -Minutes 10) `
  -RepetitionDuration (New-Timespan -Days 365)
$trigger2 = New-ScheduledTaskTrigger -AtLogOn
$settings = New-ScheduledTaskSettingsSet `
  -StartWhenAvailable -DontStopOnIdleEnd `
  -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName "HermesHeartbeat" `
  -Action $action -Trigger $trigger1,$trigger2 `
  -Settings $settings -Description "Restarts Hermes gateway if down"
```

This gives you **two safety nets** — the internal cron heartbeat (runs while the gateway is alive) and the OS-level Scheduled Task (runs even when the gateway is dead). Maximum downtime after any failure: ~15 minutes.

> **💡 Cost clarification:** The heartbeat costs **nothing** in LLM tokens. It's a `no_agent: true` cron job running a local Python script. No model is invoked. The only cost is ~2 seconds of CPU every 10 minutes — negligible on any machine.

---

## 5.4 Job Chaining — Output Pipelines

Jobs can chain together — the output of Job A feeds as context into Job B:

```mermaid
flowchart LR
    subgraph chain ["JOB CHAINING WITH context_from"]
        A["JOB A\nCollect data\n(script)"]
        B["JOB B\nSummarize\n(LLM agent)"]
        C["JOB C\nDeliver\n(telegram)"]
    end
    A -->|"stdout"| B
    B -->|"analysis"| C

    B -.- NOTE_B["context_from: [\"job-a-id\"]"]
    C -.- NOTE_C["context_from: [\"job-b-id\"]"]
```

**Practical example — daily competitive intelligence:**

```bash
# Job 1: Collect competitor updates (script-only, zero tokens)
hermes cron create "0 8 * * *" \
  --name "competitor-collect" \
  --script scripts/competitor_check.py \
  --no-agent

# Job 2: Analyze and summarize (agent, uses Job 1 output)
hermes cron create "0 8 * * *" \
  --name "competitor-analysis" \
  --prompt "Analyze the competitor updates below. Flag any threats or opportunities. Be concise." \
  --context-from "competitor-collect" \
  --skills "research,marketing-copy" \
  --deliver "telegram"
```

Job 1 runs at 8am, collects raw data. Job 2 runs at 8am on the same tick, but uses Job 1's *most recent completed output* as injected context. The result: a smart analysis delivered to your Telegram, powered by free data collection + paid LLM reasoning only where it adds value.

---

## 5.5 Webhooks — Event-Driven Automation

Webhooks flip the model: instead of Hermes checking on a schedule, external systems *push* events to Hermes:

```bash
# Subscribe to a webhook route
hermes webhook subscribe deploy-hook

# List active webhooks
hermes webhook list

# Test a webhook
hermes webhook test deploy-hook

# Remove a webhook
hermes webhook remove deploy-hook
```

This creates an HTTP endpoint at `/webhooks/deploy-hook`. When an external service (GitHub, Stripe, your CI) sends a POST to that endpoint, Hermes processes it.

```mermaid
flowchart TD
    GH["GitHub PR opened"] --> POST1["POST /webhooks/pr-hook"]
    SP["Stripe payment"] --> POST2["POST /webhooks/payment"]
    POST1 --> GW
    POST2 --> GW

    subgraph gateway ["GATEWAY"]
        GW["Receives HTTP POST\nParses payload\nTriggers agent"]
    end

    GW --> AL

    subgraph agentloop ["AGENT LOOP"]
        AL["Processes event\nRuns tools\nDelivers response"]
    end
```

**Common webhook patterns:**
- **CI/CD** — auto-review code when a PR opens
- **Payments** — log transactions, send confirmations
- **Monitoring** — PagerDuty alert → Hermes investigates
- **Forms** — new submission → CRM update + notification

---

## 5.6 Background Tasks — Long-Running Work

For tasks too long for a single turn but not recurring enough for cron, use **background terminal processes**:

```bash
# Start a long-running build
terminal(command="npm run build", background=True, notify_on_complete=True)

# The process runs in the background
# Hermes is free to work on other things
# You get notified when it finishes
```

```mermaid
flowchart TD
    START["START\nterminal(bg=true)"] --> RUNNING["RUNNING\nprocess(poll)"]
    RUNNING --> DONE["DONE\nAuto-notify"]
    RUNNING --> CHECK["CHECK PROGRESS\npoll → see progress\nlog → full output\nwait → block until done"]

    DONE -.- NOTE1["notify_on_complete=True →\none notification at end"]
    CHECK -.- NOTE2["watch_patterns=[\"Build OK\"] →\nnotify on rare mid-run text\n(rate limit: 1 per 15 sec)"]
```

**Process management commands:**

```bash
# List all background processes
process(action="list")

# Check status + new output
process(action="poll", session_id="...")

# Full output with pagination
process(action="log", session_id="...", offset=0, limit=200)

# Block until done (with timeout)
process(action="wait", session_id="...", timeout=300)

# Send input to a running process
process(action="submit", session_id="...", data="y")

# Kill a running process
process(action="kill", session_id="...")

# Send raw stdin without newline
process(action="write", session_id="...", data="partial input")

# Close stdin / send EOF
process(action="close", session_id="...")
```

---

## 5.7 Cron Safety & Best Practices

Running autonomous agents on a schedule comes with responsibility. Here's how to keep things safe:

```mermaid
flowchart TD
    subgraph safety ["CRON SAFETY CHECKLIST"]
        P["PROMPT: Self-contained — no chat context available\nCron jobs run in fresh sessions.\nInclude everything the agent needs to know."]
        SK["SKILLS: Attach the right skills\nA cron job has no conversation history.\nSkills inject the knowledge it needs."]
        NR["NO RECURSIVE CRON: Cron jobs must NOT\ncreate more cron jobs. Prevents runaway scheduling."]
        TO["TIMEOUT: 3-minute hard limit per run\nHermes enforces this — no infinite loops."]
        DD["DEDUP: .tick.lock prevents duplicate ticks\nTwo gateway processes won't run the same job twice."]
        MEM["MEMORY: Cron sessions skip memory by default\nThey don't pollute your memory with scheduled output."]
        SC["SCRIPT JOBS: Design for silence\nEmpty stdout = nothing sent.\nOnly output alerts, not noise."]
    end
    P --> SK --> NR --> TO --> DD --> MEM --> SC
```

### Cost Awareness

Cron jobs consume tokens. Here's a rough guide:

| Job Type | Tokens/Run | Runs/Day | Est. Daily Cost |
|----------|-----------|----------|-----------------|
| Script-only (no_agent) | 0 | 288 (every 5min) | $0.00 |
| Simple digest (short prompt) | ~2-5K | 1 | ~$0.01-0.05 |
| Research + summary | ~10-30K | 2 | ~$0.10-0.30 |
| Code review (full PR) | ~20-50K | 5 | ~$0.50-2.50 |
| Blog article generation | ~30-80K | 2 | ~$0.60-3.20 |

**Tip:** Use script-only jobs for data collection (free), reserve LLM agent jobs for tasks that actually need reasoning.

---

## 5.8 Automation in Practice — Three Real Workflows

### Workflow 1: Content Marketing Engine

```mermaid
flowchart TD
    subgraph pipeline ["DAILY BLOG PIPELINE (2 articles/day)"]
        M["8:00 AM — Job: morning-article\nSkills: [blog, marketing-copy, humanizer]\nPrompt: Write today's morning article...\nDeliver: telegram"]
        M --> MH["Hermes researches topics,\nwrites, edits, and publishes.\nYou get a notification."]
        E["6:00 PM — Job: evening-article\nSame pipeline, different time slot."]
        W["Weekly — Job: content-digest\ncontext_from: [morning, evening]\nSummarizes the week's content performance."]
    end
    M --> MH --> E --> W
    W -.- COST["Cost: ~$1.50-3.00/day\nValue: Replaces $2,000-5,000/mo content writer"]
```

### Workflow 2: Server Watchdog

```mermaid
flowchart TD
    subgraph infra ["INFRASTRUCTURE MONITORING"]
        H["Every 5 min — Script-only: health_check.py\nChecks: API uptime, DB connections,\ndisk space, memory usage\nOutput: silent unless something's wrong\nCost: $0.00 (no LLM)"]
        G["Every 15 min — Script-only: gpu_monitor.py\nChecks: GPU temp, memory, utilization\nOutput: alert only if >90%\nCost: $0.00"]
        A["On alert — Webhook: auto-remediation\nHermes receives the alert, investigates,\nattempts fix, notifies if manual action needed\nCost: ~$0.05-0.10 per incident"]
    end
    H -->|"alert"| A
    G -->|"alert"| A
```

### Workflow 3: GitHub PR Auto-Review

```mermaid
flowchart TD
    subgraph review ["CODE REVIEW AUTOMATION"]
        WH["Webhook: /webhooks/pr-review\nTrigger: GitHub PR opened or updated"]
        S1["1. GitHub sends PR event to webhook"]
        S2["2. Hermes loads github-code-review skill"]
        S3["3. Agent reads the diff, runs analysis"]
        S4["4. Posts inline review comments on the PR"]
        S5["5. Sends summary to Discord #engineering channel"]
    end
    WH --> S1 --> S2 --> S3 --> S4 --> S5
    S5 -.- CFG["Skills: [github-code-review, requesting-code-review]\nWorkdir: ~/projects/myapp\nDeliver: discord:#engineering\nCost: ~$0.10-0.50 per review\nValue: Catches bugs before production"]
```

---

## Chapter 5 Key Vocabulary

| Term | Definition |
|------|-----------|
| **Cron job** | A scheduled task that runs a full agent loop on a time-based schedule |
| **Schedule** | When a cron job runs — supports duration, natural language, cron expression, or ISO timestamp |
| **Script-only job** | A cron job with `no_agent=True` — runs a script, no LLM, zero token cost |
| **Job chaining** | Connecting jobs via `context_from` so Job B receives Job A's output as context |
| **Webhook** | An HTTP endpoint that triggers Hermes when an external event occurs |
| **Delivery target** | Where cron job output is sent — Telegram, Discord, Slack, or any connected platform |
| **Background task** | A terminal process started with `background=True` that runs while you continue working |
| **Model override** | Per-job model/provider setting independent of your default configuration |
| **Workdir** | The working directory for a cron job — loads project context files (AGENTS.md, etc.) |
| **.tick.lock** | Lock file preventing duplicate cron ticks across multiple processes |

---

## Chapter 5 Summary

| Topic | What You Learned |
|-------|-----------------|
| Why automation | From manual to autonomous — consistency, speed, scale, freedom |
| Cron jobs | Full agent loop on schedule, multiple schedule formats, delivery targets |
| Script-only jobs | Zero-token watchdogs — script output delivered verbatim, silent when empty |
| Gateway heartbeat | Built-in heartbeat.py keeps gateway alive after crashes, sleep, hibernation — zero cost |
| Job chaining | `context_from` pipeline — data collection → analysis → delivery |
| Webhooks | Event-driven triggers — external systems push events to Hermes |
| Background tasks | Long-running processes with `notify_on_complete` for non-blocking work |
| Safety | Self-contained prompts, no recursive cron, 3-min timeout, dedup locks |
| Cost awareness | Script-only = free, simple = pennies, complex = dollars — design accordingly |
| Real workflows | Content engine, server watchdog, PR auto-review — end-to-end examples |

**Next:** [Chapter 6: Multi-Agent Orchestration →](ch06-multi-agent.md)

---

<!-- SCREENSHOT: hermes cron list showing active jobs -->
<!-- SCREENSHOT: Cron job creation interactive flow -->
<!-- SCREENSHOT: Webhook POST in browser devtools -->
<!-- SCREENSHOT: Background task notification in Telegram -->
<!-- SCREENSHOT: process(action="log") output showing build progress -->


---

# Chapter 6: Multi-Agent Orchestration — An Army of One

> **One agent is powerful. Multiple agents working together are unstoppable. Delegation, parallel execution, Kanban boards, and external coding agents turn Hermes from a solo performer into an orchestral conductor.**

---

## 6.1 Why Multi-Agent?

You've seen Hermes handle single tasks well — write code, search the web, manage files. But real work is rarely single-threaded. A typical project involves:

- **Research** + **implementation** happening simultaneously
- **Frontend** + **backend** features built in parallel
- **Writing** + **review** as a quality gate
- **Monitoring** across multiple systems at once

One agent does these sequentially. Multiple agents do them in parallel — and parallelism is where the real throughput gains live.

```mermaid
flowchart LR
    subgraph seq ["Sequential (1 agent) — Total: ~120 min"]
        direction TB
        S1["Research: 20 min"] --> S2["Backend: 45 min"]
        S2 --> S3["Frontend: 40 min"]
        S3 --> S4["Review: 15 min"]
    end

    subgraph par ["Parallel (3 agents) — Total: ~60 min (2x faster)"]
        direction TB
        P1["Agent A: Research (20 min)"]
        P2["Agent B: Backend"]
        P3["Agent C: Frontend"]
        P1 --> P4["Review (waits for B + C): 15 min"]
        P2 --> P4
        P3 --> P4
    end
```

Hermes gives you **four mechanisms** for multi-agent work, each suited to different scenarios:

```mermaid
flowchart TD
    subgraph mechanisms ["MULTI-AGENT MECHANISMS"]
        D["1. DELEGATION (delegate_task)\nQuick synchronous subtasks inside your session\nBest for: research, code review, file analysis"]
        S["2. SPAWNING (tmux + hermes process)\nFully independent Hermes instances\nBest for: long autonomous missions, hours/days"]
        K["3. KANBAN BOARD (multi-agent work queue)\nDurable SQLite-backed task board with profiles\nBest for: project-scale work, specialist teams"]
        E["4. EXTERNAL AGENTS (KiloCode, Claude Code, Codex)\nDelegate to dedicated coding CLIs\nBest for: heavy coding, PRs, refactoring"]
    end
```

---

## 6.2 Delegation — `delegate_task`

The fastest way to parallelize. You spawn a **subagent** — an isolated worker with its own conversation, terminal session, and toolset. The parent waits for the result, then continues.

### Single Task Delegation

```
You: Research the top 5 React form libraries and compare them

Hermes: I'll delegate that research to a subagent.

  [delegate_task(
    goal="Research and compare top 5 React form libraries",
    toolsets=['web'],
    role='leaf'
  )]

  Subagent uses: web_search, web_extract
  Subagent returns: summary of 5 libraries with pros/cons

Hermes: Here's the comparison:
  1. React Hook Form — best performance, smallest bundle
  2. Formik — mature, large community
  3. Zod + React — best TypeScript integration
  ...etc
```

### Batch Delegation — Up to 3 in Parallel

Need multiple things at once? Batch them:

```
You: I need three things done: check the API health, review the
     latest PR, and find me a good icon library.

Hermes: Dispatching 3 subagents in parallel...

  [delegate_task(tasks=[
    {
      goal: "Check API health endpoints and report status",
      toolsets: ['terminal', 'web'],
    },
    {
      goal: "Review PR #42 for security and code quality",
      toolsets: ['terminal', 'file'],
    },
    {
      goal: "Find the best React icon library for a dashboard",
      toolsets: ['web'],
    }
  ])]

  All 3 run simultaneously. Results arrive together.
```

### Delegation Anatomy

```mermaid
flowchart TD
    subgraph params ["DELEGATION PARAMETERS"]
        G["goal — What the subagent should accomplish"]
        CTX["context — Background info the subagent needs"]
        TS["toolsets — Which tools to give it\n(default: inherits parent's tools)"]
        R["role — 'leaf' (default) or 'orchestrator'"]
    end
    G --> CTX --> TS --> R
    R -.- RTN["RETURNS: Final summary only.\nIntermediate tool output NEVER enters parent context."]
    R -.- LIFE["LIFETIME: Bound to parent's turn.\nIf parent is interrupted → child is cancelled.\nFor durable work, use cronjob or background terminal."]
```

### Leaf vs Orchestrator Roles

- **Leaf** (default) — focused worker. Cannot re-delegate. Best for 95% of tasks.
- **Orchestrator** — can spawn its own subagents. For multi-step workflows where a subagent needs to coordinate further workers.

```yaml
# Enable deeper nesting in config.yaml
delegation:
  max_spawn_depth: 2        # allow orchestrator subagents
  max_concurrent_children: 3  # max parallel children
  max_iterations: 50         # max agent loop turns per child
```

### Choosing What to Delegate

```mermaid
flowchart TD
    subgraph when ["WHEN TO DELEGATE"]
        subgraph do ["DO delegate"]
            D1["Research tasks (web search + synthesis)"]
            D2["Code review (read files + assess quality)"]
            D3["File analysis (search + summarize)"]
            D4["Parallel independent subtasks"]
            D5["Tasks that would flood your context with data"]
        end
        subgraph dont ["DON'T delegate"]
            N1["Single tool calls (just call the tool directly)"]
            N2["Tasks needing user interaction (subagents can't ask you)"]
            N3["Long-running work (use cronjob or background instead)"]
            N4["Simple questions (answer directly, no overhead)"]
        end
    end
```

---

## 6.3 Spawning Independent Agents

Delegation is bounded by the parent session. For **long autonomous missions** — tasks that run for hours or days — spawn a fully independent Hermes process.

### One-Shot Mode

Fire-and-forget a single task:

```bash
# Foreground (waits for completion)
hermes chat -q "Refactor the auth module to use dependency injection"

# Background (non-blocking, from inside a session)
terminal(command="hermes chat -q 'Set up CI/CD for ~/myapp'", timeout=300)
```

No PTY needed. The agent runs, finishes, and exits.

### Interactive Mode via tmux

For tasks where you want to interact with the spawned agent or monitor progress:

```bash
# 1. Start a new Hermes in tmux
tmux new-session -d -s backend -x 120 -y 40 'hermes'

# 2. Wait for startup, then send a task
sleep 8 && tmux send-keys -t backend 'Build REST API for user management' Enter

# 3. Check progress anytime
tmux capture-pane -t backend -p | tail -30

# 4. Send follow-up instructions
tmux send-keys -t backend 'Add rate limiting middleware' Enter

# 5. Done? Kill the session
tmux send-keys -t backend '/exit' Enter && sleep 2 && tmux kill-session -t backend
```

### Multi-Agent Coordination

The real power: spawn multiple agents, each on a different workstream, and relay context between them:

```mermaid
flowchart TD
    BE["BACKEND agent\n(tmux:be)"] <-->|"API schema relay"| FE["FRONTEND agent\n(tmux:fe)"]
    BE --> YOU
    FE --> YOU
    YOU["YOU (Hermes main)\nMonitor both, relay info"]

    BE -.- STEP["1. Spawn backend agent: Build REST API\n2. Spawn frontend agent: Build React dashboard\n3. Capture backend API schema\n4. Send schema to frontend agent\n5. Both work in parallel"]
```

```bash
# Agent A: Backend API
tmux new-session -d -s backend -x 120 -y 40 'hermes -w'
sleep 8 && tmux send-keys -t backend 'Build REST API for user management at ~/myapp' Enter

# Agent B: Frontend dashboard (simultaneously)
tmux new-session -d -s frontend -x 120 -y 40 'hermes -w'
sleep 8 && tmux send-keys -t frontend 'Build React dashboard for user management at ~/myapp/frontend' Enter

# Later: relay API schema from backend to frontend
BACKEND_OUTPUT=$(tmux capture-pane -t backend -p | tail -50)
tmux send-keys -t frontend "Here is the API schema from the backend agent:\n$BACKEND_OUTPUT\nBuild the frontend to consume these endpoints." Enter
```

**The `-w` flag** is crucial when spawning agents that edit code — it creates an isolated git worktree so agents don't conflict with each other's changes.

### Delegation vs Spawning — Quick Reference

```mermaid
flowchart TD
    subgraph comparison ["DELEGATE_TASK vs SPAWN HERMES"]
        subgraph dt ["delegate_task"]
            D1["Isolation: Separate convo, shared process"]
            D2["Duration: Minutes"]
            D3["Tool access: Subset of parent"]
            D4["Interactive: No"]
            D5["Survives restart: No"]
            D6["Overhead: Low"]
            D7["Best for: Quick subtasks"]
        end
        subgraph sh ["Spawn hermes"]
            H1["Isolation: Fully independent process"]
            H2["Duration: Hours/days"]
            H3["Tool access: Full access"]
            H4["Interactive: Yes (via tmux)"]
            H5["Survives restart: Yes (tmux)"]
            H6["Overhead: Medium"]
            H7["Best for: Long missions"]
        end
    end
```

---

## 6.4 Kanban Board — Multi-Agent Work Queue

For **project-scale work** that needs coordination, persistence, and specialist roles, use the Kanban board. It's a durable SQLite-backed task board where multiple Hermes profiles collaborate.

### What Makes Kanban Different

Unlike delegation (ephemeral) or spawning (manual coordination), Kanban provides:

- **Persistence** — tasks survive crashes, restarts, and reboots
- **Specialization** — different profiles handle different task types
- **Dependency tracking** — Task C waits for Task A and B to finish
- **Automatic dispatch** — the dispatcher assigns and spawns workers
- **Audit trail** — every action logged in the board's history

```mermaid
stateDiagram-v2
    [*] --> TODO
    TODO --> READY : All parents done
    READY --> CLAIMED : Dispatcher picks up
    CLAIMED --> DONE : Worker finishes
    CLAIMED --> BLOCKED : Waiting for human input
    BLOCKED --> READY : Human provides input

    NOTE_RIGHT of TODO: Parents not done → stays here
    NOTE_RIGHT of READY: Dispatcher spawns worker
    NOTE_RIGHT of DONE: Children auto-promoted
```

### Setting Up the Board

```bash
# Initialize a Kanban board
hermes kanban init

# Create tasks with profile assignment
hermes kanban create "Build authentication service" --assignee backend-dev
hermes kanban create "Design login UI" --assignee frontend-dev
hermes kanban create "Write auth documentation" --assignee writer

# View the board
hermes kanban list

# Show task details
hermes kanban show <task_id>

# Link dependencies (task 3 waits for tasks 1 and 2)
hermes kanban link <task1_id> <task3_id>
hermes kanban link <task2_id> <task3_id>
```

### The Dispatcher — Automatic Worker Spawning

The dispatcher runs inside the gateway and automatically:

1. **Claims** ready tasks for the assigned profile
2. **Spawns** a worker Hermes instance for that profile
3. **Monitors** the worker's progress
4. **Promotes** dependent tasks when parents complete
5. **Reclaims** stale claims if a worker crashes

```bash
# Start the dispatcher (runs in gateway by default)
hermes kanban dispatch

# Watch live progress
hermes kanban tail

# View run history
hermes kanban runs
```

### Profiles as Specialists

Each profile is a specialist. You configure them with different models, tools, and skills:

```bash
# Create specialist profiles
hermes profile create backend-dev --clone
hermes profile create frontend-dev --clone
hermes profile create reviewer --clone

# Configure each one
hermes -p backend-dev config set model.default deepseek/deepseek-chat
hermes -p frontend-dev config set model.default anthropic/claude-sonnet-4
hermes -p reviewer config set model.default anthropic/claude-sonnet-4

# Assign skills per profile
hermes -p backend-dev skills install test-driven-development
hermes -p reviewer skills install requesting-code-review
```

### Task Dependencies — The Real Power

Dependencies are what make Kanban shine for complex projects:

```mermaid
flowchart TD
    T1["T1: Design database schema\n(backend-dev)"]
    T2["T2: Design API contract\n(backend-dev)"]
    T3["T3: Build REST API\n(backend-dev)"]
    T4["T4: Build React UI\n(frontend-dev)"]
    T5["T5: Integration testing\n(reviewer)"]
    T6["T6: Deploy\n(backend-dev)"]

    T1 --> T3
    T2 --> T3
    T3 --> T5
    T4 --> T5
    T5 --> T6

    T1 -.- NOTE1["T1 + T2 run in parallel (no dependencies)"]
    T3 -.- NOTE2["T3 starts when both T1 and T2 complete"]
    T4 -.- NOTE3["T4 runs in parallel with T3"]
    T5 -.- NOTE4["T5 starts when both T3 and T4 complete"]
    T6 -.- NOTE5["T6 starts when T5 completes"]
```

### Managing Tasks

```bash
# Block a task (waiting for human input)
hermes kanban block <task_id> --reason "Need client approval on design"

# Unblock and resume
hermes kanban unblock <task_id>

# Add comments
hermes kanban comment <task_id> "Use JWT instead of session cookies"

# Link related tasks
hermes kanban link <parent_id> <child_id>

# Complete a task manually
hermes kanban complete <task_id> --summary "Auth service built with JWT"

# Archive completed tasks to clean the board
hermes kanban archive <task_id>

# View statistics
hermes kanban stats
```

### When to Use Kanban

```mermaid
flowchart TD
    subgraph when_kanban ["USE KANBAN WHEN..."]
        subgraph use ["Use Kanban"]
            K1["Multiple specialists are needed"]
            K2["Work should survive crashes/restarts"]
            K3["Human-in-the-loop at any step"]
            K4["Multiple subtasks can run in parallel"]
            K5["Review/iteration cycles are expected"]
            K6["Audit trail matters"]
        end
        subgraph use_delegate ["USE delegate_task FOR..."]
            D1["Quick one-off subtasks"]
            D2["Simple parallel research"]
            D3["Tasks that complete in minutes"]
        end
    end
```

---

## 6.5 External Coding Agents

Beyond its own subagents, Hermes can delegate to **dedicated coding CLIs** — specialized agents designed for heavy coding work.

### Available External Agents

| Agent | Install | Best For |
|-------|---------|----------|
| **KiloCode** | `npm i -g @anthropic/kilocode` | Multi-specialist coding, GitNexus integration |
| **Claude Code** | `npm i -g @anthropic/claude-code` | Anthropic-native coding, deep reasoning |
| **OpenAI Codex** | `npm i -g @openai/codex` | OpenAI-native coding, sandboxed execution |
| **OpenCode** | Build from source | Lightweight, extensible |

### Delegating to External Agents

```bash
# KiloCode — full feature with GitNexus context injection
kilo run --auto --format json "Implement user authentication with JWT"

# Claude Code — deep reasoning coding
claude --acp --stdio "Refactor the database layer to use repositories"

# Codex — sandboxed execution
codex "Write unit tests for the payment module"
```

Hermes wraps these via the terminal tool:

```
You: Implement the payment service with Stripe integration

Hermes: I'll delegate this to KiloCode for heavy coding.

  [terminal(command="kilo run --auto --format json 'Implement payment
   service with Stripe integration at ~/myapp/src/services/payment.ts'",
   timeout=300)]

  KiloCode completes: creates file, writes tests, commits.

Hermes: ✅ Payment service implemented by KiloCode:
  - Stripe integration with webhook handling
  - Unit tests passing (12/12)
  - Committed as feat: add payment service
```

### Why Use External Agents?

- **Specialization** — they're built specifically for coding, with deep IDE integration
- **Cost efficiency** — use cheaper models for bulk coding, premium models for review
- **Safety** — sandboxes and approval flows prevent unauthorized changes
- **Context windows** — dedicated agents can focus their entire context on the code

---

## 6.6 Coordination Patterns — Real Workflows

Let's see how these mechanisms combine in practice.

### Pattern 1: Research + Write (Delegation)

```
You: Write a blog post about Rust's ownership model

Hermes:

  1. [delegate_task: Research subagent]
     goal: "Research Rust ownership model — key concepts, common
            misconceptions, real-world examples"
     toolsets: ['web']
     → Returns: research summary with sources

  2. [Hermes writes using research]
     Uses research as context, applies blog skill,
     produces final article

  Total: ~3 minutes vs ~8 minutes sequential
```

### Pattern 2: Backend + Frontend (Spawning)

```
You: Build a user management feature — API and dashboard

Hermes:

  1. [Spawn backend agent via tmux]
     "Build REST API: /users CRUD + /auth/login + /auth/register"

  2. [Spawn frontend agent via tmux — simultaneously]
     "Build React dashboard: user list, create/edit forms, login page"

  3. [Monitor both, relay API schema when backend finishes]

  4. [Review integration when both complete]

  Total: ~50 minutes vs ~95 minutes sequential
```

### Pattern 3: Full Project Pipeline (Kanban)

```
You: Build an e-commerce checkout system

Hermes:

  T1: Design checkout database schema      [backend-dev]
  T2: Design checkout API contract          [backend-dev]    } parallel
  T3: Design checkout UI mockups            [frontend-dev]   }

  T4: Implement checkout API                [backend-dev]    ← depends on T1, T2
  T5: Implement checkout UI                 [frontend-dev]   ← depends on T3

  T6: Integration testing                   [reviewer]       ← depends on T4, T5

  T7: Security review                       [reviewer]       ← depends on T6

  T8: Deploy to staging                     [backend-dev]    ← depends on T7

  Dispatcher handles all spawning, monitoring, and promotion automatically.
```

### Pattern 4: Daily Operations (Cron + Delegation)

```mermaid
flowchart TD
    subgraph daily ["DAILY AUTOMATED PIPELINE"]
        C1["6:00 AM — Cron: Check server health\nScript-only job, $0, alert if down"]
        C2["9:00 AM — Cron: Daily competitive digest\nAgent job: web search + summarize\ndelegate_task for parallel research"]
        C3["12:00 PM — Cron: Review open PRs\nAgent job: gh pr list + code review\nUses github-code-review skill"]
        C4["6:00 PM — Cron: End-of-day report\nCollects results from all previous jobs\nUses context_from to chain outputs"]
    end
    C1 --> C2 --> C3 --> C4
    C4 -.- NOTE["All automated. You review the 6 PM digest."]
```

---

## 6.7 Multi-Agent Best Practices

### 1. Right-Size Your Tooling

Don't use a Kanban board for a 10-minute task. Don't manually coordinate what the dispatcher can automate.

```
Quick subtask (minutes)     → delegate_task
Parallel research (minutes) → delegate_task (batch)
Long coding (hours)         → spawn hermes (tmux)
Project with specialists    → Kanban board
```

### 2. Isolate File Edits

When multiple agents touch the same codebase, use **git worktrees** (`-w` flag):

```bash
hermes -w    # creates an isolated worktree for this agent
```

Without worktrees, two agents editing the same files will create merge conflicts.

### 3. Keep Subagent Context Focused

Subagents get a **fresh conversation** — no memory of your session. Provide everything they need in the `context` parameter:

```
❌ "Fix the bug we discussed earlier"
✅ "Fix the TypeError in src/api/auth.py line 42 — the login
    function expects a dict but receives a string. The function
    signature is def login(credentials: dict)."
```

### 4. Verify External Results

Subagents are **self-reporting**. They might claim "uploaded successfully" when they didn't. For operations with side effects:

```bash
# After a subagent claims it created a file:
read_file("path/to/file")  # verify it exists and has content

# After a subagent claims it deployed:
terminal(command="curl -s https://myapp.com/health")  # verify it's live
```

### 5. Don't Delegate Trivial Work

```
❌ delegate_task(goal="Read package.json")
   → Just use read_file("package.json") directly

✅ delegate_task(goal="Analyze all dependencies in package.json,
    check for security vulnerabilities, find outdated packages,
    and suggest updates")
   → Complex analysis worth the overhead
```

### 6. Handle Stuck Kanban Workers

When a worker crashes or hallucinates:

```bash
# Reclaim — abort and reset to ready
hermes kanban reclaim <task_id>

# Reassign — switch to a different profile
hermes kanban reassign <task_id> backend-dev --reclaim

# View the audit trail
hermes kanban log <task_id>
```

---

## 6.8 Key Vocabulary

| Term | Definition |
|------|-----------|
| **Delegation** | Spawning a synchronous subagent via `delegate_task` |
| **Subagent** | An isolated worker with its own conversation and tools |
| **Leaf** | A subagent that cannot re-delegate (default role) |
| **Orchestrator** | A subagent that can spawn its own subagents |
| **Batch delegation** | Running up to 3 subagent tasks in parallel |
| **Spawning** | Launching a fully independent Hermes process via tmux |
| **Worktree** | Isolated git working directory (`-w` flag) for parallel agents |
| **Kanban board** | Durable SQLite-backed task queue for multi-profile coordination |
| **Dispatcher** | Background service that auto-claims and spawns workers for ready tasks |
| **Profile** | An isolated Hermes configuration used as a specialist role |
| **Dependency** | Parent-child link — child waits for parent(s) to complete |
| **External agent** | Third-party coding CLI (KiloCode, Claude Code, Codex) |

---

## Chapter 6 Summary

| Topic | What You Learned |
|-------|-----------------|
| Why multi-agent | Parallelism = 2-5x throughput for multi-workstream tasks |
| Delegation | Quick synchronous subagents, batch up to 3 in parallel, leaf vs orchestrator |
| Spawning | Independent Hermes processes via tmux for long autonomous missions |
| Kanban board | Durable task queue with dependencies, specialist profiles, auto-dispatch |
| External agents | KiloCode, Claude Code, Codex for heavy coding with specialized CLIs |
| Coordination patterns | Research+write, backend+frontend, project pipeline, daily operations |
| Best practices | Right-size tooling, isolate edits, focused context, verify results |

**Next:** [Chapter 7: Advanced Configuration & Power User Tips →](ch07-advanced-config.md)

---

<!-- SCREENSHOT: delegate_task parallel execution output -->
<!-- SCREENSHOT: tmux multi-agent session layout -->
<!-- SCREENSHOT: hermes kanban list showing task board -->
<!-- SCREENSHOT: Kanban dependency graph visualization -->
<!-- SCREENSHOT: External agent delegation output -->


---

# Chapter 7: Advanced Configuration — Taming the Machine

> **Default Hermes works out of the box. Advanced Hermes runs securely across clients, extends with external tools, isolates environments, and never hits a rate limit. This chapter turns you from a user into an operator.**

---

## 7.1 Security & Privacy

Hermes has access to your terminal, your files, your API keys, and your messaging platforms. That power demands guardrails. Let's walk through every security control — and when to use each.

### Secret Redaction

By default, Hermes passes tool output through unmodified — terminal stdout, file contents, web responses, everything reaches the conversation verbatim. If you want Hermes to auto-mask strings that look like API keys, tokens, and secrets before they enter the context window and logs:

```bash
hermes config set security.redact_secrets true
```

After enabling, strings matching patterns like `sk-...`, `ghp_...`, `xoxb-...`, and generic `API_KEY=`, `password=`, `secret=` values get replaced with `[REDACTED]` in tool output.

**Important:** This takes effect on the next session start — not mid-conversation. That's deliberate. It prevents the LLM from flipping its own security toggle during a task.

```bash
# Verify it's on
hermes config get security.redact_secrets

# Turn it off
hermes config set security.redact_secrets false
```

### PII Redaction in Gateway Messages

Separate from secret redaction. When enabled, the gateway hashes user IDs and strips phone numbers from session context before it reaches the model:

```bash
hermes config set privacy.redact_pii true    # enable
hermes config set privacy.redact_pii false   # disable (default)
```

💡 **Tip:** If you run Hermes on a shared Telegram group or Discord server, enable PII redaction. For personal DMs, it's usually unnecessary.

### Command Approval Modes

Hermes asks for permission before running destructive shell commands (`rm -rf`, `git reset --hard`, etc.) by default. Three modes:

| Mode | Behavior | Best for |
|------|----------|----------|
| `manual` | Always prompt on flagged commands (default) | Most users — safe default |
| `smart` | Auxiliary LLM auto-approves low-risk, prompts on high-risk | Power users who want speed without full YOLO |
| `off` | Skip all approval prompts | Trusted environments, automated workflows |

```bash
# Recommended for power users
hermes config set approvals.mode smart

# Full bypass (not recommended for production)
hermes config set approvals.mode off
```

Per-session override without changing config:

```bash
# One-shot YOLO
hermes --yolo chat -q "Clean up temp files"

# Or in session
/yolo
```

**Key insight:** YOLO mode (`off`) and secret redaction are independent. Turning off approvals does NOT disable secret redaction. You can be fast AND secure.

### Security Quick Reference

```mermaid
flowchart TD
    subgraph security["🔒 SECURITY LAYERS"]
        direction TB
        subgraph L1["Layer 1: Secret Redaction"]
            L1A["Masks API keys, tokens in tool output"]
            L1B["Config: security.redact_secrets"]
            L1C["Restart required"]
        end
        subgraph L2["Layer 2: PII Redaction"]
            L2A["Hashes user IDs, strips phone numbers"]
            L2B["Config: privacy.redact_pii"]
            L2C["Gateway-only (messaging platforms)"]
        end
        subgraph L3["Layer 3: Command Approval"]
            L3A["Prompts before destructive commands"]
            L3B["Config: approvals.mode (manual/smart/off)"]
            L3C["Per-session: /yolo or --yolo flag"]
        end
        subgraph L4["Layer 4: Environment Filtering"]
            L4A["MCP subprocesses get only safe env vars"]
            L4B["API keys only passed when explicitly configured"]
        end
        L1 --> L2 --> L3 --> L4
    end
```

---

## 7.2 MCP Servers — Extending Hermes with External Tools

Hermes has 20+ built-in toolsets. But what if you need something it doesn't have — a database query tool, a custom API integration, or a specialized analysis engine?

**MCP (Model Context Protocol)** is the answer. MCP servers expose external tools that Hermes discovers automatically and uses like native ones.

### How It Works

```mermaid
flowchart LR
    subgraph hermes["HERMES AGENT"]
        H["Hermes Agent"]
    end
    H -- "stdio" --> A["MCP Server A\n(GitHub)"]
    H -- "HTTP" --> B["MCP Server B\n(Company API)"]
    H -- "stdio" --> C["MCP Server C\n(GitNexus)"]
    
    subgraph note["Tool Naming"]
        N["Tools appear as:\nmcp_github_*, mcp_company_*, etc.\nAuto-injected into all platform toolsets"]
    end
```

1. You declare MCP servers in `config.yaml`
2. On startup, Hermes connects to each server and discovers its tools
3. Tools appear with `mcp_{server}_{tool}` naming — available everywhere
4. Connections persist for the agent's lifetime with auto-reconnection

### Adding an MCP Server

**Prerequisite:** Install the MCP Python package:

```bash
pip install mcp
```

#### Stdio Transport (Local Subprocess)

Most common pattern — Hermes launches the server as a subprocess:

```yaml
# In ~/.hermes/config.yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    timeout: 30

  gitnexus:
    command: "uvx"
    args: ["gitnexus-mcp"]
    timeout: 120
```

#### HTTP Transport (Remote Server)

For shared or remote MCP servers:

```yaml
mcp_servers:
  company_api:
    url: "https://mcp.mycompany.com/v1/mcp"
    headers:
      Authorization: "Bearer sk-your-token-here"
    timeout: 180
    connect_timeout: 30
```

#### CLI Commands

```bash
# Add interactively
hermes mcp add gitnexus --url http://localhost:3000

# List configured servers
hermes mcp list

# Test a connection
hermes mcp test gitnexus

# Remove a server
hermes mcp remove gitnexus

# Toggle specific tools from a server
hermes mcp configure gitnexus
```

### Security: Environment Filtering

MCP subprocesses do NOT get your full shell environment. Only safe baseline variables (`PATH`, `HOME`, `USER`, `LANG`, etc.) are inherited. API keys and secrets are excluded unless you explicitly pass them:

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      # Only this token reaches the subprocess
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxxx"
```

💡 **Tip:** If an MCP tool fails with a credential error, check that you've passed the required env vars in the server config — they won't come from your shell automatically.

### Multiple Servers

Stack them in config — all tools from all servers are available simultaneously:

```yaml
mcp_servers:
  time:
    command: "uvx"
    args: ["mcp-server-time"]

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]

  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxxx"

  company_api:
    url: "https://mcp.internal.company.com/mcp"
    headers:
      Authorization: "Bearer sk-xxxx"
```

**Restart required** after adding or removing servers — no hot-reload yet. In gateway: `/restart`. In CLI: exit and relaunch.

---

## 7.3 Custom Providers & Base URLs

Hermes ships with 20+ built-in providers. But sometimes you need:

- A **self-hosted model** (vLLM, Ollama, LocalAI)
- A **corporate proxy** that speaks OpenAI-compatible API
- A **custom endpoint** with different auth

### Setting a Custom Base URL

```bash
# Point to a self-hosted endpoint
hermes config set model.base_url "http://localhost:11434/v1"

# Use with any model name
hermes config set model.default "local/llama3"

# Set the API key (if your endpoint requires one)
hermes config set model.api_key "your-key-here"
```

### Common Self-Hosted Setups

| Server | Base URL | Notes |
|--------|----------|-------|
| Ollama | `http://localhost:11434/v1` | Free, runs locally, no API key needed |
| vLLM | `http://localhost:8000/v1` | Production-grade, OpenAI-compatible |
| LocalAI | `http://localhost:8080/v1` | Drop-in OpenAI replacement |
| LM Studio | `http://localhost:1234/v1` | GUI app, OpenAI-compatible |
| Corporate proxy | `https://api.company.com/v1` | May require API key or Bearer token |

**Example: Ollama setup**

```bash
# Install and run Ollama (separate step)
ollama serve
ollama pull llama3

# Point Hermes to it
hermes config set model.base_url "http://localhost:11434/v1"
hermes config set model.default "local/llama3"

# Verify
hermes chat -q "Hello, are you running locally?"
```

**Example: Corporate proxy with API key**

```bash
hermes config set model.base_url "https://ai-proxy.company.com/v1"
hermes config set model.api_key "corp-key-xxxxx"
hermes config set model.default "gpt-4o"
```

### Switching Back

```bash
# Remove custom URL to use provider defaults
hermes config set model.base_url ""

# Or switch to a built-in provider
hermes model    # Interactive picker
```

💡 **Tip:** Custom base URLs apply globally. If you need different models for different tasks, use **profiles** (Section 7.4) or per-job model overrides in cron tasks.

---

## 7.4 Profiles — Isolated Hermes Instances

Profiles give you completely separate Hermes environments — each with its own config, sessions, skills, memory, and API keys. Think of them as separate users on the same machine.

### Why Profiles?

```mermaid
flowchart LR
    subgraph without["WITHOUT PROFILES"]
        direction TB
        W1["~/.hermes/"]
        W2["config.yaml ← One config for everything"]
        W3[".env ← All keys mixed together"]
        W4["sessions/ ← Work + personal sessions merged"]
        W5["skills/ ← All skills in one pool"]
        W6["state.db ← One session database"]
        W1 --> W2 & W3 & W4 & W5 & W6
    end

    subgraph with["WITH PROFILES"]
        direction TB
        P1["~/.hermes/"]
        P2["config.yaml ← Default profile"]
        P3["profiles/"]
        P1 --> P2 & P3
        subgraph work["work/"]
            W7["config.yaml ← Work config, models, keys"]
            W8[".env"]
            W9["sessions/ ← Work sessions only"]
            W10["skills/ ← Work-specific skills"]
            W11["state.db ← Work session database"]
        end
        subgraph acme["client-acme/"]
            A1["config.yaml ← Client-specific config"]
            A2[".env"]
            A3["..."]
        end
        P3 --> work & acme
    end
```

**Use cases:**

- **Work / personal separation** — different models, different API keys, different skills
- **Client isolation** — each client gets their own profile, sessions never leak
- **Experimentation** — a "lab" profile for testing new models without risking your main setup
- **Kanban workers** — specialist profiles for different task types (Chapter 6)

### Creating & Managing Profiles

```bash
# List existing profiles
hermes profile list

# Create a new profile (starts blank)
hermes profile create work

# Clone your current config into the new profile
hermes profile create work --clone

# Clone everything (config + sessions + skills + memory)
hermes profile create work --clone-all

# Set a sticky default
hermes profile use work

# Launch with a specific profile (overrides default)
hermes -p work chat -q "Check staging server logs"

# Show profile details
hermes profile show work

# Rename a profile
hermes profile rename work company

# Export/import (for backup or migration)
hermes profile export work    # Creates work.tar.gz
hermes profile import work.tar.gz

# Delete a profile
hermes profile delete old-client
```

### Per-Invocation Profile

You don't need to change your default. Use `-p` for one-off switches:

```bash
# Quick personal task from work machine
hermes -p personal chat -q "What's on my shopping list?"

# Run a cron job under a specific profile
# (via cronjob tool's profile parameter)
```

### Profile-Aware Paths

Inside a profile, all the standard paths resolve correctly:

| What | Default Profile | Named Profile |
|------|----------------|---------------|
| Config | `~/.hermes/config.yaml` | `~/.hermes/profiles/work/config.yaml` |
| Sessions | `~/.hermes/sessions/` | `~/.hermes/profiles/work/sessions/` |
| Skills | `~/.hermes/skills/` | `~/.hermes/profiles/work/skills/` |
| State DB | `~/.hermes/state.db` | `~/.hermes/profiles/work/state.db` |
| Env | `~/.hermes/.env` | `~/.hermes/profiles/work/.env` |
| Auth | `~/.hermes/auth.json` | `~/.hermes/profiles/work/auth.json` |

Hermes handles this automatically — you never need to construct these paths manually.

---

## 7.5 Credential Pools — Rate Limit Busting

API providers enforce rate limits per key. When you're running multiple agents, cron jobs, and background tasks simultaneously, a single key can throttle fast.

**Credential pools** solve this. Register multiple API keys for the same provider, and Hermes rotates across them automatically.

### Setting Up Credential Pools

```bash
# Interactive wizard — add a new credential
hermes auth add

# List all credentials for a provider
hermes auth list openrouter

# Remove a specific credential by index
hermes auth remove openrouter 2

# Reset exhaustion status (if keys got flagged)
hermes auth reset openrouter
```

### How Rotation Works

```mermaid
flowchart TD
    A["Request arrives for OpenRouter"] --> B{"Key pool lookup"}
    
    B --> K1["Key 1\nLast used: 2 min ago\n✅ USE THIS"]
    B --> K2["Key 2\nLast used: 30s ago\n⏳ Backoff"]
    B --> K3["Key 3\nLast used: 5 min ago\n✅ Available"]
    
    K1 --> C["Pick least-recently-used non-exhausted key"]
    K3 --> C
    C --> D["Mark used, attach to request"]
    
    D --> E{"Response?"}
    E -- "200 OK" --> F["Request succeeds"]
    E -- "429 Rate Limited" --> G["Mark key as exhausted\n(cooldown period)"]
    G --> H{"Retry with next available key"}
    H -- "Keys available" --> C
    H -- "All keys exhausted" --> I["Wait for shortest cooldown\nthen retry"]
    I --> C
```

**Key insight:** You don't need to manage rotation manually. Just register multiple keys and Hermes handles the rest — picking the least-recently-used key, respecting cooldowns, and spreading load evenly.

### When to Use Credential Pools

| Scenario | Single Key | Credential Pool |
|----------|-----------|-----------------|
| Personal use, light automation | ✅ | — |
| Multiple cron jobs running concurrently | — | ✅ |
| Kanban workers (3+ parallel agents) | — | ✅ |
| Heavy delegation (batch `delegate_task`) | — | ✅ |
| Production gateway with daily users | — | ✅ |

💡 **Tip:** Even 2-3 keys per provider dramatically reduces throttling. Many providers offer free tiers — stack them for burst capacity without cost.

---

## 7.6 Context Window Optimization

LLMs have finite context windows. Hermes has several mechanisms to stay within limits while keeping the most relevant information available.

### Automatic Compression

When the conversation approaches the token limit, Hermes automatically compresses older messages into a compact summary:

```yaml
# config.yaml — compression settings
compression:
  enabled: true            # default: true
  threshold: 0.50          # trigger when 50% of context is used
  target_ratio: 0.20       # compress down to 20% of context
```

```bash
# Adjust thresholds
hermes config set compression.threshold 0.40   # compress sooner
hermes config set compression.target_ratio 0.15 # compress smaller

# Manual compression mid-session
/compress
```

### Toolset Pruning

Every enabled toolset adds schema definitions to the system prompt. If you're only using 3 tools but have 20 toolsets enabled, you're wasting tokens on unused schemas.

```bash
# Interactive tool manager
hermes tools

# Enable only what you need
hermes tools enable terminal
hermes tools enable file
hermes tools enable web

# Disable everything else
hermes tools disable browser
hermes tools disable spotify
# ...
```

💡 **Tip:** A minimal toolset (`terminal` + `file` + `web`) uses ~40% fewer tokens in the system prompt than the full bundle. For long sessions or complex tasks, this matters.

### Cron Jobs: Enabled Toolsets

Cron jobs can restrict which toolsets the agent has access to — reducing both token overhead and attack surface:

```yaml
# In the cronjob tool:
enabled_toolsets: ["web", "terminal", "file"]
```

This is especially valuable for scheduled tasks that only need a few capabilities.

---

## 7.7 Debugging Hermes

When something goes wrong, Hermes has built-in diagnostic tools.

### `hermes doctor` — Health Check

```bash
# Full system check
hermes doctor

# Auto-fix common issues
hermes doctor --fix
```

Checks:
- Python version and dependencies
- Config file validity
- API key presence
- Gateway service status
- MCP server connectivity
- Session store integrity

### `/debug` — Upload Debug Report

In any session:

```
/debug
```

Uploads a debug report (system info + recent logs) and returns a shareable link. Useful for getting help from the community or filing bug reports.

### Log Inspection

```bash
# Gateway logs
cat ~/.hermes/logs/gateway.log

# Recent errors
grep -i "error\|failed\|traceback" ~/.hermes/logs/gateway.log | tail -30

# Follow logs in real-time
tail -f ~/.hermes/logs/gateway.log
```

### `hermes status` — Component Status

```bash
# Quick status
hermes status

# Detailed status (all components)
hermes status --all
```

Shows gateway state, cron scheduler, MCP connections, memory provider, and active sessions.

### Common Issues Quick-Fix

| Symptom | Fix |
|---------|-----|
| "No models provided" (HTTP 400) | Config has UTF-8 BOM — re-save without BOM (`hermes config edit`) |
| Tool not available | `hermes tools list` → check enablement → `/reset` |
| Changes not taking effect | Restart session: `/reset` (CLI) or `/restart` (gateway) |
| Model/provider errors | `hermes doctor` → check API key → `hermes model` to reconfigure |
| Voice not working | Check `stt.enabled: true` + provider setup → `/restart` |
| MCP server won't connect | `hermes mcp test <name>` → check `command` is on PATH → check YAML indent |
| Copilot 403 | `gh auth` tokens don't work for Copilot API — use `hermes model` → GitHub Copilot OAuth |

---

## 7.8 Windows-Specific Tips

Hermes runs natively on Windows — PowerShell, cmd, Windows Terminal, git-bash mintty, VS Code terminal all work. But Windows has quirks.

### Input: Ctrl+Enter for Newlines

**Alt+Enter doesn't insert a newline on Windows.** Windows Terminal intercepts it for fullscreen toggle. Use **Ctrl+Enter** instead.

```bash
# Diagnostic: see exactly how your terminal sends keystrokes
python scripts/keystroke_diagnostic.py
```

### Config: UTF-8 BOM

If `config.yaml` was saved by Notepad or another Windows editor with a UTF-8 BOM, you'll get "No models provided" errors on first run. Fix:

```bash
# Re-save without BOM
hermes config edit
```

### Paths: Forward Slashes

```bash
# ✅ Works everywhere
C:/Users/you/project
~/project

# ❌ Avoid in bash (escape hell)
C:\\Users\\you\\project
```

Forward slashes work in every Hermes tool and most Windows APIs. Prefer them.

### `execute_code` Sandbox: WinError 10106

If you see "The requested service provider could not be loaded" from the sandbox — it's usually the env scrubber dropping `SYSTEMROOT` from the child process. Fixed in current versions. If it recurs, check inside `execute_code`:

```python
import os
print(os.environ.get("SYSTEMROOT"))  # Should be C:\Windows
```

### Shell: Hermes Uses Bash on Windows

The `terminal` tool runs commands through bash (git-bash / MSYS), not PowerShell. Use POSIX syntax:

```bash
# ✅ Correct
ls $HOME && echo "done"
grep "pattern" file.txt

# ❌ Won't work
Get-ChildItem
Select-String "pattern" file.txt
$env:FOO
```

---

## Practical Patterns

### Pattern 1: Secure Production Setup

Setting up Hermes for a production gateway with multiple users:

```bash
# 1. Enable security features
hermes config set security.redact_secrets true
hermes config set privacy.redact_pii true
hermes config set approvals.mode smart

# 2. Add credential pool for rate limit handling
hermes auth add   # Add OpenRouter key 1
hermes auth add   # Add OpenRouter key 2

# 3. Create a production profile
hermes profile create prod --clone
hermes profile use prod

# 4. Tighten compression for long sessions
hermes config set compression.threshold 0.40

# 5. Verify everything
hermes doctor --fix
hermes status --all
```

### Pattern 2: Local-Model Lab Profile

Experimenting with local models without touching your main setup:

```bash
# Create isolated lab profile
hermes profile create lab

# Point to local Ollama
hermes config set model.base_url "http://localhost:11434/v1"
hermes config set model.default "local/llama3"

# Run a quick test
hermes -p lab chat -q "Explain transformer attention in one paragraph"
```

### Pattern 3: Multi-Client Agency Setup

Running Hermes for multiple clients with full isolation:

```bash
# Create per-client profiles
hermes profile create client-acme --clone
hermes profile create client-globex --clone
hermes profile create client-stark --clone

# Each gets their own:
# - config.yaml (different models, base URLs)
# - .env (different API keys)
# - sessions/ (isolated conversation history)
# - skills/ (client-specific workflows)

# Run a task for a specific client
hermes -p client-acme chat -q "Generate monthly report"

# Use Kanban with specialist profiles (Chapter 6)
```

### Pattern 4: MCP-Powered Development Environment

Extending Hermes with project-specific tools:

```yaml
# config.yaml
mcp_servers:
  gitnexus:
    command: "uvx"
    args: ["gitnexus-mcp"]
    timeout: 120

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    timeout: 30

  database:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    timeout: 60
```

```bash
# After adding servers
hermes mcp list       # Verify all connected
hermes mcp test gitnexus  # Test specific server
/reload-mcp           # Reload in session (gateway)
```

---

## 7.9 Local Models — Running Hermes Completely Offline

Cloud APIs are great until they're not. Rate limits, outages, pricing changes, data privacy concerns — local models eliminate all of them. Zero cost per token. Zero data leaving your machine. Zero dependency on anyone else's server.

### The Hardware Reality

```mermaid
flowchart LR
    subgraph hw["LOCAL LLM HARDWARE GUIDE"]
        direction TB
        S4["4 GB RAM\n1-3B params (Q4)\nbasic chat, formatting\n15-30 tok/s"]
        S8["8 GB RAM\n7-8B params (Q4_K_M)\nsolid daily assistant\n8-20 tok/s"]
        S16["16 GB RAM\n8-14B params (Q4_K_M)\nquality code, analysis\n5-15 tok/s"]
        S32["32 GB RAM\n14-32B params (Q4_K_M)\nnear-cloud quality\n3-8 tok/s"]
        GPU["GPU (8GB VRAM)\n7-8B params (Q8)\n50-100 tok/s (fast!)"]
        NOTE["No GPU? No problem.\nCPU inference works.\nSlower, but perfectly usable for batch tasks."]
        S4 --> S8 --> S16 --> S32
    end
```

### Setup: llama.cpp (Recommended)

```bash
# 1. Install llama.cpp
git clone https://github.com/ggerganov/llama.cpp ~/llama.cpp
cd ~/llama.cpp && make -j$(nproc)

# 2. Download a model (pick one based on your RAM)
# Option A: 8B params, 4.9GB — best for 16GB RAM
# Search huggingface.co for "llama 3.1 8b instruct gguf q4_k_m"

# Option B: 3B params, 2GB — best for 8GB RAM  
# Search for "phi-3 mini gguf q4_k_m"

# Option C: 1.5B params, 1.1GB — runs on anything
# Search for "qwen 2.5 1.5b gguf q4"

# 3. Save to ~/models/
mkdir -p ~/models
# Place your .gguf file there

# 4. Test it works
cd ~/llama.cpp
./llama-cli -m ~/models/llama-3.1-8b-instruct-q4_k_m.gguf \
  -p "Hello, explain quantum computing in one sentence." \
  -n 100 -c 2048
```

### Connecting Hermes to Your Local Model

```bash
# Start the local model server
./llama-server -m ~/models/llama-3.1-8b-instruct-q4_k_m.gguf \
  --host 127.0.0.1 --port 8080 \
  -c 4096 -ngl 0    # -ngl 0 = CPU only; set to 99 for GPU

# In another terminal, configure Hermes
hermes config set providers.local.type openai-compatible
hermes config set providers.local.base_url http://127.0.0.1:8080/v1
hermes config set providers.local.model "local-model"

# Use it
hermes -m local "Summarize this document for me"
```

### Setup: Ollama (Easiest)

```bash
# 1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull a model
ollama pull llama3.1:8b       # 4.9GB, best all-rounder
ollama pull phi3:mini          # 2.2GB, great for low-RAM
ollama pull deepseek-coder-v2  # For code tasks

# 3. It auto-starts on port 11434
# Configure Hermes
hermes config set providers.ollama.type ollama
hermes config set providers.ollama.base_url http://127.0.0.1:11434

# Use it
hermes -m ollama/llama3.1:8b "Write a Python script to parse CSV files"
```

### Hybrid Strategy — Best of Both Worlds

```mermaid
flowchart LR
    subgraph local["LOCAL (free, private)"]
        L1["✓ Email triage / categorization"]
        L2["✓ Document summarization"]
        L3["✓ Data extraction & formatting"]
        L4["✓ PII-sensitive tasks"]
        L5["✓ Bulk batch processing"]
        L6["✓ Late-night crons (when speed doesn't matter)"]
    end
    subgraph cloud["CLOUD (paid, smarter)"]
        C1["✓ Client-facing content"]
        C2["✓ Architecture & design decisions"]
        C3["✓ Code review (needs deep reasoning)"]
        C4["✓ Complex debugging"]
        C5["✓ Real-time interactive chat"]
    end
    RULE["Rule of thumb:\nIf nobody sees the output → local\nIf a human reads the output → cloud"]
```

### The Cost Difference

| Task | Cloud (Sonnet) | Local (llama.cpp) |
|------|---------------|-------------------|
| 100 email triages/day | ~$0.50/day = $15/mo | $0 forever |
| Daily 2000-word blog | ~$0.10/article | $0 forever |
| Weekly data report | ~$0.50/report | $0 forever |
| 24/7 monitoring analysis | ~$30/mo | $0 forever |
| **Total for 1 year** | **~$540** | **$0** |

Local models pay for themselves in electricity (negligible) after the first month.

💡 **Tip:** Create a `local` profile that defaults to your local model. Use it for batch crons and PII-heavy tasks. Switch to your cloud profile for interactive work.

---

## 7.10 Running Hermes on Android

Your phone is always with you. Your laptop isn't. Running a local LLM on Android means Hermes works anywhere — on the train, at a café, even without internet.

### Hardware Requirements

```mermaid
flowchart LR
    subgraph android["ANDROID LLM — WHAT YOUR PHONE CAN RUN"]
        direction TB
        P4["4 GB RAM\n1-1.5B (Q4)\n10-20 tok/s"]
        P6["6 GB RAM\n1.5-3B (Q4)\n8-18 tok/s"]
        P8["8 GB RAM\n3B (Q4_K_M)\n10-20 tok/s"]
        P12["12 GB RAM\n3-7B (Q4_K_M)\n5-15 tok/s"]
        P16["16 GB RAM\n7-8B (Q4_K_M)\n3-10 tok/s"]
        P4 --> P6 --> P8 --> P12 --> P16
    end
    subgraph chips["Chipset matters too"]
        CS1["Snapdragon 8 Gen 2/3 — fastest"]
        CS2["Exynos 1580+ — good"]
        CS3["Older chips — subtract 30-50% speed"]
    end
    subgraph example["Example: Samsung A56 (12GB, Exynos 1580)"]
        E1["Gemma 2 2B at Q4: ~18-25 tok/s"]
        E2["Llama 3.1 8B at Q4: ~3-6 tok/s"]
        E3["Qwen 2.5 3B at Q4: ~12-18 tok/s"]
    end
```

### Setup: Termux + llama.cpp

```bash
# 1. Install Termux from F-Droid (NOT Play Store — outdated)
#    https://f-droid.org/packages/com.termux/

# 2. Inside Termux, install dependencies
pkg update && pkg upgrade
pkg install git cmake wget

# 3. Build llama.cpp for ARM
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build && cd build
cmake .. -DGGML_OPENMP=ON
cmake --build . --config Release -j$(nproc)

# 4. Download a phone-friendly model
# Best pick: Qwen 2.5 3B Instruct (Q4_K_M, ~1.9GB)
# Or: Gemma 2 2B (Q4_K_M, ~1.4GB) — faster
mkdir -p ~/models
cd ~/models
wget "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf"

# 5. Test it
cd ~/llama.cpp/build/bin
./llama-cli \
  -m ~/models/qwen2.5-3b-instruct-q4_k_m.gguf \
  -p "Explain Docker in 3 sentences" \
  -n 150 -c 2048
```

### Connecting Phone Hermes to Telegram

```bash
# Start the model server in Termux
./llama-server \
  -m ~/models/qwen2.5-3b-instruct-q4_k_m.gguf \
  --host 127.0.0.1 --port 8080 \
  -c 2048 -t 4    # -t 4 = 4 threads (adjust for your CPU)

# In another Termux session:
# Install Hermes (if not already)
pip install hermes-agent

# Configure to use local model
hermes config set providers.local.type openai-compatible
hermes config set providers.local.base_url http://127.0.0.1:8080/v1
hermes config set providers.local.model "local"

# Connect to your existing Telegram bot
hermes gateway run

# Now your phone IS your AI assistant.
# Fully offline. Fully private. Zero API cost.
```

### The Mobile Workflow

```mermaid
flowchart TD
    subgraph morning["🌅 Morning (offline, on train)"]
        M1["→ Summarize my unread emails"]
        M2["→ Draft replies to the 3 urgent ones"]
        M3["→ Local model handles it, no internet needed"]
        M1 --> M2 --> M3
    end
    subgraph work["🏢 At work (WiFi)"]
        W1["→ Switch to cloud model for quality work"]
        W2["→ /model anthropic/claude-sonnet-4"]
        W1 --> W2
    end
    subgraph evening["🌙 Evening (offline, at home)"]
        E1["→ Write tomorrow's blog draft"]
        E2["→ Local model drafts it, you refine later"]
        E1 --> E2
    end
    subgraph travel["✈️ Travel (no WiFi at all)"]
        T1["→ Full Hermes works on phone data"]
        T2["→ Local model = zero data usage"]
        T3["→ Only Telegram API uses data (minimal)"]
        T1 --> T2 --> T3
    end
    morning --> work --> evening --> travel
```

### Tips for Mobile Performance

- **Use Q4_K_M quantization** — best speed/quality tradeoff
- **Limit context to 2048 tokens** (`-c 2048`) — saves RAM
- **Use 4 threads** (`-t 4`) — optimal for phone CPUs
- **Close other apps** — LLM needs all available RAM
- **Keep phone plugged in** — inference drains battery fast
- **Use a cooling pad** for extended sessions — phones throttle when hot

💡 **Tip:** If you have a phone + laptop on the same WiFi, run the model on your phone (it's always on) and connect your laptop's Hermes to it. Phone becomes a dedicated AI server.

---

## Summary

| Topic | Key takeaway |
|-------|-------------|
| Secret redaction | Masks API keys in tool output — `security.redact_secrets true` |
| PII redaction | Hashes user IDs in gateway messages — `privacy.redact_pii true` |
| Command approval | `manual` / `smart` / `off` — `approvals.mode smart` recommended |
| MCP servers | Extend Hermes with external tools via stdio or HTTP transport |
| Custom providers | Point to self-hosted models via `model.base_url` |
| Profiles | Isolated Hermes instances — separate config, sessions, skills, memory |
| Credential pools | Multiple API keys per provider, automatic rotation |
| Context optimization | Compression + toolset pruning = more room for real work |
| Local models | llama.cpp or Ollama — free, private, offline AI |
| Android setup | Termux + llama.cpp — AI assistant in your pocket |
| Debugging | `hermes doctor`, `/debug`, log inspection, `hermes status` |
| Windows tips | Ctrl+Enter, UTF-8 BOM, forward slashes, bash not PowerShell |

**Next:** [Chapter 8: Power Techniques — Goal, Checkpoints, Steer, Compression →](ch08-power-techniques.md)

---

<!-- SCREENSHOT: hermes doctor output showing all checks passed -->
<!-- SCREENSHOT: hermes mcp list showing connected servers -->
<!-- SCREENSHOT: hermes profile list showing multiple profiles -->
<!-- SCREENSHOT: hermes auth list showing credential pool -->
<!-- SCREENSHOT: Windows Terminal Ctrl+Enter newline -->


---

# Chapter 8: Power Techniques — The Expert's Toolkit

> **You've configured Hermes. You've automated workflows. Now learn the shortcuts, steering wheels, and escape hatches that separate power users from everyone else. This chapter is your black belt.**

---

## 8.1 YOLO Mode — Skip Approvals for Speed

Every time Hermes wants to run a flagged shell command, it pauses and asks for permission. That's safe — but slow. YOLO mode skips all approval prompts.

```mermaid
flowchart TD
    subgraph normal["NORMAL MODE"]
        direction TB
        N1["Hermes: \"Run rm -rf node_modules?\""]
        N2["You: [waits... approves]"]
        N3["Hermes: \"Run npm install?\""]
        N4["You: [waits... approves]"]
        N5["→ 3 commands = 3 approval pauses"]
        N1 --> N2 --> N3 --> N4 --> N5
    end
    subgraph yolo["YOLO MODE"]
        direction TB
        Y1["Hermes: runs all 3 commands back-to-back"]
        Y2["→ 3 commands = 0 pauses"]
        Y1 --> Y2
    end
```

### Three Ways to Activate

```bash
# 1. Per-invocation flag
hermes --yolo

# 2. Toggle mid-session
/yolo          # toggles on/off

# 3. Environment variable
export HERMES_YOLO_MODE=1
```

### When to Use It

| Scenario | YOLO? | Why |
|----------|-------|-----|
| Local development, trusted codebase | ✅ | You wrote the code, you trust it |
| CI/CD pipeline scripts | ✅ | Automated, no human in the loop |
| Exploring a new repo | ⚠️ | Risky — Hermes might modify unknown files |
| Production servers | ❌ | Always review before touching prod |
| Cron jobs / background tasks | ✅ | Unattended — needs to run autonomously |

💡 **Tip:** The sweet spot is `approvals.mode: smart` (covered in Chapter 7) — auto-approves low-risk commands, still prompts on destructive ones. Reserve full YOLO for trusted environments.

---

## 8.2 `/goal` — Standing Objectives Across Turns

Sometimes a task takes more than one message. You want Hermes to keep working on something across multiple turns without you repeating the objective every time.

```mermaid
flowchart TD
    subgraph without["WITHOUT /goal"]
        direction TB
        U1["You: \"Refactor the auth module\""]
        U2["Hermes: refactors auth"]
        U3["You: \"Also update the tests\""]
        U4["Hermes: \"What tests?\" (lost context)"]
        U1 --> U2 --> U3 --> U4
    end
    subgraph with["WITH /goal"]
        direction TB
        G1["You: /goal Refactor auth module to use JWT"]
        G2["Hermes: Goal set. Working on JWT refactor..."]
        G3["You: \"Also update the tests\""]
        G4["Hermes: Still in JWT context, updates tests"]
        G5["You: \"Check the middleware too\""]
        G6["Hermes: Still in JWT context, checks MW"]
        G1 --> G2 --> G3 --> G4 --> G5 --> G6
    end
```

### Goal Commands

```
/goal Refactor auth module to use JWT tokens     # Set a new goal
/goal status                                      # Check current goal
/goal pause                                       # Pause (keeps goal, stops steering)
/goal resume                                      # Resume a paused goal
/goal clear                                       # Clear the goal entirely
```

The goal gets injected into every subsequent turn until you clear it. It's like giving Hermes a north star — every action it takes should move toward that objective.

💡 **Tip:** Use `/goal` for multi-step refactors, research projects, or any task where you'll send 3+ follow-up messages. It prevents context drift.

---

## 8.3 `/steer` — Inject Context Mid-Task Without Interrupting

Hermes is in the middle of a 10-step refactor. You just realized it should also update the TypeScript types. But you don't want to interrupt the current step.

```
/steer Also update the TypeScript type definitions when you modify the interfaces
```

`/steer` queues a message that gets injected **after the next tool call completes** — not immediately, not at the end. It's a course correction that doesn't break stride.

```mermaid
flowchart LR
    S1["Step 1\ndone"] --> S2["Step 2\ndone"] --> S3["Step 3\nrunning"] --> S4["Step 4\nqueued"] --> S5["Step 5\nqueued"]
    S3 -.->|"/steer injected here\nafter Step 3's tool call returns"| S4
```

### When to Steer vs. Queue vs. New Message

| Method | When to use | Effect |
|--------|-------------|--------|
| `/steer` | Course-correct without stopping | Injects after next tool call |
| `/queue` | Add a follow-up task for after | Waits until current turn ends |
| New message | Change direction entirely | Interrupts current work |

💡 **Tip:** `/steer` is perfect for "also do X" and "don't forget about Y" — small additions that shouldn't derail the current operation.

---

## 8.4 `/queue` — Stack Commands While Hermes Works

Hermes is running a long test suite. You have three more things you want done after it finishes. Instead of waiting, queue them:

```
/queue Run the linter on the auth module
/queue Check if the Docker build still works
/queue Update the README with the new env vars
```

Each queued command runs sequentially after the current turn completes. You can stack as many as you want.

```mermaid
flowchart TD
    subgraph queue["QUEUE"]
        Q1["[1] Run linter on auth module ← next"]
        Q2["[2] Check Docker build"]
        Q3["[3] Update README"]
        Q1 --> Q2 --> Q3
    end
    CT["Current task: Running test suite (80%)"]
    CT --> queue
```

💡 **Tip:** `/queue` is FIFO (first in, first out). Plan your order — lint before build, build before docs.

---

## 8.5 `/branch` — Fork Conversations for Exploration

You're in the middle of a productive session and want to try a risky approach without losing your current state. Branch it.

```
/branch
```

This creates a **fork** of the current conversation — a new session that starts with the same history. Your original session remains untouched.

```mermaid
flowchart TD
    subgraph sessionA["Session A (original)"]
        A1["message 1"]
        A2["message 2"]
        A3["/branch"]
        A4["message 3"]
        A5["message 4"]
        A6["continued normally"]
        A1 --> A2 --> A3
        A3 --> A4 --> A5 --> A6
    end
    subgraph sessionB["Session B (fork)"]
        B1["risky experiment"]
        B2["didn't work"]
        B3["/quit (discard)"]
        B1 --> B2 --> B3
    end
    A3 -->|fork| sessionB
```

Use cases:
- **Try a risky refactor** — branch, test the approach, discard if it fails
- **Explore alternatives** — branch from the same point, try two different architectures
- **Parallel research** — branch to investigate a library while main thread continues coding

💡 **Tip:** Branches are cheap — they share no state with the parent after forking. Go wild in a branch without consequences.

---

## 8.6 Checkpoints & Rollback — Time Travel for Your Codebase

Hermes is about to modify 15 files in a complex refactor. What if something goes wrong? Checkpoints let you snapshot the filesystem and roll back if needed.

### Setup

```bash
# Enable checkpoints at invocation
hermes --checkpoints

# Or enable in config
hermes config set checkpoints.enabled true
hermes config set checkpoints.max_snapshots 50
```

### Using Checkpoints

```bash
# In-session: rollback to last checkpoint
/rollback

# Rollback to specific checkpoint (N steps back)
/rollback 3
```

```mermaid
flowchart LR
    CP0["CP0\n(init)"] --> CP1["CP1\n(step1)"] --> CP2["CP2\n(step2)"] --> CP3["CP3\n(step3)"] --> CP4["CP4 (current)\n(step4)"]
    CP4 -.->|"/rollback 1\nrestores to CP3"| CP3
```

Each checkpoint captures file state at that moment. Hermes creates them automatically before each tool call that modifies files when checkpoints are enabled.

⚠️ **Warning:** Checkpoints capture filesystem state, NOT conversation state. Rolling back restores files but keeps the conversation history. Use `/branch` if you need to fork the entire session.

---

## 8.7 Session Snapshots — Save and Restore Full State

While checkpoints protect the filesystem, snapshots protect your **entire Hermes configuration and state**:

```
/snapshot                    # Create a named snapshot
/snapshot pre-refactor       # Named snapshot for easy reference
/snapshot restore pre-refactor  # Restore a named snapshot
```

Snapshots capture:
- Config.yaml state
- Session transcript
- Skill loading state
- Memory state at that point

Use snapshots before major changes — model switches, config experiments, or any "I might want to undo this completely" moment.

---

## 8.8 Fast Mode — Priority Processing

```
/fast
```

Toggles fast/priority processing mode. When enabled, Hermes optimizes for speed:

- Reduced reasoning overhead
- Fewer intermediate explanations
- Streamlined tool output processing
- Prioritized in the processing queue

Use it for:
- Quick fire-and-forget questions
- Batch operations where you just want results
- Time-sensitive tasks

Toggle off with `/fast` again when you want thorough, detailed responses back.

---

## 8.9 Reasoning Control — Dial In How Hard Hermes Thinks

Different tasks need different levels of reasoning. A typo fix doesn't need extended thinking. A system architecture decision does.

```
/reasoning none       # No reasoning shown, fastest responses
/reasoning minimal    # Brief reasoning, good for simple tasks
/reasoning low        # Light reasoning for routine work
/reasoning medium     # Default — balanced
/reasoning high       # Extended reasoning for complex problems
/reasoning xhigh      # Maximum reasoning for architecture decisions
/reasoning show       # Show reasoning tokens (if model supports it)
/reasoning hide       # Hide reasoning tokens
```

### Reasoning Level Guide

| Level | When to use | Token cost | Example |
|-------|-------------|------------|---------|
| `none` | Formatting, quick lookups | Lowest | "What's the capital of France?" |
| `minimal` | Simple edits, known patterns | Low | "Fix the typo on line 42" |
| `low` | Routine coding tasks | Medium | "Add input validation to this form" |
| `medium` | Default — most tasks | Medium | "Implement user authentication" |
| `high` | Complex logic, debugging | High | "Debug this race condition" |
| `xhigh` | Architecture, multi-system design | Highest | "Design the event-driven pipeline" |

💡 **Tip:** Higher reasoning = more tokens = more cost. Use `xhigh` sparingly — only for genuinely hard problems. Default `medium` handles 90% of tasks well.

---

## 8.10 Busy Mode — What Happens When You Type While Hermes Works

Hermes is in the middle of a long operation. You send a message. What happens? That depends on your **busy mode** setting.

```
/busy queue       # Your message waits in line (default)
/busy steer       # Your message gets injected mid-task
/busy interrupt   # Your message interrupts current work
/busy status      # Check current mode
```

```mermaid
flowchart TD
    subgraph q["QUEUE: Safe, orderly but slowest"]
        Q1["Work"]
        Q2["[wait]"]
        Q3["Your msg"]
        Q1 --> Q2 --> Q3
    end
    subgraph s["STEER: Mid-flight course change"]
        S1["Work"]
        S2["inject"]
        S3["cont."]
        S1 --> S2 --> S3
    end
    subgraph i["INTERRUPT: Immediate context switch"]
        I1["Work ✗ stopped"]
        I2["New msg runs"]
        I1 --> I2
    end
```

**Recommendation:**
- **`queue`** (default) — safest, use for most work
- **`steer`** — when you need to course-correct without stopping
- **`interrupt`** — emergency stop + new direction

---

## 8.11 Background Prompts — Fire and Forget

```
/background Research the latest Next.js 15 features and write a summary to ~/research/nextjs15.md
```

Runs a prompt in the background inside your session. Hermes processes it independently while you continue chatting normally.

```mermaid
flowchart LR
    subgraph main["Main thread"]
        M1["You: ..."]
        M2["Hermes:"]
        M3["You: ..."]
        M4["Hermes:"]
        M5["You: ..."]
        M1 --> M2 --> M3 --> M4 --> M5
    end
    subgraph bg["Background thread"]
        B1["Researching Next.js"]
        B2["Reading docs..."]
        B3["Writing summary..."]
        B4["✅ Done → saved to\n~/research/"]
        B1 --> B2 --> B3 --> B4
    end
```

Background prompts:
- Don't block your main conversation
- Complete even if you send new messages
- Report back when finished (in CLI) or silently complete (in gateway)

💡 **Tip:** Use `/background` for research tasks, file generation, or any work that takes more than a minute but doesn't need your immediate attention.

---

## 8.12 Pipe Tricks — Unix Power Meets AI

Hermes runs in your terminal. That means it plays well with Unix pipes, redirects, and heredocs.

### Piped Input

```bash
# Pipe a file into Hermes for analysis
cat error.log | hermes chat -q "What's causing these errors?"

# Pipe command output
docker logs myapp 2>&1 | hermes chat -q "Diagnose the crash"

# Pipe git diff for review
git diff | hermes chat -q "Review these changes"
```

### Heredoc for Complex Prompts

```bash
hermes chat -q "$(cat <<'EOF'
Analyze the following architecture and identify:
1. Single points of failure
2. Scalability bottlenecks
3. Security concerns
4. Cost optimization opportunities

The system uses: FastAPI backend, PostgreSQL, Redis cache,
Elasticsearch, and 3 microservices on Docker Compose.
EOF
)"
```

### Chaining with Other Tools

```bash
# Generate code, format it, write to file
hermes chat -q "Write a Python FastAPI health check endpoint" | black - | tee api/health.py

# Extract todos from codebase and summarize
grep -r "TODO\|FIXME\|HACK" src/ | hermes chat -q "Prioritize these TODOs by urgency"

# Combine with jq for JSON processing
curl -s https://api.example.com/data | hermes chat -q "Extract the top 5 records by revenue and format as CSV"
```

💡 **Tip:** The `-q` flag (query mode) is essential for pipe tricks — it runs a single query non-interactively, perfect for scripting.

---

## 8.13 Model Mid-Task Switching — Change Horses Mid-Race

You started a coding task with a fast, cheap model. Halfway through, you realize you need a smarter model for the complex logic. Don't restart — switch models mid-task.

```
/model anthropic/claude-sonnet-4    # Switch to a smarter model
```

Hermes keeps the full conversation context. The new model picks up exactly where the old one left off — same session, same history, same tool state.

### Strategic Model Switching

```mermaid
flowchart LR
    subgraph phase1["Cheap model"]
        A["deepseek/deepseek-chat\n$0.14/M tokens"]
    end
    subgraph phase2["Expensive model"]
        B["anthropic/claude-sonnet-4\n$3/M tokens"]
    end
    subgraph phase3["Cheap model"]
        C["deepseek/deepseek-chat\n$0.14/M tokens"]
    end
    A -->|"Boilerplate\nscaffolding"| B
    B -->|"Complex logic\nimplementation"| C
    C -->|"Write tests\nand docs"| D["Done"]
```

💡 **Tip:** Use cheap models for scaffolding, formatting, and boilerplate. Switch to expensive models only for the hard parts — complex algorithms, architecture decisions, debugging. Switch back for tests and docs.

---

## 8.14 Compression Tricks — Squeeze More Into Every Session

Long conversations eat tokens. When you hit the context window limit, Hermes auto-compresses — but you can control it.

### Manual Compression

```
/compress
```

Forces an immediate compression cycle. Hermes summarizes the conversation so far and replaces the full history with a compressed version, freeing up context space for continued work.

### Compression Configuration

```bash
# Tune when compression triggers (fraction of context window)
hermes config set compression.threshold 0.50    # Default: compress at 50% full
hermes config set compression.threshold 0.70    # Later: more context before compressing
hermes config set compression.threshold 0.30    # Earlier: keep more room free

# Set how aggressively to compress
hermes config set compression.target_ratio 0.20  # Compress to 20% of original (default)
hermes config set compression.target_ratio 0.40  # Less aggressive: keep 40%
```

```mermaid
flowchart TD
    subgraph before["Before compression"]
        Z1["0%"] --> Z2["50% — threshold\nAuto-compress triggers here"] --> Z3["100% — Hard limit (error)"]
        Z4["Normal operation\n0% → 50%"]
    end
    subgraph after["After compression"]
        A1["0% → 10%\ntarget_ratio=0.20"]
        A2["Fresh space for\ncontinued work"]
        A1 --> A2
    end
    before --> after
```

### Compression Best Practices

| Strategy | When | How |
|----------|------|-----|
| Manual `/compress` | After completing a major task phase | Clears out the detailed work, keeps the conclusions |
| Lower threshold | Long automated sessions (cron) | `compression.threshold: 0.40` |
| Higher target ratio | Tasks where detail matters | `compression.target_ratio: 0.35` |
| Toolset pruning | Cron jobs with specific needs | `enabled_toolsets: ["terminal", "file"]` |

💡 **Tip:** The best compression strategy is prevention. Use `/goal` to keep Hermes focused, `/new` to start fresh between unrelated tasks, and toolset pruning on cron jobs to reduce prompt size from the start.

---

## 8.15 Profile-Based Separation — Work, Personal, Lab

You covered profiles in Chapter 7 for configuration isolation. Here's the **power-user pattern**: using profiles as completely separate workspaces.

```mermaid
flowchart LR
    subgraph profiles["HERMES PROFILES"]
        subgraph work["work"]
            WC["Config:\nClaude"]
            WS["Skills:\nGitHub, review, deploy"]
            WM["Memory:\nWork projects"]
            WS2["Sessions:\nIsolated"]
        end
        subgraph personal["personal"]
            PC["Config:\nDeepSeek"]
            PS["Skills:\nBlog, Spotify, home"]
            PM["Memory:\nPersonal prefs"]
            PS2["Sessions:\nIsolated"]
        end
        subgraph lab["lab"]
            LC["Config:\nLocal Ollama"]
            LS["Skills:\nExperimental only"]
            LM["Memory:\nNone (clean)"]
            LS2["Sessions:\nIsolated"]
        end
    end
```

### The Three-Profile Setup

```bash
# Create work profile (clone defaults)
hermes profile create work --clone
hermes profile use work
# Now configure: business model, work skills, work memory

# Create personal profile
hermes profile create personal --clone
# Configure: cheaper model, personal skills

# Create lab profile (clean slate, no memory)
hermes profile create lab
# Configure: local Ollama model, experimental skills
```

### Switching Contexts

```bash
# CLI: use per-invocation flag
hermes -p work        # Work session
hermes -p personal    # Personal session
hermes -p lab         # Lab experiment

# Gateway: each profile can run its own gateway
# or share one with platform routing
```

### Why This Matters

1. **No context pollution** — work projects never leak into personal chat
2. **Cost optimization** — cheap model for personal, premium for work
3. **Safe experimentation** — lab profile with local models, no API costs
4. **Memory isolation** — each profile remembers only what's relevant
5. **Skill separation** — no need to load 50 skills when you only need 5

---

## Power Techniques Quick Reference

| Technique | Command | Best for |
|-----------|---------|----------|
| Skip approvals | `/yolo` or `--yolo` | Trusted environments |
| Standing objective | `/goal <text>` | Multi-step tasks |
| Mid-task injection | `/steer <text>` | Course correction |
| Stack follow-ups | `/queue <text>` | Sequential after-current |
| Fork conversation | `/branch` | Risk-free exploration |
| Time travel | `--checkpoints` + `/rollback` | Dangerous refactors |
| Full state save | `/snapshot` | Before major changes |
| Speed mode | `/fast` | Quick results |
| Think harder | `/reasoning high` | Complex problems |
| Control busy behavior | `/busy queue\|steer\|interrupt` | Long operations |
| Fire and forget | `/background <prompt>` | Independent tasks |
| Unix integration | `hermes chat -q` + pipes | Scripting |
| Switch models | `/model <name>` | Cost/performance tuning |
| Free up context | `/compress` | Long sessions |
| Isolate workspaces | `hermes -p <profile>` | Work/life separation |

---

## Three Power-User Patterns

### Pattern 1: The Safe Refactor

```
# Step 1: Enable safety nets
hermes --checkpoints -p work

# Step 2: Set the objective
/goal Refactor the auth module from session-based to JWT

# Step 3: Let Hermes work, steering as needed
/steer Keep the existing API contract unchanged

# Step 4: If something breaks
/rollback 1

# Step 5: If everything works
/compress          # free up context
/goal clear        # done
```

### Pattern 2: The Cost-Optimized Sprint

```
# Start with cheap model for boilerplate
hermes -m deepseek/deepseek-chat

# Switch to premium for the hard part
/model anthropic/claude-sonnet-4

# Queue follow-up tasks
/queue Write unit tests for the new module
/queue Update the API documentation

# Switch back to cheap for tests and docs
/model deepseek/deepseek-chat
```

### Pattern 3: The Research Pipeline

```
# Branch for exploration
/branch

# Background research task
/background Analyze all competitors and write comparison to ~/research/competitors.md

# Meanwhile, continue main work
# ... (work on your project normally)

# When background finishes, review results
# and merge insights into main thread
```

---

## 8.16 Let Hermes Solve Its Own Problems

This is the most underused power technique. When Hermes hits an error, crashes, or produces bad output — **ask Hermes to fix itself.**

### Why This Works

Hermes has access to the same tools you do. It can read logs, inspect config, search files, run commands, and read its own source code. It knows more about its own internals than you do. Use that.

```mermaid
flowchart TD
    A["You: \"Fix it\""]
    A --> B["Hermes reads the error message"]
    B --> C["Hermes reads the relevant config / code"]
    C --> D["Hermes diagnoses the root cause"]
    D --> E["Hermes applies the fix"]
    E --> F["Hermes verifies the fix worked"]
    F --> G["Done. You watched."]
```

### The Magic Phrases

Just paste the error and say one of these:

```
"Read the error. Diagnose it. Fix it. Verify it works."
"I'm getting this error — fix it and explain what was wrong."
"This cron job failed — read the logs, find why, patch it."
"Hermes is acting weird — run hermes doctor, find issues, fix them."
"Read the last 50 lines of gateway.log. Fix whatever's broken."
```

### Real Example: Broken Cron Job

```
You: "The morning blog cron didn't fire today. Fix it."

Hermes:
  1. Runs: hermes cron list
  2. Finds job c6e4d1c962bd — status: error
  3. Runs: hermes cron log c6e4d1c962bd
  4. Reads: "API error 429: rate limit exceeded"
  5. Runs: hermes config get providers.openrouter
  6. Finds: only one API key configured
  7. Adds credential pool fallback
  8. Patches the cron retry settings
  9. Runs: hermes cron test c6e4d1c962bd
  10. Confirms: "Fixed. Added second API key to pool, set retry to 
      3 attempts with 30s delay. Test run succeeded."
```

You did nothing. Hermes diagnosed, fixed, and verified — all by itself.

### Real Example: Hermes Config Drift

```
You: "Hermes has been slow lately. Diagnose and optimize."

Hermes:
  1. Runs: hermes doctor
  2. Checks config size, context window usage, active tools
  3. Finds: 14 toolsets loaded (you only use 5 regularly)
  4. Finds: compression threshold at 0.70 (too high)
  5. Reads: config.yaml
  6. Patches: enabled_toolsets to only needed ones
  7. Patches: compression.threshold to 0.40
  8. Runs: hermes status --all
  9. Reports: "Trimmed 9 unused toolsets, tightened compression. 
      Your context window is now 60% larger per session."
```

### Real Example: Skill Gone Stale

```
You: "The blog skill keeps failing on Tuesdays. Fix it."

Hermes:
  1. Loads skill: blog
  2. Reads the SKILL.md and linked scripts
  3. Runs: hermes cron log <blog-job-id>
  4. Finds: "Tuesday topic generation fails — API returns empty array"
  5. Reads the topic generation script
  6. Finds: hardcoded category filter that returns 0 results on Tuesdays
  7. Patches the script with fallback categories
  8. Tests with a dry run
  9. Patches the skill with a new pitfall entry
  10. Reports: "Fixed. Added fallback category list. Updated skill 
      with pitfall documentation."
```

### When Self-Debug Doesn't Work

| Situation | What to do |
|-----------|-----------|
| Model keeps looping on the same wrong fix | `/stop`, then explain the error differently |
| Hermes can't see the error (gateway-side) | Check `gateway.log` manually, paste the relevant lines |
| Config is so broken Hermes won't start | `hermes doctor --fix` from terminal |
| The model itself is the problem | Switch models: `/model openai/gpt-4o` |

💡 **Tip:** After Hermes fixes its own problem, say "Save this as a skill." It'll document the diagnosis + fix so it never has to re-learn it. Each self-debug makes Hermes smarter permanently.

---

**Progress: Chapter 8 complete.** Next up: **Chapter 9 — Real Business Use Cases** — 10 scenarios with actual ROI numbers, showing how people make money with Hermes.

---

*Previous: [Chapter 7 — Advanced Configuration](ch07-advanced-config.md) · Next: [Chapter 9 — Real Business Use Cases](ch09-business-use-cases.md)*


---

# Chapter 9: Real Business Use Cases — 10 Scenarios with ROI Numbers

> **Theory is over. This chapter is about money — 10 real business scenarios where Hermes replaces expensive tools, saves hours of manual work, and generates measurable ROI. Each scenario includes architecture, setup commands, and dollar-value returns.**

---

## 9.1 Content Marketing Engine — Automated Blog Pipeline

The average business blog post costs $150-$500 when outsourced. A content schedule of 2 posts/day means $9,000-$30,000/month. Hermes can do it for the cost of API calls.

### The Architecture

```mermaid
flowchart LR
    subgraph Engine["Content Marketing Engine"]
        subgraph Triggers["Scheduled Triggers"]
            C1["Cron\n7am WIB"]
            C2["Cron\n7pm WIB"]
        end
        subgraph Agent["Hermes Agent"]
            S1["blog"]
            S2["humanizer"]
            S3["marketing-copy"]
        end
        C1 --> Agent
        C2 --> Agent
        Agent --> Blog["Blog Platform"]
        Agent --> Social["Social cross-post"]
    end
```

### Setup

```bash
# Install required skills
hermes skills install blog
hermes skills install humanizer
hermes skills install marketing-copy

# Create morning article job
hermes cron create "0 7 * * *" \
  --skills blog,humanizer,marketing-copy \
  --deliver telegram \
  --name "morning-article"

# Create evening article job
hermes cron create "0 19 * * *" \
  --skills blog,humanizer,marketing-copy \
  --deliver telegram \
  --name "evening-article"
```

When the cron fires, Hermes:
1. Picks a topic from your content calendar (stored in memory)
2. Writes a full SEO-optimized article
3. Runs it through the humanizer to strip AI patterns
4. Publishes to your blog platform
5. Sends you a Telegram notification with the link

### ROI Calculation

| Item | Manual Cost | Hermes Cost |
|------|-------------|-------------|
| Content writer ($200/post) | $12,000/mo | $0 |
| Editor review ($100/post) | $6,000/mo | $0 |
| SEO optimization ($50/post) | $3,000/mo | $0 |
| API calls (~$0.05/article) | — | $3/mo |
| **Total** | **$21,000/mo** | **$3/mo** |

**Monthly savings: ~$21,000** · Time saved: 40+ hours/month

💡 **Tip:** Use `marketing-copy` skill to generate social media snippets from each article. One article → 5 tweets, 1 LinkedIn post, 1 email teaser — zero extra effort.

---

## 9.2 Customer Support Automation — 24/7 AI Agent

Your customers ask questions at 2am. Your support team sleeps. Hermes doesn't.

### The Architecture

```mermaid
flowchart TD
    subgraph System["Customer Support System"]
        Customer["Customer"] --> Channel["Telegram / WhatsApp"]
        Channel --> Gateway["Gateway\n(24/7)"]
        Gateway --> FAQ["FAQ Bot\n(auto)\n\nSkills:\n• custom-faq-router"]
        Gateway --> Escalate["Complex Escalate\n\nSkills:\n• browse\n• search\n• doc"]
        Escalate --> Human["Human Agent\n(Telegram DM)"]
    end
```

### Setup

```bash
# 1. Create a dedicated support profile
hermes profile create support --clone
hermes profile use support

# 2. Create FAQ skill for your business
cat > ~/.hermes/skills/support/FAQ.md << 'EOF'
---
name: support-faq
description: "Customer support FAQ router for [Your Business]"
---

# Support FAQ

## Routing Rules
- Order status → Check via terminal API call
- Pricing → Return pricing table
- Technical issue → Escalate to human
- Refund request → Escalate to human with context
- General question → Answer from knowledge base

## Knowledge Base
[Paste your FAQ content here]
EOF

# 3. Set up the gateway for support
hermes gateway setup    # configure Telegram bot for support

# 4. Enable PII redaction for customer data
hermes config set privacy.redact_pii true
```

### Escalation Pattern

When Hermes can't answer, it doesn't guess — it escalates:

```bash
# In your custom support skill, include escalation logic:
# "If confidence < 70% OR topic = refund/complaint:
#  → send_message to human agent Telegram with:
#    - Customer message
#    - Attempted answer
#    - Suggested resolution"
```

### ROI Calculation

| Item | Before Hermes | With Hermes |
|------|--------------|-------------|
| Support staff (3 shifts × $2,500/mo) | $7,500/mo | $2,500/mo (1 shift) |
| Response time (avg) | 4 hours | 30 seconds |
| After-hours coverage | None | Full 24/7 |
| Customer satisfaction | 72% | 89% |
| **Monthly savings** | — | **$5,000/mo** |

**Monthly savings: ~$5,000** · Response time: -99% · CSAT: +17 points

💡 **Tip:** Use Hermes memory to store customer interaction history. When a customer returns, Hermes recognizes them and has full context — no "can you repeat your issue?" frustration.

---

## 9.3 Code Review & CI/CD Automation

A production bug costs an average of $10,000-$50,000 in lost revenue, customer trust, and emergency fixes. Catching it in review costs $50 in developer time. Hermes automates the review.

### The Architecture

```mermaid
flowchart TD
    subgraph Pipeline["Automated Code Review Pipeline"]
        Dev["Developer pushes PR"] --> GitHub["GitHub PR Event"]
        GitHub -- "Webhook" --> Hermes["Hermes"]
        Hermes --> Security["Security Scan\n\n• secrets\n• vulns\n• deps"]
        Hermes --> Quality["Quality Review\n\n• style\n• logic\n• tests"]
        Security --> Comment["PR Comment\n(inline review)"]
        Quality --> Comment
    end
```

### Setup

```bash
# Install review skills
hermes skills install github-code-review
hermes skills install requesting-code-review

# Subscribe to PR webhook
hermes webhook subscribe pr-review

# The webhook handler prompt (set during creation):
# "When a PR is opened, review the code for:
#  1. Security vulnerabilities (SQL injection, XSS, secrets)
#  2. Logic errors and edge cases
#  3. Missing tests
#  4. Style violations
#  Post inline comments on the PR via gh CLI"
```

### The Webhook in Action

```bash
# Hermes receives the webhook and runs:
gh pr diff $PR_NUMBER | hermes chat -q \
  "Review this PR for security issues, logic errors, and missing tests.
   Post inline comments for any issues found.
   Use the github-code-review skill for formatting."

# Automatic quality gate:
# If critical issues found → comment "🚫 Do not merge"
# If minor issues only    → comment "⚠️ Minor issues"
# If clean                → comment "✅ Approved"
```

### ROI Calculation

| Item | Manual Review | Hermes Review |
|------|--------------|---------------|
| Review time per PR | 2 hours | 5 minutes |
| Bugs caught in review | 60% | 85% |
| Production incidents/quarter | 4 | 1 |
| Cost per incident | $15,000 | $15,000 |
| Developer review cost | $150/PR × 40 PRs/mo | API: ~$20/mo |
| **Quarterly incident cost** | **$60,000** | **$15,000** |
| **Monthly savings** | — | **$15,000/quarter = $5,000/mo** |

**Monthly savings: ~$6,200** (review time + incident prevention) · Bug catch rate: +25%

💡 **Tip:** Combine with Chapter 5's webhook pattern. Hermes reviews PRs automatically on every push — zero manual trigger needed.

---

## 9.4 E-Commerce Operations

Missed restocks cost sales. Wrong pricing loses margin. Manual monitoring eats hours. Hermes monitors everything.

### The Architecture

```mermaid
flowchart TD
    subgraph Engine["E-Commerce Ops Engine"]
        Cron1["Cron 6am"] --> Check["Check inventory levels"]
        Check --> Low{"Low stock?"}
        Low -->|"Yes"| Alert1["Alert + auto-reorder suggestion"]
        Cron2["Cron hourly"] --> Check
        Check --> OOS{"Out of stock?"}
        OOS -->|"Yes"| Alert2["Urgent alert"]
        Check --> Price{"Price change?"}
        Price -->|"Yes"| Alert3["Competitor comparison alert"]
        Cron3["Cron 9pm"] --> Report["Daily sales report → Telegram"]
    end
```

### Setup

```bash
# Inventory monitoring script
hermes cron create "0 6 * * *" \
  --name "inventory-check" \
  --skills terminal,file \
  --deliver telegram

# Prompt: "Check inventory via API at my-store.com/api/stock.
#  Alert me of any product below 10 units.
#  Suggest reorder quantities based on 30-day sales velocity.
#  Save report to ~/reports/inventory-$(date).md"

# Competitor price watch (script-only, zero tokens)
hermes cron create "every 4h" \
  --name "price-watch" \
  --script ~/scripts/check-prices.sh \
  --deliver telegram

# Daily sales digest
hermes cron create "0 21 * * *" \
  --name "sales-digest" \
  --skills terminal \
  --deliver telegram
```

### Script-Only Price Watchdog (Zero Token Cost)

```bash
#!/bin/bash
# ~/scripts/check-prices.sh — runs without LLM, costs $0

COMPETITOR_URL="https://competitor.com/products"
THRESHOLD=5  # percentage difference to alert

# Fetch and compare prices
changes=$(curl -s "$COMPETITOR_URL" | jq -r '
  # Extract competitor prices and compare with our data
  # Alert if difference > threshold
')

if [ -n "$changes" ]; then
  echo "⚠️ Price changes detected:\n$changes"
  # Non-empty stdout = delivered to Telegram
else
  # Empty stdout = silent (no alert)
fi
```

### ROI Calculation

| Item | Before | With Hermes |
|------|--------|-------------|
| Missed restocks/month | 8-12 | 0-1 |
| Revenue lost per stockout | $500 | $0 |
| Price monitoring time | 2 hrs/day | 0 (automated) |
| Competitor reaction time | 2-3 days | 4 hours |
| **Monthly stockout loss** | **$5,000** | **$250** |
| **Monthly labor saved** | — | **$1,200** |

**Monthly savings: ~$5,950** · Stockout reduction: -90% · Reaction time: -95%

💡 **Tip:** Use the `no_agent=True` script pattern for price checks — zero API token cost. Only invoke the LLM for the daily sales digest where analysis adds value.

---

## 9.5 Research & Competitive Intelligence

Your competitors publish, patent, and launch while you sleep. A daily digest of everything happening in your market — automated.

### The Architecture

```mermaid
flowchart TD
    subgraph Engine["Competitive Intelligence Engine"]
        Cron1["Cron 8am"] --> Collect["Collect\n\nSources:\n• blogs\n• arxiv\n• news\n• Reddit"]
        Cron2["Cron weekly"] --> Collect
        Collect --> Analyze["Analyze\n\nSkills:\n• blog-watcher\n• arxiv"]
        Analyze --> Digest["Digest → Telegram"]
    end
```

### Setup

```bash
# Install intelligence skills
hermes skills install blogwatcher
hermes skills install arxiv

# Daily competitive digest
hermes cron create "0 8 * * *" \
  --name "competitive-digest" \
  --skills blogwatcher,arxiv,terminal \
  --deliver telegram

# Prompt: "Check these competitors and topics:
#  Competitors: [competitor1.com, competitor2.com]
#  Topics: [our industry keywords]
#  1. Check competitor blogs for new posts
#  2. Search arXiv for relevant papers
#  3. Summarize key findings in a 5-bullet digest
#  4. Flag anything urgent with 🚨"

# Weekly deep-dive
hermes cron create "0 10 * * 1" \
  --name "weekly-intel" \
  --skills blogwatcher,arxiv,terminal,search \
  --deliver telegram \
  --model anthropic/claude-sonnet-4

# Use a smarter model for the weekly deep analysis
```

### ROI Calculation

| Item | Manual Research | Hermes Research |
|------|----------------|-----------------|
| Daily monitoring time | 2 hours | 0 (automated) |
| Weekly deep-dive time | 8 hours | 0 (automated) |
| Research tools | $200/mo | $0 (API ~$5/mo) |
| Competitive insights missed | 40% | 5% |
| **Monthly labor saved** | — | **$4,000** |
| **Earlier opportunity detection** | — | **Priceless** |

**Monthly savings: ~$4,200** · Coverage: 3x wider · Speed: same-day vs weekly

💡 **Tip:** Chain the daily digest into the weekly deep-dive using `context_from`. The weekly report references all daily digests, giving you a comprehensive monthly picture without manual aggregation.

---

## 9.6 Freelancer / Agency Acceleration

You're a solo freelancer with 3 active clients. Each wants daily progress. You're drowning in context-switching. Hermes becomes your agency of one.

### The Architecture

```mermaid
flowchart TD
    subgraph Accel["Freelancer Acceleration"]
        subgraph Clients["Client Profiles"]
            A["Client A\nProfile"]
            B["Client B\nProfile"]
            C["Client C\nProfile"]
        end
        Clients --> Subagents["Parallel Subagents\n(delegate_task)"]
        subgraph Subagents
            SA["Agent A → Build feature\n(leaf)"]
            SB["Agent B → Write tests\n(leaf)"]
            SC["Agent C → Deploy staging\n(leaf)"]
        end
        Cron["Cron 6pm"] --> Update["Daily client update → Telegram\n(auto-generated progress report)"]
    end
```

### Setup

```bash
# Create a profile per client (isolated sessions, memory, skills)
hermes profile create client-a --clone
hermes profile create client-b --clone
hermes profile create client-c --clone

# Work on Client A's project
hermes -p client-a -m anthropic/claude-sonnet-4

# Inside the session, delegate parallel tasks:
# "Delegate these 3 tasks in parallel:
#  1. Build the user dashboard component (use React + TypeScript)
#  2. Write integration tests for the payment API
#  3. Deploy staging environment and run smoke tests"

# Daily progress report (cron per client)
hermes cron create "0 18 * * *" \
  --profile client-a \
  --name "client-a-daily" \
  --deliver telegram \
  --prompt "Generate a daily progress report for Client A.
    Summarize: commits made today, PRs opened/merged,
    blockers, and tomorrow's plan."
```

### The Multi-Client Sprint

```bash
# Morning: kick off parallel work for all clients
hermes -p client-a chat -q \
  "Continue the dashboard component. Focus on the data tables."

hermes -p client-b chat -q \
  "Fix the checkout flow bug reported yesterday. Add regression test."

hermes -p client-c chat -q \
  "Write API documentation for the new endpoints."
```

Three clients, three parallel streams, one developer.

### ROI Calculation

| Item | Solo Freelancer | With Hermes |
|------|----------------|-------------|
| Active clients manageable | 2-3 | 5-8 |
| Throughput (features/week) | 3-5 | 10-15 |
| Context-switch overhead | 40% of day | 5% |
| Daily progress reports | 1 hr (manual) | 0 (auto) |
| Monthly revenue (3 clients × $5K) | $15,000 | — |
| Monthly revenue (6 clients × $5K) | — | $30,000 |
| **Revenue increase** | — | **$15,000/mo** |

**Revenue increase: ~$15,000/mo** · Throughput: 3x · Clients manageable: 2.5x

💡 **Tip:** Use the `writing-plans` skill to auto-generate project proposals. When a prospect emails, Hermes drafts the proposal, estimates timeline, and suggests pricing — you review and send.

---

## 9.7 SaaS Monitoring & Alerting

Your SaaS goes down at 3am. Your customers notice at 3:05am. By morning, you've lost 200 users and a Twitter thread is trending. Hermes catches it at 3:00:30.

### The Architecture

```mermaid
flowchart TD
    subgraph Monitor["SaaS Monitoring System"]
        Script1["Script\n(every 1 min)"] --> Curl["curl health endpoint"]
        Curl --> OK{"200 OK?"}
        OK -->|"Yes"| Silent["Silent — no output"]
        OK -->|"500"| Alert1["Alert + auto-restart"]
        OK -->|"Timeout"| Alert2["Urgent alert"]
        Script2["Script\n(every 5 min)"] --> Resources["Check disk / memory / CPU"]
        Resources --> Breach{"Threshold\nbreach?"}
        Breach -->|"Yes"| Alert3["Alert"]
        Cron["Cron Monday"] --> Summary["Weekly metrics summary\n(uses LLM for analysis)"]
    end
```

### Setup

```bash
# Health check watchdog — script-only, zero token cost
hermes cron create "*/1 * * * *" \
  --name "health-check" \
  --script ~/scripts/health-check.sh \
  --no-agent \
  --deliver telegram

# Disk/memory watchdog
hermes cron create "*/5 * * * *" \
  --name "resource-watch" \
  --script ~/scripts/resource-check.sh \
  --no-agent \
  --deliver telegram

# Weekly metrics analysis (uses LLM for trend detection)
hermes cron create "0 9 * * 1" \
  --name "weekly-metrics" \
  --skills terminal \
  --deliver telegram \
  --model deepseek/deepseek-chat
```

### Health Check Script

```bash
#!/bin/bash
# ~/scripts/health-check.sh

ENDPOINT="https://myapp.com/health"
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$ENDPOINT")

if [ "$RESPONSE" != "200" ]; then
  echo "🚨 DOWN: $ENDPOINT returned HTTP $RESPONSE"

  # Auto-remediation attempt
  ssh deploy@myapp.com "sudo systemctl restart myapp"
  RESTART_EXIT=$?

  if [ $RESTART_EXIT -eq 0 ]; then
    echo "✅ Auto-restart succeeded. Monitoring..."
  else
    echo "❌ Auto-restart FAILED. Manual intervention required."
  fi
fi
# Empty output = silent (healthy)
```

### ROI Calculation

| Item | Without Monitoring | With Hermes |
|------|-------------------|-------------|
| Mean detection time | 4 hours | 30 seconds |
| Mean recovery time | 2 hours | 5 minutes (auto) |
| Monthly downtime cost (at $500/hr) | $12,000 | $500 |
| Monitoring SaaS (Pingdom, etc.) | $150/mo | $0 |
| On-call engineer cost | $3,000/mo | $0 |
| **Monthly savings** | — | **$14,650/mo** |

**Monthly savings: ~$14,650** · Detection: -99.8% · Recovery: -96%

💡 **Tip:** Use `no_agent=True` for all watchdog scripts. They run every minute — LLM invocation would cost $50+/month. Reserve the LLM for the weekly trend analysis where it actually adds value.

---

## 9.8 Data Analysis & Reporting

Your analytics dashboard shows numbers. It doesn't tell you *why* revenue dropped 12% last Tuesday. Hermes does.

### The Architecture

```mermaid
flowchart TD
    subgraph Engine["Data Analysis Engine"]
        Cron1["Cron weekly"] --> Fetch["Fetch Data\n\nSources:\n• DB\n• API\n• CSV"]
        Cron2["Cron ad-hoc"] --> Fetch
        Fetch --> Analyze["Analyze\n\nSkills:\n• jupyter\n• terminal"]
        Analyze --> Report["Report + Charts\n→ Telegram"]
    end
```

### Setup

```bash
# Install Jupyter skill for live data exploration
hermes skills install jupyter-live-kernel

# Weekly analytics report
hermes cron create "0 9 * * 1" \
  --name "weekly-analytics" \
  --skills jupyter-live-kernel,terminal,file \
  --deliver telegram \
  --prompt "Generate the weekly analytics report:
    1. Connect to PostgreSQL and pull this week's data
    2. Compare with previous week (revenue, users, churn)
    3. Identify top 3 changes and root causes
    4. Generate charts and save to ~/reports/
    5. Send summary to Telegram with key insights"
```

### Ad-Hoc Analysis

```bash
# Ask questions about your data on the fly
hermes chat -q "Why did our conversion rate drop last Tuesday?
  Pull data from the analytics DB and compare with the
  previous 4 Tuesdays. Factor in: traffic source, device
  type, and checkout step drop-off."
```

Hermes connects to your database, runs the queries, and returns an answer with specific numbers — not generic advice.

### ROI Calculation

| Item | Data Analyst | Hermes |
|------|-------------|--------|
| Monthly salary | $4,500/mo | $0 |
| Report turnaround | 2 days | 10 minutes |
| Ad-hoc query response | 4 hours | 2 minutes |
| Missed insights (lack of time) | 60% | 10% |
| **Monthly savings** | — | **$4,500** |

**Monthly savings: ~$4,500** · Report speed: -99% · Coverage: +50%

💡 **Tip:** Use `execute_code` for data processing — it gives Hermes access to Python, pandas, and matplotlib in a single tool call. Complex analysis without Jupyter overhead.

---

## 9.9 Email Management — Triage & Respond

You get 150 emails a day. 120 are noise. 25 need replies. 5 are urgent. Hermes sorts them all before you wake up.

### The Architecture

```mermaid
flowchart TD
    subgraph Engine["Email Triage Engine"]
        Cron["Cron 7am"] --> Fetch["Fetch Email\n(IMAP)"]
        Fetch --> Categorize["Categorize\n\n• urgent\n• reply\n• FYI\n• spam\n• action"]
        Fetch --> Drafts["Draft Replies\n\nSkills:\n• himalaya\n• terminal"]
    end
```

### Setup

```bash
# Install email skill
hermes skills install himalaya

# Morning email triage
hermes cron create "0 7 * * *" \
  --name "email-triage" \
  --skills himalaya,terminal \
  --deliver telegram \
  --prompt "Check my inbox via himalaya.
    Categorize all unread emails:
    🚨 URGENT (needs response today): list with sender + subject
    📧 REPLY NEEDED (can wait): list with suggested response
    📋 FYI (just read): count + key topics
    🗑️ SPAM: auto-delete obvious spam
    Send the digest to Telegram."

# Afternoon follow-up
hermes cron create "0 14 * * *" \
  --name "email-followup" \
  --skills himalaya,terminal \
  --deliver telegram \
  --prompt "Check for new emails since morning triage.
    Only alert on urgent items."
```

### ROI Calculation

| Item | Manual Email | Hermes Email |
|------|-------------|--------------|
| Daily email time | 2.5 hours | 30 minutes |
| Urgent emails missed | 10% | 0% |
| Response time (avg) | 4 hours | 30 minutes |
| **Daily time saved** | — | **2 hours** |
| **Monthly value (at $75/hr)** | — | **$3,000** |

**Monthly savings: ~$3,000** · Time saved: 2 hrs/day · Urgent miss rate: 0%

💡 **Tip:** Configure himalaya with `himalaya account configure` to connect your email via IMAP/SMTP. Hermes reads, categorizes, and can draft replies — you just review and approve.

---

## 9.10 Lead Generation & Market Intelligence

Speed-to-lead is the #1 predictor of conversion. A lead responded to in 5 minutes converts 21x more than one contacted after 30 minutes. Hermes responds in 30 seconds.

### The Architecture

```mermaid
flowchart TD
    subgraph Engine["Lead Generation Engine"]
        Browser["Browser Cron"] --> Scrape["Scrape Leads\n\nSkills:\n• browse\n• search"]
        Webhook["Webhook\n(form)"] --> Scrape
        Scrape --> Qualify["Qualify\n\n• Score\n• Enrich\n• Route"]
        Qualify --> Respond["Auto-respond\n→ Telegram"]
    end
```

### Setup

```bash
# Daily lead scraping (e.g., job boards, directories)
hermes cron create "0 8 * * *" \
  --name "lead-scrape" \
  --skills browser,search,terminal \
  --deliver telegram \
  --prompt "Search for companies matching our ideal customer profile:
    • Industry: [your industry]
    • Size: 10-200 employees
    • Location: [your region]
    • Hiring signals: job posts for [relevant role]
    
    For each lead found:
    1. Company name, website, size
    2. Key contact (LinkedIn if possible)
    3. Pain points (inferred from hiring/posts)
    4. Lead score (1-10)
    5. Suggested outreach message
    
    Save to ~/leads/$(date).csv and send top 5 to Telegram."

# Instant response to inbound leads
hermes webhook subscribe lead-form \
  --deliver telegram \
  --prompt "A new lead submitted our contact form.
    Qualify them based on:
    • Company size and industry
    • Budget indicated
    • Timeline urgency
    Respond via email within 5 minutes with a personalized message.
    Alert me on Telegram with lead details and score."
```

### ROI Calculation

| Item | Manual Lead Gen | Hermes Lead Gen |
|------|----------------|-----------------|
| Leads researched/day | 5-10 | 50-100 |
| Response time to inbound | 2-4 hours | 30 seconds |
| Lead qualification time | 30 min/lead | 30 sec/lead |
| Conversion rate (5min response) | 8% | 21% |
| Monthly leads generated | 200 | 2,000 |
| **Monthly revenue impact** | — | **+150% pipeline** |

**Pipeline increase: +150%** · Response time: -99.9% · Lead volume: 10x

💡 **Tip:** Combine with the CRM integration. After qualifying, Hermes can auto-create contacts in your CRM (Airtable, Notion, or Google Sheets) with all enrichment data filled in.

---

## Master ROI Summary — All 10 Scenarios

```mermaid
block-beta
    columns 1
    block:title["Total Impact: 10 Hermes Business Use Cases"]:1
    block:stats
        columns 2
        "1. Content Marketing" "$21,000"
        "2. Customer Support" "$5,000"
        "3. Code Review" "$6,200"
        "4. E-Commerce Ops" "$5,950"
        "5. Competitive Intel" "$4,200"
        "6. Freelancer Accel." "$15,000 (revenue gain)"
        "7. SaaS Monitoring" "$14,650"
        "8. Data Analysis" "$4,500"
        "9. Email Management" "$3,000"
        "10. Lead Generation" "+150% pipeline"
    end
    block:totals
        "Total Estimated Value: ~$79,500/month"
        "Hermes API Cost: ~$20–50/month"
        "ROI: 1,590x – 3,975x"
    end
```

### Hermes Cost Breakdown

| Component | Monthly Cost |
|-----------|-------------|
| LLM API calls (daily crons) | ~$15-30 |
| LLM API calls (weekly analysis) | ~$5-10 |
| Script-only watchdogs (no_agent) | $0 |
| Hosting (runs on your machine) | $0 |
| **Total** | **$20-50/mo** |

Even at the high end ($50/mo), that's replacing $79,500/mo in labor and lost revenue. The ROI isn't close — it's astronomical.

---

## Choosing Your First Scenario

Don't try all 10 at once. Pick the one with the highest immediate impact:

| Your Situation | Start With | Why |
|----------------|-----------|-----|
| Solo developer | Code Review (9.3) | Saves time immediately, zero setup |
| Content creator | Content Engine (9.1) | Biggest dollar savings |
| Agency / freelancer | Agency Accel (9.6) | Revenue multiplier |
| SaaS founder | Monitoring (9.7) | Prevents costly downtime |
| E-commerce owner | E-Commerce Ops (9.4) | Prevents lost sales |
| Job seeker | Lead Gen (9.10) | Faster applications = more interviews |
| Researcher | Competitive Intel (9.5) | Knowledge advantage |

Pick one. Set it up this week. Measure the results. Then add the next one.

---

## Chapter 9 Key Vocabulary

| Term | Definition |
|------|-----------|
| **ROI** | Return on Investment — the dollar value gained vs cost spent |
| **no_agent** | Script-only cron mode — runs without LLM, zero token cost |
| **context_from** | Cron job chaining — output of Job A feeds into Job B |
| **Lead score** | A 1-10 rating of how qualified a potential customer is |
| **Watchdog** | A script that monitors something and alerts on failure |
| **Auto-remediation** | Automatically fixing a problem when detected (e.g., restarting a service) |
| **Triage** | Sorting items by priority — in email, sorting by urgent/reply/FYI/spam |
| **Pipeline** | The total value of all potential deals/leads in progress |

## Chapter 9 Summary

| Scenario | Key Takeaway |
|----------|-------------|
| 9.1 Content Marketing | $21K/mo saved — cron + blog + humanizer skills |
| 9.2 Customer Support | 24/7 coverage with gateway + custom FAQ skill |
| 9.3 Code Review | Webhook-triggered PR review, $6K/mo saved |
| 9.4 E-Commerce Ops | Script-only price watches (free) + inventory alerts |
| 9.5 Competitive Intel | Daily digests from blogs + arXiv, 3x coverage |
| 9.6 Freelancer Accel | Profiles per client, parallel delegation, 3x throughput |
| 9.7 SaaS Monitoring | 30-second detection, auto-restart, $14K/mo saved |
| 9.8 Data Analysis | Jupyter + pandas, weekly automated reports |
| 9.9 Email Management | Himalaya IMAP triage, 2 hrs/day saved |
| 9.10 Lead Generation | Auto-respond in 30 sec, 21x conversion boost |

**Progress: Chapter 9 complete.** Next up: **Chapter 10 — Building a Business Around Hermes** — cost analysis, pricing your services, white-labeling, and scaling.

---

*Previous: [Chapter 8 — Power Techniques](ch08-power-techniques.md) · Next: [Chapter 10 — Building a Business Around Hermes](ch10-business-around-hermes.md)*


---

# Chapter 10: Building a Business Around Hermes — Costs, Pricing, and Scaling

> **You've seen what Hermes can do. Now learn how to turn it into revenue — whether you're a freelancer pricing AI services, an agency scaling with automation, or an entrepreneur building a product on top of Hermes. This chapter covers every dollar, every model, every scale strategy.**

---

## 10.1 Cost Analysis — What Hermes Actually Costs

Before you price your services, you need to know your costs. Every Hermes invocation has a price tag. Let's break it down.

### The Token Economics

Every time Hermes thinks, it consumes tokens. Here's what that means in dollars:

```mermaid
flowchart TD
    subgraph TokenFlow["Token Flow — Every Hermes Turn"]
        Input["System prompt → ~2,000–8,000 tokens (input)\n+ User message (input)\n+ Tool definitions (input)\n+ Skill content (input)\n+ Memory (input)"]
        Input --> Total["= Total input tokens"]
        Total --> LLM["LLM processes → reasoning tokens (hidden)"]
        LLM --> Output["Response → ~500–3,000 tokens (output)\n+ Tool calls (output)"]
        Output --> Cost["Cost = (input × $in) + (output × $out)"]
    end
```

### Model Pricing Comparison

| Model | Input ($/M tokens) | Output ($/M tokens) | Best For |
|-------|--------------------|---------------------|----------|
| deepseek/deepseek-chat | $0.14 | $0.28 | Daily crons, bulk work |
| google/gemini-2.0-flash | $0.10 | $0.40 | Fast, cheap tasks |
| openai/gpt-4o-mini | $0.15 | $0.60 | Balanced daily use |
| anthropic/claude-haiku-4 | $0.80 | $4.00 | Quality daily work |
| openai/gpt-4o | $2.50 | $10.00 | Complex analysis |
| anthropic/claude-sonnet-4 | $3.00 | $15.00 | Architecture, review |
| openai/gpt-5.4-mini | $0.60 | $2.40 | Good middle ground |

### Real-World Monthly Cost Scenarios

| Usage Pattern | Model | Monthly API Cost |
|---------------|-------|------------------|
| Light: 20 messages/day | deepseek-chat | ~$2-5 |
| Light: 20 messages/day | claude-sonnet-4 | ~$30-60 |
| Medium: 5 crons + 50 msgs/day | gpt-4o-mini | ~$15-30 |
| Medium: 5 crons + 50 msgs/day | claude-sonnet-4 | ~$80-150 |
| Heavy: 10 crons + 100 msgs/day | deepseek-chat | ~$20-40 |
| Heavy: 10 crons + 100 msgs/day | gpt-4o | ~$100-250 |
| Agency: 20 crons + 200 msgs/day | deepseek-chat | ~$40-80 |
| Agency: 20 crons + 200 msgs/day | claude-sonnet-4 | ~$300-600 |

💡 **Tip:** The cheapest model that does the job is the right model. Use DeepSeek for bulk crons and GPT-4o-mini for daily chat. Reserve Claude Sonnet for complex architecture decisions only.

### Break-Even Analysis

When does Hermes pay for itself?

```mermaid
block-beta
    columns 1
    block:title["Break-Even Points"]:1
    block:rows
        columns 3
        "Content writer" "$20/mo (API)" "$3,000/mo human → break-even: Day 1"
        "Support agent" "$30/mo (API)" "$2,500/mo human → break-even: Day 1"
        "Data analyst" "$40/mo (API)" "$4,500/mo human → break-even: Day 1"
        "Monitoring tool" "$0 (scripts)" "$150/mo SaaS → break-even: Day 1"
        "Full-time dev" "$200/mo (API)" "$8,000/mo human → break-even: Day 1"
    end
    block:conclusion
        "Conclusion: Hermes ALWAYS pays for itself."
        "The question isn't \"should I?\" — it's \"how much should I spend?\""
    end
```

---

## 10.2 Pricing Your AI-Powered Services

You've automated your workflow. Now sell it. Here's how to price AI-powered services for profit.

### Pricing Models

```mermaid
flowchart LR
    subgraph Pricing["Four Pricing Models"]
        subgraph M1["1. Retainer"]
            R1["$2–5K/mo"]
            R2["Ongoing monitoring,\nreports, support"]
        end
        subgraph M2["2. Per-Deliverable"]
            P1["$200–500 ea"]
            P2["Per article\nPer review\nPer audit\nPer analysis"]
        end
        subgraph M3["3. Value-Based"]
            V1["% of savings"]
            V2["\"I saved you $10K/mo,\nmy fee is $2K/mo\""]
        end
        subgraph M4["4. White-Label"]
            W1["$500–2K/mo"]
            W2["Hermes as your\ncompany AI assistant\n(hosted)"]
        end
    end
```

### Pricing by Service Type

| Service | Your Cost (API) | Price to Client | Margin |
|---------|-----------------|-----------------|--------|
| Blog article (SEO, 2000 words) | $0.05 | $200-500 | 99.9% |
| Daily social media (5 posts) | $0.10/day | $500/mo | 99% |
| Weekly analytics report | $0.50 | $500-1,000/mo | 99% |
| PR code review (per PR) | $0.02 | $50-100 | 99.9% |
| 24/7 customer support chatbot | $30/mo | $1,000-3,000/mo | 97-99% |
| Competitive intelligence weekly | $1/mo | $500-1,500/mo | 99% |
| Full monitoring + alerting | $0 (scripts) | $500-1,000/mo | 100% |
| Lead qualification pipeline | $5/mo | $1,000-2,000/mo | 99% |

### The Profit Formula

```
Revenue = Clients × Services × Price
Cost    = API calls + Your time (setup + maintenance)
Profit  = Revenue - Cost

Example agency setup:
  5 clients × 3 services × $500 avg = $7,500/mo revenue
  API costs: ~$100/mo
  Your time: ~10 hrs/mo (setup + monitoring)
  Profit: $7,400/mo at $740/hr effective rate
```

💡 **Tip:** Never price based on your API cost. Price based on the **value delivered**. A blog article that generates $5,000 in sales is worth $500 regardless of whether it cost you $0.05 or $50 to produce.

---

## 10.3 Building Reusable Skill Packages to Sell

Skills aren't just for your own use. Package them as products.

### What Makes a Sellable Skill

A sellable skill solves a specific, painful, expensive problem:

```mermaid
block-beta
    columns 1
    block:title["Sellable Skill Checklist"]:1
    block:good["✅ Must Have"]
        "✅ Solves a specific pain point"
        "✅ Saves 5+ hours per week"
        "✅ Works out of the box (minimal config)"
        "✅ Has clear ROI the client can measure"
        "✅ Doesn't require technical knowledge to use"
        "✅ Can be demonstrated in 5 minutes"
    end
    block:bad["❌ Red Flags"]
        "❌ Generic (e.g., \"write better code\")"
        "❌ Requires custom setup per client"
        "❌ Vague ROI (\"saves time\")"
        "❌ Needs a developer to operate"
    end
```

### Example: The "Auto-SEO Blog" Skill Package

```bash
# What the client gets:
~/skills/auto-seo-blog/
├── SKILL.md              # Core skill logic
├── templates/
│   ├── article.md        # Article template
│   ├── meta-tags.md      # SEO meta template
│   └── social-snippets.md # Cross-post templates
├── scripts/
│   ├── publish.sh        # Auto-publish script
│   └── analytics.sh      # Track performance
└── references/
    ├── style-guide.md    # Brand voice guide
    └── keyword-strategy.md # SEO keywords
```

### How to Package It

```bash
# 1. Build the skill locally
hermes skills create auto-seo-blog

# 2. Test it thoroughly on your own content first

# 3. Document the ROI
# "This skill generates 2 SEO-optimized articles/day.
#  At $200/article market rate, that's $12,000/mo value.
#  API cost: $3/mo."

# 4. Publish to skills hub
hermes skills publish auto-seo-blog

# 5. Or sell directly as a package
# Bundle: skill + setup + 1 month support = $500-2,000
```

### Skill Package Pricing

| Package | Includes | Price |
|---------|----------|-------|
| Basic skill | SKILL.md + templates | $100-300 |
| Pro package | Skill + scripts + references | $300-800 |
| Enterprise | Pro package + setup + 3 months support | $1,000-3,000 |
| Custom build | Bespoke skill built for client's workflow | $2,000-10,000 |

💡 **Tip:** The best marketing is a live demo. Set up the skill on a prospect's Hermes instance, run it in front of them, and show the results in real-time. The ROI sells itself.

---

## 10.4 White-Labeling Hermes for Clients

You don't sell "Hermes." You sell "Your AI Assistant." The client never needs to know what's under the hood.

### The White-Label Architecture

```mermaid
flowchart TD
    subgraph WhiteLabel["White-Label Setup"]
        subgraph ClientView["Client Sees"]
            Bot["\"Acme Corp AI Assistant\"\n(Telegram bot with their\nbranding, name, avatar)"]
        end
        Bot --> Managed["You Manage"]
        subgraph Managed["You Manage"]
            Profile["Hermes Profile: acme-corp\n• Custom skills (FAQ, etc.)\n• Company knowledge base\n• Approved actions only\n• Memory scoped to Acme\n• Your API key (not theirs)"]
        end
    end

    Finances["Client pays: $1,000–3,000/mo\nYour cost: $30–100/mo (API)\nYour margin: 90–97%"]
```

### Setup Steps

```bash
# 1. Create an isolated profile for the client
hermes profile create acme-corp

# 2. Configure with scoped skills and knowledge
hermes -p acme-corp skills create acme-support
# Build the FAQ skill with their support docs

# 3. Set up their Telegram bot
# Create a new bot via @BotFather with their branding
# Configure the gateway to use this bot for acme-corp profile

# 4. Lock down permissions
hermes -p acme-corp config set approvals.mode strict
hermes -p acme-corp config set privacy.redact_pii true
hermes -p acme-corp config set tools.enabled "terminal,file,browser,search"

# 5. Pre-load company knowledge into memory
hermes -p acme-corp memory add \
  "Acme Corp sells widgets. Support email: support@acme.com.
   Refund policy: 30 days. Shipping: 3-5 business days.
   API docs at docs.acme.com"

# 6. Start the gateway
hermes -p acme-corp gateway run
```

### Client Onboarding Checklist

- [ ] Create client profile with `--clone`
- [ ] Create branded Telegram bot via BotFather
- [ ] Build custom FAQ skill from their support docs
- [ ] Load company knowledge into profile memory
- [ ] Configure approval mode (`strict` for new clients)
- [ ] Enable PII redaction
- [ ] Set up monitoring cron (health check on their gateway)
- [ ] Test with 20 real support questions
- [ ] Hand over the Telegram bot link to client
- [ ] Schedule weekly review of unanswered questions

### White-Label Pricing Tiers

| Tier | Features | Price/mo |
|------|----------|----------|
| Starter | FAQ bot (50 Q&As), Telegram only | $500-800 |
| Professional | Full support + email triage + reports | $1,000-2,000 |
| Enterprise | Custom skills + monitoring + Slack + WhatsApp | $2,000-5,000 |
| Managed | Full operations — you handle everything | $3,000-10,000 |

💡 **Tip:** Start clients on the Starter tier. Let them see results for 2 weeks, then upsell to Professional. The upgrade pays for itself when they see the weekly analytics report showing how many support tickets Hermes handled.

---

## 10.5 Compliance & Data Privacy

When you handle client data, compliance isn't optional. Here's how to stay safe.

### The Privacy Stack

```mermaid
flowchart TD
    subgraph Privacy["Privacy Layers"]
        subgraph L1["Layer 1: PII Redaction (automatic)"]
            P1["Hermes strips: emails, phones, SSNs,\ncredit cards, addresses BEFORE sending\nto the LLM API"]
        end
        subgraph L2["Layer 2: Memory Scoping (per-profile)"]
            P2["Client A's data stays in Client A's\nprofile memory. Never shared."]
        end
        subgraph L3["Layer 3: Local Models (for sensitive data)"]
            P3["Run llama.cpp locally. Zero data leaves\nyour machine. Full GDPR compliance."]
        end
        subgraph L4["Layer 4: Approval Mode (human-in-the-loop)"]
            P4["Sensitive actions require your approval\nbefore execution."]
        end
    end
```

### Configuration

```bash
# Enable all privacy layers
hermes config set privacy.redact_pii true          # Layer 1
hermes config set privacy.redact_patterns          # Custom patterns
  "email,phone,ssn,credit_card,iban,ip_address"

# Profile isolation is automatic (Layer 2)
# Each profile has its own memory, sessions, and skills

# Local model for sensitive clients (Layer 3)
hermes config set providers.local.type llama-cpp
hermes config set providers.local.model ~/models/llama-3-8b-q4_k_m.gguf

# Approval mode (Layer 4)
hermes config set approvals.mode strict
# Options: off (YOLO), smart (auto-approve low-risk), strict (ask always)
```

### GDPR Compliance Checklist

- [ ] PII redaction enabled on all profiles
- [ ] Client data isolated per profile (no cross-contamination)
- [ ] Session data stored locally (not in cloud)
- [ ] LLM provider has data processing agreement (DPA)
- [ ] Client can request data deletion (`hermes profile delete`)
- [ ] Audit trail enabled (`hermes config set audit.enabled true`)
- [ ] Local model option available for high-sensitivity clients
- [ ] Memory export available for data portability requests

### When to Use Local Models

| Scenario | Cloud Model | Local Model |
|----------|-------------|-------------|
| Public content (blog, social) | ✅ | — |
| Internal analytics | ✅ | ⚠️ (if data is sensitive) |
| Customer PII (names, emails) | ⚠️ (with redaction) | ✅ |
| Financial data (transactions) | ❌ | ✅ |
| Healthcare/medical data | ❌ | ✅ |
| Legal documents | ❌ | ✅ |
| Government/classified | ❌ | ✅ |

💡 **Tip:** For clients with strict compliance requirements, run a local model via `llama-cpp` skill. Zero data leaves their infrastructure. Slower, but bulletproof for GDPR, HIPAA, and SOC2.

---

## 10.6 Scaling — The Multi-Profile Agency

You have 10 clients. Each has their own Hermes profile, skills, and crons. You need a system to manage it all without drowning.

### The Agency Architecture

```mermaid
flowchart TD
    subgraph Agency["Agency Setup — Managing 10+ Clients"]
        subgraph Master["Master Profile (you)"]
            M1["• Monitors all client profiles"]
            M2["• Weekly agency dashboard cron"]
            M3["• Cost tracking across profiles"]
        end
        Master --> A
        Master --> B
        Master --> C
        subgraph A["Client A Profile"]
            A1["Skills: support, faq-a"]
            A2["Cron: 24/7 support"]
        end
        subgraph B["Client B Profile"]
            B1["Skills: blog, seo"]
            B2["Cron: 2x/day article"]
        end
        subgraph C["Client C Profile × 10"]
            C1["Skills: monitor, health"]
            C2["Cron: 1/min watchdog"]
        end
        subgraph Report["Weekly Agency Report (cron)"]
            R1["• Total API cost per client"]
            R2["• Issues/escalations per client"]
            R3["• Uptime stats"]
            R4["• Revenue vs cost per client"]
        end
    end
```

### Setup Script

```bash
#!/bin/bash
# agency-setup.sh — bootstrap a new client in 5 minutes

CLIENT_NAME=$1
CLIENT_INDUSTRY=$2

if [ -z "$CLIENT_NAME" ]; then
  echo "Usage: ./agency-setup.sh <client-name> <industry>"
  exit 1
fi

echo "Setting up $CLIENT_NAME..."

# 1. Create profile
hermes profile create "$CLIENT_NAME" --clone

# 2. Create client directory
mkdir -p ~/clients/$CLIENT_NAME/{skills,reports,leads}

# 3. Copy industry-specific skill template
cp -r ~/.hermes/skills/templates/$CLIENT_INDUSTRY/* \
      ~/.hermes/profiles/$CLIENT_NAME/skills/

# 4. Set up monitoring cron
hermes cron create "*/5 * * * *" \
  --profile "$CLIENT_NAME" \
  --name "$CLIENT_NAME-monitor" \
  --script ~/clients/$CLIENT_NAME/scripts/monitor.sh \
  --no-agent \
  --deliver telegram

# 5. Set up weekly report
hermes cron create "0 9 * * 1" \
  --profile "$CLIENT_NAME" \
  --name "$CLIENT_NAME-weekly" \
  --deliver telegram \
  --prompt "Generate weekly report for $CLIENT_NAME.
    Include: API costs, issues handled, uptime, suggestions."

echo "✅ $CLIENT_NAME profile created and crons active."
echo "Next: customize skills and load knowledge base."
```

### Cost Tracking

```bash
# Add to your master profile cron — track costs across all clients
hermes cron create "0 8 * * 1" \
  --name "agency-costs" \
  --skills terminal,file \
  --deliver telegram \
  --prompt "Generate the weekly agency cost report.
    For each client profile, check:
    1. API token usage (from logs)
    2. Cron execution count
    3. Errors and escalations
    
    Format as a table:
    Client | API Cost | Revenue | Margin | Issues
    
    Flag any client where margin drops below 80%."
```

### Scaling Limits

| Clients | API Cost/mo | Your Time/mo | Revenue/mo | Profit/mo |
|---------|-------------|--------------|------------|-----------|
| 1-3 | $50-150 | 5 hrs | $2,000-6,000 | $1,850-5,850 |
| 4-10 | $150-500 | 15 hrs | $8,000-20,000 | $7,500-19,500 |
| 10-20 | $500-1,000 | 25 hrs | $20,000-50,000 | $19,000-49,000 |
| 20+ | $1,000+ | 40+ hrs | $50,000+ | Need VA/helper |

💡 **Tip:** At 20+ clients, hire a virtual assistant to handle first-line support and client communication. You focus on building skills and onboarding. Hermes handles the automation. The VA handles the humans.

---

## 10.7 Future-Proofing — Local Models & Edge Deployment

API costs will fluctuate. Providers will change pricing. The only hedge? Local models that you control completely.

### The Local Model Stack

```mermaid
block-beta
    columns 1
    block:title["Local Model Options"]:1
    block:opt1["llama.cpp (recommended)"]
        "• Runs on CPU, no GPU needed"
        "• Supports GGUF format"
        "• 2–50 tok/s depending on model size"
        "• Full offline capability"
    end
    block:opt2["Ollama (easiest setup)"]
        "• One-command install"
        "• Automatic model management"
        "• OpenAI-compatible API server"
    end
    block:opt3["vLLM (highest performance)"]
        "• Requires GPU"
        "• Production-grade serving"
        "• Best for high-throughput agency use"
    end
```

### Setting Up llama.cpp with Hermes

```bash
# 1. Install llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make

# 2. Download a model (example: Llama 3 8B quantized)
# From huggingface.co — search for "llama 3 8b gguf q4_k_m"
# Save to ~/models/

# 3. Configure Hermes to use local model
hermes config set providers.local.type llama-cpp
hermes config set providers.local.model ~/models/llama-3-8b-q4_k_m.gguf
hermes config set providers.local.context_size 4096

# 4. Switch to local model for specific tasks
hermes -m local "Summarize this document"   # Free, private
hermes -m deepseek/deepseek-chat "..."       # Cloud, smarter
```

### Hybrid Strategy: Cloud + Local

```mermaid
block-beta
    columns 2
    block:local["LOCAL (free, private, slower)"]
        "• Email triage and categorization"
        "• Document summarization"
        "• Data extraction and formatting"
        "• Watchdog alert evaluation"
        "• PII-heavy tasks"
    end
    block:cloud["CLOUD (paid, smart, fast)"]
        "• Content creation (needs quality)"
        "• Architecture decisions"
        "• Code review (needs reasoning)"
        "• Client-facing responses"
        "• Complex data analysis"
    end
    block:rule["Rule"]:2
        "If it touches client output → cloud.\nIf it's internal processing → local."
    end
```

### Edge Deployment — Hermes on a Phone

Yes, you can run a local LLM on your phone and Hermes can connect to it:

```bash
# On Android (Termux):
pkg install llama-cpp
# Download model (Q4 quantized for mobile)
llama-cli -m ~/models/gemma-2b-q4.gguf -c 2048 --host 0.0.0.0 --port 8080

# Configure Hermes to use your phone as provider
hermes config set providers.phone.type openai-compatible
hermes config set providers.phone.base_url http://192.168.1.100:8080/v1
```

💡 **Tip:** A 2B-parameter model at Q4 quantization runs at 15-25 tokens/second on a modern phone (Snapdragon 8 Gen 3, Exynos 1580). Not fast enough for complex tasks, but perfect for simple triage and categorization — and completely free.

---

## The Business of Hermes — Decision Framework

```mermaid
block-beta
    columns 1
    block:title["Should You Build a Business Around Hermes?"]:1
    block:yes["YES, if you:"]
        "• Already use Hermes daily"
        "• Have 3+ skills you built for yourself"
        "• Know businesses that waste time on manual work"
        "• Can explain AI value in plain language"
    end
    block:start["START HERE:"]
        "1. Pick ONE service (Chapter 9 scenarios)"
        "2. Build it for yourself first (dogfood it)"
        "3. Find 1 client who needs it"
        "4. Deliver results, measure ROI"
        "5. Use that case study to get 3 more clients"
        "6. Systematize with profiles and crons"
        "7. Hire VA when you hit 20 clients"
    end
    block:dont["DON'T:"]
        "• Build the agency before having clients"
        "• Over-promise what Hermes can do"
        "• Ignore compliance (GDPR, PII)"
        "• Price based on your cost (price on value)"
        "• Scale before the system is stable"
    end
```

---

## Chapter 10 Key Vocabulary

| Term | Definition |
|------|-----------|
| **White-label** | Selling a product under your brand that's built on another platform |
| **Retainer** | Monthly fee for ongoing services |
| **Value-based pricing** | Charging based on the outcome delivered, not hours spent |
| **PII** | Personally Identifiable Information — names, emails, phone numbers |
| **GDPR** | General Data Protection Regulation — EU data privacy law |
| **GGUF** | Model format for llama.cpp — quantized for efficient CPU inference |
| **Edge deployment** | Running models on local/endpoint devices instead of cloud |
| **Margin** | Revenue minus costs — your actual profit percentage |
| **Break-even** | The point where revenue covers all costs |
| **Dogfooding** | Using your own product before selling it to others |

## Chapter 10 Summary

| Topic | What You Learned |
|-------|-----------------|
| 10.1 Cost Analysis | Real API costs per model — $2/mo (DeepSeek) to $600/mo (Claude heavy) |
| 10.2 Pricing | Four pricing models — retainer, per-deliverable, value-based, white-label |
| 10.3 Skill Packages | How to package and sell reusable skills at $100-$10,000 |
| 10.4 White-Labeling | Profile-per-client setup — 90-97% margins at $500-$10K/mo |
| 10.5 Compliance | PII redaction, memory scoping, local models, GDPR checklist |
| 10.6 Scaling | Agency architecture for 10-20 clients — $19K-$49K/mo profit |
| 10.7 Future-Proofing | Hybrid cloud + local strategy, edge deployment, phone-based LLMs |

**Progress: Chapter 10 complete. All 10 chapters done.** 🎉

You've gone from zero to building a business around Hermes. The appendices cover reference material — CLI commands, provider configs, troubleshooting, and the full skills catalog.

---

*Previous: [Chapter 9 — Real Business Use Cases](ch09-business-use-cases.md) · Next: [Appendix A — CLI Reference →](appendix-a-cli-reference.md)*


---


# Chapter 3: Messaging Gateway — AI Everywhere

> **Your AI agent shouldn't live in a terminal. The gateway connects Hermes to Telegram, Discord, Slack, and 10+ platforms — full tools, full memory, everywhere you chat.**

---

## 3.1 What is the Gateway?

The **gateway** is a long-running background process that connects your Hermes agent to messaging platforms. It's the bridge between your chat apps and the AI brain:

```
┌─────────────────────────────────────────────────────────────┐
│                    GATEWAY ARCHITECTURE                      │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Telegram  │  │ Discord  │  │  Slack   │  │ WhatsApp │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       │              │              │              │         │
│       └──────────────┴──────────────┴──────────────┘        │
│                          │                                   │
│                          ▼                                   │
│                 ┌─────────────────┐                          │
│                 │     GATEWAY     │  Routes messages         │
│                 │   (Scheduler)   │  Manages sessions        │
│                 │                 │  Handles platform auth   │
│                 └────────┬────────┘                          │
│                          │                                   │
│                          ▼                                   │
│                 ┌─────────────────┐                          │
│                 │   AGENT LOOP    │  Same brain              │
│                 │                 │  Same memory              │
│                 │                 │  Same tools               │
│                 └─────────────────┘                          │
│                                                             │
│  One session per conversation — switch platforms freely.    │
└─────────────────────────────────────────────────────────────┘
```

**Key insight:** The gateway doesn't create a separate Hermes — it connects your existing agent to messaging platforms. Same memory, same tools, same sessions. Start a conversation on Telegram, continue on CLI — it's one agent.

### Supported Platforms

```
┌────────────────────────────────────────────────────────────┐
│               SUPPORTED MESSAGING PLATFORMS                 │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  💬 Chat Apps          🏢 Business         📱 Other        │
│  • Telegram            • Slack             • Signal        │
│  • Discord             • Microsoft Teams   • Matrix        │
│  • WhatsApp            • DingTalk          • Mattermost    │
│  • WeChat (Weixin)     • Feishu (Lark)     • SMS           │
│  • iMessage*           • WeCom             • Email         │
│                                                            │
│  🏠 Smart Home          🔌 Integrations                    │
│  • Home Assistant       • API Server (REST)                │
│                         • Webhooks                         │
│                         • Open WebUI                       │
│                                                            │
│  * via BlueBubbles (requires Mac)                          │
└────────────────────────────────────────────────────────────┘
```

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

```
┌──────────────────────────────────────────┐
│           VOICE TRANSCRIPTION FLOW        │
│                                          │
│  🎤 Voice message                        │
│       │                                  │
│       ▼                                  │
│  STT Provider (priority order):          │
│  1. Local faster-whisper  (free)         │
│  2. Groq Whisper          (free tier)    │
│  3. OpenAI Whisper        (paid)         │
│  4. Mistral Voxtral       (paid)         │
│       │                                  │
│       ▼                                  │
│  Transcribed text → Agent loop → Response │
└──────────────────────────────────────────┘
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

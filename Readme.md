# 🎙️ Vibe Talker Voice Coding Agent

> Code at the speed of thought. **Vibe Talker** is an AI-powered voice coding agent that lets you build, refactor, and navigate your codebase entirely through natural voice commands. 

---

## 🚀 Features

- **🗣️ Real-Time Voice-to-Code:** Seamless speech recognition powered by state-of-the-art STT models (e.g., OpenAI Whisper).
- **🤖 Agentic Code Execution:** Not just transcription—an autonomous coding agent that understands context, modifies files, runs shell commands, and debugs errors.
- **⚡ Natural "Vibe" Conversations:** Speak naturally without needing rigid syntax or keyword commands; the agent interprets your intent and asks clarifying questions when needed.
- **🔌 IDE & Terminal Integration:** Works directly within your terminal or local development workflow.
- **⚙️ Multi-Model Support:** Plug-and-play support for leading LLMs (OpenAI GPT-4o, Anthropic Claude 3.5 Sonnet, Local Models via Ollama).

---

## 📐 Architecture & Workflow

```text
[ Your Voice ] ──> [ Audio Capture (Sounddevice) ] 
                       │
                       ▼
             [ Whisper STT Model ] 
                       │
                       ▼
             [ Intent & Context Parser ] 
                       │
                       ▼
             [ Coding Agent Loop (LLM) ] 
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
[ File Modifications ]      [ Terminal Execution ]
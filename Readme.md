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
```
🛠️ Tech Stack
Core Language: Python 3.10+

Speech-to-Text: OpenAI Whisper / faster-whisper

Agent Framework: Custom Agent Loop / LangChain

Audio Processing: sounddevice, numpy, scipy

LLM Providers: OpenAI API, Anthropic API, or local Ollama instances

📦 Installation & Setup
Prerequisites
Make sure you have Python 3.10 or higher installed on your system. You will also need a microphone and audio drivers configured.

1. Clone the Repository
```text
git clone [https://github.com/sunova200/vibe-talker-voice-coding-agent.git](https://github.com/sunova200/vibe-talker-voice-coding-agent.git)
cd vibe-talker-voice-coding-agent
```
2. Create a Virtual Environment
```text
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```text
pip install -r requirements.txt
```
4. Configure Environment Variables
Create a .env file in the root directory and add your API keys:
```text
OPENAI_API_KEY=your_openai_api_key_here
# Optional: ANTHROPIC_API_KEY=your_anthropic_key_here
WHISPER_MODEL_SIZE=base
```
🕹️ Usage
Run the voice coding agent from your terminal:
```text
python main.py
```
Once started, simply start speaking to your codebase:

"Create a new FastAPI endpoint for user authentication."

"Refactor the database connection logic in db.py to use connection pooling."

"Run the pytest suite and fix any failing tests."
📂 Project Structure
```text
vibe-talker-voice-coding-agent/
├── agent/
│   ├── __init__.py
│   ├── core_loop.py       # Main agent reasoning and execution loop
│   ├── tools.py           # File system and shell execution tools
│   └── prompts.py         # System prompts for code generation
├── audio/
│   ├── recorder.py        # Audio capture utilities
│   └── transcriber.py     # Whisper integration
├── .env.example           # Template for environment variables
├── requirements.txt       # Python dependencies
├── main.py                # Entry point
└── README.md
```
🗺️ Roadmap
[] Support for local STT models for offline voice coding

[] VS Code Extension wrapper for inline voice commands

[] Streaming audio feedback & text-to-speech responses

[] Multi-file workspace memory indexing

   🤝 Contributing
    Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, new features, or performance improvements.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingVoiceFeature)

Commit your Changes (git commit -m 'Add some AmazingVoiceFeature')

Push to the Branch (git origin push feature/AmazingVoiceFeature)

Open a Pull Request
📄 License
Distributed under the MIT License. See LICENSE for more information.



   


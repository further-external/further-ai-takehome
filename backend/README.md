# Further — AI Engineer Take-Home

Welcome! This repo is your starting point for the Further AI Engineer take-home assignment.

A starter agent is included to verify your environment works. Replace it with your own.

## Quick Start

### 1. Prerequisites

- Python 3.13
- A [LangSmith](https://smith.langchain.com/) account (free) — go to **Settings → API Keys** to create one

### 2. Set up environment

```bash
cp .env.example .env
# Fill in your LANGSMITH_API_KEY and GOOGLE_API_KEY
```

### 3. Install dependencies

```bash
pip install --no-cache-dir uv
uv sync --active --locked --all-extras --dev
```

### 4. Run the LangGraph dev server

```bash
langgraph dev
```

### 5. Open LangGraph Studio

Once the server is running, open:

https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

You should see the starter agent. Send it a message to confirm everything works, then start building!

## Repo Structure

```
├── agents/
│   ├── models.py          # Model configuration (defaults to Gemini)
│   └── basic/
│       └── graph.py       # Starter agent — replace with your own
├── langgraph.json         # LangGraph server config
├── pyproject.toml         # Python dependencies
├── .env.example           # Environment variable template
└── README.md
```

## Tips

- **Add dependencies** as needed with `uv add <package>`
- **Multiple agents?** Add new graph files and register them in `langgraph.json`
- **Using a different model provider?** Uncomment the relevant lines in `pyproject.toml` and `agents/models.py`
- **Document your thinking** — if you run out of time, write down what you'd do next and why

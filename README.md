# EarlySignal 🔍

## Demo

https://github.com/user-attachments/assets/69c7603e-8cd3-4878-b79a-9163dd86d21b

> Spot what's going mainstream **before** it does.

**Live app → [earlysignal.streamlit.app](https://earlysignal.streamlit.app)**

EarlySignal is an agentic AI trend intelligence tool that scans niche corners of the internet — subreddits, underground communities, early-adopter forums — and surfaces emerging market signals before they hit mainstream media.

---

## What makes it different

- **Google Trends** shows you what's already mainstream
- **EarlySignal** shows you what Google Trends will show in 6 months
- Enterprise tools (WGSN, Trendalytics) cost $30K+/year — this is free to use

---

## How it works

Claude uses **native tool use (agentic search)** — it autonomously decides what to search, which communities to scan, and what's worth surfacing. No pre-stored database. No pipeline. Just real-time AI reasoning.

## Tech stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app + deployment |
| Claude API (Haiku) | Agentic search + signal extraction |
| Tavily API | Real-time web search |
| Reddit API | Niche community scanning |

## Run locally

```bash
git clone https://github.com/enriquehernandezit-oss/early-signal-easy.git
cd early-signal-easy
conda create -n earlysignal python=3.11
conda activate earlysignal
pip install -r requirements.txt
```

Create a `.env` file with your API keys, then run:

```bash
streamlit run app.py
```

---

Built by **Enrique C. Hernandez** — [LinkedIn](https://linkedin.com/in/enriquechernandez)


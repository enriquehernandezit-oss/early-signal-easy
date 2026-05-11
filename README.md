# EarlySignal 🔍
**Live app → [earlysignal.streamlit.app](https://earlysignal.streamlit.app)**

## Demo
https://github.com/user-attachments/assets/7d20fff4-69ae-49f7-ab90-b047b866e682

> Spot what's going mainstream **before** it does.

## What it is

EarlySignal is an agentic trend intelligence tool that scans niche corners of the internet — subreddits, underground communities, early-adopter forums — and surfaces emerging market signals before they hit mainstream media.

Most trend tools show you what's already popular. EarlySignal shows you what Google Trends will show in 6 months.

---

## How it works

No pre-stored database. No static pipeline. Claude uses native tool-use to autonomously decide which sources to query, what to search for, and when it has enough information — the full reasoning loop runs in real time on every request.

1. **Web search via Tavily** — Claude calls `search_web` with queries it generates itself, scoped to recent results
2. **Reddit API for community signal** — `search_reddit` sweeps r/all and pivots into specific subreddits when the model decides it's worth it
3. **Structured output** — returns three ranked signals with confidence scores, source attribution, and an opportunity statement per run

---

## Why it's different

| Tool | Cost | Signal type |
|---|---|---|
| Google Trends | Free | Lagging — already mainstream |
| WGSN | ~$30K/yr | Curated — human editorial |
| Trendalytics | ~$40K+/yr | Curated — human editorial |
| **EarlySignal** | **Free** | **Real-time — autonomous AI** |

---

## Tech stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app + deployment |
| Claude API (Haiku) | Agentic loop + signal extraction |
| Tavily API | Real-time web search |
| Reddit API | Niche community scanning |

---

## Run locally

```bash
git clone https://github.com/enriquehernandezit-oss/early-signal-easy.git
cd early-signal-easy
conda create -n earlysignal python=3.11
conda activate earlysignal
pip install -r requirements.txt
```

Create a `.env` file:
ANTHROPIC_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here

Then run:

```bash
streamlit run app.py
```

---

Built by **Enrique C. Hernandez** — [LinkedIn](https://linkedin.com/in/enriquechernandez)


import streamlit as st
import time
import datetime
import json
import os

from agent import run_agent
from style import apply_styles

DAILY_LIMIT = 10


def get_usage():
    usage_file = "usage.json"
    today = str(datetime.date.today())
    if os.path.exists(usage_file):
        with open(usage_file, "r") as f:
            data = json.load(f)
        if data.get("date") == today:
            return data.get("count", 0)
    return 0


def increment_usage():
    usage_file = "usage.json"
    today = str(datetime.date.today())
    count = get_usage() + 1
    with open(usage_file, "w") as f:
        json.dump({"date": today, "count": count}, f)
    return count


st.set_page_config(page_title="EarlySignal", page_icon="🔍", layout="wide")
apply_styles()

usage_now = get_usage()

# ── Top bar ──────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="es-topbar">
      <div class="es-wordmark">
        <span class="es-glyph"><span class="dot"></span></span>
        <span>Early<span class="light">Signal</span></span>
      </div>
      <div class="es-meta">
        <span class="es-live"><span class="es-pulse"></span>Live</span>
        <span class="es-usage"><b>{usage_now}</b> / {DAILY_LIMIT} queries today</span>
        <span>v1.2 · {datetime.date.today().strftime("%b %Y").upper()}</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Masthead — technical framing ─────────────────────────────────────────
st.markdown(
    """
    <div class="es-masthead">
      <div>
        <div class="es-eyebrow">Agentic trend intelligence · <span>built with Claude</span></div>
        <h1 class="es-headline">
          Real-time trend detection<br/>
          <span class="muted">powered by an autonomous AI agent.</span>
        </h1>
      </div>
      <div class="es-deck">
        An agentic system that uses Claude's tool-use API to autonomously query Tavily web search and the Reddit API, then synthesizes three emerging market signals per run.
        <div class="es-stack-tags">
          <span class="t">Python</span>
          <span class="t">Claude API</span>
          <span class="t">Tool use</span>
          <span class="t">Tavily</span>
          <span class="t">Reddit API</span>
          <span class="t">Streamlit</span>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Search row ───────────────────────────────────────────────────────────
st.markdown('<div class="es-search-marker"></div>', unsafe_allow_html=True)
col_input, col_btn = st.columns([5, 1], gap="small", vertical_alignment="bottom")

with col_input:
    industry = st.text_input(
        "industry",
        placeholder="Enter an industry to analyze — e.g. plant-based food, creator economy, agentic AI",
        label_visibility="collapsed",
    )

with col_btn:
    run_button = st.button("Run scan  →", type="primary")

st.markdown(
    """
    <div class="es-examples">
      <span class="label">TRY</span>
      <span class="es-chip">athletic wear</span>
      <span class="es-chip">creator economy</span>
      <span class="es-chip">plant-based food</span>
      <span class="es-chip">fintech for Gen Z</span>
      <span class="es-chip">sustainable packaging</span>
      <span class="es-chip">agentic AI</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Action ───────────────────────────────────────────────────────────────
if run_button and industry:
    if usage_now >= DAILY_LIMIT:
        st.error(f"Daily limit of {DAILY_LIMIT} queries reached. Come back tomorrow.")
        st.stop()

    brief_no = (hash(industry + str(datetime.date.today())) % 900) + 100
    now_fmt = datetime.datetime.now().strftime("%I:%M %p").lstrip("0")

    with st.status(f"Running agent on '{industry}'…", expanded=True) as status:
        st.write(f"tool_use · search_web('{industry} trends 2026')")
        time.sleep(0.6)
        st.write(f"tool_use · search_reddit('{industry}')")
        time.sleep(0.6)
        st.write("synthesize · rank · return top 3 signals")
        result = run_agent(industry)
        increment_usage()
        status.update(label="Agent complete", state="complete", expanded=False)

    if "error" in result:
        st.error("Something went wrong: " + result.get("error", ""))
        if "raw" in result:
            st.code(result["raw"])
    else:
        signals = result.get("signals", [])

        st.markdown(
            f"""
            <div class="es-section-head">
              <div>
                <span class="es-kicker">Report №{brief_no}</span>
                <span class="es-topic">{industry}</span>
              </div>
              <div class="es-section-right">{len(signals)} signals · {now_fmt}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for i, signal in enumerate(signals):
            title = signal.get("title", "Untitled")
            description = signal.get("description", "")
            where = signal.get("where_its_showing_up", "")
            why = signal.get("why_it_could_be_big", "")
            confidence_raw = str(signal.get("confidence", "0")).replace("%", "").strip()
            try:
                confidence = int(float(confidence_raw))
            except ValueError:
                confidence = 0

            st.markdown(
                f"""
                <article class="es-signal">
                  <div class="es-signal-num">SIG.{str(i + 1).zfill(2)}</div>
                  <div>
                    <h3 class="es-signal-title">{title}</h3>
                    <p class="es-signal-desc">{description}</p>
                    <div class="es-meta-grid">
                      <div>
                        <div class="es-meta-label">Sources</div>
                        <div class="es-meta-value">{where}</div>
                      </div>
                      <div>
                        <div class="es-meta-label">Opportunity</div>
                        <div class="es-meta-value">{why}</div>
                      </div>
                    </div>
                  </div>
                  <aside class="es-side">
                    <div class="es-side-row">
                      <span class="es-side-k">Confidence</span>
                      <span class="es-side-v">{confidence}<span style="font-size:12px;color:var(--text-3);font-weight:400;"> / 100</span></span>
                    </div>
                    <div class="es-conf-bar"><div class="es-conf-fill" style="width:{confidence}%"></div></div>
                    <div class="es-side-row">
                      <span class="es-side-k">Status</span>
                      <span class="es-momentum">Pre-mainstream</span>
                    </div>
                  </aside>
                </article>
                """,
                unsafe_allow_html=True,
            )

elif run_button and not industry:
    st.warning("Please enter an industry first.")

else:
    st.markdown(
        """
        <div class="es-empty">
          <div>
            <h2>How the agent works</h2>
            <p>No pre-stored database, no static pipeline. Claude uses native tool-use to autonomously decide which sources to query and when to stop — the full reasoning loop runs in real time on each request.</p>
            <ol class="es-howsteps">
              <li>
                <div>
                  <div class="h">Web search via Tavily</div>
                  <div class="d">Claude calls the search_web tool with queries it generates itself, scoped to recent results.</div>
                </div>
              </li>
              <li>
                <div>
                  <div class="h">Reddit API for community signal</div>
                  <div class="d">search_reddit tool sweeps r/all and pivots into specific subreddits when the model decides it's worth it.</div>
                </div>
              </li>
              <li>
                <div>
                  <div class="h">Structured JSON output</div>
                  <div class="d">The model returns three ranked signals with confidence scores, source attribution, and an opportunity statement.</div>
                </div>
              </li>
            </ol>
          </div>
          <div class="es-stack-card">
            <div class="label">Comparable tools</div>
            <div class="es-stack">
              <div class="cell"><div class="n">Google Trends</div><div class="r">Lagging · free</div></div>
              <div class="cell"><div class="n">WGSN</div><div class="r">$30k / yr</div></div>
              <div class="cell"><div class="n">Trendalytics</div><div class="r">$40k+ / yr</div></div>
              <div class="cell hi"><div class="n">EarlySignal</div><div class="r">10 / day · free</div></div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="es-footer">
      <div>Built by Enrique C. Hernandez · Claude · Tavily · Reddit API · Streamlit</div>
      <div>EARLYSIGNAL.STREAMLIT.APP</div>
    </div>
    """,
    unsafe_allow_html=True,
)

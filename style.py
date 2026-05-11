import streamlit as st


def apply_styles():
    st.markdown(
        """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">

    <style>
    :root {
        --bg:        #0e0d0c;
        --bg-2:      #141312;
        --surface:   #191817;
        --surface-2: #211f1d;
        --line:      #26241f;
        --line-2:    #353230;
        --text:      #ecebe8;
        --text-2:    #a8a4a0;
        --text-3:    #6e6a66;
        --text-4:    #46433f;

        --accent:    #e8dfd2;
        --accent-bg: rgba(232,223,210,0.06);

        --sans:  "Geist", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        --mono:  "Geist Mono", ui-monospace, "SF Mono", monospace;
    }

    /* ── Base ── */
    html, body, [class*="css"], .stApp, .stMarkdown, .stMarkdown p,
    input, textarea, button {
        font-family: var(--sans) !important;
        background-color: var(--bg);
        color: var(--text);
    }
    .stApp { background-color: var(--bg); }

    #MainMenu, footer, header { visibility: hidden; }

    .block-container {
        padding: 2.5rem 3.5rem 6rem !important;
        max-width: 1180px !important;
    }

    /* ── Top bar ── */
    .es-topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 24px;
        border-bottom: 1px solid var(--line);
    }
    .es-wordmark {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: var(--sans);
        font-size: 18px;
        font-weight: 600;
        letter-spacing: -0.01em;
        color: var(--text);
    }
    .es-wordmark .light { font-weight: 400; color: var(--text-2); }
    .es-glyph {
        width: 14px; height: 14px;
        position: relative;
        display: inline-block;
    }
    .es-glyph::before, .es-glyph::after {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 50%;
        border: 1px solid var(--text-3);
    }
    .es-glyph::after { inset: 4px; border-color: var(--text-4); }
    .es-glyph .dot {
        position: absolute;
        width: 4px; height: 4px;
        border-radius: 50%;
        background: var(--text-2);
        top: 5px; left: 5px;
    }
    .es-meta {
        display: flex;
        gap: 28px;
        align-items: center;
        font-family: var(--mono);
        font-size: 11px;
        color: var(--text-3);
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }
    .es-live {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: var(--text-2);
    }
    .es-pulse {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: var(--text-2);
        animation: es-pulse 2.4s ease-out infinite;
    }
    @keyframes es-pulse {
        0%   { box-shadow: 0 0 0 0 rgba(168,164,160,0.4); }
        70%  { box-shadow: 0 0 0 8px rgba(168,164,160,0); }
        100% { box-shadow: 0 0 0 0 rgba(168,164,160,0); }
    }
    .es-usage b { color: var(--text); font-weight: 500; }

    /* ── Masthead (technical, not poetic) ── */
    .es-masthead {
        padding: 56px 0 40px;
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 64px;
        align-items: end;
        border-bottom: 1px solid var(--line);
    }
    .es-eyebrow {
        font-family: var(--mono);
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: var(--text-3);
        margin-bottom: 24px;
    }
    .es-eyebrow span { color: var(--text-2); }
    .es-headline {
        font-family: var(--sans);
        font-weight: 500;
        font-size: clamp(40px, 4.6vw, 64px);
        line-height: 1.02;
        letter-spacing: -0.025em;
        margin: 0;
        color: var(--text);
    }
    .es-headline .muted { color: var(--text-3); font-weight: 400; }
    .es-deck {
        font-size: 15px;
        line-height: 1.6;
        color: var(--text-2);
        max-width: 380px;
    }
    .es-deck::before {
        content: "";
        display: block;
        width: 28px; height: 1px;
        background: var(--text-3);
        margin-bottom: 20px;
    }
    .es-stack-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 18px;
    }
    .es-stack-tags .t {
        font-family: var(--mono);
        font-size: 10.5px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-3);
        padding: 4px 9px;
        border: 1px solid var(--line);
        border-radius: 4px;
    }

    /* ── Search row ── */
    div[data-testid="stHorizontalBlock"]:has(.es-search-marker) {
        gap: 10px !important;
        align-items: stretch !important;
        margin-top: 36px;
    }

    .stTextInput > div > div {
        background-color: var(--surface) !important;
        border: 1px solid var(--line) !important;
        border-radius: 10px !important;
        padding: 0 !important;
        height: 56px !important;
        display: flex !important;
        align-items: center !important;
        transition: border-color .2s, box-shadow .2s;
    }
    .stTextInput > div > div:focus-within {
        border-color: var(--line-2) !important;
        box-shadow: 0 0 0 3px var(--accent-bg) !important;
    }
    /* Match input and placeholder exactly — same font, same size, same line-height */
    .stTextInput > div > div > input,
    .stTextInput input[type="text"] {
        background: transparent !important;
        border: 0 !important;
        outline: 0 !important;
        font-family: var(--sans) !important;
        font-size: 15px !important;
        font-weight: 400 !important;
        line-height: 1.4 !important;
        color: var(--text) !important;
        padding: 0 18px !important;
        margin: 0 !important;
        letter-spacing: 0 !important;
        height: 100% !important;
        width: 100% !important;
        box-sizing: border-box !important;
        display: flex !important;
        align-items: center !important;
    }
    .stTextInput > div > div > input::placeholder,
    .stTextInput input::placeholder {
        color: var(--text-4) !important;
        font-family: var(--sans) !important;
        font-size: 15px !important;
        font-weight: 400 !important;
        line-height: 1.4 !important;
        opacity: 1 !important;
    }

    /* Button matches input height exactly */
    .stButton { margin-top: 0 !important; }
    .stButton > button {
        background-color: var(--text) !important;
        color: var(--bg) !important;
        border: 1px solid var(--text) !important;
        border-radius: 10px !important;
        font-family: var(--sans) !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        padding: 0 24px !important;
        letter-spacing: 0 !important;
        height: 56px !important;
        width: 100%;
        transition: all .15s !important;
    }
    .stButton > button:hover {
        background-color: var(--accent) !important;
        border-color: var(--accent) !important;
        color: var(--bg) !important;
    }
    .stButton > button:active,
    .stButton > button:focus,
    .stButton > button:focus:not(:active) {
        background-color: var(--text) !important;
        color: var(--bg) !important;
        border-color: var(--text) !important;
        box-shadow: none !important;
    }

    /* ── Example chips ── */
    .es-examples {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        align-items: center;
        margin: 18px 0 8px;
        font-family: var(--mono);
        font-size: 11px;
        color: var(--text-3);
    }
    .es-examples .label {
        text-transform: uppercase;
        letter-spacing: 0.14em;
        margin-right: 8px;
    }
    .es-chip {
        display: inline-block;
        background: transparent;
        border: 1px solid var(--line);
        color: var(--text-2);
        padding: 6px 12px;
        border-radius: 999px;
        font-family: var(--sans);
        font-size: 12.5px;
    }

    /* ── Section heading ── */
    .es-section-head {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        padding: 48px 0 22px;
        border-bottom: 1px solid var(--line);
    }
    .es-kicker {
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--text-3);
        margin-right: 16px;
    }
    .es-topic {
        font-family: var(--sans);
        font-weight: 500;
        font-size: 18px;
        color: var(--text);
        letter-spacing: -0.005em;
    }
    .es-section-right {
        font-family: var(--mono);
        font-size: 11px;
        color: var(--text-3);
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }

    /* ── Signal card ── */
    .es-signal {
        display: grid;
        grid-template-columns: 50px 1fr 260px;
        gap: 32px;
        padding: 28px 0 32px;
        border-top: 1px solid var(--line);
        align-items: start;
    }
    .es-signal:last-child { border-bottom: 1px solid var(--line); }
    .es-signal-num {
        font-family: var(--mono);
        font-size: 13px;
        line-height: 1.4;
        color: var(--text-3);
        letter-spacing: 0.06em;
        padding-top: 6px;
    }
    .es-signal-title {
        font-family: var(--sans);
        font-weight: 500;
        font-size: 22px;
        line-height: 1.25;
        letter-spacing: -0.015em;
        color: var(--text);
        margin: 0 0 12px;
    }
    .es-signal-desc {
        font-size: 14.5px;
        line-height: 1.6;
        color: var(--text-2);
        margin: 0 0 20px;
        max-width: 62ch;
    }
    .es-meta-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px 36px;
        padding-top: 16px;
        border-top: 1px solid var(--line);
    }
    .es-meta-label {
        font-family: var(--mono);
        font-size: 10.5px;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--text-3);
        margin-bottom: 6px;
    }
    .es-meta-value {
        font-size: 13.5px;
        line-height: 1.55;
        color: var(--text);
    }

    .es-side {
        display: flex;
        flex-direction: column;
        gap: 16px;
        padding: 16px 18px;
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 10px;
    }
    .es-side-row {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
    }
    .es-side-k {
        font-family: var(--mono);
        font-size: 10.5px;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--text-3);
    }
    .es-side-v {
        font-family: var(--sans);
        font-weight: 500;
        font-size: 18px;
        color: var(--text);
        line-height: 1;
    }
    .es-conf-bar {
        height: 3px;
        background: var(--line);
        border-radius: 2px;
        overflow: hidden;
    }
    .es-conf-fill {
        height: 100%;
        background: var(--text-2);
        border-radius: 2px;
    }
    .es-momentum {
        font-family: var(--mono);
        font-size: 11px;
        color: var(--text-2);
        letter-spacing: 0.04em;
    }

    /* ── Empty state ── */
    .es-empty {
        padding: 36px 0 0;
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 64px;
        align-items: start;
    }
    .es-empty h2 {
        font-family: var(--sans);
        font-size: 22px;
        font-weight: 500;
        margin: 0 0 12px;
        letter-spacing: -0.015em;
        color: var(--text);
    }
    .es-empty p {
        font-size: 14.5px;
        line-height: 1.6;
        color: var(--text-2);
        max-width: 54ch;
        margin: 0 0 24px;
    }
    .es-howsteps {
        counter-reset: step;
        list-style: none;
        padding: 0;
        margin: 0;
        border-top: 1px solid var(--line);
    }
    .es-howsteps li {
        counter-increment: step;
        display: grid;
        grid-template-columns: 50px 1fr;
        gap: 18px;
        padding: 18px 0;
        border-bottom: 1px solid var(--line);
    }
    .es-howsteps li::before {
        content: "0" counter(step);
        font-family: var(--mono);
        font-size: 11px;
        color: var(--text-4);
        letter-spacing: 0.1em;
    }
    .es-howsteps .h {
        font-family: var(--sans);
        font-weight: 500;
        font-size: 15px;
        color: var(--text);
        margin: 0 0 4px;
        letter-spacing: -0.005em;
    }
    .es-howsteps .d {
        font-size: 13px;
        color: var(--text-3);
        line-height: 1.55;
    }
    .es-stack-card {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 22px;
    }
    .es-stack-card .label {
        font-family: var(--mono);
        font-size: 10.5px;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--text-3);
        margin-bottom: 16px;
    }
    .es-stack {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1px;
        background: var(--line);
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid var(--line);
    }
    .es-stack .cell {
        padding: 14px;
        background: var(--surface);
        min-height: 76px;
    }
    .es-stack .n {
        font-family: var(--sans);
        font-weight: 500;
        font-size: 13px;
        color: var(--text);
        margin-bottom: 4px;
    }
    .es-stack .r {
        font-family: var(--mono);
        font-size: 10.5px;
        color: var(--text-3);
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }
    .es-stack .cell.hi { background: var(--surface-2); }

    /* ── Streamlit overrides ── */
    .stSpinner > div > div {
        border-top-color: var(--text-2) !important;
        color: var(--text-2) !important;
    }
    .stAlert {
        background-color: var(--surface) !important;
        border: 1px solid var(--line) !important;
        border-radius: 10px !important;
        color: var(--text) !important;
    }
    div[data-testid="stStatusWidget"] {
        background: var(--surface) !important;
        border: 1px solid var(--line) !important;
        border-radius: 10px !important;
    }

    .es-footer {
        padding: 80px 0 0;
        display: flex;
        justify-content: space-between;
        color: var(--text-3);
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.06em;
    }

    @media (max-width: 900px) {
        .block-container { padding: 1.5rem 1.25rem 5rem !important; }
        .es-masthead { grid-template-columns: 1fr; gap: 28px; padding: 36px 0 32px; }
        .es-signal { grid-template-columns: 1fr; gap: 18px; }
        .es-meta-grid { grid-template-columns: 1fr; }
        .es-empty { grid-template-columns: 1fr; gap: 32px; }
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    /* ── Base ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0A0A0A;
        color: #E8E8E8;
    }

    .stApp {
        background-color: #0A0A0A;
    }

    /* ── Hide Streamlit branding ── */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ── Main container ── */
    .block-container {
        padding: 3rem 4rem;
        max-width: 1100px;
    }

    /* ── Title ── */
    h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        letter-spacing: -0.03em !important;
        margin-bottom: 0 !important;
    }

    /* ── Subheader ── */
    h3 {
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
        color: #666666 !important;
        margin-top: 0.25rem !important;
    }

    /* ── Input field ── */
    .stTextInput > div > div > input {
        background-color: #141414 !important;
        border: 1px solid #2A2A2A !important;
        border-radius: 10px !important;
        color: #E8E8E8 !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
        transition: border-color 0.2s;
    }

    .stTextInput > div > div > input:focus {
        border-color: #00FF88 !important;
        box-shadow: 0 0 0 1px #00FF88 !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #444444 !important;
    }

    /* ── Button ── */
    .stButton > button {
        background-color: #00FF88 !important;
        color: #0A0A0A !important;
        border: none !important;
        border-radius: 10px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.65rem 1.8rem !important;
        transition: all 0.2s !important;
        letter-spacing: 0.01em !important;
    }

    .stButton > button:hover {
        background-color: #00CC6E !important;
        transform: translateY(-1px) !important;
    }

    /* ── Divider ── */
    hr {
        border-color: #1E1E1E !important;
        margin: 2rem 0 !important;
    }

    /* ── Signal cards ── */
    .signal-card {
        background: #141414;
        border: 1px solid #1E1E1E;
        border-radius: 14px;
        padding: 1.75rem 2rem;
        margin-bottom: 1.25rem;
        transition: border-color 0.2s;
    }

    .signal-card:hover {
        border-color: #2A2A2A;
    }

    .signal-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
        color: #00FF88;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .signal-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 0.75rem;
        line-height: 1.3;
    }

    .signal-description {
        font-size: 0.9rem;
        color: #999999;
        line-height: 1.7;
        margin-bottom: 1.25rem;
    }

    .signal-meta {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 1rem;
    }

    .meta-block {
        background: #0A0A0A;
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }

    .meta-label {
        font-size: 0.7rem;
        font-weight: 600;
        color: #444444;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.3rem;
    }

    .meta-value {
        font-size: 0.85rem;
        color: #CCCCCC;
        line-height: 1.5;
    }

    .confidence-badge {
        display: inline-block;
        background: #0D2818;
        color: #00FF88;
        border: 1px solid #00FF88;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        letter-spacing: 0.05em;
    }

    /* ── How it works box ── */
    .how-it-works {
        background: #141414;
        border: 1px solid #1E1E1E;
        border-radius: 14px;
        padding: 1.5rem;
    }

    .how-it-works-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
        color: #444444;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
    }

    .how-step {
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
    }

    .step-dot {
        width: 6px;
        height: 6px;
        background: #00FF88;
        border-radius: 50%;
        margin-top: 0.45rem;
        flex-shrink: 0;
    }

    .step-text {
        font-size: 0.85rem;
        color: #888888;
        line-height: 1.5;
    }

    /* ── Success / Error ── */
    .stSuccess {
        background-color: #0D2818 !important;
        border: 1px solid #00FF88 !important;
        color: #00FF88 !important;
        border-radius: 10px !important;
    }

    .stAlert {
        border-radius: 10px !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #00FF88 !important;
    }

    /* ── Welcome section ── */
    .welcome-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
    }

    .welcome-text {
        font-size: 0.9rem;
        color: #666666;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .example-tag {
        display: inline-block;
        background: #141414;
        border: 1px solid #2A2A2A;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #888888;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        cursor: default;
    }
    </style>
    """, unsafe_allow_html=True)
    
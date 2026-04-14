import streamlit as st
import time
from agent import run_agent
from style import apply_styles

st.set_page_config(
    page_title="EarlySignal",
    page_icon="🔍",
    layout="wide"
)

apply_styles()

st.markdown('<h1>EarlySignal</h1>', unsafe_allow_html=True)
st.markdown("<h3>Spot what's going mainstream before it does.</h3>", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    industry = st.text_input(
        "",
        placeholder="e.g. athletic wear, fintech, plant-based food, creator economy",
        label_visibility="collapsed"
    )
    run_button = st.button("Find Emerging Signals", type="primary")

with col2:
    st.markdown("""
    <div class="how-it-works">
        <div class="how-it-works-title">How it works</div>
        <div class="how-step">
            <div class="step-dot"></div>
            <div class="step-text">Claude searches the web for recent developments</div>
        </div>
        <div class="how-step">
            <div class="step-dot"></div>
            <div class="step-text">Scans Reddit for niche community signals</div>
        </div>
        <div class="how-step">
            <div class="step-dot"></div>
            <div class="step-text">Surfaces 3 trends before they go mainstream</div>
        </div>
        <div class="how-step">
            <div class="step-dot"></div>
            <div class="step-text" style="color: #444444;">Powered by Claude AI + Tavily + Reddit</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if run_button and industry:
    st.markdown('<hr>', unsafe_allow_html=True)

    with st.spinner("Scanning the internet for signals in " + industry + "..."):
        time.sleep(1)
        result = run_agent(industry)

    if "error" in result:
        st.error("Something went wrong: " + result.get("error", ""))
        if "raw" in result:
            st.code(result["raw"])
    else:
        signals = result.get("signals", [])

        st.markdown(
            '<div style="margin-bottom: 1.5rem;">'
            '<span style="font-family: Space Grotesk, sans-serif; font-size: 0.75rem; font-weight: 600; color: #444444; text-transform: uppercase; letter-spacing: 0.1em;">'
            + str(len(signals)) + ' signals found in </span>'
            '<span style="font-family: Space Grotesk, sans-serif; font-size: 0.75rem; font-weight: 600; color: #00FF88; text-transform: uppercase; letter-spacing: 0.1em;">'
            + industry.upper() + '</span></div>',
            unsafe_allow_html=True
        )

        for i, signal in enumerate(signals):
            title = signal.get("title", "Untitled")
            description = signal.get("description", "")
            where = signal.get("where_its_showing_up", "")
            why = signal.get("why_it_could_be_big", "")
            confidence = signal.get("confidence", "N/A")

            st.markdown(
                '<div class="signal-card">'
                '<div class="signal-number">Signal ' + str(i + 1) + ' of ' + str(len(signals)) + '</div>'
                '<div class="signal-title">' + title + '</div>'
                '<div class="signal-description">' + description + '</div>'
                '<div class="signal-meta">'
                '<div class="meta-block">'
                '<div class="meta-label">Where it is showing up</div>'
                '<div class="meta-value">' + where + '</div>'
                '</div>'
                '<div class="meta-block">'
                '<div class="meta-label">Why it could be big</div>'
                '<div class="meta-value">' + why + '</div>'
                '</div>'
                '</div>'
                '<span class="confidence-badge">Confidence: ' + confidence + '</span>'
                '</div>',
                unsafe_allow_html=True
            )

elif run_button and not industry:
    st.warning("Please enter an industry or market space first.")

else:
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 2rem 0;">
        <div class="welcome-title">What are you tracking today?</div>
        <div class="welcome-text">
            Enter any industry or market space to discover what is gaining momentum
            before it hits mainstream media.
        </div>
        <div>
            <span class="example-tag">athletic wear</span>
            <span class="example-tag">creator economy</span>
            <span class="example-tag">plant-based food</span>
            <span class="example-tag">fintech for Gen Z</span>
            <span class="example-tag">sustainable packaging</span>
            <span class="example-tag">AI tools</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# main.py

import streamlit as st
import pandas as pd
import re
from datetime import datetime
from textblob import TextBlob
from textblob import TextBlob
# --- UI CONFIG ---
st.set_page_config(page_title="AI Marketing Assistant", layout="wide")

# --- HEADER ---
st.title("AI-Powered Marketing Tool")
st.markdown("Analyze campaign ideas, understand audience behavior, and optimize performance — all from one place.")

# --- SIDEBAR CONFIG ---
st.sidebar.header("Campaign Inputs")
campaign_name = st.sidebar.text_input("Campaign Name")
publish_date = st.sidebar.date_input("Planned Publish Date")
target_keywords = st.sidebar.text_area("Target Keywords", "e.g. AI, marketing, Dubai")

# --- TEXT ANALYSIS MODULE ---
st.subheader("📊 Campaign Idea Analyzer")

ad_text = st.text_area("Enter your advertising idea or caption", height=150)
if ad_text:
    # Sentiment analysis
    sentiment = TextBlob(ad_text).sentiment
    polarity = round(sentiment.polarity, 2)
    subjectivity = round(sentiment.subjectivity, 2)
    
    st.write(f"**Sentiment Score:** {polarity}")
    st.write(f"**Subjectivity:** {subjectivity}")

    # Keyword match
    keywords = target_keywords.split(",")
    found = [kw.strip() for kw in keywords if kw.strip().lower() in ad_text.lower()]
    st.write(f"**Matched Keywords:** {', '.join(found) if found else 'None'}")

# --- AUDIENCE INSIGHT ---
st.subheader("👥 Audience Targeting (NLP-Enhanced)")

def extract_audience_traits(text):
    traits = []
    if re.search(r"\byouth\b|\bteen\b", text, re.IGNORECASE):
        traits.append("Young audience")
    if "luxury" in text.lower():
        traits.append("High-income segment")
    if "saving" in text.lower() or "budget" in text.lower():
        traits.append("Cost-conscious audience")
    return traits

if ad_text:
    traits = extract_audience_traits(ad_text)
    st.write(f"**Inferred Traits:** {', '.join(traits) if traits else 'General audience'}")

# --- SCHEDULING & TRACKING (Placeholder) ---
st.subheader("📅 Publishing Schedule & Performance Tracker")

st.markdown("Tracking modules coming soon: engagement metrics, CTR, visual content integration, and adaptive scheduling.")

# --- LANGUAGE SUPPORT PREP (Arabic-ready but disabled) ---
# Arabic support can be activated later with NLP enhancements

# --- FOOTER ---
st.markdown("---")
st.caption(f"Session generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

import streamlit as st
import sys
import os

# Fix imports
sys.path.append(os.path.abspath("."))

from modules.data_loader import load_data
from modules.query_parser import parse_query
from modules.analytics_engine import analyze_data
from modules.insight_generator import generate_insight
from modules.visualization import create_chart
from modules.trust_layer import build_trust_info
from modules.column_detector import detect_columns

# Page config
st.set_page_config(
    page_title="Talk to Data",
    layout="wide",
    page_icon="📊"
)

# 🌈 Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .block-container {
        padding-top: 2rem;
    }
    .stTextInput input {
        background-color: #1E1E1E;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 🎯 HEADER
st.markdown("""
# 💬 Talk to Data  
### 🚀 Seamless Self-Service Intelligence
""")

st.markdown("---")

# 📂 SIDEBAR
st.sidebar.markdown("## ⚙️ Controls")
uploaded_file = st.sidebar.file_uploader("📂 Upload Dataset", type=["csv", "xlsx"])

st.sidebar.markdown("### 💡 Try asking:")
st.sidebar.markdown("""
- breakdown region  
- compare product sales  
- why did revenue drop  
- summary  
""")

# 🚀 MAIN APP
if uploaded_file:
    df = load_data(uploaded_file)

    if df is None:
        st.error("⚠️ Could not load file")
    else:
        # 📊 METRICS
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Rows", len(df))

        with col2:
            st.metric("📊 Columns", len(df.columns))

        with col3:
            st.metric("🧠 Data Points", df.size)

        st.markdown("---")

        # 📄 DATA PREVIEW (collapsible)
        with st.expander("🔍 Preview Dataset"):
            st.dataframe(df.head())

        # 💬 CHAT SYSTEM
        if "chat" not in st.session_state:
            st.session_state.chat = []

        query = st.chat_input("💬 Ask something about your data...")

        if query:
            st.session_state.chat.append({"role": "user", "content": query})

            # 🔍 Processing
            with st.spinner("🧠 Analyzing your data..."):
                parsed = parse_query(query, df)
                column_info = detect_columns(df)
                result = analyze_data(df, parsed, column_info)
                chart = create_chart(result)
                insight = generate_insight(query, result.head().to_string())
                trust = build_trust_info(parsed, column_info)

            st.session_state.chat.append({
                "role": "assistant",
                "content": insight
            })

            # 📊 RESULTS SECTION
            st.markdown("## 📊 Analysis Results")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 📄 Data")
                st.dataframe(result)

            with col2:
                st.markdown("### 📈 Visualization")
                if chart:
                    st.plotly_chart(chart, use_container_width=True)
                else:
                    st.info("No chart available")

            # 🤖 INSIGHTS
            st.markdown("## 🤖 AI Insights")
            st.success(insight)

            # 🔍 TRUST LAYER
            with st.expander("🔍 How was this computed?"):
                st.write(f"**Intent:** {trust['intent']}")
                st.write(f"**Columns Used:** {trust['columns_used']}")
                st.write(f"**Date Column:** {trust['detected_date_column']}")
                st.write(f"**Numeric Columns:** {trust['numeric_columns']}")
                st.write(f"**Categorical Columns:** {trust['categorical_columns']}")
                st.write(f"**Assumptions:** {trust['assumptions']}")

        # 💬 CHAT HISTORY DISPLAY
        st.markdown("## 💬 Conversation")

        for msg in st.session_state.chat:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

else:
    
    # 🌟 HERO SECTION
    st.markdown("""
    <h1 style='text-align: center;'>💬 Talk to Data</h1>
    <h3 style='text-align: center; color: gray;'>
    Seamless Self-Service Intelligence
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 🚀 FEATURE CARDS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🧠 Ask Anything
        Query your data in plain English  
        No SQL, no coding required
        """)

    with col2:
        st.markdown("""
        ### 📊 Instant Insights
        Get charts + explanations instantly  
        Powered by AI
        """)

    with col3:
        st.markdown("""
        ### 🔍 Full Transparency
        See exactly how results are computed  
        No black box
        """)

    st.markdown("---")

    # 💡 EXAMPLE QUESTIONS (Styled)
    st.markdown("## 💡 Try Asking Questions Like:")

    q1, q2 = st.columns(2)

    with q1:
        st.info("📊 Breakdown sales by region")
        st.info("⚖️ Compare Product A vs Product B")
        st.info("📈 Show sales trends over time")

    with q2:
        st.info("📉 Why did revenue drop last month?")
        st.info("🏆 Top performing products")
        st.info("📦 Sales distribution by category")

    st.markdown("---")

    # 📂 CALL TO ACTION
    st.markdown("""
    <div style='text-align: center;'>
        <h3>⬅️ Upload your dataset from the sidebar to get started</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 🏆 FOOTER / IMPACT LINE
    st.markdown("""
    <div style='text-align: center; color: gray;'>
    Built for fast, explainable, and intelligent data exploration 🚀
    </div>
    """, unsafe_allow_html=True)

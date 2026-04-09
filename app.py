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
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    
    .block-container {
        padding-top: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* Chat Input Styling */
    .stChatInput input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(102, 51, 153, 0.5) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 16px !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease;
    }
    
    .stChatInput input:focus {
        border-color: #9f7aea !important;
        box-shadow: 0 0 20px rgba(159, 122, 234, 0.3) !important;
    }
    
    /* Text Input Styling */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(159, 122, 234, 0.3) !important;
        border-radius: 8px !important;
        color: white !important;
        padding: 10px 14px !important;
    }
    
    .stTextInput input:focus {
        border-color: #9f7aea !important;
        box-shadow: 0 0 15px rgba(159, 122, 234, 0.2) !important;
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(159, 122, 234, 0.15), rgba(66, 153, 225, 0.15));
        border: 1px solid rgba(159, 122, 234, 0.3);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(159, 122, 234, 0.6);
        box-shadow: 0 10px 30px rgba(159, 122, 234, 0.2);
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, rgba(102, 51, 153, 0.2), rgba(66, 153, 225, 0.2));
        border: 1px solid rgba(159, 122, 234, 0.4);
        border-radius: 15px;
        padding: 25px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        border-color: rgba(159, 122, 234, 0.8);
        box-shadow: 0 15px 40px rgba(159, 122, 234, 0.3);
        transform: translateY(-5px);
    }
    
    /* Info/Success Boxes */
    .stAlert {
        border-radius: 10px !important;
        background: linear-gradient(135deg, rgba(159, 122, 234, 0.1), rgba(66, 153, 225, 0.1)) !important;
        border: 1px solid rgba(159, 122, 234, 0.3) !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, rgba(159, 122, 234, 0.1), rgba(66, 153, 225, 0.05));
        border-radius: 8px;
        border: 1px solid rgba(159, 122, 234, 0.2);
    }
    
    /* Headers */
    h1, h2, h3 {
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    h1 {
        background: linear-gradient(135deg, #9f7aea 0%, #4299e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Dataframe Styling */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Divider */
    hr {
        border: 1px solid rgba(159, 122, 234, 0.3);
        margin: 2rem 0;
    }
    
    /* Question Cards */
    .question-card {
        background: linear-gradient(135deg, rgba(159, 122, 234, 0.2), rgba(66, 153, 225, 0.2));
        border: 2px solid rgba(159, 122, 234, 0.4);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        backdrop-filter: blur(10px);
        font-size: 1.1em;
        font-weight: 500;
    }
    
    .question-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(159, 122, 234, 0.8);
        box-shadow: 0 20px 50px rgba(159, 122, 234, 0.4);
        background: linear-gradient(135deg, rgba(159, 122, 234, 0.35), rgba(66, 153, 225, 0.35));
    }
    
    .get-started-card {
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.25), rgba(237, 137, 54, 0.25));
        border: 2px solid rgba(72, 187, 120, 0.5);
        border-radius: 14px;
        padding: 30px;
        text-align: center;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        backdrop-filter: blur(10px);
    }
    
    .get-started-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(72, 187, 120, 0.9);
        box-shadow: 0 25px 60px rgba(72, 187, 120, 0.4);
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.4), rgba(237, 137, 54, 0.4));
    }
    </style>
""", unsafe_allow_html=True)

# ====== INITIALIZE SESSION STATE ======
if "page" not in st.session_state:
    st.session_state.page = "upload"  # "upload" or "analysis"
if "uploaded_file_data" not in st.session_state:
    st.session_state.uploaded_file_data = None
if "chat" not in st.session_state:
    st.session_state.chat = []

# ====== PAGE ROUTING ======

# ========== UPLOAD PAGE ==========
if st.session_state.page == "upload":
    # 🌟 HERO SECTION
    st.markdown("""
    <div style='text-align: center; padding: 40px 0;'>
        <h1 style='font-size: 3.5em; margin-bottom: 15px;'>💬 Talk to Data</h1>
        <p style='font-size: 1.3em; color: #cbd5e0; margin: 0;'>Seamless Self-Service Intelligence</p>
        <p style='color: #a0aec0; margin-top: 10px;'>Turn your data into insights with natural language queries</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # 🚀 FEATURE CARDS
    st.markdown("<h2 style='text-align: center; margin: 40px 0 30px 0;'>✨ Why Talk to Data?</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h3 style='font-size: 2.5em;'>🧠</h3>
            <h3 style='color: #9f7aea;'>Ask Anything</h3>
            <p style='color: #cbd5e0;'>Query your data in plain English. No SQL, no coding required.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h3 style='font-size: 2.5em;'>⚡</h3>
            <h3 style='color: #4299e1;'>Instant Insights</h3>
            <p style='color: #cbd5e0;'>Get charts and explanations instantly powered by AI.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='feature-card'>
            <h3 style='font-size: 2.5em;'>🔍</h3>
            <h3 style='color: #48bb78;'>Full Transparency</h3>
            <p style='color: #cbd5e0;'>See exactly how results are computed. No black box.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    # 💡 EXAMPLE QUESTIONS (Styled)
    st.markdown("""
    <div style='margin: 50px 0 40px 0;'>
        <h2 style='text-align: center; font-size: 2.2em; margin-bottom: 35px;'>💡 Try Questions Like:</h2>
    </div>
    """, unsafe_allow_html=True)

    q1, q2, q3 = st.columns(3, gap="medium")

    with q1:
        st.markdown("""
        <div class='question-card' style='color: #9f7aea;'>
            <div style='font-size: 2em; margin-bottom: 10px;'>📊</div>
            <p style='margin: 0; font-size: 1.05em;'>Breakdown sales by region</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='question-card' style='color: #4299e1; margin-top: 15px;'>
            <div style='font-size: 2em; margin-bottom: 10px;'>⚖️</div>
            <p style='margin: 0; font-size: 1.05em;'>Compare Product A vs Product B</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='question-card' style='color: #48bb78; margin-top: 15px;'>
            <div style='font-size: 2em; margin-bottom: 10px;'>📈</div>
            <p style='margin: 0; font-size: 1.05em;'>Show sales trends over time</p>
        </div>
        """, unsafe_allow_html=True)

    with q2:
        st.markdown("""
        <div class='question-card' style='color: #ed8936;'>
            <div style='font-size: 2em; margin-bottom: 10px;'>📉</div>
            <p style='margin: 0; font-size: 1.05em;'>Why did revenue drop last month?</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='question-card' style='color: #9f7aea; margin-top: 15px;'>
            <div style='font-size: 2em; margin-bottom: 10px;'>🏆</div>
            <p style='margin: 0; font-size: 1.05em;'>Top performing products</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='question-card' style='color: #4299e1; margin-top: 15px;'>
            <div style='font-size: 2em; margin-bottom: 10px;'>📦</div>
            <p style='margin: 0; font-size: 1.05em;'>Sales distribution by category</p>
        </div>
        """, unsafe_allow_html=True)

    with q3:
        st.markdown("""
        <div class='get-started-card' style='height: 100%;'>
            <div style='font-size: 3.5em; margin-bottom: 15px;'>🚀</div>
            <h3 style='font-size: 1.8em; color: #48bb78; margin: 10px 0;'>Get Started</h3>
            <p style='color: #cbd5e0; margin: 0; font-size: 1em;'>Scroll down and upload your CSV or Excel dataset to begin analyzing</p>
            <div style='margin-top: 15px; font-size: 0.9em; color: #a0aec0;'>
                ✨ Fast • Intelligent • Transparent
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    # 📂 UPLOAD SECTION AT END
    st.markdown("""
    <div style='text-align: center; padding: 40px 20px; margin-top: 40px;
                background: linear-gradient(135deg, rgba(159, 122, 234, 0.1), rgba(66, 153, 225, 0.1));
                border: 1px solid rgba(159, 122, 234, 0.3);
                border-radius: 15px;'>
        <h2 style='margin: 0 0 20px 0;'>📂 Upload Your CSV or Excel File</h2>
    </div>
    """, unsafe_allow_html=True)
    
    file_upload = st.file_uploader("", type=["csv", "xlsx"], label_visibility="collapsed")
    
    if file_upload:
        st.session_state.uploaded_file_data = file_upload
        st.session_state.page = "analysis"
        st.rerun()

    st.markdown("")

    # 🏆 FOOTER / IMPACT LINE
    st.markdown("""
    <div style='text-align: center; padding: 30px 0; color: #a0aec0; margin-top: 40px;'>
        <p style='margin: 0; font-size: 0.95em;'>✨ Built for fast, explainable, and intelligent data exploration 🚀</p>
    </div>
    """, unsafe_allow_html=True)

# ========== ANALYSIS PAGE ==========
else:  # st.session_state.page == "analysis"
    uploaded_file = st.session_state.uploaded_file_data
    
    if uploaded_file:
        df = load_data(uploaded_file)

        if df is None:
            st.error("""
            ⚠️ **Could not load file**
            
            **Troubleshooting steps:**
            1. **Check file format** - Ensure it's a valid CSV or Excel (.xlsx) file
            2. **Check file content** - Make sure the file has:
               - At least one column with a header
               - At least one row of data
               - No empty/blank sheets (for Excel)
            3. **Check file encoding** - Try saving your CSV in UTF-8 encoding:
               - Open in Excel → Save As → Choose UTF-8 CSV format
            4. **Check file size** - Ensure the file isn't too large
            5. **Test file** - Try a simple test CSV:
               ```
               name,age,city
               John,25,NYC
               Jane,30,LA
               ```
            
            **Still having issues?**
            - Check the terminal output for detailed error messages
            - Try downloading and re-uploading your file
            """)
            if st.button("📥 Try Another File"):
                st.session_state.uploaded_file_data = None
                st.session_state.page = "upload"
                st.rerun()
        else:
            # 📊 METRICS
            st.markdown("<h2 style='margin-top: 20px; margin-bottom: 20px;'>📊 Dataset Overview</h2>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3, gap="medium")

            with col1:
                st.markdown(f"""
                <div class='metric-card'>
                    <h3 style='font-size: 2.5em; color: #9f7aea;'>📄</h3>
                    <p style='font-size: 1.8em; font-weight: bold; margin: 10px 0;'>{len(df):,}</p>
                    <p style='color: #cbd5e0; margin: 0;'>Rows</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class='metric-card'>
                    <h3 style='font-size: 2.5em; color: #4299e1;'>📊</h3>
                    <p style='font-size: 1.8em; font-weight: bold; margin: 10px 0;'>{len(df.columns)}</p>
                    <p style='color: #cbd5e0; margin: 0;'>Columns</p>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class='metric-card'>
                    <h3 style='font-size: 2.5em; color: #48bb78;'>🧠</h3>
                    <p style='font-size: 1.8em; font-weight: bold; margin: 10px 0;'>{df.size:,}</p>
                    <p style='color: #cbd5e0; margin: 0;'>Data Points</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("")

            # 📄 DATA PREVIEW (collapsible)
            with st.expander("🔍 Preview Dataset"):
                st.dataframe(df.head())

            # 💬 CHAT SYSTEM
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
                st.markdown("<h2 style='margin-top: 30px; margin-bottom: 20px;'>📊 Analysis Results</h2>", unsafe_allow_html=True)

                col1, col2 = st.columns(2, gap="large")

                with col1:
                    st.markdown("<h3 style='color: #4299e1;'>📄 Data</h3>", unsafe_allow_html=True)
                    st.dataframe(result, use_container_width=True)

                with col2:
                    st.markdown("<h3 style='color: #48bb78;'>📈 Visualization</h3>", unsafe_allow_html=True)
                    if chart:
                        st.plotly_chart(chart, use_container_width=True)
                    else:
                        st.info("No chart available")

                # 🔍 TRUST LAYER
                st.markdown("<h2 style='margin-top: 30px; margin-bottom: 15px;'>🔍 Computation Details</h2>", unsafe_allow_html=True)
                
                with st.expander("📋 Show detailed analysis methodology"):
                    col1, col2 = st.columns(2, gap="medium")
                    with col1:
                        st.markdown(f"""
                        <div style='background: rgba(159, 122, 234, 0.1); border-radius: 8px; padding: 15px;'>
                            <p><strong style='color: #9f7aea;'>Intent:</strong> {trust['intent']}</p>
                            <p><strong style='color: #9f7aea;'>Date Column:</strong> {trust['detected_date_column']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style='background: rgba(66, 153, 225, 0.1); border-radius: 8px; padding: 15px;'>
                            <p><strong style='color: #4299e1;'>Columns Used:</strong> {trust['columns_used']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.write("**Numeric Columns:**", trust['numeric_columns'])
                    st.write("**Categorical Columns:**", trust['categorical_columns'])
                    st.write("**Assumptions:**", trust['assumptions'])

            # 💬 CHAT HISTORY DISPLAY
            st.markdown("<h2 style='margin-top: 40px; margin-bottom: 20px;'>💬 Conversation History</h2>", unsafe_allow_html=True)

            for msg in st.session_state.chat:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])



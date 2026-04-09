# 💬 Talk to Data

An AI-powered Streamlit application for natural language data analysis. Upload your CSV or Excel files and ask questions about your data in plain English—no SQL needed. Built with Groq LLM for intelligent insights and Plotly for interactive visualizations.

---

## 📁 Project Structure

```
talk_to_data/
├── app.py                    # Main Streamlit application with multi-page routing
├── requirements.txt          # Python dependencies (streamlit, pandas, plotly, groq)
├── config/
│   └── settings.py          # Configuration and environment variable management
└── modules/
    ├── __init__.py          # Package initializer
    ├── data_loader.py       # CSV/Excel loading with encoding support
    ├── column_detector.py   # Column data type detection
    ├── query_parser.py      # Natural language query parsing
    ├── analytics_engine.py  # Data analysis and filtering logic
    ├── insight_generator.py # Groq LLM-powered insights
    ├── visualization.py     # Plotly chart generation
    └── trust_layer.py       # Computation transparency metadata
```

---

## 📄 File Descriptions

### Root Level

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application with three pages: landing (upload), analysis (chat & results), and navigation |
| `requirements.txt` | External Python package dependencies |
| `config/settings.py` | Loads API keys and settings from `.env` file |

### Modules

| Module | Responsibility |
|--------|-----------------|
| `data_loader.py` | Opens CSV/Excel files, handles multiple encodings, cleans column names, validates data |
| `column_detector.py` | Analyzes columns to identify numeric, categorical, date, and string types |
| `query_parser.py` | Extracts intent and relevant columns from user's natural language query |
| `analytics_engine.py` | Filters, groups, and aggregates data based on parsed query |
| `insight_generator.py` | Sends data summary + query to Groq LLM and returns human-readable insights |
| `visualization.py` | Creates interactive Plotly charts based on analysis results |
| `trust_layer.py` | Builds metadata showing how results were computed (columns used, assumptions, etc.) |

---

## � Getting Started

### Prerequisites
- Python 3.8 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Installation & Setup

1. **Clone or download the project**
   ```bash
   cd talk_to_data
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your Groq API key
   # Get your free key at: https://console.groq.com
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```
   - Opens at `http://localhost:8501`

---

## �🔄 Application Flow

1. User uploads CSV/Excel file
2. `data_loader.py` validates and loads data into pandas DataFrame
3. `column_detector.py` analyzes column types (numeric, categorical, date, string)
4. User types natural language question in chat
5. `query_parser.py` extracts intent and identifies relevant columns
6. `analytics_engine.py` performs data filtering/grouping
7. `visualization.py` generates interactive charts
8. `insight_generator.py` queries Groq LLM for AI-powered explanation
9. `trust_layer.py` creates transparency metadata about the analysis
10. Results displayed in UI with computation details

---

## 🛠️ Core Technologies

- **Streamlit** - Web framework for data applications
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive chart visualization
- **Groq** - LLM API for natural language processing
- **Python-dotenv** - Environment variable configuration




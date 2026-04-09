import plotly.express as px

def create_chart(df):
    if df is None or len(df.columns) < 2:
        return None

    x = df.columns[0]
    y = df.columns[1]

    # Line chart for time-based data
    if "date" in x.lower() or "month" in x.lower():
        fig = px.line(df, x=x, y=y, title="Trend Over Time")
    else:
        fig = px.bar(df, x=x, y=y, title="Comparison Chart")

    return fig
import pandas as pd

def analyze_data(df, parsed_query, column_info=None):
    intent = parsed_query["intent"]

    # 🧩 BREAKDOWN
    if intent == "breakdown":
        if parsed_query["columns"]:
            col = parsed_query["columns"][0]
        else:
            col = column_info["categorical"][0] if column_info and column_info["categorical"] else None

        if col:
            result = df[col].value_counts().reset_index()
            result.columns = [col, "count"]
            return result

    # ⚖️ COMPARE
    elif intent == "compare":
        if len(parsed_query["columns"]) >= 2:
            col1, col2 = parsed_query["columns"][:2]
        elif column_info:
            col1 = column_info["categorical"][0]
            col2 = column_info["numeric"][0]
        else:
            return df.head()

        result = df.groupby(col1)[col2].sum().reset_index()
        return result

    # 📊 SUMMARY
    elif intent == "summary":
        return df.describe()

    # 🔥 WHY ANALYSIS (UPGRADED)
    elif intent == "why":
        if column_info:
            date_col = column_info["date"]
            num_col = column_info["numeric"][0] if column_info["numeric"] else None
        else:
            date_col = "date" if "date" in df.columns else None
            num_col = None

        if date_col and num_col:
            df[date_col] = pd.to_datetime(df[date_col])
            df = df.sort_values(date_col)

            # Monthly aggregation
            df["month"] = df[date_col].dt.to_period("M")
            trend = df.groupby("month")[num_col].sum().reset_index()

            # % change
            trend["change_%"] = trend[num_col].pct_change() * 100

            return trend.tail(6)

    # 🔁 DEFAULT
    return df.head()
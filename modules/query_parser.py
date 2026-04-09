def parse_query(query, df):
    query = query.lower()

    intent = "unknown"

    if "why" in query:
        intent = "why"
    elif "compare" in query:
        intent = "compare"
    elif "breakdown" in query:
        intent = "breakdown"
    elif "summary" in query:
        intent = "summary"

    columns = list(df.columns)

    detected_columns = [col for col in columns if col in query]

    return {
        "intent": intent,
        "columns": detected_columns,
        "raw_query": query
    }
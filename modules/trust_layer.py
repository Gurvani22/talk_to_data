def build_trust_info(parsed_query, column_info):
    return {
        "intent": parsed_query.get("intent"),
        "columns_used": parsed_query.get("columns"),
        "detected_date_column": column_info.get("date"),
        "numeric_columns": column_info.get("numeric"),
        "categorical_columns": column_info.get("categorical"),
        "assumptions": "Data aggregated using detected columns and basic grouping"
    }
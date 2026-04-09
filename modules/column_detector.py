import pandas as pd

def detect_columns(df):
    column_info = {
        "date": None,
        "numeric": [],
        "categorical": []
    }

    for col in df.columns:
        # Try detect date
        try:
            pd.to_datetime(df[col])
            column_info["date"] = col
            continue
        except:
            pass

        # Numeric
        if pd.api.types.is_numeric_dtype(df[col]):
            column_info["numeric"].append(col)
        else:
            column_info["categorical"].append(col)

    return column_info
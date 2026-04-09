import pandas as pd

def load_data(file):
    if file.name.endswith(".csv"):
        try:
            df = pd.read_csv(file, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="latin1")
    else:
        df = pd.read_excel(file)

    return clean_data(df)


def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()
    return df
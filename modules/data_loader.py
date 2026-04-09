import pandas as pd
import io

def load_data(file):
    try:
        # Seek to the beginning of the file
        if hasattr(file, 'seek'):
            file.seek(0)
        
        if file.name.endswith(".csv"):
            # Try multiple encodings
            encodings = ["utf-8", "latin1", "iso-8859-1", "cp1252"]
            df = None
            
            for encoding in encodings:
                try:
                    file.seek(0)  # Reset for each attempt
                    df = pd.read_csv(file, encoding=encoding)
                    print(f"✓ Successfully read CSV with {encoding} encoding")
                    break
                except (UnicodeDecodeError, pd.errors.EmptyDataError):
                    continue
                except Exception as e:
                    print(f"Error with {encoding}: {e}")
                    continue
            
            if df is None:
                print("Failed to read CSV with all attempted encodings")
                return None
        else:
            # Excel file
            try:
                file.seek(0)
                df = pd.read_excel(file)
            except Exception as e:
                print(f"Error reading Excel file: {e}")
                return None
        
        # Check if dataframe is empty or has no columns
        if df is None or df.empty or len(df.columns) == 0:
            print(f"Data validation failed: empty={df.empty if df is not None else 'None'}, columns={len(df.columns) if df is not None else 0}")
            return None
        
        print(f"✓ Data loaded successfully: {len(df)} rows, {len(df.columns)} columns")
        return clean_data(df)
    
    except Exception as e:
        print(f"Error loading file: {type(e).__name__}: {e}")
        return None


def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()
    return df
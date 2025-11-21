import os
import pandas as pd

RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

COLUMNS_TO_KEEP = {
    "utc_timestamp": "timestamp", 
    "DE_load_actual_entsoe_transparency": "germany_load_mw",
    "HU_load_actual_entsoe_transparency": "hungary_load_mw" 
}

def transform_load(raw_filename: str = None) -> str:
    if raw_filename is None:
        raw_filename = os.path.join(RAW_DIR, "time_series_15min_singleindex.csv")
    
    print("Loading and transforming raw data...")
    # Reading CSV without pre-parsing dates
    df = pd.read_csv(raw_filename)
    
    
    # Check the presence of all required columns
    missing_columns = [col for col in COLUMNS_TO_KEEP.keys() if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Required columns are missing from the raw data: {', '.join(missing_columns)}")
    
    # Filter columns and rename
    df = df[list(COLUMNS_TO_KEEP.keys())].rename(columns=COLUMNS_TO_KEEP)
    
    # Parse the timestamp into datetime (UTC) format and make it an index
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df = df.set_index("timestamp").sort_index()
    
    # We save the processed data
    processed_filename = os.path.join(PROCESSED_DIR, "processed_load_data.csv")
    df.to_csv(processed_filename)
    
    print(f"Processed data saved to {processed_filename}")
    print(f"The processed data contains {len(df)} rows and columns: {', '.join(df.columns)}")
    return processed_filename

if __name__ == "__main__":
    transform_load()

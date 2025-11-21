import os
import pandas as pd

RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")

def validate_load(processed_filename: str = None) -> bool:
    if processed_filename is None:
        processed_filename = os.path.join(PROCESSED_DIR, "processed_load_data.csv")
    
    print("Validating processed data...")
    
    if not os.path.exists(processed_filename):
        raise FileNotFoundError(f"Processed file not found: {processed_filename}")
    
    # Loading with index parsing
    df = pd.read_csv(processed_filename, index_col='timestamp', parse_dates=True)
    df.index = pd.to_datetime(df.index, utc=True)
    
    issues = False
    
    # 1. Gaps
    missing = df.isnull().sum()
    if missing.any():
        print("Missing values per column:")
        for col, count in missing[missing > 0].items():
            print(f"  {col}: {count} ({count/len(df)*100:.2f}%)")
        issues = True
    else:
        print("No missing values found.")
    
  # 2. Duplicates by time
    duplicates = df.index.duplicated().sum()
    if duplicates > 0:
        print(f"Found {duplicates} duplicate timestamps. Sample duplicates:")
        dup_indices = df.index[df.index.duplicated(keep=False)].unique()[:5]  # Первые 5
        print(dup_indices)
        issues = True
    else:
        print("No duplicate timestamps found.")
    
 #3. Negative/Too large values
    thresholds = {'germany_load_mw': 100000, 'hungary_load_mw': 20000}  # MW
    for col in df.columns:
        if col in thresholds:
            col_data = df[col].dropna()
            negatives = (col_data < 0).sum()
            extremes = (col_data > thresholds[col]).sum()
            
            if negatives > 0:
                print(f"Negative values in {col}: {negatives}. Sample: {col_data[col_data < 0].head()}")
                issues = True
            if extremes > 0:
                print(f"Extreme values (> {thresholds[col]/1000} GW) in {col}: {extremes}. Sample: {col_data[col_data > thresholds[col]].head()}")
                issues = True
            else:
                print(f"{col}: Values look reasonable (min: {col_data.min():.0f} MW, max: {col_data.max():.0f} MW).")
    
# General statistics
    print(f"\nOverall stats:")
    print(df.describe())
    
    if not issues:
        print("All validations passed! Data is clean.")
        return True
    else:
        print("Validation issues found! Review the reports above.")
        return False

if __name__ == "__main__":
    validate_load()

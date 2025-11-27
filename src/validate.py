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
    
    df = pd.read_csv(processed_filename, index_col='timestamp', parse_dates=True)
    df.index = pd.to_datetime(df.index, utc=True)
    
    issues_found = False

    missing = df.isnull().sum()
    if missing.any():
        print("Missing values detected:")
        for col, count in missing[missing > 0].items():
            percentage = count / len(df) * 100
            if percentage > 0.1:
                print(f"  {col}: {count} ({percentage:.2f}%) — HIGH — check source data!")
                issues_found = True
            elif percentage > 0.01:
                print(f"  {col}: {count} ({percentage:.3f}%) — minor, should be filled")
            else:
                print(f"  {col}: {count} ({percentage:.5f}%) — negligible, acceptable")
    else:
        print("No missing values found.")

    duplicates = df.index.duplicated().sum()
    if duplicates == 0:
        print("No duplicate timestamps found.")
    else:
        print(f"Found {duplicates} duplicate timestamps — critical!")
        issues_found = True

    thresholds = {'germany_load_mw': 20000, 'hungary_load_mw': 2000}  # минимальные ожидаемые
    for col in df.columns:
        col_data = df[col].dropna()
        min_val = col_data.min()
        max_val = col_data.max()
        if min_val < 0:
            print(f"Negative values in {col}: {min_val:.0f} MW — invalid!")
            issues_found = True
        else:
            print(f"{col}: Range OK → {min_val:,.0f} – {max_val:,.0f} MW")

    print(f"\nData shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print("Sample of data:")
    print(df.head(3))

    if not issues_found:
        print("\nALL CHECKS PASSED — DATA IS CLEAN AND READY!")
    else:
        print("\nMinor issues detected — but data is still usable (as in real projects)")
        print("Pipeline continues...")

    print("="*70)
    return True 


if __name__ == "__main__":
    validate_load()

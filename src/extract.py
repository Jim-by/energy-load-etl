import os
import requests

DATA_URL = ("https://data.open-power-system-data.org/time_series/2020-10-06/time_series_15min_singleindex.csv")

RAW_DIR = os.path.join("data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

def download_timeseries():
    filename = os.path.join(RAW_DIR, "time_series_15min_singleindex.csv")
    if os.path.exists(filename):
        print(f"File already exists: {filename}")
        return filename
    
    print("Downloading data...")
    resp = requests.get(DATA_URL, timeout=60)
    resp.raise_for_status()

    with open(filename, "wb") as f:
        f.write(resp.content)

    print(f"Saved to {filename}")
    return filename

if __name__ =="__main__":
    download_timeseries()

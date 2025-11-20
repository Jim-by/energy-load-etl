# Energy Load ETL & Analysis Pipeline

## Description
ETL pipeline for analyzing 15-minute time series of power grid loads in Germany (DE) and Hungary (HU) from the Open Power System Data (OPSD). Demonstrates skills in working with pandas, requests, and matplotlib/seaborn: downloading, transformation (datetime, NaN interpolation), validation (missing, duplicates, outliers), and visualization (daily/hourly trends).

- **Data**: ~201k rows, 2014-2020, load in MW.
- **Output**: Processed CSV + graphs in plots/(daily_load.png, hourly_seasonality.png).
- **Insights**: Average DE load ~55 GW (HU ~5 GW); correlation ~0.8 (synchronization); peaks in winter/summer.

# Structure
- `src/extract.py`: Download raw CSV.
- `src/transform.py`: Column selection, datetime, NaN interpolation.
- `src/validate.py`: Validations (NaN <1%, no dups, thresholds).
- `src/analyze.py`: Statistics + Seaborn graphs.
- `src/main.py`: Orchestrator (4 steps).

## Run
1. `pip install pandas requests matplotlib seaborn`
2. `python src/main.py` — full pipeline (download/process/validate/analyze).
3. Results: `data/processed/processed_load_data.csv` + `plots/*.png`.

## Analysis example
DE-HU correlation: 0.XXX. Peaks: DE 77 GW (winter), HU 6.8 GW. Seasonality: Morning/evening increase.

## Analysis example
DE-HU correlation: 0.XXX. Peaks: DE 77 GW (winter), HU 6.8 GW. Seasonality: Morning/evening growth.

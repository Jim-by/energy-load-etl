# Energy Load ETL & Analysis Pipeline

## Description
ETL pipeline for analyzing 15-minute time series of power grid loads in Germany (DE) and Hungary (HU) from the Open Power System Data (OPSD). Demonstrates core data analyst skills: working with pandas for data manipulation, requests for data retrieval, and matplotlib/seaborn for visualization. The pipeline covers:
- Automated data downloading from a public source
- Data transformation (datetime parsing, column selection, NaN interpolation)
- Quality validation (missing values, duplicate timestamps, outlier detection)
- Exploratory analysis and trend visualization (daily/hourly seasonality)

- **Data**: ~201k rows of 15-minute load data (2014–2020), measured in MW.
- **Output**: Cleaned processed CSV + visualization graphs stored in `plots/` (daily_load.png, hourly_seasonality.png).

## How to Run the Project

This project automatically downloads the raw dataset (~100 MB) from Open Power System Data (OPSD) — no manual file downloads required!

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/energy-load-etl.git
   cd energy-load-etl
   ```

2. Install required dependencies:
   ```bash
   pip install pandas requests matplotlib seaborn
   ```

3. Run the full pipeline (download → process → validate → analyze):
   ```bash
   python src/main.py
   ```

### Results:
- Cleaned analysis-ready dataset: `data/processed/processed_load_data.csv`
- Visualization graphs: 
  - `plots/daily_load.png` (long-term daily load trends for DE/HU)
  - `plots/hourly_seasonality.png` (average load patterns by hour of day)

## Project Structure
- `src/extract.py`: Automatically fetches the raw time series CSV from the OPSD public repository.
- `src/transform.py`: Filters relevant columns, parses UTC datetime, and interpolates missing values.
- `src/validate.py`: Validates data quality (missing values < 0.01%, no duplicate timestamps, realistic load thresholds).
- `src/analyze.py`: Computes key statistics and generates Seaborn visualizations.
- `src/main.py`: Orchestrates the end-to-end 4-step pipeline execution.
- `data/raw/`: Stores the downloaded raw dataset (auto-created on first run).
- `data/processed/`: Stores the cleaned, structured dataset (auto-created).
- `plots/`: Stores generated visualization outputs (auto-created).
- `LICENSE`: MIT License (permits free use, modification, and distribution).
- `README.md`: Project documentation and usage guide.

## Key Analysis Insights
- **Load Magnitudes**: Average load ~55.5 GW (Germany) and ~4.85 GW (Hungary); peak loads reach 77.9 GW (Germany, winter) and 6.82 GW (Hungary).
- **Correlation**: ~0.82 between German and Hungarian load profiles (indicates synchronized energy consumption patterns across regions).
- **Seasonality**: Clear daily peaks (morning and evening usage spikes) and seasonal trends (winter peak due to heating, minor summer peak due to cooling demand).

## License
This project is licensed under the MIT License — see the `LICENSE` file for full details.

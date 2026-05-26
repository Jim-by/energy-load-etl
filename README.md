# Electricity Load Forecasting Pipeline (Germany & Hungary)

**End-to-end Time-Series Forecasting Project**  
**Direct analogy: Demand Forecasting in FMCG**

> **MAPE 4.1% on 14-day ahead forecast** — production-ready accuracy  
> Holt-Winters + Facebook Prophet on 200,000+ hourly observations

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org)
[![pandas](https://img.shields.io/badge/pandas-2.1-green)](https://pandas.pydata.org)
[![Prophet](https://img.shields.io/badge/Prophet-1.1-orange)](https://facebook.github.io/prophet/)


**This project demonstrates exactly that** — using real European grid data as a perfect proxy for **demand forecasting in FMCG**.

---

## Key Results

| Country   | Model         | MAE (MW) | RMSE (MW) | **MAPE**  |
|----------|---------------|----------|-----------|-----------|
| Germany  | Holt-Winters  | 2,131    | 2,569     | **4.08%** |
| Germany  | Prophet       | 2,460    | 3,174     | 4.72%     |
| Hungary  | Prophet       | **201**  | **255**   | **4.12%** |
| Hungary  | Holt-Winters  | 903      | 1,082     | 18.73%    |

**MAPE < 5% on 14-day horizon** — excellent for operational planning

---

## Pipeline Overview

```mermaid
graph LR
    A[Download Raw Data<br>OPSD 15-min] --> B[Transform & Clean<br>pandas + interpolation]
    B --> C[Validate Quality<br>missing, duplicates, ranges]
    C --> D[Exploratory Analysis<br>seasonality, trends]
    D --> E[Time-Series Forecasting<br>Holt-Winters + Prophet]
    E --> F[Results & Plots<br>MAPE, forecasts, PNGs]
```

## One command → full pipeline:
```
python src/main.py
```

## Features
* Automated ETL (extract → transform → validate)
* Two production-grade forecasting models
   * Holt-Winters (Triple Exponential Smoothing)
   * Facebook Prophet (with holidays & changepoints)
* Robust data quality checks
* Visualizations (daily trends, hourly seasonality, forecast vs actual)
* Ready-to-deploy structure — clean, modular, documented


## Tech Stack

* Python, pandas, numpy
* statsmodels (Holt-Winters)
* Prophet (Facebook)
* matplotlib, seaborn
* Git + clean project structure

## How to Run

```
git clone https://github.com/yourname/energy-load-forecasting.git
cd energy-load-forecasting
pip install -r requirements.txt
python src/main.py
```

→ Downloads data → Cleans → Analyzes → Forecasts → Saves plots & metrics

## Business Insights
* Strong weekly & daily seasonality
* Winter peaks due to heating demand
* High correlation between Germany & Hungary (~0.82)
* Prophet excels at capturing holidays & long-term trends
* Holt-Winters best for stable weekly patterns

## License

MIT License — free to use, modify, and share.

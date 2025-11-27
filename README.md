# Electricity Load Forecasting Pipeline (Germany & Hungary)

**End-to-end Time-Series Forecasting Project**  
**Direct analogy: Demand Forecasting in FMCG (Nestlé, Unilever, P&G)**

> **MAPE 4.1% on 14-day ahead forecast** — production-ready accuracy  
> Holt-Winters + Facebook Prophet on 200,000+ hourly observations

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org)
[![pandas](https://img.shields.io/badge/pandas-2.1-green)](https://pandas.pydata.org)
[![Prophet](https://img.shields.io/badge/Prophet-1.1-orange)](https://facebook.github.io/prophet/)

## Why This Project Matters for Nestlé

Nestlé's **EU-wide forecasting solutions** require:
- Maintaining & improving existing time-series models
- Experimenting with new forecasting approaches
- Clear communication of results to non-technical stakeholders

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

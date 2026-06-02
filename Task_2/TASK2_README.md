# Task 2 — Predict Future Stock Prices

## Objective
The goal of this task was to predict the next day's closing price of Apple stock (AAPL) using historical stock data. I fetched live data using the `yfinance` API and trained two regression models to see how accurately they can predict tomorrow's price based on today's market data.

---

## Dataset
**Apple (AAPL) stock data**  — from **January 2020 to May 2026** — pulled directly from Yahoo Finance using `yfinance`. No manual download needed, the library fetches it straight from the API.

- Total rows: 1,610 trading days
- Total columns: 5
- Columns: Open, High, Low, Close, Volume
- No missing values in any column
- Features used for training: Open, High, Low, Close, Volume


**Libraries Used**

| Library | Purpose |
|---|---|
| `yfinance` | Fetch live stock data from Yahoo Finance API |
| `matplotlib` | Plot actual vs predicted stock prices |
| `scikit-learn` | Model training, train/test split, and accuracy evaluation |

---

## What I Did

**Data Preprocessing**
- Created a new column `Target_Close` using `shift(-1)` — this moves the closing price one day forward so the model learns to predict the next day's price
- Dropped the last row since it had no target value (NaN after shifting)
- Split data into 80% training and 20% testing


**Data Exploration**
- Checked column names and data structure using `info()`
- Verified the dataset shape — 1,610 rows and 5 columns
- Confirmed no missing values after preprocessing


**Models Applied**

| Model | Accuracy (R2 Score) |
|---|---|
| Linear Regression | 99.59% |
| Random Forest Regressor | 99.52% |

Trained both models on the same data and compared their predictions against actual prices using a graph.

---

## Key Results & Findings
- Both models performed really well with over 99% accuracy
- Linear Regression slightly outperformed Random Forest — this makes sense because stock prices have a strong linear relationship with features like Open, High, and Low
- The predicted prices follow the actual prices very closely as visible in the comparison graph
- Overall both models are suitable for short term stock price prediction but Linear Regression is the better choice here since it is simpler and more accurate on this dataset

---

## Files

| File | Description |
|---|---|
| `Predict_Future_Stock_Prices.ipynb` | Jupyter Notebook |

---

## Links
🐍 [View Python Script](Predict Future Stock Prices.ipynb)


# Stock Portfolio Performance Tracker

A Python-based investment portfolio tracking utility developed during the Datheon Engineering Cohort 2026.

## Features
- Add stock ticker symbols.
- Record purchase prices and share quantities.
- Retrieve the latest available stock prices using Yahoo Finance.
- Calculate individual stock profit and loss.
- Calculate percentage gains and losses.
- Calculate total portfolio performance.
- Store portfolio positions permanently using CSV files.
- Save performance history to a CSV file.

## Technologies Used
- Python 3
- yfinance
- CSV module
- File handling

## How to Run

1. Install Python 3.
2. Install the required library:

```bash
pip install yfinance
```

3. Run the program:

```bash
python portfolio.py
```

## Output Files
- `portfolio.csv` – Stores portfolio positions.
- `portfolio_summary.csv` – Stores performance logs.

**Note:** Stock prices are retrieved from Yahoo Finance and represent the latest available market data, which may be delayed.

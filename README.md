# Dividend Tracker

A small tracker for dividend income: total received, income by stock, income by month, and yield on cost for each holding.

## Why I built this

I follow Indian dividend stocks as part of learning how markets work, and the number I actually want each year is simple — how much cash came back, and from which holding. This script turns a short list of payouts into that answer.

## What it does

Reads `dividends.csv` (stock, ex-date, shares, cost per share, dividend per share — 8 sample payouts, May–Dec 2026) and prints:

- Total dividend income and yield on cost
- Income and yield by stock
- Income by month

The numbers are sample data for practice, not a real portfolio and not a recommendation to buy or sell anything.

## How to run

```bash
cd dividend-tracker
python dividend_tracker.py
```

Point it at your own payouts by replacing `dividends.csv` (keep the same columns).

## Sample output

```
Dividend tracker - 8 payouts
Period: 2026-05-15 to 2026-12-05
----------------------------------------------------
Total dividend income: 9,480 INR
Cost of holdings:      316,000 INR
Yield on cost:         3.00%

By stock:
Stock         Payouts      Income    Yield
COALINDIA           1       3,600    6.32%
ITC                 2       2,800    3.33%
HDFCBANK            2       1,450    1.71%
INFY                2       1,080    1.80%
POWERGRID           1         550    1.83%

By month:
  2026-05:      1,670 INR
  2026-06:      1,500 INR
  2026-08:      3,600 INR
  2026-09:        550 INR
  2026-11:        860 INR
  2026-12:      1,300 INR
```

(Data is sample data created for practice.)

## Files

- `dividend_tracker.py` — the program
- `dividends.csv` — sample payouts (8 rows)

## Next steps

- Add a yearly total, so each year's income is one line
- Compare dividend income with the same money in a fixed deposit
- Track dividend growth per stock, year over year

*Standard library only for now. Built while learning Python.*

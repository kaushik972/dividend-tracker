"""
Dividend Tracker
----------------
Practice project. Reads a list of dividends received (stock, date,
shares held, cost per share, dividend per share) and summarises it:
total dividend income, income by stock, income by month, and the yield
on cost for each holding.

The numbers are sample data for practice, not a real portfolio and not
a recommendation to buy or sell anything.

Built by Shivam Kaushik while learning Python.
Standard library only (csv).
"""

import csv

DIVIDENDS_FILE = "dividends.csv"


def load_dividends(filename):
    rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            shares = int(row["shares"])
            rows.append({
                "stock": row["stock"], "date": row["ex_date"],
                "month": row["ex_date"][:7], "shares": shares,
                "cost": shares * float(row["cost_per_share_inr"]),
                "income": shares * float(row["dividend_per_share_inr"]),
                "per_share": float(row["dividend_per_share_inr"]),
            })
    return rows


def main():
    rows = load_dividends(DIVIDENDS_FILE)
    total_income = sum(r["income"] for r in rows)
    total_cost = sum({r["stock"]: r["cost"] for r in rows}.values())
    print(f"Dividend tracker - {len(rows)} payouts")
    print(f"Period: {rows[0]['date']} to {rows[-1]['date']}")
    print("-" * 52)
    print(f"Total dividend income: {total_income:,.0f} INR")
    print(f"Cost of holdings:      {total_cost:,.0f} INR")
    print(f"Yield on cost:         {total_income / total_cost:.2%}")

    by_stock = {}
    for r in rows:
        s = by_stock.setdefault(r["stock"], {"payouts": 0, "income": 0.0, "cost": r["cost"]})
        s["payouts"] += 1
        s["income"] += r["income"]

    print("\nBy stock:")
    print(f"{'Stock':<12}{'Payouts':>9}{'Income':>12}{'Yield':>9}")
    for name, s in sorted(by_stock.items(), key=lambda i: i[1]["income"], reverse=True):
        print(f"{name:<12}{s['payouts']:>9,}{s['income']:>12,.0f}{s['income'] / s['cost']:>9.2%}")

    by_month = {}
    for r in rows:
        by_month[r["month"]] = by_month.get(r["month"], 0.0) + r["income"]
    print("\nBy month:")
    for month in sorted(by_month):
        print(f"  {month}: {by_month[month]:>10,.0f} INR")


if __name__ == "__main__":
    main()

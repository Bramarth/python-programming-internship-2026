

import yfinance as yf
import csv
import os
from datetime import datetime

# Store portfolio positions
portfolio = {}


# Load previously saved portfolio positions
def load_portfolio():
    if not os.path.exists("portfolio.csv"):
        return

    with open("portfolio.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            portfolio[row["Ticker"]] = {
                "buy_price": float(row["Buy Price"]),
                "quantity": int(row["Quantity"])
            }


# Save portfolio positions permanently
def save_portfolio():
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Ticker", "Buy Price", "Quantity"])

        for ticker, details in portfolio.items():
            writer.writerow([
                ticker,
                details["buy_price"],
                details["quantity"]
            ])


def add_stock():
    ticker = input("Enter stock ticker (e.g. AAPL): ").upper().strip()

    if not ticker:
        print("Please enter a stock ticker.")
        return

    try:
        buy_price = float(input("Enter purchase price per share ($): "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero.")
            return

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity
        }

        save_portfolio()

        print(f"{ticker} added successfully!")

    except ValueError:
        print("Please enter valid numbers.")


def track_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_invested = 0
    total_value = 0

    results = []

    print("\n========== PORTFOLIO SUMMARY ==========")

    for ticker, details in portfolio.items():
        try:
            stock = yf.Ticker(ticker)
            history = stock.history(period="5d")

            if history.empty or history["Close"].dropna().empty:
                print(f"Could not retrieve price for {ticker}. Skipping.")
                continue

            price = history["Close"].dropna().iloc[-1]

            buy_price = details["buy_price"]
            quantity = details["quantity"]

            invested = buy_price * quantity
            current_value = float(price) * quantity
            profit_loss = current_value - invested
            percentage = (profit_loss / invested) * 100

            total_invested += invested
            total_value += current_value

            print(f"\nStock: {ticker}")
            print(f"Purchase price: ${buy_price:.2f}")
            print(f"Current price: ${price:.2f}")
            print(f"Quantity: {quantity}")
            print(f"Profit/Loss: ${profit_loss:.2f}")
            print(f"Performance: {percentage:.2f}%")

            results.append([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ticker,
                buy_price,
                float(price),
                quantity,
                invested,
                current_value,
                profit_loss,
                percentage
            ])

        except Exception as error:
            print(f"Could not retrieve price for {ticker}: {error}")

    if not results:
        print("No stock prices could be retrieved.")
        return

    total_profit = total_value - total_invested

    print("\n========== TOTAL PORTFOLIO ==========")
    print(f"Total invested: ${total_invested:.2f}")
    print(f"Current value: ${total_value:.2f}")
    print(f"Total profit/loss: ${total_profit:.2f}")
    print(f"Overall performance: {(total_profit / total_invested) * 100:.2f}%")

    # Save performance results to CSV
    file_exists = os.path.isfile("portfolio_summary.csv")

    with open("portfolio_summary.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date", "Ticker", "Buy Price", "Current Price",
                "Quantity", "Invested", "Current Value",
                "Profit/Loss", "Performance (%)"
            ])

        writer.writerows(results)

    print("\nPortfolio performance saved to portfolio_summary.csv")


def main():
    # Load saved stocks when the program starts
    load_portfolio()

    while True:
        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add stock")
        print("2. View portfolio performance")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            track_portfolio()
        elif choice == "3":
            print("Thank you for using the tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

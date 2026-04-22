# Binance Futures Testnet Bot

This is a simple Python trading bot that can place **Market** and **Limit** orders on Binance Futures Testnet (USDT-M).

I built this as part of a hiring assignment to demonstrate API integration, CLI handling, logging, and basic structure.

---

## What it can do

* Place Market orders
* Place Limit orders
* Supports both BUY and SELL
* CLI-based usage
* Basic input validation
* Logs API requests and responses

---

## Project structure


bot/
  client.py
  orders.py
  logging_config.py


cli.py
test_connection.py
test_order.py
test_limit_order.py


---

## Setup

Clone the repo:

git clone https://github.com/yash-skl/Binance-futures-testnet-bot.git
cd Binance-futures-testnet-bot

Create virtual environment:

python -m venv myenv
myenv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## Environment variables

Create a .env file in root:

BINANCE_API_KEY=your_api_key

BINANCE_SECRET_KEY=your_secret_key

---

## How to run

### Market order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 70000

---

## Interactive mode (extra)

You can also run the script without CLI arguments:
python cli.py

It will prompt you to enter inputs step by step (symbol, side, order type, etc.).

---

## Example output

=== Order Request ===
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

=== Order Response ===
Order ID: 13062323834
Status: FILLED
Executed Qty: 0.0010
Avg Price: 78790.800000

---

## Logs

Logs are generated locally in:

logs/trading.log

Below are sample logs from actual runs:

### Market Order Log

2026-04-22 23:03:45 INFO Placing MARKET order | BTCUSDT BUY 0.001
2026-04-22 23:03:46 INFO Response: {'orderId': 13062310523, 'status': 'FILLED', 'executedQty': '0.0010'}

### Limit Order Log

2026-04-22 23:05:12 INFO Placing LIMIT order | BTCUSDT BUY 0.001 @ 70000
2026-04-22 23:05:13 INFO Response: {'orderId': 13062270569, 'status': 'NEW', 'executedQty': '0.0000'}

---

## Assumptions

* Binance Futures Testnet account is already set up
* API keys are valid and enabled for futures
* Only USDT-M futures are used

---

## Requirements

Install using:

pip install -r requirements.txt

---

## Notes

* Market orders get filled immediately
* Limit orders may stay open depending on price
* Logging helps track API responses and debug issues

---

## Dependencies

* python-binance
* python-dotenv

---

## Author

Yash Shukla

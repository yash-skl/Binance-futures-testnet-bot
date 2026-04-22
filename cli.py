import argparse
from bot.orders import place_market_order, place_limit_order
import time
from bot.client import client
import sys


def validate_inputs(args):
    # Quantity validation
    if args.quantity <= 0:
        print("Error: Quantity must be greater than 0")
        return False

    # Limit order validation
    if args.type == "LIMIT":
        if args.price is None:
            print("Error: LIMIT order requires --price")
            return False
        if args.price <= 0:
            print("Error: Price must be greater than 0")
            return False

    return True


def interactive_mode():
    print("\n=== Binance Futures Trading Bot ===")

    symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()
    
    side = input("Enter Side (BUY/SELL): ").upper()
    while side not in ["BUY", "SELL"]:
        side = input("Invalid. Enter BUY or SELL: ").upper()

    order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()
    while order_type not in ["MARKET", "LIMIT"]:
        order_type = input("Invalid. Enter MARKET or LIMIT: ").upper()

    quantity = float(input("Enter Quantity: "))
    
    price = None
    if order_type == "LIMIT":
        price = float(input("Enter Price: "))

    return symbol, side, order_type, quantity, price


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    # 👉 Check if no CLI args → use interactive mode
    if len(sys.argv) == 1:
        symbol, side, order_type, quantity, price = interactive_mode()

        class Args:
            pass

        args = Args()
        args.symbol = symbol
        args.side = side
        args.type = order_type
        args.quantity = quantity
        args.price = price

    else:
        args = parser.parse_args()

        # Ensure required args in CLI mode
        if not all([args.symbol, args.side, args.type, args.quantity]):
            print("Error: Missing required arguments")
            return

    print("\n=== Order Request ===")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.type == "LIMIT":
        print(f"Price: {args.price}")

    # Validation
    if not validate_inputs(args):
        return

    # Place order
    if args.type == "MARKET":
        response = place_market_order(args.symbol, args.side, args.quantity)
    else:
        response = place_limit_order(args.symbol, args.side, args.quantity, args.price)

    print("\n=== Order Response ===")

    if response:
        order_id = response.get("orderId")

        time.sleep(2)

        updated_order = client.futures_get_order(
            symbol=args.symbol,
            orderId=order_id
        )

        print(f"Order ID: {updated_order.get('orderId')}")
        print(f"Status: {updated_order.get('status')}")
        print(f"Executed Qty: {updated_order.get('executedQty')}")
        print(f"Avg Price: {updated_order.get('avgPrice')}")
    else:
        print("Order failed")


if __name__ == "__main__":
    main()
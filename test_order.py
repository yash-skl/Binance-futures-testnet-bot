import time
from bot.orders import place_market_order
from bot.client import client

client.futures_change_leverage(symbol="BTCUSDT", leverage=10)

order = place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

print("Initial Order:", order)

time.sleep(2)

updated_order = client.futures_get_order(
    symbol="BTCUSDT",
    orderId=order["orderId"]
)

print("Updated Order:", updated_order)
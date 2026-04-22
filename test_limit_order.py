from bot.orders import place_limit_order

response = place_limit_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001,
    price="70000"   
)

print(response)
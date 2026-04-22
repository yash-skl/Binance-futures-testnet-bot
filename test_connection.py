# test_connection.py
from bot.client import client

balance = client.futures_account_balance()
print(balance)
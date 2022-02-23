import requests


url = "https://khalti.com/api/v2/payment/verify/"
payload = {
    "token": "QUao9cqFzxPgvWJNi9aKac",
    "amount": 1000
}
headers = {
    "Authorization": "Key test_secret_key_f59e8b7d18b4499ca40f68195a846e9b"
}

response = requests.post(url, payload, headers=headers)

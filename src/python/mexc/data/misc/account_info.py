import requests
import time
import hashlib
import hmac
from pathlib import Path
import json5
import json

# Load API keys
home_dir = Path.home()
with open(f"{home_dir}/CRYPTO-Trader/src/dist/apikey-crypto.json", "r") as file:
    config = json5.load(file)

API_KEY = config.get("key")
SECRET_KEY = config.get("secret")

# 📥 Endpoint for account info
url = 'https://api.mexc.com/api/v3/account'

# 📅 Generate timestamp
timestamp = int(time.time() * 1000)

# 🔗 Build the query string
query_string = f'timestamp={timestamp}'

# 🖊️ Sign the request
signature = hmac.new(
    SECRET_KEY.encode('utf-8'),
    query_string.encode('utf-8'),
    hashlib.sha256
).hexdigest()

# 📦 Add the signature to the query string
query_string += f'&signature={signature}'

# 📤 Make the request
headers = {
    'X-MEXC-APIKEY': API_KEY
}

response = requests.get(url, headers=headers, params={'timestamp': timestamp, 'signature': signature})

# 📋 Print the response
if response.status_code == 200:
    print("Account Info:")
    print(json.dumps(response.json(), indent=4, sort_keys=True))
else:
    print(f"Error: {response.status_code}")
    print(response.text)

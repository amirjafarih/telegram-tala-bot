import requests
import time
from datetime import datetime

url = "https://www.drbobshome.org/about/dr-bobs-library-copy/"  # آدرس سایتت

while True:
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{now}] Site status: {status_code}")

    except requests.exceptions.RequestException as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Error connecting to site: {e}")

    time.sleep(0.01)  # 2 دقیقه

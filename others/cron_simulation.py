import requests
import time

while True:
    time.sleep(60)
    req = requests.get('http://127.0.0.1:5000/cron')
    print(req.text)

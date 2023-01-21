import datetime
import json
import requests
import time

dict_of_urls = {
    "maria.ru": "http://maria.ru/api/count",
    "rose.ru": "http://rose.ru/api/count",
    "sina.ru": "http://sina.ru/api/count"
}

while True:
    current_time = datetime.datetime.now()
    current_time = current_time.replace(second=0, microsecond=0)
    for key, value in dict_of_urls.items():
        resp = requests.get(value).json()
        resp_as_dict = json.load(resp)
        print(current_time, key, resp_as_dict["count"])
    time.sleep(60)

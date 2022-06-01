import time
from datetime import datetime as dt

host_path = "etc/hosts"
redirect = "127.0.0.1"
website_list = ["https://www.youtube.com","https://yandex.ru","https://www.tiktok.com/?!",""]

while True:
    ymd = (dt.now().year, dt.now().month, dt.now().day)
    if dt(*ymd, 5) < dt.now() < dt(*ymd,22):
        print("Bloced")
    else:
        print("OK")
    time.sleep(5)

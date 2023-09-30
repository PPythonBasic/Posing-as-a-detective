try:
    import requests
except:
    import os
    os.system('pip install requests')

import json


def pull_database_suspect():
    """
    ฟังก์ชันดึงข้อมูลจากฐานข้อมูลผู้ต้องสงสัย API https://ppythonbasic.github.io/apis/suspects.json
    """
    response = requests.get("https://ppythonbasic.github.io/apis/suspects.json").text
    response_json = json.loads(response)
    list_respone = response_json["suspects"]
   
    for i in list_respone:
        if i["gender"] == "female":
            print(i["name"])
            

            
def run_code():
    pull_database_suspect()

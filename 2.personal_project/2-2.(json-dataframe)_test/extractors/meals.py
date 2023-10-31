# 전국 초중고 급식정보
import requests
from school_code import get_school_code
from datetime import datetime
import json
import pandas as pd
import sqlite3

def get_meal(school_name):
    api_key = 'f468427a1c1b4faea6e3b3626c2b53ad' # 나이스 교육정보 개방포털 api key
    data_type = 'json'    
    schools = get_school_code(school_name)
    meal_month = datetime.today().strftime("%Y%m")
    
    results = pd.DataFrame()
    
    for school in schools:
        office_code = school['office_code']
        school_code = school['school_code']

        params = {
            'Key': api_key,
            'Type': data_type,
            'pIndex': 1,
            'pSize': 1000,
            'ATPT_OFCDC_SC_CODE': office_code,
            'SD_SCHUL_CODE': school_code,
            'MLSV_YMD': meal_month
        }

        base_url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
        meal_info = "mealServiceDietInfo"
        response = requests.get(base_url, params=params)
        json_data = None
        
        if response.status_code != 200 :
            print("Can't access the information")
        else:
            json_data = response.json()
            df = pd.DataFrame(json_data[meal_info][1]['row'])
            pd.concat([df, results])

    
    return results


test = get_meal("기장")
print(test)

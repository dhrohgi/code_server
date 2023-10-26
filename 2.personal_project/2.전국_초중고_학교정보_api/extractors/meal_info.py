# 전국 초중고 급식정보

import requests
import json
from extractors.school_code import get_school_code
from datetime import datetime

def get_meal():
    api_key = 'c5dd73feb40b45d695c4c042cbd0d041' # 나이스 교육정보 개방포털 api key
    data_type = 'json'
    school_name = input('조회할 학교명?')
    meal_month = datetime.today().strftime("%Y%m")
    schools = get_school_code(school_name)
    
    results = []
    
    for school in schools:
        
        office_code = school['office_code']
        school_code = school['school_code']

        param_dict = {}
        param_dict.setdefault('Key', api_key)
        param_dict.setdefault('Type', data_type)
        param_dict.setdefault('pIndex', 1)
        param_dict.setdefault('pSize', 100)
        param_dict.setdefault('ATPT_OFCDC_SC_CODE', office_code)
        param_dict.setdefault('SD_SCHUL_CODE', school_code)
        param_dict.setdefault('MLSV_YMD', meal_month)

        base_url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

        response = requests.get(base_url, params=param_dict)
        json_data = None


        if response.status_code != 200 :
            print("Can't access the information")
        else:
            json_data = response.json()
            
            if next(iter(json_data)) == "mealServiceDietInfo":
                meals = json_data['mealServiceDietInfo'][1]['row']
                for meal in meals:
                    meal_data = {
                        "school_name": meal["SCHUL_NM"],
                        "date": meal["MLSV_YMD"],
                        "dish_name": meal["DDISH_NM"],
                        "calory": meal["CAL_INFO"]
                    }
                    if meal_data not in results:
                        results.append(meal_data)            
    return results

# 전국 초중고 급식정보
import requests
from extractors.school_code import get_school_code
from datetime import datetime

def get_meal(school_name):
    api_key = 'f468427a1c1b4faea6e3b3626c2b53ad' # 나이스 교육정보 개방포털 api key
    data_type = 'json'    
    schools = get_school_code(school_name)
    meal_month = datetime.today().strftime("%Y%m")
    
    results = []
    
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
            first_key = list(json_data.keys())[0]
            
            if first_key == meal_info:
                meals = json_data[meal_info][1]['row']
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

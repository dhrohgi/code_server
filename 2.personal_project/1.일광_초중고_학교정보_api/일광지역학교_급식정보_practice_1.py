# 일광지역학교 급식정보

import requests
import json


def get_school_code(number):
    code = '7211240'
    if number == '1':
        code = '7211240' # 일광초등학교
        return code
    elif number == '2':
        code = '7211243' # 해빛초등학교
        return code
    elif number == '3':
        code = '7211242' # 일광중학교
        return code
    else:
        return code


api_key = 'c5dd73feb40b45d695c4c042cbd0d041' # 나이스 교육정보 개방포털 api key
data_type = 'json'
office_code = "C10"
school_num = input('조회할 학교를 선택하세요!(1=일광초, 2=해빛초, 3=일광중): ')
school_code = get_school_code(school_num)
meal_month = input('조회할 연월을 입력하세요!(ex. 202310): ')


header_dict = {}
header_dict.setdefault('KEY', api_key)
param_dict = {}
param_dict.setdefault('KEY', api_key)
param_dict.setdefault('Type', data_type)
param_dict.setdefault('pIndex', 1)
param_dict.setdefault('pSize', 100)
param_dict.setdefault('ATPT_OFCDC_SC_CODE', office_code)
param_dict.setdefault('SD_SCHUL_CODE', school_code)
param_dict.setdefault('MLSV_YMD', meal_month)

base_url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

request_data = requests.get(base_url, headers=header_dict, params=param_dict)
json_data = None

if request_data.status_code == 200 :
    json_data = request_data.json()
    for i in range(0, 19) :
        dish_date = json_data['mealServiceDietInfo'][1]['row'][i]['MLSV_YMD']
        dish_name = json_data['mealServiceDietInfo'][1]['row'][i]['DDISH_NM']
        school_name = json_data['mealServiceDietInfo'][1]['row'][i]['SCHUL_NM']
        calory_info = json_data['mealServiceDietInfo'][1]['row'][i]['CAL_INFO']
        trimed_name = dish_name.replace('<br/>', '\n')
        print(f'📌 {dish_date} {school_name}')
        print(trimed_name)
        print('-> 총칼로리 :', calory_info, '\n')




# 일광지역학교 시간표정보

import requests
import json
from extractors.school_code import get_school_code
from datetime import datetime

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
school_num = input('학교를 선택하세요!(1=일광초, 2=해빛초, 3=일광중): ')
school_semester = input('학기를 입력하세요!(1=1학기, 2=2학기): ')
school_grade = input('학년을 입력하세요!(1=1학년, 2=2학년, 3=3학년...)')
school_class = input('반을 입력하세요!(1=1반, 2=2반, 3=3반...)')
school_date = input('날짜를 입력하세요!(ex. 20231023)')
school_year = school_date[0:4]
school_code = get_school_code(school_num)

header_dict = {}
header_dict.setdefault('Key', api_key)
param_dict = {}
param_dict.setdefault('Key', api_key)
param_dict.setdefault('Type', data_type)
param_dict.setdefault('pIndex', 1)
param_dict.setdefault('pSize', 100)
param_dict.setdefault('ATPT_OFCDC_SC_CODE', office_code)
param_dict.setdefault('SD_SCHUL_CODE', school_code)
param_dict.setdefault('AY', school_year)
param_dict.setdefault('SEM', school_semester)
param_dict.setdefault('GRADE', school_grade)
param_dict.setdefault('CLASS_NM', school_class)
param_dict.setdefault('ALL_TI_YMD', school_date)

base_url_els = "https://open.neis.go.kr/hub/elsTimetable"
base_url_mis = "https://open.neis.go.kr/hub/misTimetable"
base_url_his = "https://open.neis.go.kr/hub/hisTimetable"
final_url = None

if school_num == "1" or school_num == "2":
    final_url = base_url_els
elif school_num == "3":
    final_url = base_url_mis


response = requests.get(final_url, headers=header_dict, params=param_dict)
json_data = None

if response.status_code != 200 :
    print("Can't access the information")
else:
    json_data = response.json()
    results = []
    if next(iter(json_data)) == "elsTimetable":
        subjects = json_data["elsTimetable"][1]['row']
        for subject in subjects:
            subject_data = {
                "school_name" : subject["SCHUL_NM"],
                "date" : subject["ALL_TI_YMD"],
                "perio" : subject["PERIO"],
                "subject_name" : subject["ITRT_CNTNT"]
            }
            results.append(subject_data)
    elif next(iter(json_data)) == "misTimetable":
        subjects = json_data["misTimetable"][1]['row']
        for subject in subjects:
            subject_data = {
                "school_name" : subject["SCHUL_NM"],
                "date" : subject["ALL_TI_YMD"],
                "perio" : subject["PERIO"],
                "subject_name" : subject["ITRT_CNTNT"]
            }
            results.append(subject_data)
    else:
        print("😩 class subject information wasn't uploaded yet!")

    
    for result in results:
        print(f"{result["perio"]}교시:{result['subject_name']}")
    

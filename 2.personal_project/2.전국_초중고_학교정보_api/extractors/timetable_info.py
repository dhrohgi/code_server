# 전국 초중고 시간표정보

import requests
import json
from extractors.school_code import get_school_code
from datetime import datetime

def get_timetable():

    api_key = 'c5dd73feb40b45d695c4c042cbd0d041' # 나이스 교육정보 개방포털 api key
    data_type = 'json'
    school_name = input('조회할 학교명?')
    code = get_school_code(school_name)
    office_code = code[0]['office_code']
    school_code = code[0]['school_code']
    school_grade = input('학년을 입력하세요!(1=1학년, 2=2학년, 3=3학년...)')
    school_class = input('반을 입력하세요!(1=1반, 2=2반, 3=3반...)')
    school_semester = ""
    school_date = datetime.today().strftime("%Y%m%d")
    school_year = school_date[0:4]

    if int(school_date) < int(f"{datetime.today().strftime('%Y')}0701"):
        school_semester = 1
    else:
        school_semester = 2

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

    if "초등학교" in code[0]['school_name'] or "(초)" in code[0]['school_name']:
        final_url = base_url_els
    elif "중학교" in code[0]['school_name'] or "(중)" in code[0]['school_name']:
        final_url = base_url_mis
    elif "고등학교" in code[0]['school_name'] or "(고)" in code[0]['school_name']:
        final_url = base_url_his


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
        elif next(iter(json_data)) == "hisTimetable":
            subjects = json_data["hisTimetable"][1]['row']
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
            print(f"{result['perio']}교시:{result['subject_name']}")
        

# 전국 초중고 시간표정보
import requests
from extractors.school_code import get_school_code
from datetime import datetime, date, timedelta

def get_timetable(school_name):
    api_key = '2349feb6b7134d43831f415416e58d88' # 나이스 교육정보 개방포털 api key
    data_type = 'json'
    schools = get_school_code(school_name)
    school_date = datetime.today().strftime("%Y%m%d")
    school_year = school_date[0:4]
    school_semester = None
    if int(school_date) < int(f"{datetime.today().strftime('%Y')}0701"):
            school_semester = 1
    else:
        school_semester = 2
    
    base_url_sps = "https://open.neis.go.kr/hub/spsTimetable"
    base_url_his = "https://open.neis.go.kr/hub/hisTimetable"
    base_url_mis = "https://open.neis.go.kr/hub/misTimetable"
    base_url_els = "https://open.neis.go.kr/hub/elsTimetable"
    
    final_url = None
    final_timetable = None
    
    def check_school_kind():
        url = None
        timetable = None
        
        if ("특수" or "(특)") in school['school_kind'] or ("특수" or "(특)") in school['school_name']:
            url = base_url_sps
            timetable = "spsTimetable"
        elif ("고등" or "(고)") in school['school_kind'] or ("고등" or "(고)") in school['school_name']:
            url = base_url_his
            timetable = "hisTimetable"
        elif ("중학" or "(중)") in school['school_kind'] or ("중학" or "(중)") in school['school_name']:
            url = base_url_mis
            timetable = "misTimetable"
        elif ("초등" or "(초)") in school['school_kind'] or ("초등" or "(초)") in school['school_name']:
            url = base_url_els
            timetable = "elsTimetable"
        else:
            pass
        return url, timetable
    
    def get_subject(final_url, final_timetable):
            response = requests.get(final_url, params=params)
            json_data = None

            if response.status_code != 200 :
                print("Can't access the information")
            else:
                json_data = response.json()
                first_key = list(json_data.keys())[0]
                
                if first_key == final_timetable:
                    subjects = json_data[final_timetable][1]['row']
                    for subject in subjects:
                        subject_data = {
                            "school_name" : subject["SCHUL_NM"],
                            "date" : subject["ALL_TI_YMD"],
                            "perio" : subject["PERIO"],
                            "subject_name" : subject["ITRT_CNTNT"],
                            "grade" : subject["GRADE"],
                            "class" : subject["CLASS_NM"]
                        }
                        if subject_data not in results:
                            results.append(subject_data)
    
    results = []
    
    for school in schools:
        office_code = school['office_code']
        school_code = school['school_code']
        
        final_url, final_timetable = check_school_kind()
                
        for i in [-3, -2, -1, 0, 1, 2, 3]:
            school_date = (date.today() + timedelta(i)).strftime("%Y%m%d")

            params = {
                'Key': api_key,
                'Type': data_type,
                'pIndex': 1,
                'pSize': 1000,
                'ATPT_OFCDC_SC_CODE': office_code,
                'SD_SCHUL_CODE': school_code,
                'ALL_TI_YMD': school_date,
                'AY': school_year,
                'SEM': school_semester            
            }
                        
            if final_url != None:
                get_subject(final_url, final_timetable)        
                
    return results

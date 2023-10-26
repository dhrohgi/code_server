# 학교이름으로 school code 를 알아내는 함수

import requests
import json

def get_school_code(school_name):
    api_key = 'c5dd73feb40b45d695c4c042cbd0d041' # 나이스 교육정보 개방포털 api key
    data_type = 'json'
    
    param_dict = {}
    param_dict.setdefault('Key', api_key)
    param_dict.setdefault('Type', data_type)
    param_dict.setdefault('pIndex', 1)
    param_dict.setdefault('pSize', 100)
    param_dict.setdefault('SCHUL_NM', school_name)
    
    base_url = "https://open.neis.go.kr/hub/schoolInfo"

    response = requests.get(base_url, params=param_dict)
    json_data = None
    
    if response.status_code != 200 :
        print("Can't access the information")
    else:
        json_data = response.json()
        results = []
        if next(iter(json_data)) == "schoolInfo":
            basicinfos = json_data['schoolInfo'][1]['row']
            for basicinfo in basicinfos:
                data = {
                    "office_code": basicinfo["ATPT_OFCDC_SC_CODE"],
                    "office_name": basicinfo["ATPT_OFCDC_SC_NM"],
                    "school_code": basicinfo["SD_SCHUL_CODE"],
                    "school_name": basicinfo["SCHUL_NM"],
                    "school_kind": basicinfo["SCHUL_KND_SC_NM"],
                    "city_name": basicinfo["LCTN_SC_NM"],
                    "zipcode": basicinfo["ORG_RDNZC"],
                    "address_1": basicinfo["ORG_RDNMA"],
                    "address_2": basicinfo["ORG_RDNDA"],
                    "homepage": basicinfo["HMPG_ADRES"],
                    "gender": basicinfo["COEDU_SC_NM"]
                }
                results.append(data)
        else:
            print("😩 information wasn't uploaded yet!")            
        return results


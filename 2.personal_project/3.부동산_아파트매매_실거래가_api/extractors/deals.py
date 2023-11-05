import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import xmltodict

def get_apart_deal(lawd):
    api_key = 'kXGNvED+3aj7NZ9UyzWuiQunJXT01FvEXfhdEDmrwZIPAIh+ghITRyP1zAMBiv6GR7oVx8Ka1j0AkzSAtB+Q5w==' 
    # 공공 데이터 포털 api key
    
    results = []
    
    for i in range(-5, 0):
        checking_month = (datetime.today() + relativedelta(months = i)).strftime("%Y%m")
        params = {
            'serviceKey': api_key,
            'LAWD_CD': lawd,
            'DEAL_YMD': checking_month
        }
        base_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
        response = requests.get(base_url, params=params)
        xml_data = None
        dict_data = None
        json_data = None
        if response.status_code != 200 :
            print("Can't access the information")
        else:
            xml_data = response.text
            dict_data = xmltodict.parse(xml_data)
            json_data = json.loads(json.dumps(dict_data))
            deals = json_data['response']['body']['items']['item']
            for deal in deals:
                i = {
                    '거래금액': deal['거래금액'],
                    '거래유형': deal['거래유형'],
                    '건축년도': deal['건축년도'],
                    '년': deal['년'],
                    '등기일자': deal['등기일자'],
                    '법정동': deal['법정동'],
                    '아파트': deal['아파트'],
                    '월': deal['월'],
                    '일': deal['일'],
                    '전용면적': deal['전용면적'],
                    '중개사소재지': deal['중개사소재지'],
                    '지번': deal['지번'],
                    '지역코드': deal['지역코드'],
                    '층': deal['층'],
                    '해제사유발생일': deal['해제사유발생일'],
                    '해제여부': deal['해제여부']                    
                }
                results.append(i)
    return sorted(results, key=lambda apart: apart['아파트'])



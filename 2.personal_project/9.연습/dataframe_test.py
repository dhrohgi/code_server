import requests
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import xmltodict
import json
import sqlite3

def get_apart_deal(lawd):
    api_key = 'kXGNvED+3aj7NZ9UyzWuiQunJXT01FvEXfhdEDmrwZIPAIh+ghITRyP1zAMBiv6GR7oVx8Ka1j0AkzSAtB+Q5w==' 
    # 공공 데이터 포털 api key
    
    results = []
    
    for i in range(-11, 0):
        checking_month = (datetime.today() + relativedelta(months = i)).strftime("%Y%m")
        params = {
            'serviceKey': api_key,
            'LAWD_CD': lawd,
            'DEAL_YMD': checking_month
        }
        base_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
        response = requests.get(base_url, params=params)
        data = None
        if response.status_code != 200 :
            print("Can't access the information")
        else:
            data = json.loads(json.dumps(xmltodict.parse(response.text)))
            df = pd.DataFrame(data['response']['body']['items']['item'])
            results.append(df)
            con = sqlite3.connect("gijang.db")
            df.to_sql("apart_deal", con, if_exists='append', index=False)
    return results


test = get_apart_deal("26710")
print(test)



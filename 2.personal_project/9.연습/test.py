from datetime import datetime

x = datetime.today().strftime("%Y%m%d")
print(x)


test_string = "(초)부산국민"
if "(고)" not in test_string:
    print("초등학교 아님")
else:
    print("초등학교")
    
    
    
cur_price = {'Daum KAKAO': 80000, 'naver':800000, 'daeshin':30000}
keys = cur_price.keys()
print(keys)
stock_list = list(cur_price.keys())
print(stock_list)



school_date = datetime.today().strftime("%Y%m%d")
school_year = school_date[0:4]
print(school_year)
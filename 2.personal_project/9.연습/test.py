from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

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

three_day_before = (date.today() - timedelta(3)).strftime("%Y%m%d")
three_day_after = (date.today() + timedelta(3)).strftime("%Y%m%d")
print(three_day_before)
print(three_day_after)


checking_month = (datetime.today() + relativedelta(months = -1)).strftime("%Y%m")
print(checking_month)

for i in range(-7, 0):
    print(i)
    
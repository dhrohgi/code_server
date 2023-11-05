from extractors.deals import get_apart_deal
import file

deals = get_apart_deal("26710")
for deal in deals:
    print(f'{deal['월']}월, {deal['일']}일, {deal['아파트']}, {deal['층']}층, {round(float(deal['전용면적'])/3.3)}평, {deal['거래금액']}만원')
    print('-------------------------------------------------------------')
# 파일로 저장

def save_to_deal_file(file_name, deals):
    file = open(f'{file_name}.csv', "w", encoding='utf-8-sig')
    file.write("거래금액,아파트,월,일,전용면적,층\n")
    
    for deal in deals:
        file.write(f'{deal['거래금액']},{deal['아파트']},{deal['월']},{deal['일']},{deal['전용면적']},{deal['층']}\n')
    
    file.close()

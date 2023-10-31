# 파일로 저장

def save_to_timetable_file(file_name, timetables):
    file = open(f'{file_name}.csv', "w", encoding='utf-8-sig')
    file.write("학교,날짜,학년,반,교시,과목\n")
    
    for timetable in timetables:
        file.write(f'{timetable['school_name']},{timetable['date']},{timetable['grade']},{timetable['class']},{timetable['perio']},{timetable['subject_name']}\n')
    
    file.close()


def save_to_meal_file(file_name, meals):
    file = open(f'{file_name}.csv', "w", encoding='utf-8-sig')
    file.write("학교,날짜,메뉴,칼로리\n")
    
    for meal in meals:
        file.write(f'{meal['school_name']},{meal['date']},{meal['dish_name']},{meal['calory']}\n')
    
    file.close()

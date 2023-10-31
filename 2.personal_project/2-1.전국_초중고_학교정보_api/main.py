from flask import Flask, render_template, request
from extractors.meals import get_meal
from extractors.timetables import get_timetable
from datetime import datetime
import file

school_name = input('조회할 학교명?')


meals = get_meal(school_name)
file.save_to_meal_file("meal", meals)
for meal in meals:
    print(meal)
    print("----------------------")
    

timetables = get_timetable(school_name)
file.save_to_timetable_file("timetable", timetables)
for timetable in timetables:
    print(timetable)
    print("----------------------")



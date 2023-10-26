from flask import Flask, render_template, request
from extractors.meal_info import get_meal
from extractors.timetable_info import get_timetable

meals = get_meal()
for meal in meals:
    print(meal)
    print("----------------------")
    

timetables = get_timetable()
for timetable in timetables:
    print(timetable)
    print("----------------------")
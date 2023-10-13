import numpy as np

a = np.array([5, 6, 7, 24])
b = np.array([1, 2, 3, 6])
marks = a * b
print(marks)

number = 0

for mark in marks :
    number = number + 1
    if mark >= 20 :
        print(f'{number}번 학생은 합격입니다.')
    else :
        print(f'{number}번 학생은 불합격입니다.')


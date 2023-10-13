nums = range(0, 7)
print(nums)
print(list(nums))
print(list(nums[2:4]))
print(list(nums[2:2]))
print(list(nums[2:]))
print(list(nums[:5]))
print(list(nums[:]))
print(list(nums[:-2]))
print(list(nums[2:6:3]))

print('/////////////////')

print(list(range(10)))
print(list(range(1, 10)))
print(list(range(2, 20, 3)))
print(list(range(20, 0, -2)))

print('/////////////////')

for i in range(10, 0, -1) :
    if i == 5 :
        print('5 is middle')
    else :
        print(f'countdown : {i}')









# range(stop)
# range(10)은 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 숫자를 생성한다.
# 마지막 숫자 10(stop)은 포함되지 않는다.
# (range 함수의 결과를 바로 확인하기 위해 리스트(list)로 변환)


# range(start, stop)
# range(1, 11)은 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 숫자를 생성
# 인자를 2개 전달하는 경우 첫번째 인자는 시작하는 숫자가 된다.


# range(start, stop, step)
# range(0, 20, 2)
# 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
# 마지막 인자 step은 숫자의 간격을 나타낸다.
# range(20, 0, -2)
# 20, 18, 16, 14, 12, 10, 8, 6, 4, 2
# step으로 음수를 지정할 수 있다.


# range() 함수의 결과는 반복가능(iterable)하기 때문에 for문을 사용해 출력할 수 있다.


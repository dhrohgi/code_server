
numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

sum_of_numbers = 0

"""
for number in numbers:
  if not (number == '💖' or number == '🔥' or number == '⭐️'):
    sum_of_numbers += number
    
print(sum_of_numbers)
"""

for number in numbers:
    number = str(number)
    if number.isdecimal():
        sum_of_numbers += int(number)

print(f'The result is {sum_of_numbers}')

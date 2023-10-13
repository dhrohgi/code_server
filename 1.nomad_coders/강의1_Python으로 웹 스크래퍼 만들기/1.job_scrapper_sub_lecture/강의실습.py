def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_calc(5000000)
pay_tax(f"${to_pay}")


def make_juice(fruit):
    return f"{fruit}+🧃"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍭"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)



password_correct = False
if password_correct:
    print('Here is your money!')
else:
    print('wrong password!')


winner = 8
if winner > 10:
    print('winner is greater than 10')
elif winner < 10:
    print('winner is less than 10')
else:
    print('winner is 10')


age = int(input("How old are you?"))
if age < 18:
    print("You can't drink, Get out")
elif age >= 18 and age <= 35:
    print("Drink beer!")
elif age >= 80 and age < 100:
    print("You're too old to drink achole")
elif age >= 100:
    print("You should think about your health")
else:
    print("Go ahead Buddy!")


distance = 0
while distance < 20:
    distance = distance + 1
    print(f"I'm running {distance}km")


from random import randint
print("Welcome to Python Casino!")

pc_choice = randint(1, 100) # I imported this from random module

playing = True

while playing:
    user_choice = int(input("Choose number(1-100):"))

    if user_choice == pc_choice:
        print("You won!", pc_choice)
        playing = False
    elif user_choice > pc_choice:
        print("Try with lower number!")
    elif user_choice < pc_choice:
        print("Try with higher number!")




# data structure


# List -> 리스트는 [] 으로 만들며, modify 가능한 mutable 데이터 구조이다.
test = [1, 2, 3, 'Mon', True, False]
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

days_of_week.remove("Mon")
print(days_of_week)

days_of_week.append("Mon")
print(days_of_week)

print(days_of_week[2])



# Tuple -> 튜플은 () 으로 만들며, modify 할 수 없는 immutable 데이터 구조이다.
test = (1, 2, 3, 'True', True)
days = ("Mon", "Tue", "Wed")
print(days.count("Mon"))
print(days[-1])


# Dictionary -> 딕셔너리는 {} 으로 만들며, modify 할 수 있는 mutable 데이터 구조이다.
player = {
    "name" : "Daehan",
    "age" : 12,
    'alive' : True,
    'fav_food' : ['🍕', '🌭', '🥚', '🍚', '🍥']
}

print(player.get('alive'))
print(player['fav_food'])
print(player.get('fav_food'))

player['xp'] = 1500

print(player)

player['fav_food'].append('🍨')

print(player)
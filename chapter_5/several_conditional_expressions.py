# 5.3
alien_color = 'red'
if alien_color == 'red':
    print("Вы заработали 5 очков")
if alien_color == 'green':
    print()

# 5.4
alien_color = 'red'
if alien_color == 'green':
    print("Вы заработали 5 очков")
else:
    print("Вы заработали 10 очков")

if alien_color == 'red':
    print("Вы заработали 5 очков")
else:
    print("Вы заработали 10 очков")

# 5.5
alien_color = 'green'
if alien_color == 'green':
    print("Вы заработали 5 очков")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков")
elif alien_color == 'red':
    print("Вы заработали 15 очков")

alien_color = 'yellow'
if alien_color == 'green':
    print("Вы заработали 5 очков")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков")
elif alien_color == 'red':
    print("Вы заработали 15 очков")

alien_color = 'red'
if alien_color == 'green':
    print("Вы заработали 5 очков")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков")
elif alien_color == 'red':
    print("Вы заработали 15 очков")

# 5.6
age = 25
if age < 2:
    print("Младенец")
elif 2 <= age < 4:
    print("Малыш")
elif 4 <= age < 13:
    print("Ребенок")
elif 13 <= age < 20:
    print("Подросток")
elif 20 <= age < 65:
    print("Взрослый")
else:
    print("Пожилой человек")

# 5.7
favorite_fruits = ['банан', 'апельсин', 'груша']
if 'банан' in favorite_fruits:
    print(f"Тебе правда нравятся бананы")
if 'апельсин' in favorite_fruits:
    print(f"Тебе правда нравятся апельсины")
if 'груша' in favorite_fruits:
    print(f"Тебе правда нравятся груши")
if 'ананас' in favorite_fruits:
    print(f"Тебе правда нравятся ананасы")
if 'гранат' in favorite_fruits:
    print(f"Тебе правда нравятся гранаты")

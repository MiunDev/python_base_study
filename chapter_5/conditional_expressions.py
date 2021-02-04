#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\n car == 'audi'? I predict False.")
print(car == 'audi\n')

#5.2
car = 'audi'
print(f"Равны ли строки: {car == 'mercedes'}")
print(f"Равны ли строки: {car == 'audi'}")
car = 'BMW'
print(f"Использование функции lower(): {car.lower() == 'bmw'}")
a = 5
b = 6
c = 4
print(f"a = {a}; b = {b}; c = {c}")
print(f"a > b {a > b}; a < b {a < b}; a >= b {a >= b}; a <= b {a <= b}")
print(f"a > b & a > c: {a > b and a > c}")
print(f"a > c || a < b: {a > c or a < b}")
list_cars = ['bmw', 'audi', 'mercedes']
if 'bmw' in list_cars:
    print("Yes, buy bmw")
check_car = 'kia'
if check_car not in list_cars:
    print(f"Какого фига, {check_car.title()} не включена в подборку авто?")
    list_cars.append(check_car)
print(list_cars)
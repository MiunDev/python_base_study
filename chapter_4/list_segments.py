# 4.10
food_list = ['cannoli', 'pizza', 'ice cream', 'carrot cake', 'cake']
print(f"The irst three items in the list are: {food_list[:3]}")
print(f"Three items from the middle of the list are: {food_list[1:4]}")
print(f"The last three items in the list are: {food_list[-3:]}\n")

# 4.11
friend_pizzas = food_list[:]
food_list.append('margarita')
friend_pizzas.append('meat')
print(f"My favorite pizzas are: ")
for pizza in food_list:
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
print("\n")

# 4.12 упражнение идентично 4.11

# 4.13
list_simple_food = ('meat', 'apple', 'orange', 'juice', 'coffee')
for food in list_simple_food:
    print(food)
print("\n")
list_simple_food = ('potato', 'tea')
for food in list_simple_food:
    print(food)
print("\n")

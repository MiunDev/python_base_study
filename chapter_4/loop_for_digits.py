#4.3
for digit in range(1, 21):
    print(digit)

#4.4
# for digit in range(1, 1000001):
#     print(digit)

#4.5
list_digits = list(range(1, 1000001))
print(min(list_digits))
print(max(list_digits))
print(sum(list_digits))

#4.6
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

#4.7
list_odd_number = []
for odd_num in range(3, 30):
    if odd_num % 3 == 0:
        list_odd_number.append(odd_num)
print(list_odd_number)

#4.8
cube_nums = []
for i in range(1, 11):
    cube_nums.append(i**3)
print(cube_nums)

#4.9
cubes_num = [i**3 for i in range(1, 11)]
for item in cubes_num:
    print(item)
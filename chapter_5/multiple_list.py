# 5.8
users = ['admin', 'user1', 'user2', 'user3', 'user4']
for user in users:
    if 'admin' == user:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")
print()

# 5.9
users = ['admin', 'user1', 'user2', 'user3', 'user4']
for user in users:
    if 'admin' == user:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")

users.clear()
if len(users) == 0:
    print("We need to ind some users!\n")

# 5.10
current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['admin', 'user5', 'user6', 'user3', 'user4']
for new_user in new_users:
    if new_user in current_users:
        print(f"Имя пользователя: {new_user} уже используется")
    else:
        print(f"Имя пользователя: {new_user} доступно для регистрации")
print()

# 5.11
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in list_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

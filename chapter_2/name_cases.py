#2.3
userName = "mars"
print(f"Hello {userName.capitalize()}, would you like to learn some Python today?\n")

#2.4
print(f"Нижний регистр: {userName.lower()}; Верхний регистр: {userName.upper()}; Капитализация начальных букв: {userName.capitalize()}\n")

#2.5
print('Albert Einstein once said, "A person who never made\n'
      'a mistake never tried anything new."\n')

#2.6
famous_name = "albert einstein"
message = f'{famous_name.capitalize()} once said, "A person who never made\n a mistake never tried anything new."\n'
print(message)

#2.7
userNameSecond = " \tmarhell\n "
print(userNameSecond)
print(f"lstrip: {userNameSecond.lstrip()}")
print(f"rstrip: {userNameSecond.rstrip()}")
print(f"strip: {userNameSecond.strip()}")
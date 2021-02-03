# 3.4
friends = ['Юлия', 'Андрей', 'Георгий']
#3.9
print(len(friends))

# 3.5
lost_friend = friends.pop()
friends.append('Разиль')
print(f'Приходи: {friends[0]}')
print(f'Приходи: {friends[1]}')
print(f'Приходи: {friends[2]}')
print(f"Этот гость не придет: {lost_friend}\n")

# 3.6
friends.insert(0, 'Алина')
friends.insert(2, 'Лилия')
friends.append('Рита')
print(f"Приходите все: {friends}\n")

#3.7
print("Сорян, места только 2\n")
print(f"Мне охренеть как жаль, но ты слабое звено: {friends.pop()}")
print(f"Мне охренеть как жаль, но ты слабое звено: {friends.pop()}")
print(f"Мне охренеть как жаль, но ты слабое звено: {friends.pop()}")
print(f"Мне охренеть как жаль, но ты слабое звено: {friends.pop()}")
print(f"Ты в танцах: {friends[0]}")
print(f"Ты в танцах: {friends[1]}")
print("А, нет, покедова и вам")
del friends[0]
del friends[0]
print(f"Пустой список приглашенных: {friends}")
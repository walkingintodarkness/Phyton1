list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Находим середину списка
middle = len(list_players) // 2

# Первая команда - первые половина игроков
first_team = list_players[:middle]

# Вторая команда - вторая половина игроков
second_team = list_players[middle:]

# Выводим результаты
print("Первая команда:", first_team)
print("Вторая команда:", second_team)

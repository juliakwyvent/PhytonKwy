import random

group1 = ["Иванов", "Белоусов", "Горбачев", "Матрёхин", "Шестаков","Шатилов","Мартьянов","Романов","Яковлев","Лиханов"]
group2 = ["Петров", "Платонов", "Лифарь", "Алимов", "Яблоков","Леонтьев","Савельев","Пыхов","Цомаев","Дорофеев"]


sports_team = tuple(random.sample(group1, 5) + random.sample(group2, 5))

print("Группа 1:", group1)
print("Группа 2:", group2)

print("Спортивная команда:", sports_team)
print("Длина кортежа:", len(sports_team))
sorted_team = sorted(sports_team)

surname = "Иванов"
if surname in sorted_team:
    print(f"Фамилия {surname} есть в команде")
else:
    print(f"Фамилия {surname} не найдена в команде")
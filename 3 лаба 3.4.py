import random

MAX_ERRORS = 3

right = 0
mistakes = 0

while mistakes < MAX_ERRORS:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    prompt = f"{number1} + {number2} = "
    answer = input(prompt)

    if int(answer) == number1 + number2:
        print("Правильно!")
        right += 1
    else:
        print("Ответ неверный")
        mistakes += 1
print(f"Игра окончена. Правильных ответов: {right}")

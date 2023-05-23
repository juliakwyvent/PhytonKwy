import random

MAX_ERRORS = 3

num_correct = 0
num_errors = 0

while num_errors < MAX_ERRORS:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    prompt = f"{number1} + {number2} = "
    answer = input(prompt)

    if int(answer) == number1 + number2:
        print("Правильно!")
        num_correct += 1
    else:
        print("Ответ неверный")
        num_errors += 1
print(f"Игра окончена. Правильных ответов: {num_correct}")
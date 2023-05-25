def divide():
    try:
        num = float(input("Введите число: "))
        result = 100 / num
        print(f"Результат деления: {result}")
    except ValueError:
        print("Ошибка: введено некорректное значение. Пожалуйста, введите число.")
    except ZeroDivisionError:
        print("Ошибка: нельзя делить на 0. Пожалуйста, введите другое число.")

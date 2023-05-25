def divide_numbers():
    try:
        number = float(input("Введите число: "))
        result = 100 / number
        print(f"Результат : {result}")
    except ValueError:
        print("Error! Введено не число")
    except ZeroDivisionError:
        print("Error! Делить на 0 нельзя")


divide_numbers()

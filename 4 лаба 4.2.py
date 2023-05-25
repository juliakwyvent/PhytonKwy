def divide_numbers():
    try:
        number = float(input("Введите число, на которое нужно разделить 100: "))
        result = 100 / number
        print(f"Результат деления: {result}")
    except ValueError:
        print("Вы ввели не число")
    except ZeroDivisionError:
        print("Вы ввели 0")
    
divide_numbers()

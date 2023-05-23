def divide_100_by_num(num):
    try:
        result = 100 / num
        return result
    except ValueError:
        print("Error! Введено не число.")
    except ZeroDivisionError:
        print("Error! Делить на 0 нельзя.")

while True:
    num_str = input("Введите число: ")
    try:
        num = int(num_str)
        break
    except ValueError:
        print("Ошибка! Введено не число.")

result = divide_100_by_num(num)
if result is not None:
    print(f"Результат равен {result}")
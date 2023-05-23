seat_number = int(input("Введите номер места: "))
if seat_number % 2 == 0:
    print("Это нижнее место", end='')
    if seat_number <= 36:
        print(" в купе.")
    else:
        print(" боковое.")
else:
    print("Это верхнее место", end='')
    if seat_number <= 35:
        print(" в купе.")
    else:
        print(" боковое.")

def is_magical_date(date_str):
    date_list = date_str.split('.')
    day, month, year = map(int, date_list)
    if day * month == year % 100:
        return True
    else:
        return False
date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magical_date(date_str):
    print("Дата является магической")
else:
    print("Дата не является магической")
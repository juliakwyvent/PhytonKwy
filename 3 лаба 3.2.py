result = ""

while True:
    word = input("Введите слово ('stop' чтобы остановить): ")
    if word == "stop":
        break
    result += word + " "

print("Результат:", result.strip())
N = int(input("Введите количество слов: "))
result = ""
for i in range(N):
    word = input("Введите слово")
    result += word + " "
result = result.rstrip()
print(result)

N = int(input("Введите количество слов: "))
words = []
for i in range(N):
    word = input(f"Введите слово {i + 1}: ")
    words.append(word)
result = ""
for word in words:
    result += word + " "
result = result.rstrip()

print(result)

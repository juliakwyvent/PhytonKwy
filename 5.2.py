list1 = [1, 2, 3, 4, 5, 2, 6, 7]
list2 = set(list1)

if len(list1) == len(list2):
  print("Повторяющихся элементов в списке нет.")
else:
  for item in list2:
    if list1.count(item) > 1:
      print("Повторяющийся элемент в списке: ", item)
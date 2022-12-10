liist = [['Иванов', 'Иван', '+380992364622', 'ivan@gmail.com'],
      ['Сидоров', 'Сергей', '+380931545712', 'sidov@ukr.net'],
      ['Петров', 'Артем', '+380501392227', 'petrov@gmail.com'],
      ['Васичкин', 'Александр', '+3806603762820', 'vasichkin@gmail.com'],
      ['Седов', 'Роман', '+380991279629', 'sedov@ukr.net']]
def SortInsert(sorting_list, start = 1):
    for i in range(start, len(sorting_list)):
        for j in range(i, 0, -1):
            if sorting_list[j] < sorting_list[j-1]:
                sorting_list[j], sorting_list[j-1] = sorting_list[j-1], sorting_list[j]
            else:
                break
SortInsert(liist)
print(liist)
fio = input('Введите Фамилию по которым хотите найти данные')
def BinarySearch(li, key):
      leftInd = 0
      rightInd = len(li) - 1
      k = 0
      while leftInd <= rightInd:
            k += 1
            i = leftInd + (rightInd - leftInd) // 2
            if li[i] == key:
                  print('k:', k)
                  return i
            elif li[i] < key:
                  leftInd = i + 1
            else:
                  rightInd = i - 1
      print('k:', k)
      return None
print('по Фамилии', fio, 'следующие данные', BinarySearch(liist, fio))
l = {'Иванов': ['Иван', '+380992364622', 'ivan@gmail.com'],
     'Сидоров': ['Сергей', '+380931545712', 'sidov@ukr.net'],
     'Петров': ['Артем', '+380501392227', 'petrov@gmail.com'],
     'Васичкин': ['Александр', '+3806603762820', 'vasichkin@gmail.com'],
     'Седов': ['Роман', '+380991279629', 'sedov@ukr.net']}
l1 = dict(sorted(l.items(), key=lambda i: i[1]))
print(l1)
fio = input('Введите Фамилию по которым хотите найти данные')
def BinarySearch(li, key):
    leftInd = 0
    rightInd = len(li) - 1
    l1 = list(li.keys())
    while leftInd <= rightInd:
        i = leftInd + (rightInd - leftInd) // 2
        if l1[i] == key:
            j = l1[i]
            print('Найдено по Фамилии ', key, 'следующие ', li[j])
            return i
        elif l1[i] < key:
            leftInd = i + 1
        else:
            rightInd = i - 1

    return print('Введенной Фамилии нет', fio)
BinarySearch(l1, fio)


#for j in l1:
 #   if j == fio:
 #       print('Найдено по Фамилии ', fio, 'следующие ', l1[j])
#        break
#    else:
#        print('Введенной Фамилии нет', fio)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

N = int(input("Введите значение числа N:  "))
i = 0
print(f'Степени двойки, не превосходящие число {N}')
while 2 ** i <= N:
    print(f' 2 в {i} степени - {2 ** i}')
    i += 1
    


"""
n = int(input("Величина списка: "))
n_digits = [int(input("Введите числа: ")) for i in range(n)]
print(n_digits)
n_digits = set(n_digits)
print(n_digits)
print(len(n_digits))


list_1 = [1, 2, 3, 4, 5]
k = 3
# for i in range(k):  
#     list_1.append(list_1.pop(0))
# print(list_1)
print(list_1[k:]+ list_1[:k])


for item in dictionary:
    print('{}:{}'.format(item,dictionary[item]))
print(dictionary.items())

x = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},{" VIII":" S007 "}]
y = set ()

for i in x:
    for j in i.values():
        y.add(j.strip())  #strip() - убирает пробелы с начала и с конца
print(y)
"""
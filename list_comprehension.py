# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = [1, 2, 3, 5, 1, 5, 3, 10]

res = [x for x in lst if lst.count(x)==1]

print(res)
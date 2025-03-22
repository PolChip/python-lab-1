import random
a=[random.randint(1,100) for i in range(10)] # берем рандомные 10 чисел
ch=[]
print(a) # список
print(max(a), min(a)) # min и max значения
print(sum(a)) # сумма чисел
print(sorted(a)) # сортировка по возрастанию

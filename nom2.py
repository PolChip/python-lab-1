n=int(input('ввидите число'))
a=[]
b=[]
c=[]
for i in range(1, n+1): # находим все числа от 1 до n
  a+=[i] # записываем все числа 
  b+=[i**2] # находим и записываем их квадраты
c+=[sum(a)] # находим и записываем общюю сумму
print(a,b,c)

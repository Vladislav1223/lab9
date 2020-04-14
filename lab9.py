import numpy as np
import random
import timeit #импортируем модуль для подсчета времени
while True:
 vvod=input('Как  вводить?Если рандомно-1,если с клавиатуры-любая кнопка')  #Выбираем одно из значений для нашей переменной
 metod=input('Каким методом?пузырьковым-1,выбора-2,вставками-любая кнопка')
 sortirovka=input('Как сортировать?Если по возрастанию-1,если по убыванию-любая копка')
 def bubl_up(s): #заводим функцию для пузыркового метода,для сортировки по возрастанию,где s-это количество элементов(s-это обязательный параметр)
    global count #Заводим 2 счетчика и делаем их глобальными что бы их можно было вызвать в дальнейшем в функции оценки работы
    global obmen
    count=0
    obmen=0
    for i in range(1,n): #Сам пузырьковый алгоритм
        count+=1
        for j in range(n-1,i-1,-1):
            count+=1
            obmen+=1
            if (A[j-1]>A[j]):
                obmen+=1
                count+=1
                A[j],A[j-1]=A[j-1],A[j]
    print(A)
 def bubl_down(s):#заводим функцию для пузырькового метода,для сортировки по убыванию
    global count
    global obmen
    count=0
    obmen=0
    for i in range(1,n):
        count+=1
        for j in range(n-1,i-1,-1):
            count+=1
            obmen+=1
            if (A[j-1]<A[j]):
                obmen+=1
                count+=1
                A[j],A[j-1]=A[j-1],A[j]
    print(A)
 def select_up(s):#заводим функцию для алгоритма сортировки метода выбора,для сортировки по возростанию
    global count_se
    global obmen_se
    count_se=0
    obmen_se=0
    for i in range(n-1):#cам алгоритм выбора
        count_se+=1
        min=i
        for j in range(i+1,n):
            obmen_se+=1
            count_se+=1
            if A[j]<A[min]:
                obmen_se+=1
                count_se+=1
                min=j
        A[i],A[min]=A[min],A[i]
    print(A)
 def select_down(s):#заводим функцию для алгоритма сортировки метода выбора,для сортировки по убыванию
    global count_se
    global obmen_se
    count_se=0
    obmen_se=0
    for i in range(n-1):
        count_se+=1
        min=i
        for j in range(i+1,n):
            obmen_se+=1
            count_se+=1
            if A[j]>A[min]:
                obmen_se+=1
                count_se+=1
                min=j
        A[i],A[min]=A[min],A[i]
    print(A)
 def insertion_up(s):#заводим функцию для алгоритма сортировки метода вставки,для сортировки по возростанию
    global count_ins
    global obmen_ins
    count_ins=0
    obmen_ins=0
    for i in range(1,n):# сам алгоритм вставки
        j=i-1
        key=A[i]
        while j>=0 and A[j]>key:
            count_ins+=2
            obmen_ins+=1
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
 def insertion_down(s):#заводим функцию для алгоритма сортировки метода вставки,для сортировки по убыванию
    global count_ins
    global obmen_ins
    count_ins=0
    obmen_ins=0
    for i in range(1,n):
        j=i-1
        key=A[i]
        while j>=0 and A[j]<key:
            count_ins+=2
            obmen_ins+=1
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
        
 if vvod=='1': 
  x=int(input('Введите количество цифр'))
  A=np.zeros(x,dtype=int) #Заводим масив,и заполняем его рандомными значениями
  for i in range(x):
   A[i]=random.randint(0,100000)
  print(A)
  n=len(A)
  s=x
 else:#если значение vvod !=1,то мы заполняем наш масив сами,до 30 значений
   x=int(input('Введите количество цифр'))
   while x>30:
      x=int(input('Введите количество  до 30'))
   A=np.zeros(x,dtype=int)
   for i in range(x):
    A[i]=int(input('Введите число '))
   print(A)
   n=len(A)
   s=x
 def xarakteristika_bubl(countner): #Заводим функции для оценки работы каждого из методов
    print('Колличество сравнений пузырькогового метода',countner)
    print('Количество обменов пузырькового метода',obmen)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)#Присваевам t,значение времени за которое работал каждый алгоритм
    print('Программа выполнялась',t)
 def xarakteristika_select(countner):
    print('Колличество сравнений метода выбора',countner)
    print('Количество обменов метода выбора',obmen_se)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Программа выполнялась',t)
 def xarakteristika_ins(countner):
    print('Количество сравнений метода вставками',countner)
    print('Количество обменов метода вставками',obmen_ins)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Программа выполнялась',t)
 if metod=='1': #В зависимости от выбранных значений выводим наши функции
  if sortirovka=='1':
    bubl_up(s)
    xarakteristika_bubl(countner=count)#counter является поименнованым параметром функции
  else:
    bubl_down(s)
    xarakteristika_bubl(countner=count)
 elif metod=='2':
     if sortirovka=='1':
         select_up(s)
         xarakteristika_select(countner=count_se)
     else:
         select_down(s)
         xarakteristika_select(countner=count_se)
 else:
    if sortirovka=='1':
        insertion_up(s)
        xarakteristika_ins(countner=count_ins)
    else:
        insertion_down(s)
        xarakteristika_ins(countner=count_ins)
 result = input('Хотите продолжить? Если да - 1, Если нет - інше: ') #зацикливаем нашу программу
 if result == '1':
   continue
 else:
   break

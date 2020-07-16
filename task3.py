# 3) Напишите функцию которая принимает число 'N' и
# возвращает квадраты всех натуральных чисел кроме числа 'N', в порядке возрастания
# например если число 'N' = 4 ,то должен выйти список из чисел: 0,1,4,9

def chislo():
    a = int(input())
    new_list=[]
    for num in range(a):
        new_list.append(num**2)
    print(new_list)

chislo()
def chislo2():
    a = int(input())
    new_list=[ num**2 for num in range(a) ]
    print(new_list)
chislo2()



# 2) Напишите программу которая принимает любое число если число четное,
# то программа должна сказать ,что это число четное если нет, то сказать ,что оно
# нечетное

def oddornot():
    a = int(input('введите число: '))
    if a %2 ==0:
        print('четное')
    else:
        print('нечетное')
oddornot()
# 6)Напишите функцию которая принимает 3-значное число и выводит сумму его цифр
def func():
    xxx = int(input("введите число: "))
    try:
        if len(str(xxx))<=3:
            xxx2=str(xxx)
            x= int(xxx2[0])+int(xxx2[1])+int(xxx2[2])
            print(x)
        else:
            print("введите трехзначное число")
            func()
    except Exception:
        print('введите трехзначное число')
        func()
func()



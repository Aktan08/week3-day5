# Напиши калькулятор используя функции и используйте Try Except во время
# деления, деление на ноль нельзя
def func():
        vvod =input('выберите оператор "+" "-" "/" "*"')
        if vvod ==  "+" or "-" or "/" or"*":
            try:
                a = float(input("введите первое число: "))
                b = float(input("введите второе число: "))
                try:
                    if vvod == "+":
                        print(a+b)
                    elif vvod == "-":
                        print(a-b)
                    elif vvod=="/":
                        print(a/b)
                    elif vvod == "*":
                        print(a*b)
                    else:
                        func()
                except ZeroDivisionError:
                    print("деление на ноль нельзя")
                    func()
            except Exception:

                print("нельзя вводить строки: ")
                func()
func()


        

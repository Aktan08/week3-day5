# 5)Напишите функцию которая принимает: день, месяц, год
# и возвращает 'True' если такая дата есть, если нет то 'False'

def true_ili_false():
    try:
        day = int(input('введите день: '))
        month = int(input('введите месяц: '))
        year = int(input('введите год: '))
        year2 = str(year)
        if len(year2)<=4 and day <= 31 and month <=12:
            if day <= 29 and month ==2:
                print(True)
            elif month%2==0 and day<=30:
                if month==12 or month==8 or month ==10 and day<=31:
                    print(True)
                else:
                    print(False)
            elif month%2!=0 and day<=31:
                if month==11 and day<=30:
                    print(True)
                else:
                    print(False)
            else:
                print(False)   
        else:
            print(False)
    except ValueError:
        print("нельзя вводить строки")
        true_ili_false()

        
true_ili_false()
    

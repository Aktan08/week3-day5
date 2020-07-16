# 8) Напишите программу которая будет принимать числа до тех пока пользователь
# сам не решит остановиться, затем выведите самое максимальное число
# (нельзя использовать функцию 'max()')
# (дополнительно: напишите Функцию которая принимает уже готовый список
# чисел(например[22,-3,11])
# и выводит минимальное и максимальное значение)
new_list=[]
def func():
    try:
        x = int(input("введите строку чтобы оно остановилось \nвведите число: "))
        new_list.append(x)
        func()
    except Exception:
        print('остановилось')
func()
new_list.append(1)
# my_list=[]
my_list= [ new_list[num] for num in range(len(new_list)-1 )if new_list[num-1]<new_list[num] >new_list[num+1] and new_list[0]<new_list[num]]
my_list2= [ new_list[num] for num in range(len(new_list)-1 )if new_list[num-1]>new_list[num]<new_list[num+1] ]
    # for num in range(len(new_list)-1):
    #     if new_list[num] > new_list[range(len(new_list))]:
    #         my_list.insert(0,new_list[num])
    #     else:
    #         my_list.append(new_list[num])

print(new_list)
print(my_list[0],my_list2[0])









                





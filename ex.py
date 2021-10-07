def my_func(stroka = ""):
    count = 0
    for bukva in stroka:
        if bukva.isupper():
            # count =+ 1
            count = count + 1
    return count

print(my_func("Проектирование IT-решений"))


l = [-1, 2, 3,5,8,13,7,10]
summ = 0
for el in l:
    if el < 10:
        summ += el

print(summ)
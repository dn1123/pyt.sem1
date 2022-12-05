number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели неверное число!')
elif number > 5:
    print('Этот день выходной!')
else:
    print('Это рабочий день!')
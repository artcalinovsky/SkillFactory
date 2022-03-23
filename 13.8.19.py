Amount = int(input('Введите количество билетов:'))
Sum = 0
Age = 0
for i in range(Amount):
    Age = int(input('Введите возраст:'))
    if Age < 0:
        print('Да быть такого не может!')
    elif 0 <= Age < 18:
        Sum += 0
    elif 18 <= Age < 25:
        Sum += 990
    else:
        Sum += 1390
if Amount <= 3:
    print('Полная стоимость билетов составит:', Sum)
else:
    print('Полная стоимость билетов составит:', Sum * 0.9)
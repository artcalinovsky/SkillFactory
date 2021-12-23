money = int(input("Введите сумму размещения в рублях:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print((list(int(per_cent/100 * money) for per_cent in per_cent.values()))) #Вывод дохода при ставках во всех банках
print('Максимальная сумма, которую вы сможете получить - ', max((list(int(per_cent/100 * money) for per_cent in per_cent.values())))) #Вывод дохода при наивысшей из ставок


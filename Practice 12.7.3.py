money = input('Ваша сумма: ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [
    per_cent['ТКБ'] * int(money) / 100,
    per_cent['СКБ'] * int(money) / 100,
    per_cent['ВТБ'] * int(money) / 100,
    per_cent['СБЕР'] * int(money) / 100
                                        ]
print(deposit)
print('Максимальная сумма, которую вы можете заработать: ', max(deposit))

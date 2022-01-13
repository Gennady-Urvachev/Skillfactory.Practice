quantity = int(input('Количество билетов: '))
price = []
for i in range(1, quantity + 1):
    age = int(input(f"Возраст для {i} билета?\n"))
    if age < 18:
        price.append(0)
    elif 18 <= age < 25:
        price.append(990)
    elif age >= 25:
        price.append(1390)
if quantity > 3:
    print("Сумма сo скидкой: ", (sum(price) - (sum(price) / 100) * 10), "руб")
else:
    print("Сумма", sum(price), 'руб')
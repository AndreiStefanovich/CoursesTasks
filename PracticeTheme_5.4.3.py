x = int(input("Введите текущую температуру среды: "))
left_border = int(input("Введите нижнюю границу температуры среды: "))
right_border = int(input("Введите верхнюю границу температуры среды: "))
if x < left_border or x > right_border:
    print("Внимание - температура среды вышла за пределы допустимой")
else:
    print("Температура среды в пределах нормы")
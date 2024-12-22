year = int(input("Введите дату выпуска: "))
speed_count = int(input("Введите кол-во скоростей: "))
if year < 2018 or speed_count < 24:
    print("Не соответсвует критериям")
else:
    print("Подходит")
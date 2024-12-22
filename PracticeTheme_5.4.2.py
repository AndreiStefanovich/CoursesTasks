points = int(input("Сколько баллов набрал: "))
gold_medal = int(input("Есть медаль: "))
if points >= 280 and gold_medal >= 1:
    print("Поздравляем! Ты поступил!")
else:
    print("К сожалению, ты не прошёл в наш университет")
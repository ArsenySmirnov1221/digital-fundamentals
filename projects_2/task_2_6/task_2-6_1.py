pH = float(input("Введите значение pH: "))

if pH < 0:
    print("Чрезвычайно кислая среда")
elif pH > 0 and pH < 7:
    print("Кислая среда")
elif pH == 7:
    print("Нейтральная среда (физиологический уровень pH)")
elif pH > 7:
    print("Щелочная среда")

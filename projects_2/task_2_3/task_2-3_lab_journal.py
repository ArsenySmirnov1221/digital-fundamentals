from itertools import count

fio = input('ФИО исследователя (меньше 30 символов): ')
date = input('Дата: ')
exp_name = input('Название эксперимента (меньше 35 символов): ')
conc = input('Вывод (меньше 90 символов): ')

ui_border = "+--------------------------------------------------+" # 52 символа
print(ui_border)
print("| Электронный лабораторный журнал                  ", end='|\n')

print(ui_border)
if 0<len(fio) and len(fio)<30:
    space_n = 52 - 20 - 3 - len(fio)
    print(f"| ФИО исследователя: {fio}", " "*space_n, end='|\n')

if 0<len(date) and len(date)<30:
    space_n = 52 - 7 - 3 - len(date)
    print(f"| Дата: {date}", " "*space_n, end='|\n')

if 0<len(exp_name) and len(exp_name)<35:
    space_n = 52 - 14 - 3 - len(exp_name)
    print(f"| Эксперимент: {exp_name}", " "*space_n, end='|\n')

print(ui_border)
if 0<len(conc) and len(conc)<42: # Если вывод на одну строку
    space_n = 52 - 11 - len(conc)
    print(f"| Вывод: {conc}", " "*space_n, end='|\n')
    print(ui_border)

if 42<=len(conc) and len(conc)<(42+48):
    line = conc[:41]
    print(f"| Вывод: {line}", end=' |\n')
    line = conc[41:90]
    space_n = 47 - len(conc[41:90])
    print(f"| {line}", " "*space_n, end=' |\n')
    print(ui_border)
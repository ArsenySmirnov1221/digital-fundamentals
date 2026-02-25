operator_name = input('Введите имя оператора: ')
pa_index = input('Введите текущее значение давления (Па): ')

with open("sensor_log.txt", "w", encoding="utf-8") as infofile:
    infofile.write(f"{operator_name} \t {pa_index}")

print("Данные успешно сохранены в sensor_log.txt")
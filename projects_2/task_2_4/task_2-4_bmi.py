weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

height_m = height / 100  # Преобразуем рост из см в метры
imt = weight / (height_m ** 2)  # Формула расчета ИМТ

print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height} см")
print(f"Вес:\t{weight} кг")
print(f"Индекс массы тела: {imt:.2f}")


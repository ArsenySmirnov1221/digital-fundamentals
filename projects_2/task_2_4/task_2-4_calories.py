proteins = float(input("Введите массу белков в продукте (г): "))
fats = float(input("Введите массу жиров в продукте (г): "))
carbohydrates = float(input("Введите массу углеводов в продукте (г): "))

cal = (proteins * 4) + (fats * 9) + (carbohydrates * 4)

print(f"Общая калорийность продукта: {cal} ккал")

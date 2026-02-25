# the name of the nutrient medium, the concentration of agar (%) and the temperature of sterilization.
nutrient_medium_name = input('Название питательной среды: ')
agar_conc = input('Концентрация агара (%): ')
sterilization_temp = input('Тепмпература стерилизации: ')

with open("recipe.txt", "w", encoding="utf-8") as infofile:
    infofile.write(f"Название питательной среды: {nutrient_medium_name}")
    infofile.write(f"нцентрация агара (%): {agar_conc}")
    infofile.write(f"Тепмпература стерилизации: {sterilization_temp}")
print("Файл 'recipe.txt' успешно сформирован!")
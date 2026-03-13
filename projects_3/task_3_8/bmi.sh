#!/bin/bash

read -p "Введите массу (в кг): " weight
read -p "Введите рост (в метрах): " height

# Вычисляем ИМТ
bmi=$(echo "scale=2; $weight / ($height * $height)" | bc)

echo "Ваш индекс массы тела (ИМТ): $bmi"

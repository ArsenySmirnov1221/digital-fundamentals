#!/bin/bash

read -p "Имя гена: " gene_name
read -p "Уровень экспрессии (обязательно целое число): " expression_level

if [ -z "$gene_name" ] || [ -z "$expression_level" ]; then
    echo "Недостаток входящих данных"
    exit 1
fi

echo "Экспрессия гена $gene_name составляет $expression_level единиц."

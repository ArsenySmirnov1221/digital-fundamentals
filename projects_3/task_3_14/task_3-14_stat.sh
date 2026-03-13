#!/bin/bash

sum=0
count=0

while read -r name score; do
    sum=$((sum + score))
    count=$((count + 1))
done < students.txt

if [[ $count -ne 0 ]]; then
    average=$(echo "scale=2; $sum / $count" | bc)
else
    average=0
fi

max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)

echo "Сумма всех оценок: $sum"
echo "Средняя оценка: $average"
echo "Максимальная оценка: $max"

dna_sequence = input("Введите последовательность ДНК: ").strip()
dna_sequence_upper = dna_sequence.upper()

print(f"Последовательность в верхнем регистре: {dna_sequence_upper}\n")

count_a = dna_sequence_upper.count('A')
count_t = dna_sequence_upper.count('T')
count_g = dna_sequence_upper.count('G')
count_c = dna_sequence_upper.count('C')

total_length = len(dna_sequence_upper)

print("Подсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}")

print(f"Общая длина: {total_length} нуклеотидов")

percent_a = (count_a / total_length) * 100
percent_t = (count_t / total_length) * 100
percent_g = (count_g / total_length) * 100
percent_c = (count_c / total_length) * 100

print("Процентное содержание нуклеотидов:")
print(f"A: {percent_a:.2f}%")
print(f"T: {percent_t:.2f}%")
print(f"G: {percent_g:.2f}%")
print(f"C: {percent_c:.2f}%")


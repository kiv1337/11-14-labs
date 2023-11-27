import csv

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple = []

for el in original_tuple:
        if el % 2 != 0:
            new_tuple.append(el)

with open("мусор/lab14_4.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Все числа"] + list(original_tuple))
        writer.writerow(["Нечётные числа"] + list(new_tuple))
    
with open("мусор/lab14_4.csv", "r", newline='', encoding="utf-8") as f:
    data = csv.reader(f)
    for row in data:
            print(row)

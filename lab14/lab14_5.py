import openpyxl

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple = []

for el in original_tuple:
    if el % 2 != 0:
        new_tuple.append(el)

book = openpyxl.Workbook()

sheet = book.active

sheet.append(["Все числа"] + list(original_tuple))
sheet.append(["Нечётные числа"] + list(new_tuple))

with open("мусор/lab14_5.xlsx", "wb") as file:
    book.save(file)

with open("мусор/lab14_5.xlsx", "rb") as file:
    book = openpyxl.load_workbook(file)
    print("Все числа:", original_tuple)
    print("Нечётные числа:", new_tuple)

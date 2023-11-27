import json

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple = []

for el in original_tuple:
        if el % 2 != 0:
            new_tuple.append(el)

data = {
        "Все числа": original_tuple,
        "Нечётные числа": new_tuple
    }

with open("мусор/lab14_2.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=1))

with open("мусор/lab14_2.json", encoding="utf-8") as file:
        my_tuples = json.load(file)
        print(my_tuples)



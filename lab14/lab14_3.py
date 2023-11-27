import xml.etree.ElementTree as xml

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple = []

for el in original_tuple:
    if el % 2 != 0:
        new_tuple.append(el)

root = xml.Element("new_tuple")

odd_element = xml.SubElement(root, "value")
odd_element.text = str(new_tuple)

tree = xml.ElementTree(root)

with open("мусор/lab14_3.xml", "wb") as file:
    tree.write(file)

with open("мусор/lab14_3.xml", "r", encoding="utf-8") as file:
    result = file.read()
    print(original_tuple)

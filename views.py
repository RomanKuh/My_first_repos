from models import create_item,choos_item,read_item
from presenter import items

while True:
    choice = input("Menu1.1-створити,2-прочитати все,3-працюємо з вибраним товаром,4-вихід: ")
    if choice == "1":
        item = create_item()
        items.append(item)
    if choice == "2":
        read_item()
    if choice == "3":
        read_item()
        number = choos_item()
    if choice == "4":
        break

from presenter import items
#import views

def create_item():
    item = {"name":input("Введіть назву товару: "),
            "description":input("Введіть опис товару: "),
            "price": input("Введіть ціну товару: ")}
    return item

def choos_item():
    number = input("Menu2.Введіть номер товару для роботи з ним: ")
    if number.isdigit() and 0 <= int(number) < len(items):
        number = int(number)
        while True:
            choice = input("Menu3.1-вивести,2-змінити,3-видалити,4-вихід: ")
            if choice == "1":
                print(items[number])
            if choice == "2":
                items[number].update(create_item())
            if choice == "3":
                items.pop(number)
                break
            if choice == "4":
                break

def read_item():
    print(items)



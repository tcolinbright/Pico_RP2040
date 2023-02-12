
shopping_list = {}

def add_item(item_name, quantity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("Bread")
add_item("Milk", 2)
add_item("Milk")
print(shopping_list)
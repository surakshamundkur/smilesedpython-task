# Defined the initial shopping list
shopping_list = ["Milk", "Bread", "Eggs", "Apples", "Bananas"]
print("Shopping list:", ', '.join(shopping_list))


item_to_remove = "Eggs"
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"{item_to_remove} removed from the list.")
else:
    print(f"{item_to_remove} is not on the shopping list.")


item_to_check = "Cheese"
if item_to_check in shopping_list:
    print(f"{item_to_check} is on the shopping list.")
else:
    print(f"{item_to_check} is not on the shopping list.")

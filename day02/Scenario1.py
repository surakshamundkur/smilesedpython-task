shopping_list = ["apples", "bananas", 3, "milk", 2, "eggs"]

#1.	Print the number of apples:
count_apples = shopping_list.count("apples")
print("number of apples=",count_apples )

#2.	Extract the dairy items (milk and eggs):(including quantity)
dairy_items = [item for item in shopping_list if item == "milk" or item == "eggs"]
count_milk = dairy_items.count("milk")
count_eggs = dairy_items.count("eggs")
print("dairy_items:", dairy_items)  
print("Count of 'milk':", count_milk)     
print("Count of 'eggs':", count_eggs)    

#3.	Create a new list with just the fruit names:
fruits = ["apples", "bananas"]
print(fruits)



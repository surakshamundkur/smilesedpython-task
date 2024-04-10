#Task: You're planning a party and need to create guest lists for different tables.
guest_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

#1.	Create a list for each table with 2 guests (replicate the original list):
num_tables = (len(guest_list) + 1) // 2  
for i in range(num_tables):
    table_guests = guest_list[i*2:i*2+2]
    print(f"Table {i+1}: {table_guests}")
#########################################
num_tables = (len(guest_list)) // 2  
for i in range(num_tables):
    table_guests = guest_list[i*1:i*1+2]
    print(f"Table {i+1}: {table_guests}")
####################################
    num_tables = (len(guest_list)+1) // 2  
for i in range(num_tables):
    table_guests = guest_list[i*1:i*1+2]
    print(f"Table {i+1}: {table_guests}")

#2.	Create a single list with all guests invited twice (repeat the list):
combined_guest_list = guest_list + guest_list
print(f"Combined guest list: {combined_guest_list}")
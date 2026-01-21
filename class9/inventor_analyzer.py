raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]
inventory_list_in_tuples = [tuple(item.split(':')) for item in raw_inventory]
print(inventory_list_in_tuples)


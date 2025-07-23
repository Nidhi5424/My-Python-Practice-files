data = input("Enter numbers separated by commas: ")

num_list = data.split(",")

num_set = set(num_list)

num_tuple = tuple(num_list)

print("As list:", num_list)
print("\nAs set:", num_set)
print("\nAs tuple:", num_tuple)

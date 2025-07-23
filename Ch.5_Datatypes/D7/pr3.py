user_input = input("Enter numbers separated by space: ")
num_list = set()
for x in user_input.split():
    num_list.add(x)

#num_list = [int(x) for x in user_input.split()]

unique_set = set(num_list)

print("\nUnique numbers:", unique_set)

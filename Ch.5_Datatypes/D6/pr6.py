user_input = input("Enter numbers separated by space: ")

num_list = []

for x in user_input.split():
    num_list.append(float(x))

largest = max(num_list)
smallest = min(num_list)

print("Largest number is:", largest)
print("Smallest number is:", smallest)

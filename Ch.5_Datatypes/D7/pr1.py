""" my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

my_set.add(6)
print("After adding 6:", my_set)

my_set.remove(3)
print("After removing 3:", my_set)

my_set.add(2)
print("After trying to add duplicate 2:", my_set)

print("Note: 2 is not duplicated in the set.")
 """


user_input = int(input("Enter some numbers separated by space: "))

my_set = set()
for x in user_input.split():
    my_set.add(x)
print("Original set:", my_set)

new_element = int(input("Enter a number to add to the set: "))
my_set.add(new_element)
print(f"After adding {new_element} : {my_set}")

remove_element = int(input("Enter a number to remove from the set: "))
if remove_element in my_set:
    my_set.remove(remove_element)
    print(f"After removing {remove_element} : {my_set}")
else:
    print(remove_element, "was not found in the set.")

duplicate = int(input("Enter a number to try adding again (duplicate): "))
my_set.add(duplicate)
print(f"After trying to add duplicate {duplicate} : {my_set}")

print("Note: Sets do not store duplicates.")

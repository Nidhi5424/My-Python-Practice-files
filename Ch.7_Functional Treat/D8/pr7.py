def print_students(*students):
    if not students:
        print("Student list is empty.")
    else:
        print("Student Names:")
        for name in students:
            print("-", name)

print_students("Aarav", "Neha", "Zoya")
print_students()

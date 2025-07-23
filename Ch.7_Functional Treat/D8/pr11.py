def employee_info(**kwargs):
    required = ["name", "department", "salary"]
    missing = [field for field in required if field not in kwargs]
    
    if missing:
        print("Missing fields:", ", ".join(missing))
    else:
        for key, value in kwargs.items():
            print(f"{key.capitalize()}: {value}")

employee_info(name="Aanya", department="HR", salary=30000)
employee_info(name="Ravi")

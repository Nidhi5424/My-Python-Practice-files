def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

person_info(name="Ankit", age=21, city="Rajkot")

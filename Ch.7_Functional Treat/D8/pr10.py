def total_cost(**products):
    total = 0
    for name, details in products.items():
        price = details.get("price", 0)
        qty = details.get("qty", 0)
        cost = price * qty
        print(f"{name}: ₹{cost}")
        total += cost
    return f"Total Cost: ₹{total}"

print(total_cost(Pen={"price": 10, "qty": 3}, Notebook={"price": 50, "qty": 2}))

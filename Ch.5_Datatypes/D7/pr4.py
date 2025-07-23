products = {'Pen': 10, 'Pencil': 5, 'Notebook': 50, 'Eraser': 3}
print("\nProduct list:", products)

max_product = max(products, key=products.get)
print("\nProduct with highest price:", max_product, "=>", products[max_product])

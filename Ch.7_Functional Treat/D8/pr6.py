def sum_and_product(*nums):
    total = 0
    product = 1
    for n in nums:
        total += n
        product *= n
    return total, product

print(sum_and_product(1, 2, 3, 4))  

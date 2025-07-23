def cube(n):
    return n ** 3

def apply_function(func, numbers):
    return [func(n) for n in numbers]

nums = [1, 2, 3, 4]
result = apply_function(cube, nums)
print("Cubed list:", result)

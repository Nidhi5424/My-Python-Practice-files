def fibonacci(n):
    """
    Generates Fibonacci sequence up to the nth term.
    Input: n (int)
    Output: List of Fibonacci numbers from 0 to nth term
    """
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print(fibonacci(10))
print(fibonacci.__doc__)

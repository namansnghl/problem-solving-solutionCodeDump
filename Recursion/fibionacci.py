def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
    # Write your code here.


n = 3
print(fibonacci(n))

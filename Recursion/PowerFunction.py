count = 0

# O(log N) Time Complexity


def power_fun(a, n):
    global count
    count += 1
    if n == 1:
        return a

    if n % 2 == 0:
        return power_fun(a*a, n/2)
    else:
        return power_fun(a, n-1) * a


print(power_fun(1, 1500000000), count, sep='\n')


def prime_factor(n):
    list_factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            list_factors.append(i)
            n = n / i
        else:
            i += 1
    return list_factors


print(prime_factor(630))

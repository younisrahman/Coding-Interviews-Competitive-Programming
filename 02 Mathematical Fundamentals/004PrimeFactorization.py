# First approach: brute force
# def prime_factor(n):
#     list_factors = []
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             list_factors.append(i)
#             n = n / i
#         else:
#             i += 1
#     return list_factors

# First approach: brute force with exponent
# def prime_factor(n):
#     list_factors = []
#     for i in range(2, n + 1):
#         count = 0

#         while n % i == 0:
#             count += 1
#             n = n / i
#         if count > 0:
#             list_factors.append((i, count))  # (i, count)
#     return list_factors

# Third approach: O(sqrt(n))

import math  # sqrt


def prime_factor(n):
    list_factors = []
    for i in range(2, int(math.sqrt(n))):
        count = 0

        while n % i == 0:
            count += 1
            n = n / i
        if count > 0:
            list_factors.append((i, count))  # (i, count)
    if n > 1:
        list_factors.append((n, 1))  # (n, 1)
    return list_factors


print(prime_factor(72))

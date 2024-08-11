def phi(n):
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            res *= (1.0 - (1.0 / float(p)))
        p += 1
    if n > 1:
        res -= res // n
    return int(res)


n = int(input())
print(phi(n))

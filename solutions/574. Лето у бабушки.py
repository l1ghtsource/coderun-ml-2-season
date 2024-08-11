from collections import defaultdict

MOD = 1000000007


def modinv(a, m):
    return pow(a, m - 2, m)


def prime_factors_up_to(k):
    sieve = [True] * (k + 1)
    p = 2
    primes = []
    while p * p <= k:
        if sieve[p]:
            for i in range(p * p, k + 1, p):
                sieve[i] = False
        p += 1
    for p in range(2, k + 1):
        if sieve[p]:
            primes.append(p)

    factorizations = [defaultdict(int) for _ in range(k + 1)]
    for num in range(2, k + 1):
        n = num
        for prime in primes:
            while n % prime == 0:
                factorizations[num][prime] += 1
                n //= prime
            if n == 1:
                break
    return factorizations


def count_perfect_square_products(m, k):
    factorizations = prime_factors_up_to(k)

    primes = set()
    for factors in factorizations:
        primes.update(factors.keys())
    primes = list(primes)
    prime_indices = {prime: idx for idx, prime in enumerate(primes)}
    num_primes = len(primes)

    dp = defaultdict(int)
    dp[tuple([0] * num_primes)] = 1

    for _ in range(m):
        new_dp = defaultdict(int)
        for num in range(1, k + 1):
            factors = factorizations[num]
            for exp_state, count in dp.items():
                new_exp_state = list(exp_state)
                for prime, exp in factors.items():
                    prime_idx = prime_indices[prime]
                    new_exp_state[prime_idx] = (new_exp_state[prime_idx] + exp) % 2
                new_dp[tuple(new_exp_state)] += count
                new_dp[tuple(new_exp_state)] %= MOD
        dp = new_dp

    favorable_outcomes = 0
    for exp_state, count in dp.items():
        if all(exp == 0 for exp in exp_state):
            favorable_outcomes += count
            favorable_outcomes %= MOD

    return favorable_outcomes


def probability_of_victory(m, k):
    total_outcomes = pow(k, m, MOD)
    favorable_outcomes = count_perfect_square_products(m, k)

    p = favorable_outcomes
    q = total_outcomes

    q_inv = modinv(q, MOD)
    result = (p * q_inv) % MOD

    return result


m, k = map(int, input().split())
result = probability_of_victory(m, k)
print(result)

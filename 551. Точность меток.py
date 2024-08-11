from collections import defaultdict
from math import gcd

n = int(input())
p = list(map(int, input().split()))
v = list(map(int, input().split()))

p_counter = defaultdict(int)
v_counter = defaultdict(int)
pv_counter = defaultdict(lambda: defaultdict(int))

diff = 0

for i in range(n):
    diff += p_counter[p[i]] + v_counter[v[i]] - 2 * pv_counter[p[i]][v[i]]
    p_counter[p[i]] += 1
    v_counter[v[i]] += 1
    pv_counter[p[i]][v[i]] += 1

total = n * (n - 1) // 2 - diff
zn = n * (n - 1) // 2
gcd_val = gcd(total, zn)

ch = total // gcd_val
zn = zn // gcd_val

print(f'{ch}/{zn}')
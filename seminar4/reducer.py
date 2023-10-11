#!/usr/bin/env python3

from operator import itemgetter 
import sys

tot_sum = 0
cnt = 0
mx = None
mn = None

for line in sys.stdin:
    line = line.strip()
    _, value = line.split('\t')
    value = int(value)
    if mx is None:
        mx = value
        mn = value
    mx = max(mx, value)
    mn = min(mn, value)
    cnt += 1
    tot_sum += value

print(f"sum\t{tot_sum}")
print(f"max\t{mx}")
print(f"min\t{mn}")
print(f"count\t{cnt}")
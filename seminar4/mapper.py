#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    print(f"value\t{columns[1]}")
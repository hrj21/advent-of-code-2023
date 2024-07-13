# import package
import re

# read data
with open('data/day1.txt') as f:
    lines = f.readlines()

# iterate
digits = [0]*len(lines)

for idx, text in enumerate(lines):
    first = re.search(r'\d', text).group()
    last  = re.search(r'\d', text[::-1]).group()
    digits[idx] = int(first + last)

# sum
sum(digits)
# import package
import regex as re

# read data
with open('data/day1.txt') as f:
    lines = f.readlines()

# define dict of numbers as strings
nums = {
    'one'   : 1,
    'two'   : 2,
    'three' : 3,
    'four'  : 4,
    'five'  : 5, 
    'six'   : 6,
    'seven' : 7, 
    'eight' : 8,
    'nine'  : 9
}

dgts = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5, 
    '6' : 6,
    '7' : 7, 
    '8' : 8,
    '9' : 9
}

both = dict(nums)
both.update(dgts)

# define regex pattern
pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'

# iterate
digits = [0]*len(lines)

for idx, text in enumerate(lines):
    matches = re.findall(pattern, text, overlapped = True)
    first   = matches[0]
    last    = matches[-1]

    digits[idx] = int(str(both[first]) + str(both[last]))

# sum
sum(digits)

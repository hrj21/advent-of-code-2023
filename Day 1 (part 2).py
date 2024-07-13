# import package
import re

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

# iterate
digits = [0]*len(lines)
positions = [0]*9

for idx, text in enumerate(lines):
    for word, value in nums.items():
         positions[value - 1] = text.find(word)
         first = positions.index(min(n for n in positions if n > -1))
         last = positions.index(max(n for n in positions if n > -1))
         digits[idx] = int(first + last)

digits

for idx, text in enumerate(lines):
    text.find('one')


re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', lines[0]).group()
re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', lines[0]).group()


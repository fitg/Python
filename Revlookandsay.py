from __future__ import print_function
import sys
import math
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_next_two(input_string):
    times = 0
    base = ""
    for number in input_string:
        if times == 0:
            times = int(number)
        if base != "":
            break
        elif base == "":
            base = number
    
    return times, base

def calc_new_two(times, base):
    result = ""
    for i in range(0,times-1):
        result += base
    
    return result
        

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
eprint(s)
times = 0
base = s
output = s
#while base != "":
times, base = read_next_two(output)
eprint(times)
eprint(base)
output = calc_new_two(times, base)

eprint(output)
print(output)

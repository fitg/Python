from __future__ import print_function
import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#Goal
#A happy number is defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits in base-ten, and repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
#
#Given a list of numbers, classify each of them as happy or unhappy.
#Input
#Line 1: An integer N for the number of numbers to test.
#Following N Lines: Each line has a positive integer you should test whether it is happy or not.
#
#Be aware that some input numbers are really BIG, much bigger than your Integer type can handle. Find a way to overcome it.
#Output
#Output N lines.
#Following the same order as inputs, each line starts with a given number from the list, a space, and then an ascii art :) or :( to indicate this number is happy or unhappy.
#Constraints
#1 ≤ N ≤ 100
#0 ≤ each number ≤ 10^26

class HappyDigit:
    
    UNHAPPY = ":("
    HAPPY = ":)"
    
    def initialize(self, number_of_digits, all_digits):
        self.number_of_digits = number_of_digits
        self.all_digits = all_digits
        self.results = {}
        
    def __eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)
    
    def print_debug_to_stderr(self):
        self.__eprint(self.number_of_digits)
        self.__eprint(self.all_digits)
        self.__eprint(self.results)
        
    def print_result_to_stdout(self):
        for key in self.results:
            print(str(key) + " " + self.results[key])
        
    def __is_happy(self,input_number):
    	my_list = []
    	while True:
    		number_to_string = str(input_number)
    		r = 0
    		for i in number_to_string:
    			r += (int(i) * int(i))
    		if r == 1:
    			return True
    		elif r in my_list:
    			return False
    		my_list.append(r)
    		input_number = r
    
    def process_digits(self):
        for i in self.all_digits:
            is_happy = self.HAPPY
            if self.__is_happy(i) == False:
                is_happy = self.UNHAPPY
            self.results[i] = is_happy
    		
class Game:
    def __init__(self):
        self.__happy_digit = HappyDigit() 
        
    def load_parameters(self):
        number_of_digits = int(input())
        all_digits = []
        for i in range(number_of_digits):
            all_digits.append(int(input()))
        self.__happy_digit.initialize(number_of_digits,all_digits)
        
    def run(self):
        self.__happy_digit.process_digits()
        
    def print_debug(self):
        self.__happy_digit.print_debug_to_stderr()
        
    def print_result(self):
        self.__happy_digit.print_result_to_stdout()
        
    
game = Game()
game.load_parameters()
game.run()
game.print_debug()
game.print_result()

# Sorting in a webApi should be tricky as you have to pass all your parameters in a single URL in a GET request, your team decided to do use this convention to order the result by prop1 ascending, then by prop2 descending, then by prop3 ascending.
# +prop1-prop2+prop3
#
# You have to read the given items and print their Ids ordered by the given sorting expression.
# Input
# Line 1 : The sorting expression
# Line 2: The associated types of previously given properties separated by ","
# Line 3 : An integer N of the next input lines
# N next lines an object formatted like this :
# prop1:value1,prop2:value2,prop3:value3
# Output
# The sorted objects ids (there will always be an id property which is an integer).
# In case all property fields have the same values, sort it by the id acsendingly.
# Constraints
# Types can be "int" or "string"
# Example
# Input
# +name
# string
# 3
# id:1,name:maria
# id:2,name:jason
# id:3,name:robert
# Output
# 2
# 1
# 3

# Note: I have cheated on the reverse search and ... could not get it working in full in Codingame :(


import sys
import json
import math
from operator import itemgetter

DESCENDING = 1
ASCENDING = 2

# quick debug method as codingame does not display stdout
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Game:
    def __init__(self, expression, types, number_of_elements):
        self.expression = Expression(expression, types)
        self.number_of_elements = number_of_elements
        self.elements = Elements()
        self.results = []
        self.sort = None
        eprint(f"Expressions to sort by: {self.expression.expressions}")
        eprint(f"Number of elements: {self.number_of_elements}")

    def initialize_elements(self):
        for i in range(self.number_of_elements):
            self.elements.load_element(input())
        eprint(f"Elements to sort: {self.elements.elements}")

    def initialize_sort(self):
        self.sort = BubbleSort()

    def sort_items(self):
        for expression in self.expression.expressions:
            self.results.extend(self.sort.sort_items(expression,self.elements.elements))

    def print_results(self):
        for item in self.results:
            print(item["id"])
        

class Expression:
    def __init__(self, expression, types):
        self._load_expressions(expression)
        self._load_types(types)

    def _load_expressions(self, expression):
        results = []
        expressions = list(filter(None,expression.split("|")))
        for item in expressions:
            if "+" in item:
                results.append(
                    {
                        "sort_by": f"{item.replace('+','')}",
                        "direction": ASCENDING,
                    }
                )
            if "-" in item:
                results.append(
                    {
                        "sort_by": f"{item.replace('-','')}",
                        "direction": DESCENDING,
                    }
                )
        self.expressions = results

    def _load_types(self, types):
        input = types.split(",")
        i = 0
        results = []
        for item in self.expressions:
            item.update({"type": input[i]})
            results.append(
                item
            )
            i = i + 1
        self.expressions = results        

class Elements:
    def __init__(self):
        self.elements = []

    def load_element(self, element):        
        output = "{ "
        for item in element.split(","):
            contents = item.split(":")
            try:
                item_value = int(contents[1])
            except:
                item_value = f"\"{str(contents[1])}\""
            output += f"\"{contents[0]}\":{item_value},"
        output = output[:-1]
        output += " }"
        self.elements.append(json.loads(output))

class BubbleSort:

    def sort_items(self, expression, elements):     
        output = elements
        if expression["direction"] == ASCENDING:
            output = self._sort_ascending(output, expression)
        else:
            output = self._sort_descending(output, expression)

        eprint(f"Sorted list: {output}")
        return output        

    def _sort_ascending(self, input, expression):
        output = input
        length = len(output)
        for i in range(length-1):
            for j in range(0, length-i-1): 
                if output[j][expression["sort_by"]] > output[j + 1][expression["sort_by"]]:
                    output[j], output[j+1] = output[j+1], output[j] 
        return output

    def _sort_descending(self, input, expression):
        return sorted(input, key=itemgetter(expression["sort_by"]), reverse=True)

expression = input()
types = input()
n = int(input())
# add separators to inputs and initialize the game
game = Game(expression.replace("+","|+").replace("-","|-"),types, n)

game.initialize_elements()
game.initialize_sort()
game.sort_items()
game.print_results()

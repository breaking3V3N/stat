# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Set:
    def __init__(self, elements):
        self.elements = elements

    #Set Subtraction
    def set_subtraction(self, set_2):
        new_set = []
        for element in self.elements:
            if element not in set_2.elements:
                new_set.append(element)
        return  new_set

    #Set Multiplication
    def set_multiplication(self, set_2):
        new_set = []
        for element in self.elements:
            for element_2 in set_2.elements:
                new_set.append([element] + [element_2])
        return new_set

    #SET CARDINALITY
    def set_cardinality(self):
        return len(self.elements)

    #need to do
    def gen_contingency_table(self, x_sample_space,y_sample_space, outcomes):
        table = [[]]
        for x in range(0,len(x_sample_space)):
            table[0].append(x)
        print(table)






a = Set([1,2,3])
b = Set([1,2,3])
a.gen_contingency_table([1,2,3],[1,2,3],a.set_multiplication(b))
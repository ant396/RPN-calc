import math
import operator
import os
import time
from rpn import abc
from corrector import Amend

operators = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.div,
             '`': operator.floordiv,   # for //-operator
             '%': operator.mod,
             '^': operator.pow,
             'sqrt': math.sqrt,
             'abs': operator.abs,
             'log': math.log,
             'logt': math.log10,
             'sin': math.sin,
             'cos': math.cos,
             'tan': math.tan,
             'asin': math.asin,
             'acos': math.acos,
             'atan': math.atan,
             'atant': math.atan2,
             'hypot': math.hypot}

def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def convertor(equ):
    stack = []
    result = 0
    for i in equ:
        if isNum(i):
            stack.insert(0, i)
        else:
            if len(i) == 1 or i == 'hypot' or i == 'atant':
                n1 = float(stack.pop(1))
                n2 = float(stack.pop(0))
                result = operators[i](n1, n2)
                stack.insert(0, str(result))
            else:
                n1 = float(stack.pop(0))
                result = operators[i](n1)
                stack.insert(0, str(result))

    return result

def calculate(ex):
    amendStr = Amend(ex)
    equ = amendStr.runCorr()
    answer = convertor(abc(equ))
    print "Result: %f" % answer

    logFile = file('log.txt', 'a')
    logFile.write("{0}\nFixed expression: {1}\nRPN: \
     {2}\n\n".format(time.asctime(), equ, str(abc(equ))))


if __name__ == "__main__":
    ex = raw_input("Please enter your expression: ")
    calculate(ex)

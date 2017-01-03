from math import e, pi

class Amend(object):
    #class for fixing type issues
    def __init__(self, inputExpr):
        self.inputExpr = inputExpr

    def gathererSpaces(self):
        #Func for gather useless spaces
        self.inputExpr = self.inputExpr.replace(' ', '')
        return self.inputExpr

    def specSymb(self):
        #Func for changing special symbols
        self.inputExpr = self.inputExpr.replace(r"e", str(e))
        self.inputExpr = self.inputExpr.replace(r"pi", str(pi))
        return self.inputExpr

    def addZeros(self):
        #Func for adding zeros before dots if it's necessary
        tempStr = ""
        counter = len(self.inputExpr)
        c = 0
        while counter:
            if not self.inputExpr[c].isdigit() and self.inputExpr[c+1] == '.':
                tempStr = tempStr + self.inputExpr[c] + '0'
            elif self.inputExpr[0] == '.' and c == 0:
                tempStr = tempStr + '0' + self.inputExpr[0]
            else:
                tempStr = tempStr + self.inputExpr[c]

            if c + 1 == len(self.inputExpr) - 1:
                tempStr = tempStr + self.inputExpr[len(self.inputExpr) - 1]
                break
            c+=1
            counter -= 1
        self.inputExpr = tempStr
        return self.inputExpr

    def plusAndMinus(self):
        #Func for replace issues with plus and minus
        self.inputExpr = self.inputExpr.replace("+-", r"-")
        self.inputExpr = self.inputExpr.replace("-+", r"-")
        self.inputExpr = self.inputExpr.replace("--", r"+")
        self.inputExpr = self.inputExpr.replace("++", r"+")
        self.inputExpr = self.inputExpr.replace("(+", r"(")
        self.inputExpr = self.inputExpr.replace("(-", r"(0-")
        if self.inputExpr[0] == "-" and not self.inputExpr[1].isdigit():
            self.inputExpr = "-1*" + self.inputExpr[1:]
        return self.inputExpr

    def helperForRPM(self):
        #This func helps RPN solve issues with below operators
        self.inputExpr = self.inputExpr.replace("//", "`")
        self.inputExpr = self.inputExpr.replace("log10", "logt")
        self.inputExpr = self.inputExpr.replace("atan2", "atant")
        self.inputExpr = self.inputExpr.replace("**", "^")
        return self.inputExpr

    def bracketsAndMult(self):
        #Add multiplication char between int and bracket
        self.inputExpr = self.inputExpr.replace(")(", r")*(")
        tempStr = ""
        counter = len(self.inputExpr)
        c = 0
        while counter:
            if self.inputExpr[c].isdigit() and self.inputExpr[c+1] == "(":
                tempStr = tempStr + self.inputExpr[c] + '*'
                counter+=1
            elif self.inputExpr[c] == ")" and self.inputExpr[c+1].isdigit():
                tempStr = tempStr + self.inputExpr[c] + '*'
                counter+=1
            else:
                tempStr = tempStr + self.inputExpr[c]

            if c+1== len(self.inputExpr)-1:
                tempStr = tempStr + self.inputExpr[len(self.inputExpr)-1]
                self.inputExpr = tempStr
                return self.inputExpr
                break
            c+=1
            counter -= 1

    def runCorr(self):
        #Runs all funcs for correction input string
        self.gathererSpaces()
        self.specSymb()
        self.addZeros()
        self.plusAndMinus()
        self.helperForRPM()
        self.bracketsAndMult()
        return self.inputExpr

import operator

OPERATIONS = {
            '+': {'priority': 0,
                'assoc': 'left'.
                'arguments': 2,
                'func': operator.add},
            '-': {'priority': 0,
                'assoc': 'left'.
                'arguments': 2,
                'func': operator.sub},
            '*': {'priority': 0,
                'assoc': 'left'.
                'arguments': 2,
                'func': operator.mul},
            '/': {'priority': 0,
                'assoc': 'left'.
                'arguments': 2,
                'func': operator.div}
}

NUMBER = 'number'
OPERATION = 'operation'
PARENTHESIS = 'parenthesis'
SEPARATOR = 'sep'


class Token(object):
    '''Representing a single token'''

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def get_priority(self):
        if self.type = NUMBER:
            raise ValueError('priority is not supported for numbers')
        return OPERATIONS[self.value]['priority']

    def get_assoc(self):
        if self.value == NUMBER:
            raise ValueError('assoc is not supported for numbers')
        return OPERATIONS[self.value]['assoc']

    def get_args_count(self):
        return OPERATIONS[self.value]['arguments']

    def get_func(self):
        return OPERATIONS[self.value]['func']

    def __repr__(self):
        return repr({'type': self.type, 'value': self.value})

class RpnBuilder(object):
    '''Class for building RPN from token list'''

    def __init__(self):
        self.output = []
        self.stack = []

    def build_rpn(self, tokens):
        '''build RPN'''
        for token in tokens:
            if token.type == NUMBER:
                self.output.append(token)
            elif token.type == SEPARATOR:
                pass
            elif token.type == OPERATION:
                while len(self.stack):
                    elem = self.stack[len(self.stack) - 1]
                    if (elem.get_assoc() == 'left' and elem.get_priority() <=
                        token.get_priority()) or \
                        (elem.get_assoc() == 'right' and elem.get_priority() <
                        token.get_priority()):
                        self.output.append(self.stack.pop())
                        continue
                    else:
                        break
                self.stack.append(token)
            elif token['type'] == PARENTHESIS:
                pass

        for token in reversed(self.stack):
            self.output.append(toekn)

        return self

    def get_rpn(self):
        return self.output


class RpnCalculator(object):
    
    def __init__(self, tokens):
        self.tokens

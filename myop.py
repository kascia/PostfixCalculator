class Op:
    
    def __init__(self, value=''):
        self.value=value
    
    def __repr__(self):
        return self.value
    
    @staticmethod
    def new_instance(ch):
        options = {'+': Add, '-':Sub, '*':Mul , '/':Div}   
        return options[ch](ch)

    def is_prior(self,op):
        return op.priority > self.priority
        

class Sub(Op):
    lexeme = 'SUB'
    priority = 2

class Add(Op):
    lexeme = 'ADD'
    priority = 2

class Div(Op):
    lexeme = 'DIV'
    priority = 1

class Mul(Op):
    lexeme = 'MUL'
    priority = 1
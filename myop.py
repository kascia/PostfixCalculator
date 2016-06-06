from mynumber import Number

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
    def operate(self, a, b):
        return Number.new_instance(a.get_value() - b.get_value())
    
class Add(Op):
    lexeme = 'ADD'
    priority = 2
    def operate(self, a, b):
        return Number.new_instance(a.get_value() + b.get_value())
    
class Div(Op):
    lexeme = 'DIV'
    priority = 1
    def operate(self, a, b):
        return Number.new_instance(a.get_value() / b.get_value())
    
class Mul(Op):
    lexeme = 'MUL'
    priority = 1
    def operate(self, a, b):
        return Number.new_instance(a.get_value() * b.get_value())
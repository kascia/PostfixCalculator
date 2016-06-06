from mynumber import Number
from myop import Op
from myparan import Paran

class Converter:
    
    def __init__(self):
        self.stacks = []
        
    def infix2postfix(self,infix):
        postfix = []
        stack = Stack()
        for token in infix:
            if token.lexeme is 'LPARAN':
                self.stacks.append(stack)
                stack = Stack()
            elif token.lexeme is 'RPARAN': 
                stack.popall()
                stack = self.stacks.pop()
            else: # Op or Number
                stack.push(token)
        stack.popall()
        postfix = stack.postfix
        
        return postfix
    
    
class Stack: # for postfix 
    postfix = []
    def __init__(self):
        self.stack = []
        
        
    def push(self, token):
        if isinstance(token, Number):
            self.stack.append(token)
        elif isinstance(token, Op):
            for i in range(len(self.stack)):
                if not token.is_prior(self.stack[-1]):
                    self.postfix.append(self.stack.pop())
            self.stack.append(token)
        
    def popall(self):
        for i in range(len(self.stack)):
            self.postfix.append(self.stack.pop())
                    
    
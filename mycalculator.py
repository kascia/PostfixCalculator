from myop import Op

class StackCalculator:
    
    def __init__(self):
        pass
    
    def calculate(self,postfix):
        ans = 0.0
        stack = []
        
        while len(postfix) is not 0: 
            print(stack) # for debuging
            if isinstance(postfix[0], Op):
                b = stack.pop()
                a = stack.pop()
                stack.append(postfix.pop(0).operate(a, b))
            else :
                stack.append(postfix.pop(0))
            
        ans = stack[0]
        return ans
    
    
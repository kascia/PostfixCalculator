from mytokenizer import Tokenizer
from myconverter import Converter
from mycalculator import StackCalculator

class Solver:
    
    def __init__(self):
        pass
        
    
    def solve(self, infix):
        
        tokenizer = Tokenizer()
        converter = Converter()
        stack_calculator = StackCalculator()
        
        tokens_infix = tokenizer.tokenize(infix)
        print(tokens_infix)
        
        tokens_postfix = converter.infix2postfix(tokens_infix)
        ans = stack_calculator.calculate(tokens_postfix)
        
        return ans
    
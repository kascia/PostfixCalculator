import re

#from number import Number
#from paran import Paran
#from op import Op

class Tokenizer:
    
    re_token = re.compile('[0-9]+[\.][0-9]+|[0-9]+|[\+\-\*\/]|[\(\)]')
    re_number = re.compile('[0-9]+[\.][0-9]+|[0-9]+')
    re_op = re.compile('[\+\-\*\/]')
    re_paran = re.compile('[\(\)]')
    
    def __init__(self):
         self.tokens=[]
   
    def tokenize(self, str_):        
        
        raw_tokens = self.re_token.findall(str_)
        '''        
        self.tokens = [re_number.match(token) and Number.new_instance(token) or 
        re_op.match(token) and Op.new_instance(token) or 
        re_paran.match(token) and Paran.new_instance(token) for token in raw_tokens]
        '''
        self.tokens = raw_tokens
        return self.tokens
'''
        numbers = self.re_number.findall(strcalc)
        ops = self.re_op.findall(strcalc)
        parans = self.re_paran.findall(strcalc)
        
        self.tokenize_numbers(strcalc,numbers)
        self.tokenize_ops(strcalc,ops)
        self.tokenize_parans(strcalc,parans)
        self.tokens.sort(key=lambda dic: dic['index'])
  
    
    def tokenize_numbers(self, _str, numbers):
        self.tokenize_class(_str, numbers, Number)

    def tokenize_ops(self, _str, ops):
        self.tokenize_class(_str,ops,Op)
    
    def tokenize_parans(self, _str, parans):
        self.tokenize_class(_str,parans,Paran)
    
    def tokenize_class(self, _str, items, _Class):
        findfrom = 0
        for item in items:
            token = dict()
            index = _str.find(item, findfrom)
            findfrom = index + 1
            token['index'] = index
            token['instance'] = _Class.new_instance(item)
            self.tokens.append(token)  
'''
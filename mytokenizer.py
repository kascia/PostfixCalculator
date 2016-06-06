import re

from mynumber import Number
from myparan import Paran
from myop import Op

class Tokenizer:
    
    re_token = re.compile('[0-9]+[\.][0-9]+|[0-9]+|[\+\-\*\/]|[\(\)]')
    re_number = re.compile('[0-9]+[\.][0-9]+|[0-9]+')
    re_op = re.compile('[\+\-\*\/]')
    re_paran = re.compile('[\(\)]')
    
    def __init__(self):
         self.tokens=[]
   
    def tokenize(self, str_):        
        
        raw_tokens = self.re_token.findall(str_)
           
        self.tokens = [self.re_number.match(token) and Number.new_instance(token) 
                       or self.re_op.match(token) and Op.new_instance(token) 
                       or self.re_paran.match(token) and Paran.new_instance(token) 
                       for token in raw_tokens]
        
        return self.tokens
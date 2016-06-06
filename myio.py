import sys

class IO:
    def __init__(self):
        self.infix=''
        self.ans=0.0
        
    def get_infix(self):
        argv = sys.argv[1:]
        argc = len(argv)
        
        for i in range(argc):
            self.infix += argv[i]
            
        return self.infix
    
    def print_ans(self,ans):
        self.ans = ans
        print('answer' , self.ans)
    
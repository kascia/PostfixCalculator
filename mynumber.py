class Number:
    lexeme = 'NUMBER'
    priority = 0
    def __init__(self, value=0.0):
        self.value=value

    def __repr__(self):
        return str(self.value)
    
    def get_value(self):
        return float(self.value)
    
    @staticmethod
    def new_instance(value):
        return Number(value)
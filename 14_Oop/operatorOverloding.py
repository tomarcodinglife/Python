#   +	    __add__(self, other)	    Addition of objects
#   -	    __sub__(self, other)	    Subtraction of objects
#   *	    __mul__(self, other)	    Multiplication of objects
#   /	    __truediv__(self, other)	True division of objects
#   %	    __mod__(self, other)	    Modulus of objects
#   ==	    __eq__(self, other)	        Comparison for equality
#   <	    __lt__(self, other)	        Less than comparison
#   <=	    __le__(self, other)	        Less than or equal comparison
#   >	    __gt__(self, other)	        Greater than comparison
#   >=	    __ge__(self, other)	        Greater than or equal comparison
#   !=	    __ne__(self, other)	        Not equal comparison

class Number:
    def __init__(self, value):
        self.num = value
    
    def __add__(self, value1):
        return self.num + value1.num
    
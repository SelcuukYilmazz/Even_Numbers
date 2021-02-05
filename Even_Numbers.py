import re
import sys
def even_number(x):
    
    
    L = map(int, re.findall(r'-?\d+', S))
    
    L = [x for x in L if x > 0]
    
    K = [x for x in L if x % 2 == 0]
    
    print("Even Numbers: ", K)
    print("Sum of Even Numbers:", sum(K))
    print("Even Number Rate:", sum(K) / sum(L))

    
del sys.argv[0]
S = str(sys.argv)
    
even_number(S)
    

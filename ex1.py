import sys
sys.path.append('..')

from lib.stack import Stack

def dec_to_bin(dec):
    s = Stack()
    while(dec>0):
        s.push(dec%2)
        dec // 2
    binary = 0

    for i in range(s.size()):
        num = s.pop()
        binary += num*(10**s.size())
    
    return binary
        
dec_to_bin(42)
dec_to_bin(100)
    
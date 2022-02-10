"""
exemple:
    myself --> mys / elf --> elfmys
    
"""

def cc_even(word):
    word = word.lower()
    
    m = int(len(word)/2)

    a = word[:m]
    b = word[m:]

    return b+a


"""
C4: end,start,middle
"""

def C4a(word,n):
    """
    AB CD E (5)
    """
    if n == 0:
        a  = word[0:2]
        b = word[2:4]
        c = word[4]
        return c+a+b
    elif n == 1:
        a = word[1:5]
        b = word[0]

        return a+b


def C4b(word,n):
    """
    ABC DEF G (7)
    """
    a  = word[0:3]
    b = word[3:6]
    c = word[6]

    if n == 0:
        return c+a+b
    elif n == 1:
        a = word[1:9]
        b = word[0]

        return a+b


def C4c(word,n):
    """
    ABCD EFGH I (9)
    """

    if n == 0:
        a  = word[0:4]
        b = word[4:8]
        c = word[8]

        return c+a+b

    elif n == 1:
        a = word[1:9]
        b = word[0]

        return a+b


def C4d(word,n):
    """
    ABCDE FGHIJ K (11)
    """
    a  = word[0:5]
    b = word[5:10]
    c = word[10]

    if n == 0:
        return c+a+b
    elif n == 1:
        a = word[1:12]
        b = word[0]
        return a+b


def C4e(word,n):
    """
    ABCDEF GHIJKL M (13)
    """

    a  = word[0:6]
    b = word[6:12]
    c = word[12]

    if n == 0:
        return c+a+b
    elif n == 1:
        a = word[1:13]
        b = word[0]
        return a+b
        

def sub_letter_c4(word):
    
    if len(word) == 5:
        return C4a(word,0)
    elif len(word) == 7:
        return C4b(word,0)
        
    elif len(word) == 9:
        return C4c(word,0)
    elif len(word) == 11:
        return C4d(word,0)
    elif len(word) == 13:
        return C4e(word,0)
    else:
        return word


def desub_letter_c4(word):
    
    if len(word) == 5:
        return C4a(word,1)
    elif len(word) == 7:
        return C4b(word,1)
        
    elif len(word) == 9:
        return C4c(word,1)
    elif len(word) == 11:
        return C4d(word,1)
    elif len(word) == 13:
        return C4e(word,1)
    else:
        return word


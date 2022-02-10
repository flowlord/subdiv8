"""
C5: end,middle,start
"""

def C5a(word,n):
    """
    AB CD E (5)
    """
    if n == 0:
        a  = word[0:2]
        b = word[2:4]
        c = word[4]
        return c+b+a
    elif n == 1:
        a = word[3:5]
        b = word[1:3]
        c = word[0]

        return a+b+c


def C5b(word,n):
    """
    ABC DEF G (7)
    """
    a  = word[0:3]
    b = word[3:6]
    c = word[6]

    if n == 0:
        return c+b+a
    elif n == 1:
        a = word[4:7]
        b = word[1:4]
        c = word[0]

        return a+b+c


def C5c(word,n):
    """
    ABCD EFGH I (9)
    """

    if n == 0:
        a  = word[0:4]
        b = word[4:8]
        c = word[8]

        return c+b+a

    elif n == 1:
        a = word[5:10]
        b = word[1:5]
        c = word[0]
        return a+b+c


def C5d(word,n):
    """
    ABCDE FGHIJ K (11)
    """
    a  = word[0:5]
    b = word[5:10]
    c = word[10]

    if n == 0:
        return c+b+a
    elif n == 1:
        a = word[6:11]
        b = word[1:6]
        c = word[0]
        return a+b+c


def C5e(word,n):
    """
    ABCDEF GHIJKL M (13)
    """

    a  = word[0:6]
    b = word[6:12]
    c = word[12]

    if n == 0:
        return c+b+a
    elif n == 1:
        a = word[7:13]
        b = word[1:7]
        c = word[0]

        return a+b+c


def sub_letter_c5(word):
    
    if len(word) == 5:
        return C5a(word,0)
    elif len(word) == 7:
        return C5b(word,0)
        
    elif len(word) == 9:
        return C5c(word,0)
    elif len(word) == 11:
        return C5d(word,0)
    elif len(word) == 13:
        return C5e(word,0)
    else:
        return word


def desub_letter_c5(word):
    
    if len(word) == 5:
        return C5a(word,1)
    elif len(word) == 7:
        return C5b(word,1)
        
    elif len(word) == 9:
        return C5c(word,1)
    elif len(word) == 11:
        return C5d(word,1)
    elif len(word) == 13:
        return C5e(word,1)
    else:
        return word


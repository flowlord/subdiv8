"""
C3: middle,start,end
"""

def C3a(word):
    """
    AB CD E (5)
    """

    a  = word[0:2]
    b = word[2:4]
    c = word[4]

    return b+a+c


def C3b(word,n):
    """
    ABC DEF G (7)
    """
    a  = word[0:3]
    b = word[3:6]
    c = word[6]

    if n == 0:
        return b+a+c
    elif n == 1:
        return b+a+c


def C3c(word):
    """
    ABCD EFGH I (9)
    """
    a  = word[0:4]
    b = word[4:8]
    c = word[8]

    return b+a+c


def C3d(word,n):
    """
    ABCDE FGHIJ K (11)
    """
    a  = word[0:5]
    b = word[5:10]
    c = word[10]

    return b+a+c


def C3e(word):
    """
    ABCDEF GHIJKL M (13)
    """

    a  = word[0:6]
    b = word[6:12]
    c = word[12]

    return b+a+c


def sub_letter_c3(word):
    
    if len(word) == 5:
        return C3a(word)
    elif len(word) == 7:
        return C3b(word,0)
        
    elif len(word) == 9:
        return C3c(word)
    elif len(word) == 11:
        return C3d(word,0)
    elif len(word) == 13:
        return C3e(word)

    else:
        return word


def desub_letter_c3(word):
    
    if len(word) == 5:
        return C3a(word)
    elif len(word) == 7:
        return C3b(word,1)
        
    elif len(word) == 9:
        return C3c(word)
    elif len(word) == 11:
        return C3d(word,1)
    elif len(word) == 13:
        return C3e(word)

    else:
        return word



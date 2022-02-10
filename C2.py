"""
C2: middle,end,start

"""

def C2a(word,n):
    """
    AB CD E (5)
    """
    a  = word[0:2]

    if n == 0:
        b = word[2:4]
        c = word[4]

        return b+c+a

    elif n == 1:
        b = word[2:3]
        c = word[3:5]

        return c+a+b


def C2b(word,n):
    """
    ABC DEF G (7)
    """
    a  = word[0:3]

    if n == 0:
        b = word[3:6]
        c = word[6]

        return b+c+a

    elif n == 1:
        b = word[3:4]
        c = word[4:7]

        return c+a+b


def C2c(word,n):
    """
    ABCD EFGH I (9)
    """
    a  = word[0:4]

    if n == 0:
        b = word[4:8]
        c = word[8]

        return b+c+a

    elif n == 1:
        b = word[5:9]
        c = word[4:5]

        return b+a+c


def C2d(word,n):
    """
    ABCDE FGHIJ K (11)
    """

    a  = word[0:5]

    if n == 0:
        b = word[5:10]
        c = word[10]

        return b+c+a

    elif n == 1:
        b = word[6:11]
        c = word[5:6]

        return b+a+c


def C2e(word,n):
    """
    ABCDEF GHIJKL M (13)
    """

    a  = word[0:6]

    if n == 0:
        b = word[6:12]
        c = word[12]

        return b+c+a

    elif n == 1:
        b = word[7:13]
        c = word[6:7]

        return b+a+c


def sub_letter_c2(word):
    
    if len(word) == 5:
        return C2a(word,0)
    elif len(word) == 7:
        return C2b(word,0)
        
    elif len(word) == 9:
        return C2c(word,0)
    elif len(word) == 11:
        return C2d(word,0)
    elif len(word) == 13:
        return C2e(word,0)

    else:
        return word


def desub_letter_c2(word):
    
    if len(word) == 5:
        return C2a(word,1)
    elif len(word) == 7:
        return C2b(word,1)
        
    elif len(word) == 9:
        return C2c(word,1)
    elif len(word) == 11:
        return C2d(word,1)
    elif len(word) == 13:
        return C2e(word,1)

    else:
        return word





"""
INIT ---> start,middle,end

combination = C

C1: start,end,middle

C2: middle,end,start
C3: middle,start,end

C4: end,start,middle

C5: end,middle,start

IF IS ONLY IF THE LENGTH OF THE WORD IS ODD

"""

from C1 import sub_letter_c1,desub_letter_c1
from C2 import sub_letter_c2,desub_letter_c2
from C3 import sub_letter_c3,desub_letter_c3
from C4 import sub_letter_c4,desub_letter_c4
from C5 import sub_letter_c5,desub_letter_c5

from random import randint


def cc(word):
    word = word.lower()
    
    x = randint(1,5)
    if x == 1:
        return sub_letter_c1(word)
    elif x == 2:
        return sub_letter_c2(word)
    elif x == 3:
        return sub_letter_c3(word)
    elif x == 4:
        return sub_letter_c4(word)
    else:
        return sub_letter_c5(word)


def dd(word):
    word_lst = open('odd_length_word_list.txt','r').readlines()
    word_lst = [word.replace('\n','') for word in word_lst]

    if word in word_lst:
        return word

    aux = word

    while word not in word_lst:
        x = randint(1,5)

        if x == 1:
            word = desub_letter_c1(aux)
        elif x == 2:
            word = desub_letter_c2(aux)
        elif x == 3:
            word = desub_letter_c3(aux)
        elif x == 4:
            word = desub_letter_c4(aux)
        else:
            word = desub_letter_c5(aux)

    return word





#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
[ Temporary title ]

Example:
    Hello word

    1) hello (5 letters so it's odd)
    2) Choose a random combination
    3) substitute the places !
    --> he-ll-o --> ohell

    ---------------------------
    
    1) word (4 letters so it's even)
    2) substitute the places !
    --> wo-rd --> rdwo

    ---------------------------
    
    I repeat the same operation for each word of the sentence !


only english words

Created on Tue Jun 22 00:00:00 2021

@author: FLOW LORD

twitter: https://twitter.com/flowlord_

"""

from sub_even_word import cc_even
from sub_odd_word import cc,dd


def change_place(sentence):
    words = sentence.split(' ')
    nt = ''

    for word in words:
        if len(word)%2 == 0:
            nt = nt + cc_even(word)+' '
        else:
            nt = nt + cc(word)+' '

    return nt


def change_place_ins(sentence):
    words = sentence.split(' ')
    nt = ''

    for word in words:
        if len(word)%2 == 0:
            nt = nt + cc_even(word)+' '
        else:
            nt = nt + dd(word)+' '

    return nt


sentences = ['meeting tonight for speak','hello world','see you at night','where do you live',
			'What do you do','see you soon','see you next week','see you on monday',
			'see you tomorrow','have a good weekend','i will do that later',
			'i can talk to you','we can see each other','im afraid im busy then',
            'you can help me do my homework','they are there','so far so good']


def sub_sentences():
    for sentence in sentences:
        print(change_place(sentence))


def demo():
    print('sub word place')
    s = change_place('hello world')
    print(s,'\n\n')
    print('inverse')
    ds = change_place_ins(s)
    print(ds)


demo()




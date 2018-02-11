# -*- coding: utf-8 -*-
def first_word(text):
    i = 0

    while True:
        if text[i].find('o'):
            print(i)
        else:
            i += 1


first_word("Hello world")
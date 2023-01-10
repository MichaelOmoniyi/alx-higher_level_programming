#!/usr/bin/python3

def multiple_returns(sentence):
    sent_len = len(sentence)
    if sent_len == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return ((sent_len, f_char))

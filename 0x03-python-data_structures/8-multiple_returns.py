#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        print("Length: {:d} - First character: none:".format(len(sentence)))
    print("Length: {:d} - First character: {:c}".format(len(sentence),
                                                            sentence[0]))

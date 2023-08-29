#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0


    try:
        for i in range(0, x):
            printf(f"{my_list[i]}", end="")
            lenth += 1
        print(end="")
        return(length)
    except IndexError:
        print("{x} greater the the length of the list")
    

#    for i in range(x):
#        try:
#            print(f"{my_list[i]}", end="")
#            length += 1
#        except IndexError:
#            break
#    print()

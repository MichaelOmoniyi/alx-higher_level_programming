#!/usr/bin/python3

if __name__ == "__main__":
    result = 0

    for arguments in sys.argv:
        if len(sys.argv) == 0:
            print()
        elif len(sys.argv) == 1:
            print(sys.argv[0])
        else:
            result += sys.argv

    print(result)

'''
This script takes a string and multiplies it by a number.
sys.argv[1] is a string
sys.stdin is a file containing a number
'''

import sys

string1 = sys.argv[1]
number1 = int(sys.stdin.read())

def main():
    print(string1 * number1)


if __name__ == "__main__":
    main()
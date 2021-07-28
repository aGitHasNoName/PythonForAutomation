'''
This script takes a string and multiplies it by a number.
sys.argv[1] is a string
sys.argv[2] is a number
'''

import sys

string1 = sys.argv[1]
number1 = int(sys.argv[2])

def main():
    print(string1 * number1)
    print("DONE")

if __name__ == "__main__":
    main()
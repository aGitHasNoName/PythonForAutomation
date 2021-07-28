import sys

def main():
    print("\nObject type of sys.argv:")
    print(type(sys.argv))
    print("\nLength of sys.argv:")
    print(len(sys.argv))    
    for i in sys.argv:
        print("\nThis is an argument:")
        print(i)
        print("of type:")
        print(type(i))

if __name__ == "__main__":
    main()

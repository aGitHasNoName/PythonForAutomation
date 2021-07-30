import sys

lines = [line for line in sys.stdin]


def getCount(a_list):
    i = 0
    for x in a_list:
        if x != "\n":
            i += 1
        else:
            break
    return(i)

def createLines(a_list, num):
    new_lines = []
    for n in range(1, num):
        name = a_list[n-1].rstrip('\n')
        email = a_list[n+num].rstrip('\n')
        new_lines.append(f"{name},{email}\n")
    return new_lines
    
def main():
    total = getCount(lines)
    for i in createLines(lines, total):
        sys.stdout.write(i)
        
if __name__ == "__main__":
    main()
    
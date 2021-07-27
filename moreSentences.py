from statistics import mode

def printMode(a_list):
    '''Finds the mode of a list and returns it in a complete sentence'''
    m = mode(a_list)
    return f"The mode of the numbers provided is {m}."

def printMax(a_list):
    '''Finds the max of a list and returns it in a complete sentence'''
    m = max(a_list)
    return f"The max of the numbers provided is {m}."

def printMin(a_list):
    '''Finds the min of a list and returns it in a complete sentence'''
    m = min(a_list)
    return f"The min of the numbers provided is {m}."

if __name__ == "__main__":
    main()
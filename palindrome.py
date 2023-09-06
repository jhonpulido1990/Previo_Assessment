#!/usr/bin/python3
def comparador(array, a, b):
    if array[a] != array[b]:
        if (array[a] < array[b]):
            array[a] = array[b]
        if (array[b] < array[a]):
            array[b] = array[a]
        return False
    else:
        return True

if __name__ == "__main__":
    import sys
    letter = sys.argv[1]
    arrayString = []
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    differ = 0
    palindrome = ''
    change = 0
    for i in range(len(letter)):
        arrayString.append(int(letter[i]))
    long = n - 1
    for j in range(int(n / 2)):
        if arrayString[j] != arrayString[long]:
            differ += 1
        long -= 1
    if (differ > k):
        print(-1)
        exit(-1)
    long = n - 1
    init = 0
    for ini in range(long):
        comparador(arrayString, long, init)
        long -= 1
        init += 1
    k = k -differ
    print(k)

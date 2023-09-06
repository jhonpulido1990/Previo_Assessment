#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    letter = sys.argv[1]
    arrayString = []
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    differ = 0
    for i in range(len(letter)):
        arrayString.append(int(letter[i]))
    long = n - 1
    for j in range(int(len(arrayString) / 2)):
        if arrayString[j] == arrayString[long]:
            continue
        differ += 1
        long -= 1
    if (differ > k):
        print(-1)
        exit(-1)
    long = n - 1
    init = 0
    while (long >= init):
        if k <= 0:
            break;
        if arrayString[init] == arrayString[long]:
            if (k - 2) >= differ:
                if arrayString[init] != 9:
                    arrayString[init] = arrayString[long] = 9
                    k -= 2
            else:
                if (k - 2) >= differ:
                    if arrayString[init] != 9:
                        arrayString[init] = 9
                        k - 1
                    if arrayString[long] != 9:
                        arrayString[long] = 9
                else:
                    if arrayString[init] > arrayString[long]:
                        arrayString[long] = arrayString[init]
                    else:
                        arrayString[init] = arrayString[long]
                    k -= 1
                differ -= 1
            if long == init:
                if k > 0:
                    arrayString[long] = 9
                    k -= 1
        long -= 1
        init += 1
        letter = ''.join(str(indexes) for indexes in arrayString)
    print(letter)

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for n in range(passnum):
            if alist[n] > alist[n + 1]:
                alist[n], alist[n + 1] = alist[n + 1], alist[n]
                
alist = [0, 1, 2, 5, 7, 9, 8, 3, 4, 6]
bubbleSort(alist)
print(alist)
#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i, j = 0, 0
    size1 = len(L1)
    size2 = len(L2)

    while i < size1 and j < size2:
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    L = L + L1[i:] + L2[j:]

    return L

def main():
   L1 = [1, 4, 5, 7, 11, 13]
   L2 = [2, 6,]
   print(merge(L1, L2))

if __name__ == "__main__":
    main()

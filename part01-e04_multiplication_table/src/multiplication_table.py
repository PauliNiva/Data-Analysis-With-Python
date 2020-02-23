#!/usr/bin/env python3


def main():
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if n < 10:
                print ('{:4d}'.format(i*n), end="")
            else:
                print ('{:4d}'.format(i*n))
if __name__ == "__main__":
    main()

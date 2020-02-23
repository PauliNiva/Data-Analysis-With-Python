#!/usr/bin/env python3

def main():
    for i in [1, 2 , 3, 4, 5, 6]:
        for n in [1, 2, 3, 4, 5, 6]:
            if i+n==5:
                print(f'({i}, {n})')

if __name__ == "__main__":
    main()

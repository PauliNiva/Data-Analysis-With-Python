#!/usr/bin/env python3


lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main():
    for t in lst:
        n=triple(t)
        m=square(t)

        if m>n:
            break
        else:
            print(f"triple({t})=={n} square({t})=={m}")
       

def triple(t):
    "Multiplies its argument by 3"
    s=t*3
    return s

def square(t):
    "Computes the square of its argument"
    s=t*t
    return s

if __name__ == "__main__":
    main()

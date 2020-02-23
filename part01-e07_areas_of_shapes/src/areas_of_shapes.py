#!/usr/bin/env python3
import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle):").lower()
        if shape == "triangle":
            b = float(input("Give base of the triangle:"))
            h = float(input("Give height of the triangle:"))
            triangle(b, h)
        elif shape == "rectangle":
            w = float(input("Give width of the rectangle:"))
            l = float(input("Give height of the rectangle:"))
            rectangle(w, l)
        elif shape == "circle":
            r = float(input("Give radius of the circle:"))
            circle(r)
        elif shape == "":
            break
        else:
            print("Unknown shape!")


def triangle(b, h):
    printer(0.5*b*h)

def rectangle(l, w):
    printer(l*w)

def circle(r):
    printer(math.pi*math.pow(r, 2))

def printer(n):
    print(f"The area is {n}")

if __name__ == "__main__":
    main()

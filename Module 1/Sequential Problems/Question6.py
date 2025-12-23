from math import sqrt
if __name__ == "__main__":
    a, b, c = map(float, input("Enter length of 3 sides: ").split())
    s = (a + b + c)/ 2
    v = s*(s-a)*(s-b)*(s-c)
    if v > 0:
        print(f"Perimeter: {a + b + c}")
        print(f"Area: {sqrt(v)}")
    else:
        print("This Cannot Form a Triangle!!!")

'''
O/P
Enter length of 3 sides: 4 5 8
Perimeter: 17.0
Area: 8.181534085976786
'''
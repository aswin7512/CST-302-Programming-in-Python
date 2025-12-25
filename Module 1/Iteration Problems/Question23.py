asc = ord("A")
def starPyramid(n = 5):
    for i in range(1, n*2, 2):
        print((" " * ((n -(i // 2))- 1)) + ("*" * i))


def invStarPyramid(n = 5):
    for i in range((n*2)-1, 0, -2):
        print((" " * ((n -(i // 2))- 1)) + ("*" * i))


def starTriangle(n = 5):
    for i in range(1, n+1):
        print("* " * i)


def invStarTriangle(n = 5):
    for i in range(n, 0, -1):
        print("* " * i)


def alphaPyramid(n = 5):
    for i in range(n):
        s = " " * (n -i- 1)
        for j in range(asc, asc+i+1): s += f"{chr(j)} "
        print(s)


def alphaTriangle(n = 5):
    for i in range(n):
        print(f"{chr(asc+i)} " * (i+1))


def numberPyramid(n = 5):
    for i in range(n):
        s = " " * (n - i - 1)
        for j in range(1, (i * 2)+ 2): s += f"{j}"
        print(s)


def numberTriangle(n = 5):
    for i in range(1, n+1):
        s = ""
        for j in range(1, i+1): s += f"{j} "
        print(s)


def invNumberTriangle(n = 5):
    for i in range(n, 0, -1):
        s = ""
        for j in range(1, i+1): s += f"{j} "
        print(s)


def contNumberTriangle(n = 5):
    c = 1
    for i in range(1, n+1):
        s = ""
        for _ in range(i): s += f"{c} "; c+= 1
        print(s)


if __name__ == "__main__":
    n = int(input("Enter a Number: "))

    print("\n1.")
    starPyramid(n)

    print("\n2.")
    invStarPyramid(n)

    print("\n3.")
    starTriangle(n)

    print("\n4.")
    invStarTriangle(n)

    print("\n5.")
    alphaPyramid(n)

    print("\n6.")
    alphaTriangle(n)

    print("\n7.")
    numberPyramid(n)

    print("\n8.")
    numberTriangle(n)

    print("\n9.")
    invNumberTriangle(n)

    print("\n10.")
    contNumberTriangle(n)

'''
O/P
Enter a Number: 5

1.
    *
   ***
  *****
 *******
*********

2.
*********
 *******
  *****
   ***
    *

3.
* 
* * 
* * * 
* * * * 
* * * * * 

4.
* * * * * 
* * * * 
* * * 
* * 
* 

5.
    A 
   A B 
  A B C 
 A B C D 
A B C D E 

6.
A 
B B 
C C C 
D D D D 
E E E E E 

7.
    1
   123
  12345
 1234567
123456789

8.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

9.
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

10.
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''
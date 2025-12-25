def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    v = 0
    for i in range(1, n+1):
        v += i / factorial(i)
    print("%.2f" % v)

'''
O/P
Enter a Number: 10
2.72
'''
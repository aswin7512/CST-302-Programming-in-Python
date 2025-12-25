from Question25 import factorial

if __name__ == "__main__":
    x, n = map(int,input("Enter x, n: ").split())
    v = 0
    for i in range(n+1):
        v += (x ** i) / factorial(i)
    print("%.2f" % v)

'''
O/P
Enter x, n: 5 100
148.41
'''
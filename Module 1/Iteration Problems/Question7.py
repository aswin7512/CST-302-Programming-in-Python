if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    n = n-1 if n % 2 else n
    for i in range(n, -1, -2):
        print(i, end = ", ")

'''
O/P
Enter a Number: 9
8, 6, 4, 2, 0, 
'''
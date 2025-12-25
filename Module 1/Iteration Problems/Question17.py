if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    while n != 0:
        print(n % 10, end = ", ")
        n //= 10

'''
O/P
Enter a Number: 1923
3, 2, 9, 1, 
'''
if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    nc, s = n, 0
    while n != 0:
        s += n % 10
        n //= 10
    
    print(f"Sum of Digits of {nc}: {s}")

'''
O/P
Enter a Number: 17312   
Sum of Digits of 17312: 14
'''
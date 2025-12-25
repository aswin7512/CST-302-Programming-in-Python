if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    nc, so, se = n, 0, 0
    while n != 0:
        if (n % 10)% 2:
            so += n % 10
        else:
            se += n % 10
        n //= 10
    
    print(f"Difference btw Sum of Odd Digits and Even digits of {nc}: {abs(so - se)}")

'''
O/P
Enter a Number: 1191123          
Difference btw Sum of Odd Digits and Even digits of 1191123: 14
'''
if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f"Factorial of {n}: {f}")

'''
O/P
Enter a Number: 5
Factorial of 5: 120
'''
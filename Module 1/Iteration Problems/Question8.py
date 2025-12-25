if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    print(f"Factors of {n}:", end = " ")
    for i in range(1, n+1):
        if not (n % i):
            print(i, end = ", ")

'''
O/P
Enter a Number: 256
Factors of 256: 1, 2, 4, 8, 16, 32, 64, 128, 256, 
'''
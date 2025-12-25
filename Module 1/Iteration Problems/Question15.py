if __name__ == "__main__":
    n1, n2 = map(int, input("Enter 2 numbers: ").split())
    print(f"Amstrong Numbers between {n1} and {n2}: ", end = "")
    for i in range(n1, n2+1):
        d, n, am = len(str(i)), i, 0
        for _ in range(d):
            am += (n % 10)** d
            n //= 10
        print(f"{i}, " if am == i else "", end = "")

'''
O/P
Enter 2 numbers: 1 100000
Amstrong Numbers between 1 and 100000: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 
'''
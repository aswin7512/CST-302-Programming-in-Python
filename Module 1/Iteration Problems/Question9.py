if __name__ == "__main__":
    n, s = int(input("Enter a Number: ")), 0
    for i in range(1, n):
        if not(n % i):
            s += i
    print(f"{n} is {"not " if n != s else ""}a Perfect Number")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question9.py"
Enter a Number: 496
496 is a Perfect Number
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question9.py"
Enter a Number: 498
498 is not a Perfect Number
'''
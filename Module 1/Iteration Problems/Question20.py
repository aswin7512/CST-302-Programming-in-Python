if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    nc, nr = n, 0
    while nc != 0:
        nr *= 10
        nr += nc % 10
        nc //= 10
    nr = (-1 * nr) if n < 0 else nr
    print(f"{n} is {"" if n == nr else "Not "}Palindrome")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question20.py"
Enter a Number: 19791
19791 is Palindrome
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question20.py"
Enter a Number: 239345
239345 is Not Palindrome
'''
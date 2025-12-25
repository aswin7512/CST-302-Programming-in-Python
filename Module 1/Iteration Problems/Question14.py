if __name__ == "__main__":
    n = input("Enter a Number: ")
    d, nc, n = len(n), int(n), int(n)
    am = 0
    for i in range(d):
        am += (n % 10)** d
        n //= 10
    print(f"{nc} is {"" if nc == am else "Not "}an Amstrong Number")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question14.py"
Enter a Number: 153
153 is an Amstrong Number
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question14.py"
Enter a Number: 1533
1533 is Not an Amstrong Number
'''
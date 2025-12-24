if __name__ == "__main__":
    n = input("Enter a Number: ")
    print(f"{n} is {"" if len(n) == 3 else f"Not "}a 3 digit Number")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question11.py"
Enter a Number: 456
456 is a 3 digit Number
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question11.py"
Enter a Number: 4455
4455 is Not a 3 digit Number
'''
if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    print(f"{"Zero" if n == 0 else ("Positive" if n > 0 else "Negative")}")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question4.py"
Enter a Number: 50
Positive
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question4.py"
Enter a Number: -50
Negative
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question4.py"
Enter a Number: 0
Zero
'''
if __name__ == "__main__":
    a, b, c = map(int, input("Enter a, b, c: ").split())
    f = (b ** 2) - (4 * a * c)
    print(f"Solution is {"Real and Distinct" if f > 0 else ("Real and same" if f == 0 else "Imaginary")}")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question9.py"
Enter a, b, c: 1 -4 3
Solution is Real and Distinct
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question9.py"
Enter a, b, c: 1 -6 9
Solution is Real and same
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question9.py"
Enter a, b, c: 1 4 5
Solution is Imaginary
'''
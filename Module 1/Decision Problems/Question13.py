if __name__ == "__main__":
    n = float(input("Enter mark percentage: "))
    if n >= 90:
        print(f"{n}: O (Outstanding)")
    elif n >= 85:
        print(f"{n}: A+ (Excellent)")
    elif n >= 80:
        print(f"{n}: A (Very Good)")
    elif n >= 70:
        print(f"{n}: B+ (Good)")
    elif n >= 60:
        print(f"{n}: B (Above Average)")
    elif n >= 50:
        print(f"{n}: C (Average)")
    elif n >= 45:
        print(f"{n}: P (Pass)")
    else:
        print(f"{n}: F (Fail)")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 92
92.0: O (Outstanding)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 87
87.0: A+ (Excellent)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 82
82.0: A (Very Good)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 74
74.0: B+ (Good)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 63
63.0: B (Above Average)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 54
54.0: C (Average)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 47
47.0: P (Pass)
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question13.py"
Enter mark percentage: 40
40.0: F (Fail)
'''
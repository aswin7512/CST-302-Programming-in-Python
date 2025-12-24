if __name__ == "__main__":
    c = input("Enter a Character: ")
    if c.isalpha():
        if c.lower() in ('a', 'e', 'i', 'o', 'u'):
            print(f"{c} is a Vowel")
        else:
            print(f"{c} is a Consonant")
    else:
        print("Invalid Input!!!")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question7.py"
Enter a Character: O
O is a Vowel
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question7.py"
Enter a Character: c
c is a Consonant
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question7.py"
Enter a Character: (
Invalid Input!!!
'''
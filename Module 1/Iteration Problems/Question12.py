if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    if n != 1:
        for i in range(2, (n//2)+1):
            if not(n % i):
                print(f"{n} is not a Prime Number...")
                break
        else:
            print(f"{n} is a Prime Number...")
    else:
        print(f"{n} is neither prime nor composite...")

'''
O/P
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question12.py"
Enter a Number: 5 
5 is a Prime Number...
aswinrd@fedora ~/CST 362 Programming in Python (main)> python -u "Question12.py"
Enter a Number: 10
10 is not a Prime Number...
'''
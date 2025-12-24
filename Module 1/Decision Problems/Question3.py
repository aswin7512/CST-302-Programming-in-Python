if __name__ == "__main__":
    n1, n2 = map(int, input("Enter 2 Numbers: ").split())
    print(f"{n1} is {"Not " if n1 % n2 else ""}Completely Divisible by {n2}")

'''
O/P
Enter 2 Numbers: 45 5
45 is Completely Divisible by 5
'''
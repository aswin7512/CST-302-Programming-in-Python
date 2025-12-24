if __name__ == "__main__":
    n1, n2 = map(int, input("Enter 2 Numbers: ").split())
    print(f"{n1 if n1 > n2 else n2}")

'''
O/P
Enter 2 Numbers: 4 9
9
'''
if __name__ == "__main__":
    n, m = map(int, input("Enter 2 Numbers: ").split())
    t = n
    n = m
    m = t
    print(f"n: {n}, m: {m}")

'''
O/P
Enter 2 Numbers: 4 7
n: 7, m: 4
'''
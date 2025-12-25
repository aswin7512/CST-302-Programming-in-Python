if __name__ == "__main__":
    ns, ne = map(int, input("Enter Starting number and ending number: ").split())
    ns = ns+1 if ns % 2 else ns
    for i in range(ns, ne+1, 2):
        print(i, end = ", ")

'''
O/P
Enter Starting number and ending number: 3 11
4, 6, 8, 10, 
'''
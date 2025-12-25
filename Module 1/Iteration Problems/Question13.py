if __name__ == "__main__":
    n1, n2 = map(int, input("Enter 2 Numbers: ").split())
    for i in range(n1, n2+1):
        for j in range(2, (i//2)+1):
            if not(i % j):
                break
        else:
            if i != 1:
                print(i, end = ", ")

'''
O/P
Enter 2 Numbers: 1 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
'''
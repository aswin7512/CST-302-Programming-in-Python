if __name__ == "__main__":
    a, d, n = map(int, input("Enter a, d, n: ").split())
    for i in range(a, (d * n)+ a, d):
        print(i, end = ", ")

'''
O/P
Enter a, d, n: 2 3 10
2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 
'''
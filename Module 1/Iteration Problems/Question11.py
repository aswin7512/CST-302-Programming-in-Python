if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    np, nc = 0, 1
    print(f"{np}, {nc}, ", end = "")
    for _ in range(n-2):
        print(f"{np + nc}, ", end = "")
        np, nc = nc, np+nc

'''
O/P
Enter a Number: 10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 
'''
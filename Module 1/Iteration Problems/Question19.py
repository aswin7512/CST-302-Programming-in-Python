if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    nc, nr = n, 0
    while nc != 0:
        nr *= 10
        nr += nc % 10
        nc //= 10
    nr = (-1 * nr) if n < 0 else nr
    print(f"Reverse of {n}: {nr}")

'''
O/P
Enter a Number: 1023521
Reverse of 1023521: 1253201
'''
if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    nc, s = n, 0
    while n != 0:
        if (n % 10)% 2:
            s += n % 10
        n //= 10
    
    print(f"Sum of Odd Digits of {nc}: {s}")

'''
O/P
Enter a Number: 125889
Sum of Odd Digits of 125889: 15
'''
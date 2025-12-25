if __name__ == "__main__":
    s = set(map(int, input("Enter a set of numbers: ").split()))
    sum = 0
    for i in s:
        if i % 2:
            sum += i
    print(f"Sum of odd elements: {sum}")
'''
O/P
Enter a set of numbers: 4 5 8 2 9 1
Sum of odd elements: 15
'''
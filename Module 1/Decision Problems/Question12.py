if __name__ == "__main__":
    c = float(input("Enter Energy Consumed: "))
    if c <= 200:
        print(f"Cost: {c * 0.5}")
    elif c <= 400:
        print(f"Cost: {100 +((c - 200) * 0.65)}")
    elif c <= 600:
        print(f"Cost: {230 +((c - 400) * 0.8)}")
    else:
        print(f"Cost: {425 +((c - 600) * 1.25)}")

'''
O/P
Enter Energy Consumed: 650
Cost: 487.5
'''
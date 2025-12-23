if __name__ == "__main__":
    p, r, t = map(float, input("Enter p, r, t: ").split())
    i = (p * r * t)/ 100
    print(f"Interest: {i}\nTotal Amount: {p + i}")

'''
O/P
Enter p, r, t: 1000 10 3
Interest: 300.0
Total Amount: 1300.0
'''
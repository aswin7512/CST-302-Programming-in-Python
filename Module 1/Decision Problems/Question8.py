if __name__ == "__main__":
    p = input("Enter Your Password: ")
    print(f"{p} is a {"Weak" if len(p) < 6 else ("Medium" if len(p) < 10 else "Strong")} password...")

'''
O/P
Enter Your Password: password
password is a Medium password...
'''
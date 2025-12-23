if __name__ == "__main__":
    s = int(input("Enter Time in Seconds: "))
    h, s = s // 3600, s % 3600
    m, s = s // 60, s % 60
    print(f"{h}:{m}:{s}")

'''
O/P
Enter Time in Seconds: 5975
1:39:35
'''
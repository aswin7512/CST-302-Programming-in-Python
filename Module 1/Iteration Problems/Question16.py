if __name__ == "__main__":
    print("Numbers Between 100 & 200 Divisible by 3 but not by 4 are...")
    for i in range(100, 201):
        if not(i % 3) and i % 4:
            print(i, end = ", ")

'''
O/P
Numbers Between 100 & 200 Divisible by 3 but not by 4 are...
102, 105, 111, 114, 117, 123, 126, 129, 135, 138, 141, 147, 150, 153, 159, 162, 165, 171, 174, 177, 183, 186, 189, 195, 198, 
'''
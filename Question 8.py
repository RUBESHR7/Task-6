# 8)if input is 1 (or) 10 (or) 2 (or) 8 (or) 3 output will be Favorite number
#   if input is 7 (or) 4 (or) 6 (or) 5 (or) 9 output will be not  Favorite number


a=int(input("enter the number: "))
if a in [1, 10, 2, 8, 3]:
    print("Favorite number")
else:
    print("Not Favorite number")
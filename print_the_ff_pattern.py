# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# CODE #

for i in range(0, 5):
    for j in range(0, i+1):
        print(i+1, end="")
    print("\r")
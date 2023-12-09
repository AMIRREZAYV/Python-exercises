n = int(input("Enter the size of the diamond: "))

# Print upper half of the diamond
for i in range(1, n+1, 2):
    print(" " * ((n-i)//2) + "*" * i)

# Print middle line of the diamond
if (n % 2) == 0 : 
    print("*" * n,"\n"+"*" * (n-1))
    

# Print lower half of the diamond
for i in range(n-2, 0, -2):
    print(" " * ((n-i)//2) + "*" * i)
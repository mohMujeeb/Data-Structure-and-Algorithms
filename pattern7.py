def starTRIANGLE(n):
    for i in range(n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(0, n-i-1):
            print(" ", end="")
        print(end="\n")
        
starTRIANGLE(5)
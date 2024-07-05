def starTRIANGLE(n):
    for i in range(n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(0, n-i-1):
            print(" ", end="")
        print(end="\n")
        
def starTRIANGLEdown(n):
    for i in range(n):
        for j in range(0, i):
            print(" ", end="")
        for j in range(2*n-(2*i+1)): #2*5-(2*0+1) == 9
            print("*", end="")
        for j in range(0, i):
            print(" ", end="")
        print(end="\n")

starTRIANGLE(5)
starTRIANGLEdown(5)
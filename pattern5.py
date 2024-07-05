def pattern5(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print("*", end="")
        print(end="\n")
        
pattern5(5)
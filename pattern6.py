def pattern6(n):
    for i in range(n):
        for j in range(1, n-i+1):
            print(j, end="")
        print(end="\n")
        
pattern6(5) 
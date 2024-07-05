def starLINE(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print(end="\n")
        
starLINE(5)
def pattern11(n):
    for i in range(n):
        start = 1
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(1, i+1):
            print(start, end="")
            start = 1 - start
        print("\n")   
            
        
pattern11(5)
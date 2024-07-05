
def countLEFT(n):
    
    for i in range(1,n): 
        for j in range(i): 
            print(i, end="") 
        print(end="\n")
        
countLEFT(5)
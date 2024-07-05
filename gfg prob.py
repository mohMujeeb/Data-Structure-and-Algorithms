"""
Given an integer choice denoting the choice of the user and a list containing
the single value R or two values L and B depending on the choice.
If the user's choice is 1,calculate the area of the circle having the given radius(R).  
Else if the choice is 2, calculate the area of the rectangle with the given 
length(L) and breadth(B).
"""

class  Solution:
    
    def switchcase(self, choice, arr):
        if choice == 1:
            r = arr[0]
            return 3.14 * r ** 2
        elif choice == 2:
            l = arr[0]
            w = arr[1]
            return l * w
        
if __name__ == "__main__":
    
    choice = int(input("Enter Choice"))
    
    arr = list(map(int, input().split()))
    
    obj = Solution()
    if choice == 1:
        result = obj.switchcase(choice, arr)
        print("%.2f"%round(result, 2))
    else:
        result = obj.switchcase(choice, arr)
        print(int(result))
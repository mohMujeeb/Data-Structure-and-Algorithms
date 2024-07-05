class Solution:
    
    def compareNM(self, n, m):
        
        if n < m:
            return "lesser"
        elif n == m:
            return "equal"
        else:
            return "greater"
        
if __name__ == "__main__":
        
    n = int(input("Enter n: "))
        
    m = int(input("Enter m: "))
        
    obj = Solution()
    result = obj.compareNM(n , m)

    print(result)
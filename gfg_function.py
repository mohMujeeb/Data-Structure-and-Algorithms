#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def passedBy(self, a, b):
        a += 1
        b += 2
        return a,b

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ("Enter Test Case"))
    for _ in range (t):
        a, b = list(map(int, input("Enter a, b").split()))
        ob = Solution()
        res = ob.passedBy(a, b)
        print(res[0], res[1])
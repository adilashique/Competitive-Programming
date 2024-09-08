#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def isPrime(self,N):
        # code here
        
        
        if N == 1:
            return False
        if (N == 2 or N == 3):
            return True
        if (N%2 == 0 or N%3 == 0):
            return False
        i = 5
        while i*i<=N:
            if (N%i == 0 or N%(i+2) == 0):
                return False
            i+=6
        return True
           

#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        ob=Solution()
        if(ob.isPrime(N)):
            print("Yes")
        else:
            print("No")
        T-=1
    
    
if __name__=="__main__":
    main()
# } Driver Code Ends
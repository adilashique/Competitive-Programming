#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


# } Driver Code Ends
#User function Template for python3
def primnum(n):
        if n==1:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        i=5
        while i<=math.sqrt(n):
            if n%i==0 or n%(i+2)==0:
                return False
            i=i+6
        return True
class Solution:
    
           
        
    
    def exactly3Divisors(self,N):
        # code here
        count = 0
        if N<3:
            return count
        
        i=2
        while i*i<=N :
            j = i*i
            if ((j%math.sqrt(j)==0) or j==4):
                if primnum(i):
                    count = count+1
                    
            if i%2==0:
                i=i+1
            else:
                i=i+2
        return count            
        
            

#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
# } Driver Code Ends
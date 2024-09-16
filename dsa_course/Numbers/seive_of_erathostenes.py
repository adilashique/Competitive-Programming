#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    
           
        
    
    def seieve_of_erathostenes(self,N):
        # code here
        isPrime = [True for i in range(0,N+1)]       
        
        i=2
        while i*i<=N:
            if isPrime[i]:
               for j in range(i*i,N+2,1):
                 isPrime[j]=False
            i=i+1
        for i in range(2,N+1):
            if isPrime[i]:
                print(i,end=" ")
                


        
            

#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.seieve_of_erathostenes(N))
        
        T-=1
    

if __name__=="__main__":
    main()
# } Driver Code Ends
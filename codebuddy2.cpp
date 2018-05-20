#include<stdio.h>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

struct a
 { int num1;
   int num2;
 };
 bool acompare(a lhs, a rhs) 
 { return lhs.num1 < rhs.num1; }

int main()
{
 
 int n,i,largest,num;
 a arr[100];
 int temp[100];
 
 cin>>n;
 
 for(i=0;i<n;i++)
 {cin>>arr[i].num1;
  arr[i].num2=i;
 }
 
 std::sort(arr, arr+n, acompare);
 
 for(i=0;i<n;i++)
 {temp[i]=arr[i].num2;
 }
 
 largest=*max_element( temp+1, temp + n)-temp[0];
 
 for(i=1;i<n-1;i++)
 { num=*max_element( temp+i+1, temp + n)-temp[i];
   
   if(num>=largest)
    largest=num;
    
 }
 cout<<"\n"
     <<largest;
}
   

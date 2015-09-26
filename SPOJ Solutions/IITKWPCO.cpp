#include <stdio.h>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
 int t;
 scanf("%d",&t);
 while(t--)
 {
  int check[1000001]={0};
  int n;
  scanf("%d",&n);
  int a[n];
  for(int i=0;i<n;i++){
   scanf("%d",&a[i]);
   check[i]=0;}
  sort(a,a+n);
  int count=0;
  for(int i=1;i<n;i++)
  {
   if(a[i]%2==0)
   {
    for(int j=0;j<n;j++)
    {
     if(a[i] == 2*a[j] && check[j]==0)
     {
      count++;
      check[i]=1;
      check[j]=1;
      break;
     }
    }
   }
  }
  printf("%d\n",count);
 }
 return 0;
}

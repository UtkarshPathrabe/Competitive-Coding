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
  int n;
  scanf("%d",&n);
  long long a[n];
  bool check[n];
  for(int i=0;i<n;i++){
   scanf("%lld",&a[i]);
   check[i]=0;}
  sort(a,a+n);
  int re=n-1,flag=0,count=0;
  for(int i=n-1;i>=0;i--)
  {
   if(check[i])
    continue;
   flag=0;
   for(int j=re;j>=0;j--)
   {
    if(check[j])
     continue;
    if(a[j] < a[i]/2)
    {
     re=j;
     flag=1;
     break;
    }
    else if(a[j] == a[i]/2)
    {
     count++;
     check[j]=true;
     re=j;
     flag=1;
     break;
    }
   }
   if(!flag)
    break;
  }
  printf("%d\n",count);
 }
 return 0;
}

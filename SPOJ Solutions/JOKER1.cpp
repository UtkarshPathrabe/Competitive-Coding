#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <climits>
#include <ctime>
#include <algorithm>
using namespace std;
#define MOD 1000000007
int main()
{
 int t;
 scanf("%d",&t);
 while(t--)
 {
  int n;
  scanf("%d",&n);
  int a[n+9];
  for(int i=0;i<n;i++)
   scanf("%d",&a[i]);
  sort(a,a+n);
  long long result=1,flag=1;
  for(int i=n-1;i>=0;i--)
  {
   if(a[i]-i<=0)
   {
    flag=0;
    break;
   }
   result=(result*(a[i]-i))%MOD;
  }
  if(!flag)
   printf("0\n");
  else
   printf("%lld\n",result);
 }
 printf("KILL BATMAN\n");
 return 0;
}

#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
 int n,start,end,tempstart;
 scanf("%d",&n);
 int array[n];
 for (int i=0; i<n; i++)
  scanf("%d",&array[i]);
 int max=-1,temp;
 for (int i=0; i<n; i++)
 {
  temp=array[i];
  tempstart=i;
  if (max<temp)
  {
   max=temp;
   start=tempstart;
   end=i;
  }
   
  for (int j=i+1; j<n; j++)
  {
   temp=temp^array[j];
   if (max<temp)
   {
    max=temp;
    start=tempstart;
    end=j;
   }
  }
 }
 printf("%d\n%d %d\n",max,start+1,end+1);
 return 0;
}

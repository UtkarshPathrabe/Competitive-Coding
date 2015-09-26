#include <bits/stdc++.h>
using namespace std;
int main()
{
 int t,k;
 scanf("%d",&t);
 for(k=1;k<=t;k++)
 {
  int n,temp;
  vector<int>v;
  scanf("%d",&n);
  for(int i=0;i<n;i++){
   scanf("%d",&temp);
   v.push_back(temp);
  }
  int height=0,max_h=-1,count=-1;
  sort(v.begin(),v.end());
  bool status = true;
  while(status)
  {
   status = false;
   for(int i=0;i<n;i++){
    if(v[i]!=-1)
     status=true;
   }
   count++;
   for(int i=0;i<n;i++)
   {
    if(v[i]>=height)
    {
     height++;
     v[i]=-1;
    }
   }
   if(max_h<height)
    max_h=height;
   height = 0;
  }
  printf("Case #%d: %d %d\n",k,count,max_h);
 }
 return 0;
}

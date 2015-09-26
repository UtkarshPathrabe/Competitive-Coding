#include <bits/stdc++.h>
using namespace std;
int main()
{
 int t;
 scanf("%d",&t);
 while(t--)
 {
  int n,m;
  scanf("%d%d",&n,&m);
  map<int ,int>mp1,mp2,result;
  map<int ,int>::iterator t;
  for(int i=2;i*i<=n;i++)
  {
       while(n%i==0)
       {
           mp1[i]+=1;
           n/=i;
        }
  }
  if(n>1)
     mp1[n]+=1;
  for(int i=2;i*i<=m;i++)
  {
        while(m%i==0)
        {
            mp2[i]+=1;
            m/=i;
        }
  }
  if(m>1)
     mp2[m]+=1;
  long long k=1;
  for(t=mp1.begin();t!=mp1.end();t++)
  {
       if(t->second > mp2[t->first])
           result[t->first]=t->second;
  } 
  for(t=mp2.begin();t!=mp2.end();t++)
  {
       if(t->second > mp1[t->first] && result[t->first] < t->second)
            result[t->first]=t->second;
  }
  for(t=result.begin();t!=result.end();t++)
       for(int i=0;i<t->second;i++)
            k*=(long long)(t->first);
  printf("%lld\n",k);
 }
 return 0;
}

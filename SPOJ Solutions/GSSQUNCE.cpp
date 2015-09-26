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
#include <bits/stdc++.h>
using namespace std;
int main()
{
 int t;
 scanf("%d",&t);;
 while(t--)
 {
  int n;
  scanf("%d",&n);
  int a[60000],flag=1;
  map<int ,int>mp;
  map<int ,int >::iterator t;
  for(int i=0;i<n;i++)
   scanf("%d",&a[i]),mp[a[i]]+=1;
  for(t=mp.begin();t!=mp.end();t++)
   if((*t).second >2){
    flag=0;
    break;}
  if(flag==0 || n==1)
   printf("NO\n");
  else
   printf("YES\n");
 }
 return 0;
}

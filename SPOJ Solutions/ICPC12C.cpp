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
int cum[26];
int main()
{
 int t;
 scanf("%d ",&t);
 while(t--)
 {
  char s[100009],o[100009];
  scanf("%s",s);
  scanf("%s",o);
  int i=0,a[27],j,flag,k;
  for(i=0;i<26;i++)
   cum[i]=0,a[i]=0;
  i=0;
  while(o[i] != '\0')
  {
   j=o[i] - 97;
   a[j]++;
   i++;
  }
  int size=i;
  i=0;
  while(i<size)
  {
   k=s[i++] -97;
   cum[k]++;
  }
  if(size == strlen(s)){
   flag=1;
   for(i=0;i<26;i++)
    if(cum[i] != a[i])
    {
     flag=0;
     break;
    }
   if(flag)
    printf("YES\n");
   else
    printf("NO\n");
   continue;
  }
  i=size;
  while(s[i]!='\0')
  {
   flag=1;
   k=s[i] - 97;
   cum[k]++;
   k=s[i-size]-97;
   cum[k]--;
   for(j=0;j<26;j++)
    if(cum[j] != a[j])
    {
     flag=0;
     break;
    }
   if(flag)
    break;
   i++;
  }
  if(flag)
   printf("YES\n");
  else
   printf("NO\n");
 }
 return 0;
}

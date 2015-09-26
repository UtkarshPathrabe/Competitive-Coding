#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <sstream>
using namespace std;
int main()
{
 int n;
 int a[10]={0,1,1,1,1,2,3,5,11,11};
 scanf("%d ",&n);
 string s[n+9];
 int i;
 for(i=0;i<n;i++)
  getline(cin,s[i]);
 map<string , int >mp;
 map<string ,int >::iterator t;
 i=0;
 string word;
 for(i=0;i<n;i++){
  istringstream iss(s[i]);
  while(iss>>word)
   mp[word]+=1;
 }
 int count=0,max=-1;
 for(i=0;i<n;i++)
 {
  count=0;
  istringstream iss(s[i]);
  while(iss>>word)
  {
   t=mp.find(word);
   if((*t).second==1)
   {
    if((*t).first.size()>7)
     count+=11;
    else
     count+=a[(*t).first.size()];
   }
  }
  if(max<count)
   max=count;
 }
 cout<<max<<endl;
 return 0;
}

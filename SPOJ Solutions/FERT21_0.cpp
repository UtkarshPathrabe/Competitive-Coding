#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cfloat>
#include <map>
#include <fstream>
#include <sstream>
#include <bits/stdc++.h>
#include <climits>
using namespace std;
string arr[1009];
string multiply(string s,int a)
{
 int i,carry=0,j;
 string temp;
 char c;
 for(i=s.size() - 1;i>=0;i--)
 {
  j= s[i] - 48;
  c = (j*a + carry)%10 + 48;
  carry = (j*a + carry)/10;
  temp = c + temp;
 }
 if(carry!=0)
  c=carry+48,temp=c+temp;
 return temp;
}
void pre()
{
 arr[0] =49;
 for(int i=1;i<=1000;i++)
  arr[i] = multiply(arr[i-1],5);
}
int main()
{
 int t;
 scanf("%d",&t);
 pre();
 while(t--)
 {
  int n,l,p;
  ios_base::sync_with_stdio(false);
  scanf("%d",&n);
  if(n==1)
   cout<<"1"<<endl;
  else
  {
   cout<<"0.";
   p=arr[n-1].size();
   l= abs((n-1) - p);
   for(int i=0;i<l;i++)
    cout<<"0";
   cout<<arr[n-1]<<endl;
  }
 }
 return 0;
}

#include <bits/stdc++.h>
using namespace std;
int main()
{
 int t;
 scanf("%d",&t);
 while(t--){
 int k,x;
 scanf("%d%d",&k,&x);
 char a[1000009];
 int temp,carry,temp1;
 int flag=0;
 for(int i=x;i<=9;i++)
 {
  a[k-1]=i+48;
  carry=0;
  for(int j=k-2;j>=0;j--)
  {
   a[j]=((a[j+1]-48)*x + carry)%10 + 48;
   carry = ((a[j+1]-48)*x + carry)/10;
  }
  a[k]=0;
  temp=a[0]-48;
  temp1= (temp*x + carry)%10;
  carry=(temp*x + carry)/10;
  if(temp1 == i && carry==0){
   printf("%s\n",a);
   flag=1;
   break;
  }
 }
 if(!flag)
  printf("Impossible\n");
 }
 return 0;
}

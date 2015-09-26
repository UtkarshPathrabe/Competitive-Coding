#include<stdio.h>
#include<iostream>
#include<map>
#include<math.h>
#include<cmath>
 
using namespace std;
 
int main(){
	int n,i,l,r,t;
	long long int temp,lsum=0,rsum=0,temp1,temp2,temp3,temp4,temp5,sum=0;
	scanf("%d",&n);
	
	std::map<long long int,long long int> mymap;
	
	for(i=0;i<n;i++){
		scanf("%lld",&temp);
		sum+=temp;
		mymap.insert(std::pair<long long int,long long int>(temp,i));
	}
	
	std::map<long long int,long long int>::iterator it;
	std::map<long long int,long long int>::reverse_iterator rit;
	
/*   for(it=mymap.begin();it!=mymap.end();++it){
	
		
		std::cout<<it->first<<"=>"<<it->second<<endl;
	//	std::cout<<rit->first<<"=>"<<rit->second<<endl;
	}
	cout<<endl;
*/
 
	
	it=mymap.begin(),rit=mymap.rbegin();
	
	//initialise.........
	lsum=0;rsum=0;
		
	//cout<<rit->second+1<<endl;
	
	lsum=it->first+rit->first;
	//cout<<it->second+1<<endl<<rit->second+1<<endl;
	int turn=1;
	sum=sum/2;
//	cout<<sum<<endl;
	while(it->first<rit->first){
	if(rsum+rit->first<sum)
	{
		rsum+=rit->first;
	cout<<rit->second+1<<endl;
	++rit;
	}
	else break;
	}
	
	
	
	
	
	return 0;
} 

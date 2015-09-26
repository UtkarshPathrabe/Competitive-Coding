#include <cstdio>
#include <cstdlib>
#include <set>
#include <algorithm>

using namespace std;

int t, n, i, array[10000000] = {0}, temp, sum;
long long int entry, exi;
set<long long int> record;
set<long long int>::iterator it;

int main(){
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		for(i=0; i<n; i++){
			scanf("%lld %lld", &entry, &exi);
			record.insert(entry);
			record.insert(exi);
			array[entry] = 1;
			array[exi] = -1;
		}
		temp = sum = 0;
		for(it=record.begin(); it!=record.end(); it++){
			sum += array[(*it)];
			temp = max(sum, temp);
			array[(*it)] = 0;
		}
		printf("%d\n", temp);
		record.clear();
	}
	return 0;
}

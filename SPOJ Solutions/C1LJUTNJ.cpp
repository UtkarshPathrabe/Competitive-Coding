#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n, i, anger, array[100000] = {0};
long long total, ans, m;

int main(){
	scanf("%lld %d", &m, &n);
	total = ans = 0;
	for(i=0; i<n; i++){
		scanf("%d", &array[i]);
		total += array[i];
	}
	total -= m;
	sort(array, array+n);
	for(i=0; i<n; i++){
		anger = min((long long)array[i], (total/(n-i)));
		ans += (long long)(anger*anger);
		total -= anger;
	}
	printf("%lld\n", ans);
	return 0;
}

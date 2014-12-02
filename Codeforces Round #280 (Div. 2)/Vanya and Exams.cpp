/* Question can be found at http://codeforces.com/contest/492/problem/C */

#include <bits/stdc++.h>

using namespace std;

vector < pair <int, int> > exam;

bool compare(pair <int, int> x, pair <int, int> y) {
	return (x.second < y.second);
}

int main(void) {
	long long int n, i, r, avg, a, b, need, pages = 0, grade = 0;
	scanf("%lld %lld %lld", &n, &r, &avg);
	avg *= n;
	for(i = 0; i < n; i++) {
		scanf("%lld %lld", &a, &b);
		exam.push_back(make_pair(a, b));
		grade += a;
	}
	sort(exam.begin(), exam.end(), compare);
	need = avg - grade;
	i = 0;
	while(need > 0 && i < n) {
		if(exam[i].first < r) {
			if(need > (r - exam[i].first)) {
				pages += (exam[i].second * (r - exam[i].first));
				need -= (r - exam[i].first);
			}else {
				pages += (exam[i].second * need);
				need = 0;
			}
		}
		i += 1;
	}
	printf("%lld\n", pages);
	return 0;
}

/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/492/problem/B 
*  Algorithms: Math and Sorting
*/

#include <bits/stdc++.h>

using namespace std;

vector <double> pos;
vector <double>::iterator it;

int main(void) {
	int n;
	double l, d, maximum, prev, a;
	scanf("%d %lf", &n, &l);
	for(int i = 0; i < n; i++) {
		scanf("%lf", &a);
		pos.push_back(a);
	}
	sort(pos.begin(), pos.end());
	it = pos.begin();
	prev = 0 - *(it);
	maximum = (*(it)) * 2;
	for(; it != pos.end(); it++) {
		maximum = max(maximum, *(it) - prev);
		prev = *(it);
	}
	maximum = max(maximum, (l - prev) * 2);
	d = (double) maximum / 2.0;
	printf("%lf\n", d);
	return 0;
}

/* Author: Utkarsh Pathrabe
*  Question can be found at: http://www.spoj.com/problems/DEFKIN/
*  Algorithms: Sorting
*/

#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int t, w, h, n, x, y, xBest, yBest, previous, distance;
	set<int> xSet, ySet;
	set<int>::iterator it;
	scanf("%d", &t);
	while(t--) {
		xBest = 0;
		yBest = 0;
		scanf("%d %d %d", &w, &h, &n);
		for(int i = 0; i < n; i++) {
			scanf("%d %d", &x, &y);
			xSet.insert(x);
			ySet.insert(y);
		}
		xSet.insert(w+1);
		ySet.insert(h+1);
		previous = 0;
		for(it = xSet.begin(); it != xSet.end(); it++) {
			distance = (*it) - previous - 1;
			xBest = max(xBest, distance);
			previous = *it;
		}
		previous = 0;
		for(it = ySet.begin(); it != ySet.end(); it++) {
			distance = (*it) - previous - 1;
			yBest = max(yBest, distance);
			previous = *it;
		}
		printf("%d\n", xBest*yBest);
		xSet.clear();
		ySet.clear();
	}
	return 0;
}

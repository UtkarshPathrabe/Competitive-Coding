/* Author: Utkarsh Pathrabe
*  Question can be found at: https://www.spoj.com/problems/CUBEROO2/
*  Algorithms: Binary Search
*/

#include <bits/stdc++.h>

using namespace std;

double binarySearch(double low, double high, double number) {
	int i = 80;
	double cube, mid;
	while(i--) {
		mid = (low + high) / 2;
		cube = mid * mid;
		if(cube > number) {
			high = mid;
			continue;
		}
		cube = cube * mid;
		if(cube > number) {
			high = mid;
			continue;
		}
		low = mid;
	}
	return low;
}

int main(void) {
	int test;
	double N;
	scanf("%d", &test);
	while(test--) {
		scanf("%lf", &N);
		printf("%.4lf\n", floor(10000 * binarySearch(0, N, N)) / 10000);
	}
	return 0;
}

/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/492/problem/A 
*  Algorithms: Implementation Based
*/

#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n, height = 0, i = 1;
	scanf("%d", &n);
	while(n >= ((i * (i + 1)) / 2)) {
		n -= ((i * (i + 1)) / 2);
		i += 1;
		height += 1;
	}
	printf("%d\n", height);
	return 0;
}

/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/492/problem/E 
*  Algorithms: Math
*/

#include <bits/stdc++.h>

using namespace std;

int N, M, dx, dy;
int indexCount[1000005];

inline int add(int x, int y) { return (x + y) % N; }
inline int mul(int x, int y) { return (long long int)x * y % N; }

int main() {
	int x, y;
	cin >> N >> M >> dx >> dy;
	for(int i = 1; i < N; i++) {
		if(mul(dy, i) == (N - 1)) {
			dx = mul(dx, i);
			break;
		}
	}
	while(M--) {
		cin >> x >> y;
		indexCount[add(x, mul(dx, y))]++;
	}
	printf("%ld 0\n", max_element(indexCount, indexCount + N) - indexCount);
	return 0;
}

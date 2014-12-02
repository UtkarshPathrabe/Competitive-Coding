/* Question can be found at http://codeforces.com/contest/492/problem/D */

#include <bits/stdc++.h>

using namespace std;

vector <long long int> attack;

int main(void) {
	long long int i, n, x, y, index, hit, nextX, nextY;
	cin >> n >> x >> y;
	nextX = x;
	nextY = y;
	for(index = 0; index < (x + y); index++) {
		if(nextX < nextY) {
			attack.push_back(nextX);
			nextX += x;
		}else if(nextX > nextY) {
			attack.push_back(nextY);
			nextY += y;
		}else {
			attack.push_back(nextX);
			attack.push_back(nextY);
			index += 1;
			nextX += x;
			nextY += y;
		}
	}
	for(i = 0; i < n; i++) {
		cin >> hit;
		hit -= 1;
		index = hit % (x + y);
		if(attack[index] % x == 0) {
			if(attack[index] % y == 0) {
				printf("Both\n");
			}else {
				printf("Vova\n");
			}
		}else {
			printf("Vanya\n");
		}
	}
	return 0;
}

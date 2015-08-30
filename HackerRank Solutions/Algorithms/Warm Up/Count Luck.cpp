#include <bits/stdc++.h>
#define N 101
#define M 101

using namespace std;

int X[] = {0, 1, 0, -1}, Y[] = {1, 0, -1, 0};
bool flag[N][M] = false;
char mapping[N][M + 1] = {'\0'};

bool isValid (int x, int y, int i, int j, int n, int m) {
	if (mapping[x+X[]])
}

int main (void) {
	int T;
	while (T--) {
		int n, m, K, startX, startY, endX, endY, wand = 0;
		cin >> n >> m;		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				flag[i][j] = false;
			}
		}		
		for (int i = 0; i < n; i++) {
			cin >> mapping[i];
			for (int j = 0; j < m; j++) {
				if (mapping[i][j] == 'M') {
					startX = i;
					startY = j;
				}
				if (mapping[i][j] == '*') {
					endX = i;
					endY = j;
				}
			}
		}
		int x = startX; 
		int y = startY, count;
		flag[x][y] = true;
		
	}
	return 0;
}

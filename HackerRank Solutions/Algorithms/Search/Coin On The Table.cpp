#include <bits/stdc++.h>

using namespace std;

char mapping[52][52];
int best[52][52][1001];
int N, M, K;

void update (int row, int col, int time, int val) {
	if ((row < 0) || (row >= N)) {
		return;
	}
	if ((col < 0) || (col >= M)) {
		return;
	}
	if (time > K) {
		return;
	}
	if ((val < best[row][col][time]) || (best[row][col][time] == -1)) {
		best[row][col][time] = val;
		if (mapping[row][col] != '*') {
			update (row, col + 1, time + 1, val + (mapping[row][col] != 'R'));
			update (row, col - 1, time + 1, val + (mapping[row][col] != 'L'));
			update (row - 1, col, time + 1, val + (mapping[row][col] != 'U'));
			update (row + 1, col, time + 1, val + (mapping[row][col] != 'D'));
		} else {
			update (row, col, time + 1, val);
		}
	}
}

int main (void) {
	cin >> N >> M >> K;
	int row, col;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> mapping[i][j];
			if (mapping[i][j] == '*') {
				row = i;
				col = j;
			}
		}
	}
	memset (best, -1, sizeof (best));
	update (0, 0, 0, 0);
	cout << best[row][col][K] << endl;
	return 0;
}

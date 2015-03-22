#include <bits/stdc++.h>

using namespace std;

char grid[101][101] = {0};

int main (void) {
	int T;
	cin >> T;
	while (T--) {
		int N;
		cin >> N;
		getchar();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				grid[i][j] = getchar();
			}
			getchar();
		}
		for (int i = 0; i < N; i++) {
			sort (grid[i], grid[i] + N);
		}
		bool flag = true;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N - 1; j++) {
				if (grid[j][i] > grid[j + 1][i]) {
					flag = false;
					break;
				}
			}
			if (!flag)
				break;
		}
		if (flag)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}

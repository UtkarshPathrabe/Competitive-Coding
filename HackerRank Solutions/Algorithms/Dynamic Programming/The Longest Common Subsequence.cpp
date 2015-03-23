#include <bits/stdc++.h>

using namespace std;

char marker[101][101];

void Print_LCS (int b[], int i, int j) {
	if ((i == 0) || (j == 0)) {
		return;
	}
	if (marker[i][j] == 'd') {
		Print_LCS (b, i - 1, j - 1);
		cout << b[i - 1] << " ";
	} else if (marker[i][j] == 'u') {
		Print_LCS (b, i - 1, j);
	} else if (marker[i][j] == 'a') {
		Print_LCS (b, i, j - 1);
	}
}

int LCS (int a[], int b[], int N, int M) {
	int Max[N + 1][M + 1];
	for (int i = 0; i <= N; i++) {
		Max[i][0] = 0;
	}
	for (int j = 0; j <= M; j++) {
		Max[0][j] = 0;
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			if (a[i - 1] == b[j - 1]) {
				Max[i][j] = Max[i - 1][j - 1] + 1;
				marker[i][j] = 'd';
			} else {
				if ((Max[i - 1][j]) > (Max[i][j - 1])) {
					Max[i][j] = Max[i - 1][j];
					marker[i][j] = 'u';
				} else {
					Max[i][j] = Max[i][j - 1];
					marker[i][j] = 'a';
				}
			}
		}
	}
	return Max[N][M];
}

int main (void) {
	int N, M, len;
	cin >> N >> M;
	int a[N], b[M];
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < M; i++) {
		cin >> b[i];
	}
	len = LCS (a, b, N, M);
	Print_LCS (a, N, M);
	return 0;
}

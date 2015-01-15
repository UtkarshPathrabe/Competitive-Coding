#include <bits/stdc++.h>

using namespace std;

int inp[501][501] = {{0}}, output[501][501] = {{0}};
char in[501];

int main (void) {
	int N, M, sum, maxsum = INT_MIN, count = 0;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> in;
		for (int j = M - 1; j >= 0; j--) {
			inp[i][j] = in[j] - '0';
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			sum = 0;
			for (int k = 0; k < M; k++) {
				sum += (inp[i][k] | inp[j][k]);
			}
			maxsum = max (maxsum, sum);
			output[i][j] = sum;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			if (output[i][j] == maxsum) {
				count += 1;
			}
		}
	}
	cout << maxsum << endl << count << endl;
	return 0;
}

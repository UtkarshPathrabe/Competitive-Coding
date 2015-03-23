#include <bits/stdc++.h>

using namespace std;

int arr[1005] = {0};

int ValidLen (int l) {
	int vlen = 0;
	for (int i = 0; i < l; i++) {
		if (arr[i] > 0) {
			vlen += 1;
		}
	}
	return vlen;
}

int * DecreaseByMin (int l) {
	int mini = INT_MAX;
	for (int i = 0; i < l; i++) {
		if (arr[i] > 0) {
			mini = min (mini, arr[i]);
		}
	}
	for (int i = 0; i < l; i++) {
		arr[i] -= mini;
	}
	return arr;
}

int main (void) {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	while (ValidLen(N) > 0) {
		cout << ValidLen(N) << endl;
		DecreaseByMin(N);
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int modifiedSearch (int seq[], int ele, int start, int end) {
	for (int i = start; i < end; i++) {
		if (seq[i] == ele) {
			return i;
		}
	}
	return -1;
}

int main (void) {
	int N;
	long long int K;
	cin >> N >> K;
	int seq[N];
	for (int i = 0; i < N; i++) {
		cin >> seq[i];
	}
	int start = 0, index, temp;
	while ((K != 0) && (start < N)) {
		index = modifiedSearch (seq, N - start, start, N);
		if (start != index) {
			temp = seq[index];
			seq[index] = seq[start];
			seq[start] = temp;
			K--;
		}
		start++;
	}
	for (int i = 0; i < N; i++) {
		cout << seq[i] << " ";
	}
	cout << endl;
	return 0;
}

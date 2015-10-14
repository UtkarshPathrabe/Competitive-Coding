#include <bits/stdc++.h>

using namespace std;

void findArea (int side[], int a, int b, int *count) {
	if (a < b) {
		int temp = b;
		b = a;
		a = temp;
	}
	if ((a == 0) || (b == 0)) {
		return;
	}
	int index = (int)(log(b) / log(2));
	while ((index >= 0) && (side[index] == 0)) {
		index--;
	}
	if (index == -1) {
		return;
	}
	side[index]--;
	(*count)++;
	int rec = 1 << index;
	findArea (side, b-rec, rec, count);
	findArea (side, a-rec, b, count);
}

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("D-large-practice.out");
	cin.open("D-large-practice.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, M, side[32] = {0};
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			int temp;
			cin >> temp;
			side[temp]++;
		}
		cout << "Case #" << t << ": ";
		int count = 0, ans = 0;
		for (; count < N; ans++) {
			findArea (side, M, M, &count);
		}
		cout << ans << endl;
	}
	cout.close();
	cin.close();
	return 0;
}

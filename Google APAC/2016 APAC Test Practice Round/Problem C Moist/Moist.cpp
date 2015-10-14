#include <bits/stdc++.h>

using namespace std;

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("C-small-practice-2.out");
	cin.open("C-small-practice-2.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, cost = 0;
		string last = " ", buf;
		cin >> N;
		getline (cin, buf);
		for (int i = 0; i < N; i++) {
			string str;
			getline (cin, str);
			if (str < last) {
				cost++;
			} else {
				last = str;
			}
		}
		cout << "Case #" << t << ": " << cost << endl;
	}
	cout.close();
	cin.close();
	return 0;
}

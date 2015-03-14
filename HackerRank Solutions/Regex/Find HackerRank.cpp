#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N;
	string s, buff = "hackerrank";
	cin >> N;
	getline (cin, s);
	while (N--) {
		getline (cin, s);
		int flag = -1;
		for (int i = 0; i < s.length(); i++) {
			if (!buff.compare(s.substr(i, 10))) {
				if (i == 0) {
					flag = 1;
				}
				if (i + 10 == s.length()) {
					if (flag == 1) {
						flag = 0;
					} else {
						flag = 2;
					}
				}
			}
		}
		cout << flag << endl;
	}
	return 0;
}

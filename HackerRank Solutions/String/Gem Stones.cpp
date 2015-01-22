#include <bits/stdc++.h>

using namespace std;

int c[26] = {0};

int main (void) {
	int N, temp, total = 0;
	string s;
	cin >> N;
	temp = N;
	while (temp--) {
		cin >> s;
		bool flag[26];
		fill (flag, flag + 26, false);
		for (int i = 0; i < s.length(); i++) {
			if (flag[s[i] - 'a'] == false) {
				c[s[i] - 'a']++;
				flag[s[i] - 'a'] = true;
			}
		}
	}
	for (int i = 0; i < 26; i++) {
		if (c[i] == N) {
			total++;
		}
	}
	cout << total << endl;
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, len;
	cin >> T;
	while (T--) {
		string s, s1, s2;
		int f1[26], total;
		cin >> s;
		len = s.length();
		if (len % 2 == 1) {
			total = -1;
		} else {
			for (int i = 0; i < 26; i++) {
				f1[i] = 0;
			}
			s1 = s.substr(0, len / 2);
			s2 = s.substr(len / 2);
			total = s1.length();
			for (int i = 0; i < s2.length(); i++) {
				f1[s2[i] - 'a']++;
			}
			for (int i = 0; i < s1.length(); i++) {
				if (f1[s1[i] - 'a'] > 0) {
					total--;
					f1[s1[i] - 'a']--;
				}
			}
		}
		cout << total << endl;
	}
	return 0;
}

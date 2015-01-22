#include <bits/stdc++.h>

using namespace std;

bool IsPalindrome (string s) {
	int i = 0, j = s.length() - 1;
	while (i < j) {
		if (s[i] != s[j]) {
			return false;
		}
		i++;
		j--;
	}
	return true;
}

int main (void) {
	int T, len, i, j, ans;
	string s, s1;
	cin >> T;
	while (T--) {
		cin >> s;
		i = 0; 
		len = s.length();
		j = len - 1;
		ans = -1;
		while ((i < j) && (s[i] == s[j])) {
			i++;
			j--;
		}
		if (i < j) {
			s1 = s.substr(0, i) + s.substr(i + 1, len - i - 1);
			if (IsPalindrome (s1)) {
				ans = i;
			}
			s1 = s.substr(0, j) + s.substr(j + 1, len - j - 1);
			if (IsPalindrome (s1)) {
				ans = j;
			}
		}
		cout << ans << endl;
	}
	return 0;
}

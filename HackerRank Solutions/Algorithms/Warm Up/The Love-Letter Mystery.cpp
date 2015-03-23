#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, first, last, i, l, mini, maxi, ops;
	char str[10005];
	cin >> T;
	while (T--) {
		cin >> str;
		i = 0;
		l = strlen (str) - 1;
		ops = 0;
		while (i < l) {
			first = str[i++] - 'a';
			last = str[l--] - 'a';
			mini = min(first, last);
			maxi = max(first, last);
			ops += (maxi - mini);
		}
		cout << ops << endl;
	}
	return 0;
}

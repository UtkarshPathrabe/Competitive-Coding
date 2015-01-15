#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, l;
	char str[100005];
	cin >> T;
	while (T--) {
		cin >> str;
		l = strlen (str);
		int del = 0;
		for (int i = 0, j = 1; i < l && j < l; ) {
			if (str[i] == str[j]) {
				del += 1;
				j += 1;
			} else {
				i = j;
				j = i + 1;
			}
		}
		cout << del << endl;
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int l, sum = 0, arr[26] = {0};
	char str[100005];
	cin >> str;
	l = strlen (str);
	for (int i = 0; i < l; i++) {
		arr[str[i] - 'a'] ^= 1;
	}
	for (int i = 0; i < 26; i++) {
		sum += arr[i];
	}
	if (sum == 0 || sum == 1) {
		cout << "YES" << endl;
	} else {
		cout << "NO" << endl;
	}
	return 0;
}

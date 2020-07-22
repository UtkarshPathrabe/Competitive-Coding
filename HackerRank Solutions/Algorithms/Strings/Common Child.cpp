#include <bits/stdc++.h>

using namespace std;

int LCS[5001][5001] = {0};

int main (void) {
	string s1, s2;
	cin >> s1 >> s2;
	int len1 = s1.length(), len2 = s2.length();
	for (int i = 1; i <= len1; i++) {
		for (int j = 1; j <= len2; j++) {
			if (s1[i - 1] == s2[j - 1]) {
				LCS[i][j] = 1 + LCS[i - 1][j - 1];
			} else {
				LCS[i][j] = max (LCS[i][j - 1], LCS[i - 1][j]);
			}
		}
	}
	cout << LCS[len1][len2] << endl;
	return 0;
}

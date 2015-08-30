/* 	Time Complexity: O(n)
	Special Pattern case is all characters of pattern are different.
*/

#include <bits/stdc++.h>

using namespace std;

void naiveSpecialSearch (string text, string pattern) {
	int N = text.length(), M = pattern.length(), i = 0, j;
	while (i <= N - M) {
		for (j = 0; j < M; j++) {
			if (text[i+j] != pattern[j]) {
				break;
			}
		}
		if (j == M) {
			cout << "Pattern found at index " << i << "." << endl;
			i += M;
		} else if (j == 0) {
			i++;
		} else {
			i += j;
		}
	}
}

int main (void) {
	string text = "ABCEABCDABCEABCD";
	string pattern = "ABCD";
	naiveSpecialSearch (text, pattern);
	return 0;
}

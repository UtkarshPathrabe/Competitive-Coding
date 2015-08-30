/* Time Complexity: O(n); Space Complexity: O(m) */

#include <bits/stdc++.h>

using namespace std;

void computeLPS (string pattern, int *lps) {
	int len = 0, i = 1;
	lps[0] = 0;
	int M = pattern.length();
	while (i < M) {
		if (pattern[i] == pattern[len]) {
			lps[i++] = ++len;
		} else {
			if (len != 0) {
				len = lps[len-1];
			} else {
				lps[i++] = 0;
			}
		}
	}
}

void KMPSearch (string text, string pattern) {
	int N = text.length(), M = pattern.length();
	int *lps = (int*) calloc (M, sizeof(int));
	computeLPS (pattern, lps);
	int i = 0, j = 0;
	while (i < N) {
		if (pattern[j] == text[i]) {
			i++;
			j++;
		}
		if (j == M) {
			cout << "Found pattern at index " << i-j << "." << endl;
			j = lps[j - 1];
		} else if ((i < N) && (pattern[j] != text[i])) {
			if (j != 0) {
				j = lps[j-1];
			} else {
				i++;
			}
		}
	}
	free (lps);
}

int main (void) {
	string text = "ABABDABACDABABCABAB";
	string pattern = "ABABCABAB";
	KMPSearch (text, pattern);
	return 0;
}

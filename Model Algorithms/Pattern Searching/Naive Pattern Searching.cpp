/*	Time Complexity: 
	The best case occurs when the first character of the pattern is not present in text at all. The number of comparisons in best case is O(n).
	The worst case of Naive Pattern Searching occurs in following scenarios.
		1) When all characters of the text and pattern are same.
		2) Worst case also occurs when only the last character is different.
		Number of comparisons in worst case is O(m*(n-m+1)).
*/

#include <bits/stdc++.h>

using namespace std;

void naiveSearch (string text, string pattern) {
	int N = text.length(), M = pattern.length();
	for (int i = 0; i <= N-M; i++) {
		int j;
		for (j = 0; j < M; j++) {
			if (text[i+j] != pattern[j]) {
				break;
			}
		}
		if (j == M) {
			cout << "Pattern found at index " << i << "." << endl;
		}
	}
}

int main (void) {
	string text = "AABAACAADAABAAABAA";
	string pattern = "AABA";
	naiveSearch (text, pattern);
	return 0;
}

/* The average and best case running time of the Rabin-Karp algorithm is O(n+m), but its worst-case time is O(n*m). */

#include <bits/stdc++.h>
#define	d	256

using namespace std;

void RKsearch (string text, string pattern, int q) {
	int N = text.length(), M = pattern.length(), p = 0, t = 0, h = 1;
	for (int i = 0; i < M-1; i++) {
		h = (h * d) % q;
	}
	for (int i = 0; i < M; i++) {
		p = (d * p + pattern[i]) % q;
		t = (d * t + text[i]) % q;
	}
	for (int i = 0; i <= N - M; i++) {
		if (p == t) {
			int j;
			for (j = 0; j < M; j++) {
				if (text[i+j] != pattern[j]) {
					break;
				}
			}
			if (j == M) {
				cout << "Pattern found at index " << i << endl;
			}
		}
		if (i < N - M) {
			t = (d * (t - text[i] * h) + text[i + M]) % q;
			if (t < 0) {
				t = t + q;
			}
		}
	}
}

int main (void) {
	string text = "GEEKS FOR GEEKS";
	string pattern = "GEEK";
	int q = 101;
	RKsearch (text, pattern, q);
	return 0;
}

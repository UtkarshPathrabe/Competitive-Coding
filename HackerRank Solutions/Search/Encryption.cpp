#include <bits/stdc++.h>

using namespace std;

int main (void) {
	char str[82];
	cin >> str;
	int l = strlen (str), w = floor (sqrt (l)), h = ceil (sqrt (l));
	if ((w * h) < l) {
		w = h;
	}
	int k = l;
	while (k < (h * w)) {
		str[k++] = '@';
	}
	str[k] = '\0';
	char encry[w][h];
	for (int i = 0, k = 0; i < w; i++) {
		for (int j = 0; j < h; j++) {
			encry[i][j] = str[k++];
		}
	}
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (encry[j][i] != '@') {
				cout << encry[j][i];
			}
		}
		cout << " ";
	}
	return 0;
}

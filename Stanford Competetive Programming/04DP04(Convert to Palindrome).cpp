#include <bits/stdc++.h>
#define MAXLENGTH 51

using namespace std;

int D[MAXLENGTH][MAXLENGTH] = {{0}};

int main(void) {
	char string[MAXLENGTH];
	cout << "Enter the String:" << endl;
	cin >> string;
	for (int t = 2; t <= strlen(string); t++) {
		for (int i= 1, j = t; j <= strlen(string); i++, j++) {
			if (string[i] == string[j]) {
				D[i][j] = D[i+1][j-1];
			}else {
				D[i][j] = 1 + min(D[i][j-1], D[i+1][j]);
			}
		}
	}
	cout << D[MAXLENGTH-1][MAXLENGTH-1] << endl;
	return 0;
}

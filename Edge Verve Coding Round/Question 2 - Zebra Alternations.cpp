#include <bits/stdc++.h>
#define MAXLENGTH 105

using namespace std;

char str1[MAXLENGTH];
int array[53] = {0}, mapping[53][MAXLENGTH] = {{0}}, le = 53;

void maximum () {
	int maxi1 = INT_MIN, maxIndex1 = 0, maxIndex2 = 0, maxi2 = INT_MIN, prev = INT_MIN, count = 0, flag = 0;
	for (int i = 0; i < le; i++) {
		maxi1 = max(maxi1, array[i]);
		if (prev != maxi1) {
			maxIndex1 = i;
			prev = maxi1;
		}
	}
	array[maxIndex1] = 0;
	prev = INT_MIN;
	for (int i = 0; i < le; i++) {
		maxi2 = max(maxi2, array[i]);
		if (prev != maxi2) {
			maxIndex2 = i;
			prev = maxi2;
		}
	}
	for (int i = 0; i < le; i++) {
		if (flag == 1) {
			if (mapping[maxIndex1][i] == 1) {
				count += 1;
				flag = 2;
			}
		} else if (flag == 2) {
			if (mapping[maxIndex2][i] == 1) {
				count += 1;
				flag = 1;
			}
		} else {
			if (mapping[maxIndex1][i] == 1) {
				count += 1;
				flag = 2;
			}
			if (mapping[maxIndex2][i] == 1) {
				count += 1;
				flag = 1;
			}
		}
		
	}
	cout << str1 << " has " << count << " alternations." << endl;
}

int main (void) {
	cin >> str1;
	int l = strlen(str1);
	for (int i = 0; i < l; i++) {
		if (str1[i] >= 'a' && str1[i] <= 'z') {
			array[str1[i] - 'a'] += 1;
			mapping[str1[i] - 'a'][i] = 1;
		} else if (str1[i] >= 'A' && str1[i] <= 'Z') {
			array[str1[i] - 'A' + 26] += 1;
			mapping[str1[i] - 'A' + 26][i] = 1;
		}
	}
	maximum ();
	return 0;
}

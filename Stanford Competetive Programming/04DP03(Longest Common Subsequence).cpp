#include <bits/stdc++.h>
#define MAXLENGTH 51

using namespace std;

int array[2][MAXLENGTH] = {{0}};

int main(void) {
	char string1[MAXLENGTH], string2[MAXLENGTH];
	cout << "Enter two Strings(with a space in between):" << endl;
	cin >> string1 >> string2;
	for (int i = 0; i < strlen(string1); i++) {
		for (int j = 0; j < strlen(string2); j++) {
			if (string1[i] == string2[j]) {
				array[i%2][j] = array[(i-1)%2][j-1] + 1;
			}else {
				array[i%2][j] = max(array[(i-1)%2][j], array[i%2][j-1]);
			}
		}
	}
	cout << array[(strlen(string1) - 1)%2][strlen(string2) - 1] << endl;
	return 0;
}

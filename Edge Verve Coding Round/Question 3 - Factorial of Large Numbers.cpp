#include <bits/stdc++.h>
#define MAX 100

using namespace std;

int facto[MAX] = {0}, length = 0;

void multiply (int num) {
	int i, r = 0, arr[MAX] = {0};
	for (i = 0; i <= length; i++) {
		arr[i] = facto[i];
	}
	for (i = 0; i <= length; i++) {
		facto[i] = ((arr[i] * num) + r) % 10;
		r = ((arr[i] * num) + r) / 10;
	}
	while (r != 0) {
		facto[i] = r % 10;
		r = r / 10;
		i += 1;
	}
	length = i - 1;
}

void factorial (int number) {
	for (int i = 1; i <= number; i++) {
		multiply (i);
	}
}

int main (void) {
	int number;
	cin >> number;
	facto[0] = 1;
	factorial (number);
	for (int i = length; i >= 0; i--) {
		cout << facto[i];
	}
	cout << endl;
	return 0;
}

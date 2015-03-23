#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, count, digit;
	long long int N, temp;
	cin >> T;
	while (T--) {
		cin >> N;
		temp = N;
		count = 0;
		while (temp) {
			digit = temp % 10;
			if (digit != 0) {
				if (N % digit == 0) {
					count += 1;
				}
			}
			temp /= 10;
		}
		cout << count << endl;
	}
	return 0;
}

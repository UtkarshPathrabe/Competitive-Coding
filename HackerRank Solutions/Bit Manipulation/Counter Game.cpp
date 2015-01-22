#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, len, count;
	unsigned long long int N, factor, temp;
	cin >> T;
	while (T--) {
		cin >> N;
		count = 0;
		while (N != 1) {
			len = 0;
			temp = N;
			while (temp != 0) {
				temp /= 2;
				len++;
			}
			factor = (unsigned long long int) 1 << (len - 1);
			if (N == factor) {
				N /= 2;
			} else {
				N -= factor;
			}
			count++;
		}
		if (count % 2 == 0) {
			cout << "Richard" << endl;
		} else {
			cout << "Louise" << endl;
		}
	}
	return 0;
}

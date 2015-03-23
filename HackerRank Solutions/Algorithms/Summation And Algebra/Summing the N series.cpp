#include <bits/stdc++.h>

using namespace std;

int main (void) {
	long long int test, num, C = 1e9 + 7;
	cin >> test;
	while (test--) {
		cin >> num;
		num = num % C;
		cout << (num * num) % C << endl;
	}
	return 0;
}

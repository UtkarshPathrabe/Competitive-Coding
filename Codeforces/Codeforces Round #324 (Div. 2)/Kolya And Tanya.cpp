#include <bits/stdc++.h>

using namespace std;

const long long int mod = 1000000007;

long long int pow (int x, int y) {
	if (y == 0) {
		return 1;
	}
	long long int s = 1, temp = 1;
	if (y % 2 == 1) {
		s = x;
	}
	temp = (pow(x, y/2))%mod;
	return (temp*temp*s)%mod;
}

int main (void) {
	int n;
	cin >> n;
	cout << (pow(3, 3*n) - pow(7, n)%mod + mod)%mod << endl;
	return 0;
}

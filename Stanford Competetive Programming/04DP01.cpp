#include <bits/stdc++.h>

using namespace std;

long long int D[10000];

int main(void) {
	long long int n;
	cout << "Enter a number" << endl;
	cin >> n;
	if(n < 0)
		cout << "0" << endl;
	else {
		D[0] = 1;
		D[1] = 1;
		D[2] = 1;
		D[3] = 2;
		for(long long int i = 4; i <= n; i++) {
			D[i] = D[i-1] + D[i-3] + D[i-4];
		}
		cout << D[n] << endl;
	}
	return 0;
}

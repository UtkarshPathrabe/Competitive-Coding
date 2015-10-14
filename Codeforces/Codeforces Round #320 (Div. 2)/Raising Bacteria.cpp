#include <bits/stdc++.h>
#define LLI long long int

using namespace std;

int main (void) {
	LLI x, count = 0;
	cin >> x;
	while (x) {
		if (x & 1) {
			count++;
		}
		x = x >> 1;
	}
	cout << count << endl;
	return 0;
}

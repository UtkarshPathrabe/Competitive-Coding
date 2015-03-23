#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, Count[100] = {0}, Freq[100] = {0}, temp;
	char str[50];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp >> str;
		Count[temp] += 1;
	}
	Freq[0] = Count[0];
	for (int i = 1; i < 100; i++) {
		Freq[i] = Freq[i - 1] + Count[i];
	}
	for (int i = 0; i < 100; i++) {
		cout << Freq[i] << " ";
	}
	return 0;
}

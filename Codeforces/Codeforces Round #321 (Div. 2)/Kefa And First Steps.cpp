#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n;
	vector <long long int> arr;
	cin >> n;
	for (int i = 0; i < n; i++) {
		long long int temp;
		cin >> temp;
		arr.push_back(temp);
	}
	int maxi = 1, temp = 1;
	for (int i = 1; i < n; i++) {
		if (arr[i] >= arr[i-1]) {
			temp++;
		} else {
			temp = 1;
		}
		maxi = max(temp, maxi);
	}
	cout << maxi << endl;
	return 0;
}

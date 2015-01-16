#include <bits/stdc++.h>

using namespace std;

void InsertionSort (vector<int> &Arr) {
	int len = Arr.size(), shift = 0;
	for (int i = 1; i < len; i++) {
		int Val = Arr[i], j = i - 1;
		while ((j >= 0) && (Arr[j] > Val)) {
			Arr[j + 1] = Arr[j];
			j -= 1;
			shift += 1;
		}
		Arr[j + 1] = Val;
	}
	cout << shift << endl;
}

int main (void) {
	vector <int> Arr;
	int ArrSize;
	cin >> ArrSize;
	for (int i = 0; i < ArrSize; i++) {
		int temp;
		cin >> temp;
		Arr.push_back(temp);
	}
	InsertionSort(Arr);
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

void PrintArray (vector<int> &Arr) {
	for (int i = 0; i < Arr.size(); i++) {
		cout << Arr[i] << " ";
	}
	cout << endl;
}

void InsertionSort (vector<int> &Arr) {
	int len = Arr.size(), Val = Arr[len - 1], j = len - 2;
	while ((j >= 0) && (Arr[j] > Val)) {
		Arr[j + 1] = Arr[j];
		PrintArray (Arr);
		j -= 1;
	}
	Arr[j + 1] = Val;
	PrintArray (Arr);
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

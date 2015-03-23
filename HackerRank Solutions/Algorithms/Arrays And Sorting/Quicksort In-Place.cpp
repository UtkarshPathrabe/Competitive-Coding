#include <bits/stdc++.h>

using namespace std;

void PrintArray (vector<int> &Arr) {
	for (int i = 0; i < Arr.size(); i++) {
		cout << Arr[i] << " ";
	}
	cout << endl;
}

void Swap (int * a, int * b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int Partition (vector<int> &Arr, int start, int end) {
	int i, j, p = Arr[end];
	for (i = start - 1, j = start; j < end; j++) {
		if (Arr[j] < p) {
			i += 1;
			Swap(&Arr[i], &Arr[j]);
		}
	}
	Swap (&Arr[i + 1], &Arr[end]);
	PrintArray (Arr);
	return (i + 1);
}

void QuickSort (vector<int> &Arr, int start, int end) {
	if (start < end) {
		int pivot = Partition (Arr, start, end);
		QuickSort (Arr, start, pivot - 1);
		QuickSort (Arr, pivot + 1, end);
	}
}

int main (void) {
	vector <int> Arr;
	int Size;
	cin >> Size;
	for (int i = 0; i < Size; i++) {
		int temp;
		cin >> temp;
		Arr.push_back(temp);
	}
	QuickSort (Arr, 0, Size - 1);
	return 0;
}

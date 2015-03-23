#include <bits/stdc++.h>

using namespace std;

int shiftI = 0, shiftQ = 0;

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
			shiftQ += 1;
		}
	}
	Swap (&Arr[i + 1], &Arr[end]);
	shiftQ += 1;
	return (i + 1);
}

void QuickSort (vector<int> &Arr, int start, int end) {
	if (start < end) {
		int pivot = Partition (Arr, start, end);
		QuickSort (Arr, start, pivot - 1);
		QuickSort (Arr, pivot + 1, end);
	}
}

void InsertionSort (vector<int> &Arr) {
	int len = Arr.size();
	for (int i = 1; i < len; i++) {
		int Val = Arr[i], j = i - 1;
		while ((j >= 0) && (Arr[j] > Val)) {
			Arr[j + 1] = Arr[j];
			j -= 1;
			shiftI += 1;
		}
		Arr[j + 1] = Val;
	}
}

int main (void) {
	vector <int> Arr1, Arr2;
	int Size;
	cin >> Size;
	for (int i = 0; i < Size; i++) {
		int temp;
		cin >> temp;
		Arr1.push_back(temp);
		Arr2.push_back(temp);
	}
	InsertionSort (Arr1);
	QuickSort (Arr2, 0, Size - 1);
	cout << shiftI - shiftQ << endl;
	return 0;
}

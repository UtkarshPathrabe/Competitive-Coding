#include <bits/stdc++.h>

using namespace std;

void PrintArray (vector<int> &Arr) {
	for (int i = 0; i < Arr.size(); i++) {
		cout << Arr[i] << " ";
	}
	cout << endl;
}

void Partition (vector<int> &Arr) {
	int p = Arr[0], len = Arr.size(), i = 0;
	vector<int> Less, Greater;
	vector<int>::iterator it;
	for (int j = 1; j < len; j++) {
		if (Arr[j] < p) {
			Less.push_back(Arr[j]);
		} else {
			Greater.push_back(Arr[j]);
		}
	}
	for (it = Less.begin(); it != Less.end(); it++) {
		Arr[i++] = *it;
	}
	Arr[i++] = p;
	for (it = Greater.begin(); it != Greater.end(); it++) {
		Arr[i++] = *it;
	}
	PrintArray (Arr);
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
	Partition (Arr);
	return 0;
}

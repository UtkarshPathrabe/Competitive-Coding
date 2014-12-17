/* Author: Utkarsh Pathrabe */

#include <bits/stdc++.h>

using namespace std;

int ArraySize = 0;
vector<int> Array;

void PrintArray(vector<int> &A) {
	printf("The present ARRAY contents are:\n");
	for(vector<int>::iterator it = A.begin(); it != A.end(); it++){
		printf("%d\t", *it);
	}
	printf("\n");
}

void AddElement(vector<int> &A, int key) {
	A.push_back(key);
	ArraySize = A.size();
}

void Merge(vector<int> &A, int p, int q, int r) {						// Merge takes Theta(n) time.
	int n1, n2, i, j, k;
	vector<int> Left;
	vector<int> Right;
	n1 = q - p + 1;
	n2 = r - q;
	for (i = 0; i < n1; i++) {
		Left.push_back(A[p + i]);
	}
	for (i = 0; i < n2; i++) {
		Right.push_back(A[q + i + 1]);
	}
	Left.push_back(INT_MAX);
	Right.push_back(INT_MAX);
	i = 0;
	j = 0;
	for (k = p; k <= r; k++) {
		if (Left[i] <= Right[j]) {
			A[k] = Left[i];
			i += 1;
		} else {
			A[k] = Right[j];
			j += 1;
		}
	}
}

void MergeSort(vector<int> &A, int p, int r){							// Time Complexity Theta(n*log(n)) 
	int q;
	if (p < r) {
		q = floor ((p + r) / 2);
		MergeSort (A, p, q);
		MergeSort (A, q + 1, r);
		Merge (A, p, q, r);
	}
}

int main(void) {
	AddElement(Array, 20);
	AddElement(Array, 18);
	AddElement(Array, 15);
	AddElement(Array, 10);
	AddElement(Array, 8);
	AddElement(Array, 14);
	AddElement(Array, 1);
	AddElement(Array, 2);
	AddElement(Array, 3);
	AddElement(Array, 21);
	AddElement(Array, 11);
	AddElement(Array, 16);
	AddElement(Array, 17);
	PrintArray(Array);
	MergeSort(Array, 0, ArraySize - 1);
	PrintArray(Array);
	return 0;
}

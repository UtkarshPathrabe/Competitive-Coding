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

void InsertionSort(vector<int> &A){							// Worst Running Time O(n^2), Average Running Time O(n^2), Best Running Time O(n) 
	int key, i;
	for(int j = 1; j < ArraySize; j++) {
		key = A[j];
		i = j - 1;
		while(i >= 0 && A[i] > key) {
			A[i + 1] = A[i];
			i--;
		}
		A[i+1] = key;
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
	InsertionSort(Array);
	PrintArray(Array);
	return 0;
}

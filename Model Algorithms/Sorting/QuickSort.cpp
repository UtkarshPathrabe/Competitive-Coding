/* Author: Utkarsh Pathrabe */

#include <bits/stdc++.h>

using namespace std;

vector<int> Array;
int ArraySize = 0;

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

void Swap(int *i, int *j) {
	int temp = *i;
	*i = *j; 
	*j = temp;
}

int Partition(vector<int> &A, int p, int r){
	int i = (rand() % (r-p+1)) + p;
	Swap(&A[i], &A[r]);
	int key = A[r];
	i = p-1;
	for(int j = p; j < r; j++) {
		if(A[j] <= key) {
			i += 1;
			Swap(&A[i], &A[j]);
		}
	}
	Swap(&A[i+1], &A[r]);
	return i+1;
}

void QuickSort(vector<int> &A, int p, int r) {}						// Worst Running Time O(n^2), Average Running Time O(n*lg(n)), Best Running Time O(n*lg(n)
	if(p < r) {
		int q = Partition(A, p, r);
		QuickSort(A, p, q-1);
		QuickSort(A, q+1, r);
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
	QuickSort(Array, 0, ArraySize - 1);
	PrintArray(Array);
	return 0;
}

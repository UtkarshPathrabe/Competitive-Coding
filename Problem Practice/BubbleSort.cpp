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

void BubbleSort(vector<int> &A) {							// Worst Running Time O(n^2), Average Running Time O(n^2), Best Running Time O(n^2) 
	for(int i = 1; i < ArraySize; i++) {
		for(int j = 0; j < i; j++) {
			if(A[i] < A[j]){
				Swap(&A[i], &A[j]);
			}
		}
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
	BubbleSort(Array);
	PrintArray(Array);
	return 0;
}

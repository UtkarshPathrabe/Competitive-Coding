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

int Select(vector<int> &A, int p, int r, int i) {
	if(p == r) {
		return A[p];
	}
	int q = Partition(A, p, r);
	int k = q - p;
	if(i == k) {
		return A[q];
	}else if(i < k) {
		return Select(A, p, q-1, i);
	}else{
		return Select(A, q, r, i-k);
	}
}

int main(void) {
	int input = 0;
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
	printf("Enter which smallest element do you want?\t");
	scanf("%d", &input);
	printf("The %dth smallest element is %d.\n", input, Select(Array, 0, ArraySize - 1, (input-1)));
	PrintArray(Array);
	return 0;
}

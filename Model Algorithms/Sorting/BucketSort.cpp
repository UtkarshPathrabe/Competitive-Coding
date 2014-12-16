/* Author: Utkarsh Pathrabe */

#include <bits/stdc++.h>

using namespace std;

vector<float> Array;
int ArraySize = 0;
vector<float>::iterator it;

void PrintArray(vector<float> &A) {
	printf("The present ARRAY contents are:\n");
	for(it = A.begin(); it != A.end(); it++){
		printf("%f\t", *it);
	}
	printf("\n");
}

void AddElement(vector<float> &A, float key) {
	A.push_back(key);
	ArraySize = A.size();
}

void BucketSort(vector<float> &A) {
	vector<float> Bucket[ArraySize];
	for(it = A.begin(); it != A.end(); it++) {
		int index = ArraySize * (*it);
		Bucket[index].push_back(*it);
	}
	for(int i = 0; i < ArraySize; i++) {
		sort(Bucket[i].begin(), Bucket[i].end());
	}
	A.erase(A.begin(), A.end());
	for(int i = 0; i < ArraySize; i++) {
		for(int j = 0; j < Bucket[i].size(); j++) {
			A.push_back(Bucket[i][j]);
		}
 	}
}

int main(void) {
	AddElement(Array, 0.897);
	AddElement(Array, 0.565);
	AddElement(Array, 0.656);
	AddElement(Array, 0.1234);
	AddElement(Array, 0.665);
	AddElement(Array, 0.3434);
	AddElement(Array, 0.0123);
	PrintArray(Array);
	BucketSort(Array);
	printf("The Array after sorting is:\n");
	PrintArray(Array);
	return 0;
}

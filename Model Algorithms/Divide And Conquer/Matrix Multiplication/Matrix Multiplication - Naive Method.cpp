/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Naive method for Matrix Multiplication
*/

/* Time Complexity: O(N^3) */

#include <bits/stdc++.h>
#define N 2

using namespace std;

void SquareMatrixMultiply (int A[N][N], int B[N][N]) {
	int C[N][N] = {{0}};
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				C[i][j] += A[i][k] * B[k][j];
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << C[i][j] << " ";
		}
		cout << endl;
	}
}

int main (void) {
	int A[N][N] = {{1, 3}, {7, 5}}, B[N][N] = {{6, 8}, {4, 2}};
	SquareMatrixMultiply (A, B);
	return 0;
}

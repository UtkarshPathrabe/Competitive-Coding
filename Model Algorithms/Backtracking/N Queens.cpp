/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Problem Statement: The N Queen is the problem of placing N chess queens on an N * N chessboard so that no two queens attack each other. */

#include <bits/stdc++.h>
#define N 100

using namespace std;

int n, board[N][N] = {{0}};

void PrintSolution () {
	cout << "Solution is:" << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << board[i][j] << "\t";
		}
		cout << endl;
	}
}

bool IsSafe (int row, int column) {
	for (int i = 0; i <= column; i++) {
		if (board[row][i]) {
			return false;
		}
	}
	for (int i = row, j = column; i >= 0 && j >= 0; i--, j--) {
		if (board[i][j]) {
			return false;
		}
	}
	for (int i = row, j = column; i < n && j >= 0; i++, j--) {
		if (board[i][j]) {
			return false;
		}
	}
	return true;
}

bool NQueenUtility (int column) {
	if (column >= n) {
		return true;
	}
	for (int i = 0; i < n; i++) {
		if (IsSafe (i, column)) {
			board[i][column] = 1;
			if (NQueenUtility (column + 1)) {
				return true;
			} else {
				board[i][column] = 0;
			}
		}
	}
	return false;
}

void NQueen () {
	if (NQueenUtility (0)) {
		PrintSolution ();
	} else {
		cout << "Solution does not exist." << endl;
	}
}

int main (void) {
	cout << "Enter the size of board:" << endl;
	cin >> n;
	NQueen ();
	return 0;
}

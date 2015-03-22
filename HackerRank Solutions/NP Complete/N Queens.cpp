#include <bits/stdc++.h>
#define N 100

using namespace std;

int n = 27, board[N][N] = {{0}};
int coX[N], coY[N];

void PrintStatement () {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j]) {
				cout << j+1 << " ";
				break;
			}
		}
	}
	cout << endl;
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
	if (column >= 2) {
		bool flag = true;
		coX[column] = row;
		coY[column] = column;
		for (int i = 1; column - (2*i) >= 0; i++) {
			if ((coX[column]-coX[column-i] == coX[column-i]-coX[column-(2*i)]) && (coY[column]-coY[column-i] == coY[column-i]-coY[column-(2*i)])) {
				flag = false;
				break;
			}
		}
		coX[column] = -1;
		coY[column] = -1;
		return flag;
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
			coX[column] = i;
			coY[column] = column;
			if (NQueenUtility (column + 1)) {
				return true;
			} else {
				board[i][column] = 0;
				coX[column] = -1;
				coY[column] = -1;
			}
		}
	}
	return false;
}

void NQueen () {
	if (NQueenUtility (0)) {
		PrintStatement ();
	}
}

int main (void) {
	cout << "27" << endl;
	for (int i = 0; i < N; i++) {
		coX[i] = coY[i] = -1;
	}
	NQueen ();
	return 0;
}

/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Problem Statement: Given an partially filled 9*9 2-D Array Grid[9][9], the goal is to assign digits(from 1 to 9) to the empty cells so that every row, column 
*  and subgrid of size 3*3 contains exactly one instance of the digits from 1 to 9 */

#include <bits/stdc++.h>
#define N 9

using namespace std;

int Grid[N][N];

void PrintGrid () {
	cout << "The Sudoku Solution is:" << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << Grid[i][j] << "\t";
		}
		cout << endl;
	}
}

bool IsLocationUnassigned (int &row, int &column) {
	for (row = 0; row < N; row++) {
		for (column = 0; column < N; column++) {
			if (Grid[row][column] == 0) {
				return true;
			}
		}
	}
	return false;
}

bool IsRowUsed (int row, int number) {
	for (int column = 0; column < N; column++) {
		if (Grid[row][column] == number) {
			return true;
		}
	}
	return false;
}

bool IsColumnUsed (int column, int number) {
	for (int row = 0; row < N; row++) {
		if (Grid[row][column] == number) {
			return true;
		}
	}
	return false;
}

bool IsBoxUsed (int BoxRow, int BoxColumn, int number) {
	for (int row = 0; row < 3; row++) {
		for (int column = 0; column < 3; column++) {
			if (Grid[BoxRow + row][BoxColumn + column] == number) {
				return true;
			}
		}
	}
	return false;
}

bool IsSafe (int row, int column, int number) {
	return ((!IsRowUsed (row, number)) && (!IsColumnUsed (column, number)) && (!IsBoxUsed (row - (row % 3), column - (column % 3), number)));
}

bool SudokuSolveUtility () {
	int row, column;
	if (!IsLocationUnassigned (row, column)) {
		return true;
	}
	for (int number = 1; number < 10; number++) {
		if (IsSafe (row, column, number)) {
			Grid[row][column] = number;
			if (SudokuSolveUtility ()) {
				return true;
			} else {
				Grid[row][column] = 0;
			}
		}
	}
	return false;
}

void SudokuSolve () {
	if (SudokuSolveUtility ()) {
		PrintGrid();
	} else {
		cout << "Solution for given Sudoku doesn't exist!" << endl;
	}
}

int main (void) {
	cout << "Enter the Sudoku Grid(first fill all elements of a row, enter '0' where the value is to be filled):" << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> Grid[i][j];
		}
	}
	SudokuSolve ();
	return 0;
}

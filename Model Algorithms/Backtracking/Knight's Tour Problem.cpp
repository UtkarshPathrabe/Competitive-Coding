/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Problem Statement: Program to print Knight's Tour */

#include <bits/stdc++.h>
#define N 8

using namespace std;

void PrintSolution (int board[N][N]) {
	cout << "The Knight's Tour is:" << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << board[i][j] << "\t";
		}
		cout << endl;
	}
}

bool IsSafe (int x, int y, int board[N][N]) {
	if (x >= 0 && y >= 0 && x < N && y < N && board[x][y] == INT_MIN) {
		return true;
	}
	return false;
}

bool KnightTourUtility (int X, int Y, int Move, int board[N][N], int MoveX[N], int MoveY[N]) {
	if (Move == N*N) {
		return true;
	}
	for (int i = 0; i < N; i++) {
		int NextX = X + MoveX[i];
		int NextY = Y + MoveY[i];
		if (IsSafe (NextX, NextY, board)) {
			board[NextX][NextY] = Move;
			if (KnightTourUtility (NextX, NextY, Move + 1, board, MoveX, MoveY)) {
				return true;
			} else {
				board[NextX][NextY] = INT_MIN;
			}
		}
	}
	return false;
}

void KnightTour (int StartX, int StartY) {
	int board[N][N];
	int MoveX[8] = {1, 2, 2, 1, -1, -2, -2, -1};
	int MoveY[8] = {2, 1, -1, -2, -2, -1, 1, 2};
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			board[i][j] = INT_MIN;
		}
	}
	board[StartX][StartY] = 0;
	if (KnightTourUtility (StartX, StartY, 1, board, MoveX, MoveY) == false) {
		cout << "The Knight's Tour doesn't exist!" << endl;
	} else {
		PrintSolution (board);
	}
}

int main (void) {
	int x, y;
	cout << "Enter the Knight's initial position(X Y):" << endl;
	cin >> x >> y;
	KnightTour (x, y);
	getchar();
	return 0;
}

/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Problem Statement: A Maze is given as N*N binary matrix of blocks. A rat starts from source and has to reach destination. */

#include <bits/stdc++.h>
#define N 100

using namespace std;

int rows, columns, StartX, StartY, DestX, DestY, Maze[N][N] = {{0}}, Sol[N][N] = {{0}}, MoveX[4] = {0, 1, 0, -1}, MoveY[4] = {1, 0, -1, 0};

void PrintSolution () {
	cout << "The Maze Solution is:" << endl;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < columns; j++) {
			cout << Sol[i][j] << "\t";
		}
		cout << endl;
	}
}

bool IsSafe (int x, int y) {
	if (x >= 0 && x < rows && y >= 0 && y < columns && (Maze[x][y] == 1) && (Sol[x][y] == 0)) {
		return true;
	}
	return false;
}

bool MazeSolveUtility (int X, int Y) {
	if ((X == DestX) && (Y == DestY)) {
		Sol[X][Y] = 1;
		return true;
	}
	for (int i = 0; i < 4; i++) {
		int NextX = X + MoveX[i];
		int NextY = Y + MoveY[i];
		if (IsSafe (NextX, NextY)) {
			Sol[NextX][NextY] = 1;
			if (MazeSolveUtility (NextX, NextY)) {
				return true;
			} else {
				Sol[NextX][NextY] = 0;
			}
		}
	}
	return false;
}

void MazeSolve () {
	if (IsSafe (StartX, StartY) && IsSafe (DestX, DestY)) {
		Sol[StartX][StartY] = 1;
		if (MazeSolveUtility (StartX, StartY) == false) {
			cout << "Maze Solution Doesn't Exist!" << endl;
		} else {
			PrintSolution ();
		}
	} else {
		cout << "Invalid Source/Destination." << endl;
	}
}

int main (void) {
	cout << "Enter the number of rows and columns in the maze:" << endl;
	cin >> rows >> columns;
	cout << "Enter the Maze Matrix (first fill all elements of a row, '0' means the block is dead end and '1' means the block can be used in the path from source to destination):" << endl;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < columns; j++) {
			cin >> Maze[i][j];
		}
	}
	cout << "Enter the Source(X Y) and Destination(X Y) Co-ordinates:" << endl;
	cin >> StartX >> StartY >> DestX >> DestY;
	MazeSolve ();
	return 0;
}

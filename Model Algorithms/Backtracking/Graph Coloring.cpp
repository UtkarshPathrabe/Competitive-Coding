/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Problem Statement: Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that
*  no two adjacent vertices of the graph are with same color */

#include <bits/stdc++.h>
#define N 100

using namespace std;

int V, M, Graph[N][N] = {{0}}, Color[N] = {0};

void PrintSolution () {
	cout << "The Coloring of Vertices is:" << endl;
	for (int i = 0; i < V; i++) {
		cout << Color[i] << "\t";
	}
	cout << endl;
}

bool IsSafe (int vertex, int color) {
	for (int i = 0; i < V; i++) {
		if ((Graph[vertex][i]) && (color == Color[i])) {
			return false;
		}
	}
	return true;
}

bool GraphColorUtility (int vertex) {
	if (vertex == V) {
		return true;
	}
	for (int c = 1; c <= M; c++) {
		if (IsSafe (vertex, c)) {
			Color[vertex] = c;
			if (GraphColorUtility (vertex + 1)) {
				return true;
			} else {
				Color[vertex] = 0;
			}
		}
	}
	return false;
}

void GraphColor () {
	if (GraphColorUtility (0)) {
		PrintSolution ();
	} else {
		cout << "Solution of Graph Coloring does not exist!" << endl;
	}
}

int main (void) {
	cout << "Enter the number of vertices in the graph and number of different colors:" << endl;
	cin >> V >> M;
	cout << "Enter the Graph as Adjacency Matrix (first fill all elements of a row):" << endl;
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			cin >> Graph[i][j];
		}
	}
	GraphColor ();
	return 0;
}

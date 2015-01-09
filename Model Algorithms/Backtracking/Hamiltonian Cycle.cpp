/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. 
*  A Hamiltonian Cycle (or Hamiltonian Circuit) is a Hamiltonian Path such that there is an edge (in graph) from the last vertex to the first vertex of the Hamiltonian Path. */

/* Problem Statement: Determine whether a given graph contains Hamiltonian Cycle or not. */

#include <bits/stdc++.h>
#define N 100

using namespace std;

int V, Path[N], Graph[N][N] = {{0}};
bool Valid[N] = {false};

void PrintSolution () {
	cout << "The Hamiltonian Cycle is:" << endl;
	for (int i = 0; i < V; i++) {
		cout << Path[i] << "\t";
	}
	cout << Path[0] << "." << endl;
}

bool IsSafe (int vertex, int pos) {
	if (Graph[Path[pos - 1]][vertex] == 0) {
		return false;
	}
	if (Valid[vertex]) {
		return false;
	}
	return true;
}

bool HamiltonUtility (int pos) {
	if (pos == V) {
		if (Graph[Path[pos - 1]][Path[0]]) {
			return true;
		} else {
			return false;
		}
	}
	for (int i = 1; i < V; i++) {
		if (IsSafe (i, pos)) {
			Path[pos] = i;
			Valid[i] = true;
			if (HamiltonUtility (pos + 1)) {
				return true;
			} else {
				Path[pos] = -1;
				Valid[i] = false;
			}
		}
	}
	return false;
}

void Hamilton () {
	for (int i = 0; i < V; i++) {
		Valid[i] = false;
		Path[i] = -1;
	}
	Path[0] = 0;
	Valid[0] = true;
	if (HamiltonUtility (1)) {
		PrintSolution ();
	} else {
		cout << "Hamilton Cycle does not exist!" << endl;
	}
}

int main (void) {
	cout << "Enter the number of vertices in the Graph:" << endl;
	cin >> V;
	cout << "Enter the Graph as Adjacency Matrix (first fill all elements of a row):" << endl;
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			cin >> Graph[i][j];
		}
	}
	Hamilton ();
	return 0;
}

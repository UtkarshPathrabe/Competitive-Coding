/* Author: Utkarsh Pathrabe
*  Algorithm: Prims Minimum Spanning Tree for Adjacency List Representation Algorithm
*/

/* MST-PRIM(G, w, r):
*	1 for each u belonging to V[G]
*	2 		do	key[u] <- Infinity
*	3 			parent[u] <- NIL
*	4 key[r] <- 0
*	5 Q <- V[G]
*	6 while Q != Empty
*	7 		do u <- EXTRACT-MIN(Q)
*	8 			for each v belonging to Adj[u]
*	9 				do if v belonging to Q and w(u, v) < key[v]
*	10 					then parent[v] <- u
*	11 						key[v] <- w(u, v)
*/

/* Time Complexity of below program is O(V^2)
*/

#include <bits/stdc++.h>
#define MAXIMUM 10000

using namespace std;

vector <int> Key;
vector <int> Parent;
vector <bool> MstSet;

int V;
int AdjMat[MAXIMUM][MAXIMUM];

int MinKey () {
	int min = INT_MAX, minIndex;
	for (int i = 0; i < V; i++) {
		if ((MstSet[i] == false) && (Key[i] < min)) {
			min = Key[i];
			minIndex = i;
		}
	}
	return minIndex;
}

void Prims () {
	Key[0] = 0;
	Parent[0] = -1;
	for (int count = 0; count < V - 1; count++) {
		int u = MinKey();
		MstSet[u] = true;
		for (int v = 0; v < V; v++) {
			if ((AdjMat[u][v]) && (MstSet[v] == false) && (AdjMat[u][v] < Key[v])) {
				Parent[v] = u;
				Key[v] = AdjMat[u][v];
			}
		}
	}
	cout << "Prims MST for Adjacency Matrix gives:" << endl;
	for (int i = 1; i < V; i++) {
		cout << (Parent[i] + 1) << "\t" << (i + 1) << "\t" << AdjMat[i][Parent[i]] << endl;
	}
}

int main (void) {
	int from, to, weight;
	cout << "Enter number of Vertices in the graph:" << endl;
	cin >> V;
	for (int i = 0; i < V; i++) {
		Key.push_back(INT_MAX);
		Parent.push_back(-1);
		MstSet.push_back(false);
		for (int j = 0; j < V; j++) {
			AdjMat[i][j] = 0;
		}
	}
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number <Space> Weight of Edge) in each line(Write '-1 -1 -1' if the list of edges is over):" << endl;
	cin >> from >> to >> weight;
	do {
		AdjMat[from - 1][to - 1] = weight;
		AdjMat[to - 1][from - 1] = weight;
		cin >> from >> to >> weight;
	} while (from != -1);
	Prims ();
	return 0;
}

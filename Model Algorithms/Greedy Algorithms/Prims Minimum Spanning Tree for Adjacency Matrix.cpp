// Time Complexity: O(V^2)

#include <bits/stdc++.h>
#define V 5

using namespace std;

int minKey (int key[], bool mstFlag[], int noVertices) {
	int minKey = INT_MAX, minIndex = -1;
	for (int i = 0; i < noVertices; i++) {
		if ((mstFlag[i] == false) && (minKey > key[i])) {
			minKey = key[i];
			minIndex = i;
		}
	}
	return minIndex;
}

void printMST (int parent[], int vertices, int graph[V][V]) {
	cout << "Edge\t\tWeight" << endl;
	for (int i = 1; i < vertices; i++) {
		cout << parent[i] << "-" << i << "\t:\t" << graph[i][parent[i]] << endl;
	}
}

void primMST (int graph[V][V], int n) {
	int parent[n], key[n];
	bool mstFlag[n];
	for (int i = 0; i < n; i++) {
		key[i] = INT_MAX;
		mstFlag[i] = false;
		parent[i] = -1;
	}
	key[0] = 0;
	for (int i = 0; i < n-1; i++) {
		int u = minKey (key, mstFlag, n);
		mstFlag[u] = true;
		for (int v = 0; v < n; v++) {
			if (graph[u][v] && mstFlag[v] == false && graph[u][v] < key[v]) {
				parent[v] = u;
				key[v] = graph[u][v];
			}
		}
	}
	printMST (parent, n, graph);
}

int main (void) {
	int graph[V][V] = {{0, 2, 0, 6, 0},
                      {2, 0, 3, 8, 5},
                      {0, 3, 0, 0, 7},
                      {6, 8, 0, 0, 9},
                      {0, 5, 7, 9, 0}};
    primMST (graph, V);
	return 0;
}

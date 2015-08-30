#include <bits/stdc++.h>
#define	V	9

using namespace std;

int minDistance (int dist[], bool flag[]) {
	int min = INT_MAX, min_index = -1;
	for (int v = 0; v < V; v++) {
		if ((flag[v] == false) && (dist[v] <= min)) {
			min = dist[v];
			min_index = v;
		}
	}
	return min_index;
}

void printSolution (int dist[]) {
	cout << "Vertex Distance from Source" << endl;
	for (int v = 0; v < V; v++) {
		cout << v << "\t" << dist[v] << endl;
	}
}

void dijkstra (int graph[V][V], int src) {
	int dist[V];
	bool flag[V];
	for (int i = 0; i < V; i++) {
		dist[i] = INT_MAX;
		flag[i] = false;
	}
	dist[src] = 0;
	for (int count = 0; count < V-1; count++) {
		int u = minDistance (dist, flag);
		flag[u] = true;
		for (int v = 0; v < V; v++) {
			if ((flag[v] == false) && (graph[u][v]) && (dist[u] != INT_MAX) && (dist[u] + graph[u][v] < dist[v])) {
				dist[v] = dist[u] + graph[u][v];
			}
		}
	}
	printSolution (dist);
}

int main (void) {
	int graph[V][V] =	{
						{0, 4, 0, 0, 0, 0, 0, 8, 0},
						{4, 0, 8, 0, 0, 0, 0, 11, 0},
						{0, 8, 0, 7, 0, 4, 0, 0, 2},
						{0, 0, 7, 0, 9, 14, 0, 0, 0},
						{0, 0, 0, 9, 0, 10, 0, 0, 0},
						{0, 0, 4, 0, 10, 0, 2, 0, 0},
						{0, 0, 0, 14, 0, 2, 0, 1, 6},
						{8, 11, 0, 0, 0, 0, 1, 0, 7},
						{0, 0, 2, 0, 0, 0, 6, 7, 0}
						};
	dijkstra(graph, 0);
	return 0;
}

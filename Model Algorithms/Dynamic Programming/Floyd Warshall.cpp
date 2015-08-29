/* Time Complexity: O(V^3); Space Complexity: O(V^2) */

#include <bits/stdc++.h>
#define V	4
#define INF	INT_MAX

using namespace std;

void PrintSolution (const int Distance[V][V]) {
	cout << "Following Matrix gives the Shortest Distance between every pair of vertices:" << endl;
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			if (Distance[i][j] == INF) {
				cout << "INF\t";
			} else {
				cout << Distance[i][j] << "\t";
			}
		}
		cout << endl;
	}
}

void FloydWarshall (int Distance[V][V], int Graph[V][V]) {
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			Distance[i][j] = Graph[i][j];
		}
	}
	for (int k = 0; k < V; k++) {
		for (int i = 0; i < V; i++) {
			for (int j = 0; j < V; j++) {
				if ((Distance[i][k] != INF) && (Distance[k][j] != INF) && (Distance[i][k] + Distance[k][j] < Distance[i][j])) {
					Distance[i][j] = Distance[i][k] + Distance[k][j];
				}
			}
		}
	}
}

int main (void) {
	int Graph[][V] = {{0,	5,	INF,	10},
					{INF,	0,	3,	INF},
					{INF,	INF,	0,	1},
					{INF,	INF,	INF,	0}};
	int Distance[V][V] = {0};
	FloydWarshall (Distance, Graph);
	PrintSolution (Distance);
	return 0;
}

/* Time Complexity: O((V^3)*k); Space Complexity: O(V^2) */

#include <bits/stdc++.h>

using namespace std;

int shortestPath (vector < vector <int> > &graph, int src, int dest, int k) {
	int V = graph.size();
	int sp[V][V][2];
	for (int e = 0; e <= k; e++) {
		for (int i = 0; i < V; i++) {
			for (int j = 0; j < V; j++) {
				sp[i][j][e%2] = INT_MAX;
				if (e == 0 && i == j) {
					sp[i][j][e] = 0;
				}
				if (e == 1 && graph[i][j] != INT_MAX) {
					sp[i][j][e] = graph[i][j];
				}
				if (e > 1) {
					for (int l = 0; l < V; l++) {
						if ((graph[i][l] != INT_MAX) && (i != l) && (j != l) && (sp[l][j][(e-1)%2] != INT_MAX)) {
							sp[i][j][e%2] = min (sp[i][j][e%2], graph[i][l] + sp[l][j][(e-1)%2]);
						}
					}
				}
			}
		}
	}
	return sp[src][dest][k%2];
}

int main (void) {
	vector < vector <int> > graph;
	vector <int> temp;
	temp.push_back (0);
	temp.push_back (10);
	temp.push_back (3);
	temp.push_back (2);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (INT_MAX);
	temp.push_back (0);
	temp.push_back (INT_MAX);
	temp.push_back (7);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (INT_MAX);
	temp.push_back (INT_MAX);
	temp.push_back (0);
	temp.push_back (6);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (INT_MAX);
	temp.push_back (INT_MAX);
	temp.push_back (INT_MAX);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	int src = 0, dest = 3, k = 2;
	cout << "The weight of the shortest path from " << src << " to " << dest << " with exactly " << k << " edges is: " << shortestPath (graph, src, dest, k) << "." << endl;
	return 0;
}

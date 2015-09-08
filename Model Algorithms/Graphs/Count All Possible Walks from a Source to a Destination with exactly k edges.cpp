/* Space Complexity: O(V); Time Complexity: O((V^2)*k) */

#include <bits/stdc++.h>

using namespace std;

int countWalks (vector < vector <int> > &graph, int src, int dest, int k) {
	int V = graph.size();
	int ans[2][V];
	if (src == dest && k != 0) {
		return 0;
	}
	if (k > V-1) {
		return 0;
	}
	for (int i = 0; i < V; i++) {
		ans[0][i] = graph[src][i];
	}
	for (int i = 1; i < k; i++) {
		for (int j = 0; j < V; j++) {
			if (ans[(i-1)%2][j] > 0) {
				for (int l = 0; l < V; l++) {
					ans[i%2][l] += (ans[(i-1)%2][j]) * ((graph[j][l] > 0) ? 1 : 0);
				}
			}
		}
	}
	return ans[(k-1)%2][dest];
}

int main (void) {
	vector < vector <int> > graph;
	vector <int> temp;
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (1);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	int src = 0, dest = 3, k = 2;
	cout << "The number of walks from " << src << " to " << dest << " with " << k << " edges are: " << countWalks(graph, src, dest, k) << endl;
	return 0;
}

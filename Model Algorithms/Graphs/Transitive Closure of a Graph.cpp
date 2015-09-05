#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

void transitiveClosure (vector< vector <int> > &graph) {
	int V = graph.size();
	bool reach[V][V];
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			if (graph[i][j] == INF) {
				reach[i][j] = false;
			} else {
				reach[i][j] = true;
			}
		}
	}
	for (int k = 0; k < V; k++) {
		for (int i = 0; i < V; i++) {
			for (int j = 0; j < V; j++) {
				reach[i][j] = (reach[i][j]) || (reach[i][k] && reach[k][j]);
			}
		}
	}
	cout << "Following Matrix is the transitive closure of the given graph:" << endl;
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			cout << reach[i][j] << "\t";
		}
		cout << endl;
	}
}

int main (void) {
	vector < vector <int> > graph;
	vector <int> temp;
	temp.push_back (0);
	temp.push_back (5);
	temp.push_back (8);
	temp.push_back (9);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (INF);
	temp.push_back (0);
	temp.push_back (3);
	temp.push_back (4);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (INF);
	temp.push_back (INF);
	temp.push_back (0);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (INF);
	temp.push_back (INF);
	temp.push_back (INF);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	transitiveClosure (graph);
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

bool isBipartite (vector< vector<int> > &G, int src) {
	int V = G.size();
	int color[V];
	for (int i = 0; i < V; i++) {
		color[i] = -1;
	}
	color[src] = 1;
	queue<int> Q;
	Q.push(src);
	while (!Q.empty()) {
		int u = Q.front();
		Q.pop();
		for (int v = 0; v < V; v++) {
			if ((G[u][v]) && (color[v] == -1)) {
				color[v] = 1 - color[u];
				Q.push(v);
			} else if ((G[u][v]) && (color[u] == color[v])) {
				return false;
			}
		}
	}
	return true;
}

int main (void) {
	vector < vector <int> > G;
	vector <int> temp;
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (1);
	G.push_back (temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	G.push_back (temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (1);
	G.push_back (temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	G.push_back (temp);
	temp.erase(temp.begin(), temp.end());
	isBipartite (G, 0) ? cout << "Graph is Bipartite" << endl : cout << "Graph is not Bipartite" << endl;
	return 0;
}

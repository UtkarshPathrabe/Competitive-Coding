#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list <int> *adj;
	void DFSUtil (int u, bool visited[], bool isCatPresent[], int m, int count, int *ans);
	public:
		Graph (int v) {V = v; adj = new list<int>[V];}
		void addEdge (int u, int v) {adj[u].push_back(v); adj[v].push_back(u);}
		int DFS (int src, int m, bool isCatPresent[]);
};

void Graph::DFSUtil (int u, bool visited[], bool isCatPresent[], int m, int count, int *ans) {
	visited[u] = true;
	if (isCatPresent[u]) {
		count++;
	} else {
		count = 0;
	}
	if (count > m) {
		return;
	}
	if ((adj[u].size() == 1) && (u != 1)) {
		(*ans)++;
	}
	for (list<int>::iterator it = adj[u].begin(); it != adj[u].end(); it++) {
		if (!visited[*it]) {
			DFSUtil (*it, visited, isCatPresent, m, count, ans);
		}
	}
}

int Graph::DFS (int src, int m, bool isCatPresent[]) {
	bool *visited = new bool[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
	}
	int ans = 0;
	DFSUtil (src, visited, isCatPresent, m, 0, &ans);
	return ans;
}

int main (void) {
	int n, m;
	cin >> n >> m;
	Graph g(n+1);
	bool isCatPresent[n+1];
	isCatPresent[0] = false;
	for (int i = 1; i <= n; i++) {
		int temp;
		cin >> temp;
		(temp == 0) ? (isCatPresent[i] = false) : (isCatPresent[i] = true);
	}
	for (int i = 0; i < n-1; i++) {
		int u, v;
		cin >> u >> v;
		g.addEdge(u, v);
	}
	cout << g.DFS(1, m, isCatPresent) << endl;
	return 0;
}

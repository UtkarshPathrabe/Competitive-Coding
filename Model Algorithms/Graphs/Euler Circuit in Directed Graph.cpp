/* Time Complexity: O(V+E) */

#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	int *in;
	void DFSUtil (int u, bool visited[]);
	public:
		Graph (int v) {V = v; adj = new list<int>[V]; in = new int[V]; for (int i = 0; i < V; i++) in[i] = 0;}
		~Graph () {delete [] adj;}
		void addEdge (int u, int v) {adj[u].push_back(v); (in[v])++;}
		Graph transpose ();
		bool isSC ();
		bool isEulerianCycle ();
};

void Graph::DFSUtil (int u, bool visited[]) {
	visited[u] = true;
	for (list<int>::iterator i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[*i]) {
			DFSUtil (*i, visited);
		}
	}
}

Graph Graph::transpose () {
	Graph g(V);
	for (int v = 0; v < V; v++) {
		for (list<int>::iterator i = adj[v].begin(); i != adj[v].end(); i++) {
			g.adj[*i].push_back(v);
		}
	}
	return g;
}

bool Graph::isSC () {
	bool *visited = new bool[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
	}
	DFSUtil (0, visited);
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			return false;
		}
	}
	Graph g = transpose ();
	for (int i = 0; i < V; i++) {
		visited[i] = false;
	}
	g.DFSUtil (0, visited);
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			return false;
		}
	}
	return true;
}

bool Graph::isEulerianCycle () {
	if (!isSC()) {
		return false;
	}
	for (int i = 0; i < V; i++) {
		if (adj[i].size() != in[i]) {
			return false;
		}
	}
	return true;
}

int main (void) {
	Graph g(5);
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(3, 4);
	g.addEdge(4, 0);
    if (g.isEulerianCycle())
       cout << "Given directed graph is Eulerian." << endl;
    else
       cout << "Given directed graph is not Eulerian." << endl;
	return 0;
}

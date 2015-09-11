#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	void DFSUtil (int u, bool visited[]);
	public:
		Graph (int v) {V = v; adj = new list<int>[V];}
		~Graph () {delete [] adj;}
		void addEdge (int u, int v) {adj[u].push_back(v);}
		Graph transpose ();
		bool isSC ();
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

int main (void) {
	Graph g1(5);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 3);
    g1.addEdge(3, 0);
    g1.addEdge(2, 4);
    g1.addEdge(4, 2);
    cout << "Graph g1 is ";
    g1.isSC() ? cout << "" : cout << "Not ";
    cout << "Strongly Connected." << endl;
    Graph g2(4);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    cout << "Graph g2 is ";
    g2.isSC() ? cout << "" : cout << "Not ";
    cout << "Strongly Connected." << endl;
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	bool isCyclicUtil (int u, bool visited[], int parent);
	public:
		Graph (int V);
		void addEdge (int u, int v);
		bool isTree ();
};

Graph::Graph (int V) {
	this->V = V;
	adj = new list<int>[V];
}

void Graph::addEdge (int u, int v) {
	adj[u].push_back (v);
	adj[v].push_back (u);
}

bool Graph::isCyclicUtil (int u, bool visited[], int parent) {
	visited[u] = true;
	list<int>::iterator i;
	for (i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[*i]) {
			if (isCyclicUtil(*i, visited, u)) {
				return true;
			}
		} else if (*i != parent) {
			return true;
		}
	}
	return false;
}

bool Graph::isTree () {
	bool *visited = new bool[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
	}
	if (isCyclicUtil (0, visited, -1)) {
		return false;
	}
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			return false;
		}
	}
	return true;
}

int main (void) {
	Graph g1 (5);
    g1.addEdge (1, 0);
    g1.addEdge (0, 2);
    g1.addEdge (0, 3);
    g1.addEdge (3, 4);
    g1.isTree () ? cout << "Graph is a Tree." << endl : cout << "Graph is not a Tree." << endl;

    Graph g2 (5);
    g2.addEdge (1, 0);
    g2.addEdge (0, 2);
    g2.addEdge (2, 1);
    g2.addEdge (0, 3);
    g2.addEdge (3, 4);
    g2.isTree () ? cout << "Graph is a Tree." << endl : cout << "Graph is not a Tree." << endl;
	
	return 0;
}

/* Time Complexity: O(V+E) */

#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	bool isCyclicUtil (int v, bool visited[], bool rs[]);
	public:
		Graph (int V);
		void addEdge (int u, int v);
		bool isCyclic ();
};

Graph::Graph (int V) {
	this->V = V;
	this->adj = new list<int>[V];
}

void Graph::addEdge (int u, int v) {
	adj[u].push_back(v);
}

bool Graph::isCyclicUtil (int v, bool visited[], bool rs[]) {
	if (!visited[v]) {
		visited[v] = true;
		rs[v] = true;
		list<int>::iterator i;
		for (i = adj[v].begin(); i != adj[v].end(); i++) {
			if ((!visited[*i]) && (isCyclicUtil(*i, visited, rs))) {
				return true;
			} else if (rs[*i]) {
				return true;
			}
		}
	}
	rs[v] = false;
	return false;
}

bool Graph::isCyclic () {
	bool *visited = new bool[V];
	bool *rs = new bool[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
		rs[i] = false;
	}
	for (int i = 0; i < V; i++) {
		if (isCyclicUtil (i, visited, rs)) {
			return true;
		}
	}
	return false;
}

int main (void) {
	Graph g (4);
	g.addEdge (0, 1);
	g.addEdge (0, 2);
    g.addEdge (1, 2);
    g.addEdge (2, 0);
    g.addEdge (2, 3);
    g.addEdge (3, 3);
    if (g.isCyclic ()) {
    	cout << "Graph contains a cycle." << endl;
    } else {
    	cout << "Graph does not contain a cycle." << endl;
    }
	return 0;
}

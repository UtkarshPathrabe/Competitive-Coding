#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	void APUtil (int u, bool visited[], int discovery[], int low[], int parent[], bool ap[]);
	public:
		Graph (int v);
		void addEdge (int u, int v);
		void AP ();
};

Graph::Graph (int v) {
	V = v;
	adj = new list<int>[v];
}

void Graph::addEdge (int u, int v) {
	adj[u].push_back(v);
	adj[v].push_back(u);
}

void Graph::APUtil (int u, bool visited[], int discovery[], int low[], int parent[], bool ap[]) {
	static int time = 0;
	int children = 0;
	visited[u] = true;
	discovery[u] = low[u] = ++time;
	list<int>::iterator i;
	for (i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[*i]) {
			children++;
			parent[*i] = u;
			APUtil (*i, visited, discovery, low, parent, ap);
			low[u] = min (low[u], low[*i]);
			if ((parent[u] == -1) && (children > 1)) {
				ap[u] = true;
			}
			if ((parent[u] != -1) && (low[*i] >= discovery[u])) {
				ap[u] = true;
			}
		} else if (*i != parent[u]) {
			low[u] = min (low[u], discovery[*i]);
		}
	}
}

void Graph::AP () {
	bool *visited = new bool[V];
	bool *ap = new bool[V];
	int *discovery = new int[V];
	int *low = new int[V];
	int *parent = new int[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
		ap[i] = false;
		parent[i] = -1;
		low[i] = -1;
		discovery[i] = -1;
	}
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			APUtil (i, visited, discovery, low, parent, ap);
		}
	}
	for (int i = 0; i < V; i++) {
		if (ap[i]) {
			cout << i << "\t";
		}
	}
	cout << endl;
}

int main (void) {
	cout << "Articulation points in first graph:" << endl;
    Graph g1(5);
    g1.addEdge(1, 0);
    g1.addEdge(0, 2);
    g1.addEdge(2, 1);
    g1.addEdge(0, 3);
    g1.addEdge(3, 4);
    g1.AP();
 
    cout << "Articulation points in second graph:" << endl;
    Graph g2(4);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.AP();
 
    cout << "Articulation points in third graph:" << endl;
    Graph g3(7);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 0);
    g3.addEdge(1, 3);
    g3.addEdge(1, 4);
    g3.addEdge(1, 6);
    g3.addEdge(3, 5);
    g3.addEdge(4, 5);
    g3.AP();
	return 0;
}

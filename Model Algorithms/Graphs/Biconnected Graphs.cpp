#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	bool isBCUtil (int u, bool visited[], int discovery[], int low[], int parent[]);
	public:
		Graph (int V);
		void addEdge (int u, int v);
		bool isBC ();
};

Graph::Graph (int V) {
	this->V = V;
	adj = new list<int>[V];
}

void Graph::addEdge (int u, int v) {
	adj[u].push_back (v);
	adj[v].push_back (u);
}

bool Graph::isBCUtil (int u, bool visited[], int discovery[], int low[], int parent[]) {
	static int time = 0;
	int children = 0;
	visited[u] = true;
	discovery[u] = low[u] = ++time;
	list<int>::iterator i;
	for (i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[*i]) {
			parent[*i] = u;
			children++;
			if (isBCUtil (*i, visited, discovery, low, parent)) {
				return true;
			}
			low[u] = min (low[u], low[*i]);
			if (parent[u] == -1 && children > 1) {
				return true;
			}
			if (parent[u] != -1 && low[*i] >= discovery[u]) {
				return true;
			}
		} else if (*i != parent[u]) {
			low[u] = min (low[u], discovery[*i]);
		}
	}
	return false;
}

bool Graph::isBC () {
	bool *visited = new bool[V];
	int *discovery = new int[V];
	int *low = new int[V];
	int *parent = new int[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
		discovery[i] = -1;
		low[i] = -1;
		parent[i] = -1;
	}
	if (isBCUtil (0, visited, discovery, low, parent)) {
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
	Graph g1 (2);
    g1.addEdge (0, 1);
    cout << "G1 is ";
    g1.isBC () ? cout << "Biconected Graph." << endl : cout << "Not a Biconected Graph." << endl;
    
    Graph g2 (5);
    g2.addEdge (1, 0);
    g2.addEdge (0, 2);
    g2.addEdge (2, 1);
    g2.addEdge (0, 3);
    g2.addEdge (3, 4);
    g2.addEdge (2, 4);
    cout << "G2 is ";
    g2.isBC () ? cout << "Biconected Graph." << endl : cout << "Not a Biconected Graph." << endl;
 
    Graph g3 (3);
    g3.addEdge (0, 1);
    g3.addEdge (1, 2);
    cout << "G3 is ";
    g3.isBC () ? cout << "Biconected Graph." << endl : cout << "Not a Biconected Graph." << endl;
 
    Graph g4 (5);
    g4.addEdge (1, 0);
    g4.addEdge (0, 2);
    g4.addEdge (2, 1);
    g4.addEdge (0, 3);
    g4.addEdge (3, 4);
    cout << "G4 is ";
    g4.isBC () ? cout << "Biconected Graph." << endl : cout << "Not a Biconected Graph." << endl;
 
    Graph g5 (3);
    g5.addEdge (0, 1);
    g5.addEdge (1, 2);
    g5.addEdge (2, 0);
    cout << "G5 is ";
    g5.isBC () ? cout << "Biconected Graph." << endl : cout << "Not a Biconected Graph." << endl;
    
	return 0;
}

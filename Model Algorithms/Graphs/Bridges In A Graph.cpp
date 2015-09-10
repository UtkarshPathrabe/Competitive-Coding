/* Time Complexity : O(V+E); Space Complexity: O(V) */

#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	void bridgeUtil (int u, bool visited[], int discovery[], int low[], int parent[], int* time);
	public:
		Graph (int V) {this->V = V; adj = new list<int>[V];}
		void addEdge (int u, int v) {adj[u].push_back(v); adj[v].push_back(u);}
		void bridge();
};

void Graph::bridgeUtil (int u, bool visited[], int discovery[], int low[], int parent[], int *time) {
	visited[u] = true;
	discovery[u] = low[u] = ++(*time);
	list<int>::iterator i;
	for (i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[*i]) {
			parent[*i] = u;
			bridgeUtil (*i, visited, discovery, low, parent, time);
			low[u] = min (low[u], low[*i]);
			if (low[*i] > discovery[u]) {
				cout << u << "---" << *i << endl;
			}
		} else if (*i != parent[u]) {
			low[u] = min (low[u], discovery[*i]);
		}
	}
}

void Graph::bridge () {
	bool *visited = new bool[V];
	int *discovery = new int[V];
	int *low = new int[V];
	int *parent = new int[V];
	int time = 0;
	for (int i = 0; i < V; i++) {
		visited[i] = false;
		discovery[i] = -1;
		low[i] = -1;
		parent[i] = -1;
	}
	cout << "Following are the bridges in the graph:" << endl;
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			bridgeUtil (i, visited, discovery, low, parent, &time);
		}
	}
}

int main (void) {
	cout << "\nBridges in first graph \n";
    Graph g1(5);
    g1.addEdge(1, 0);
    g1.addEdge(0, 2);
    g1.addEdge(2, 1);
    g1.addEdge(0, 3);
    g1.addEdge(3, 4);
    g1.bridge();
 
    cout << "\nBridges in second graph \n";
    Graph g2(4);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.bridge();
 
    cout << "\nBridges in third graph \n";
    Graph g3(7);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 0);
    g3.addEdge(1, 3);
    g3.addEdge(1, 4);
    g3.addEdge(1, 6);
    g3.addEdge(3, 5);
    g3.addEdge(4, 5);
    g3.bridge();
	return 0;
}

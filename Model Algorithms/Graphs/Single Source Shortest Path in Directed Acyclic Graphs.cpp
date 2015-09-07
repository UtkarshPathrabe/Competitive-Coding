/* Time Complexity: O(V + E) */

#include <bits/stdc++.h>

using namespace std;

class AdjListNode {
	int dest;
	int weight;
	public:
		AdjListNode (int dest, int weight) {this->dest = dest; this->weight = weight;}
		int getDest () {return dest;}
		int getWeight () {return weight;}
};

class Graph {
	int V;
	list<AdjListNode> *adj;
	void topologicalSortUtil (int u, bool visited[], stack<int> &Stack);
	public:
		Graph (int V);
		void addEdge (int u, int v, int weight);
		void shortestPath (int src);
};

Graph::Graph (int V) {
	this->V = V;
	adj = new list<AdjListNode>[V];
}

void Graph::addEdge (int u, int v, int weight) {
	AdjListNode node(v, weight);
	adj[u].push_back(node);
}

void Graph::topologicalSortUtil (int u, bool visited[], stack<int> &Stack) {
	visited[u] = true;
	list<AdjListNode>::iterator i;
	for (i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[i->getDest()]) {
			topologicalSortUtil (i->getDest(), visited, Stack);
		}
	}
	Stack.push(u);
}

void Graph::shortestPath (int src) {
	bool *visited = new bool[V];
	stack<int> Stack;
	int dist[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
		dist[i] = INT_MAX;
	}
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			topologicalSortUtil (i, visited, Stack);
		}
	}
	dist[src] = 0;
	while (!Stack.empty()) {
		int u = Stack.top();
		Stack.pop();
		if (dist[u] != INT_MAX) {
			for (list<AdjListNode>::iterator i = adj[u].begin(); i != adj[u].end(); i++) {
				if (dist[i->getDest()] > dist[u] + i->getWeight()) {
					dist[i->getDest()] = dist[u] + i->getWeight();
				}
			}
		}
	}
	cout << "Folowing are the shortest distances from source node " << src << ":" << endl;
	for (int i = 0; i < V; i++) {
		(dist[i] == INT_MAX) ? cout << i << "\t:\tINF" << endl : cout << i << "\t:\t" << dist[i] << endl;
	}
}

int main (void) {
	Graph g(6);
    g.addEdge(0, 1, 5);
    g.addEdge(0, 2, 3);
    g.addEdge(1, 3, 6);
    g.addEdge(1, 2, 2);
    g.addEdge(2, 4, 4);
    g.addEdge(2, 5, 2);
    g.addEdge(2, 3, 7);
    g.addEdge(3, 4, -1);
    g.addEdge(4, 5, -2);
    int s = 0;
    g.shortestPath(s);
	return 0;
}

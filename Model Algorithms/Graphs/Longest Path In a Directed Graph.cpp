/* Time Complexity: O(V+E) */

#include <bits/stdc++.h>

using namespace std;

class AdjListNode {
	int dest;
	int weight;
	public:
		AdjListNode (int _v, int _w) {dest = _v; weight = _w;}
		int getDest () {return dest;}
		int getWeight () {return weight;}
};

class Graph {
	int V;
	list<AdjListNode> *adj;
	void topologicalSortUtil (int v, bool visited[], stack<int> &Stack);
	public:
		Graph (int V);
		void addEdge (int u, int v, int weight);
		void longestPath (int s);
};

Graph::Graph(int V) {
	this->V = V;
	this->adj = new list<AdjListNode>[V];
}

void Graph::addEdge (int u, int v, int weight) {
	AdjListNode node (v, weight);
	adj[u].push_back (node);
}

void Graph::topologicalSortUtil (int v, bool visited[], stack<int> &Stack) {
	visited[v] = true;
	list<AdjListNode>::iterator i;
	for (i = adj[v].begin(); i != adj[v].end(); i++) {
		AdjListNode node = *i;
		if (!visited[node.getDest()]) {
			topologicalSortUtil (node.getDest(), visited, Stack);
		}
	}
	Stack.push(v);
}

void Graph::longestPath (int s) {
	stack<int> Stack;
	int dist[V];
	bool *visited = new bool[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
		dist[i] = INT_MIN;
	}
	for (int i = 0; i < V; i++) {
		if (!visited[i]) {
			topologicalSortUtil (i, visited, Stack);
		}
	}
	dist[s] = 0;
	while (!Stack.empty()) {
		int u = Stack.top();
		Stack.pop();
		list<AdjListNode>::iterator i;
		if (dist[u] != INT_MIN) {
			for (i = adj[u].begin(); i != adj[u].end(); i++) {
				if (dist[i->getDest()] < dist[u] + i->getWeight()) {
					dist[i->getDest()] = dist[u] + i->getWeight();
				}
			}
		}
	}
	for (int i = 0; i < V; i++) {
		(dist[i] == INT_MIN) ? cout << "INF\t" : cout << dist[i] << "\t";
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
    g.addEdge(3, 5, 1);
    g.addEdge(3, 4, -1);
    g.addEdge(4, 5, -2);
    int s = 0;
    cout << "Following are longest distances from source vertex " << s << ":" << endl;
    g.longestPath(s);
	return 0;
}

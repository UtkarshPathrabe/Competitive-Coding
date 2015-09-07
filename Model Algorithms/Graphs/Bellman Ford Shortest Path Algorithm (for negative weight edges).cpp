/* Time Complexity: O(V*E) */

#include <bits/stdc++.h>

using namespace std;

struct Edge {
	int src, dest, weight;
};

struct Graph {
	int V, E;
	struct Edge* edge;
};

struct Graph* createGraph (int V, int E) {
	struct Graph* graph = (struct Graph*) malloc (sizeof (struct Graph));
	graph->V = V;
	graph->E = E;
	graph->edge = (struct Edge*) malloc (sizeof (struct Edge) * E);
	return graph;
}

void BellmanFord (struct Graph* graph, int src) {
	int V = graph->V;
	int E = graph->E;
	struct Edge* edge = graph->edge;
	int dist[V];
	for (int i = 0; i < V; i++) {
		dist[i] = INT_MAX;
	}
	dist[src] = 0;
	for (int i = 1; i <= V-1; i++) {
		for (int j = 0; j < E; j++) {
			int u = edge[j].src;
			int v = edge[j].dest;
			int w = edge[j].weight;
			if ((dist[u] != INT_MAX) && (dist[u] + w < dist[v])) {
				dist[v] = dist[u] + w;
			}
		}
	}
	for (int j = 0; j < E; j++) {
		int u = edge[j].src;
		int v = edge[j].dest;
		int w = edge[j].weight;
		if ((dist[u] != INT_MAX) && (dist[u] + w < dist[v])) {
			cout << "Graph contains a negative weight cycle." << endl;
			return;
		}
	}
	cout << "Distance to following destinations from source node " << src << " are:" << endl;
	for (int i = 0; i < V; i++) {
		cout << i << "\t:\t" << dist[i] << endl;
	}
}

int main (void) {
    int V = 5;  // Number of vertices in graph
    int E = 8;  // Number of edges in graph
    struct Graph* graph = createGraph(V, E);
    // add edge 0-1
    graph->edge[0].src = 0;
    graph->edge[0].dest = 1;
    graph->edge[0].weight = -1;
    // add edge 0-2
    graph->edge[1].src = 0;
    graph->edge[1].dest = 2;
    graph->edge[1].weight = 4;
    // add edge 1-2
    graph->edge[2].src = 1;
    graph->edge[2].dest = 2;
    graph->edge[2].weight = 3;
    // add edge 1-3
    graph->edge[3].src = 1;
    graph->edge[3].dest = 3;
    graph->edge[3].weight = 2;
    // add edge 1-4
    graph->edge[4].src = 1;
    graph->edge[4].dest = 4;
    graph->edge[4].weight = 2;
    // add edge 3-2
    graph->edge[5].src = 3;
    graph->edge[5].dest = 2;
    graph->edge[5].weight = 5;
    // add edge 3-1
    graph->edge[6].src = 3;
    graph->edge[6].dest = 1;
    graph->edge[6].weight = 1;
    // add edge 4-3
    graph->edge[7].src = 4;
    graph->edge[7].dest = 3;
    graph->edge[7].weight = -3;
    BellmanFord(graph, 0);
	return 0;
}

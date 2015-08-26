#include <bits/stdc++.h>

using namespace std;

struct Edge {
	int src;
	int dest;
	int weight;
};

struct Graph {
	int V;
	int E;
	struct Edge *edge;
};

struct subset {
	int parent;
	int rank;
};

struct Graph *createGraph (int V, int E) {
	struct Graph * graph = (struct Graph*) malloc (sizeof (struct Graph));
	graph->V = V;
	graph->E = E;
	graph->edge = (struct Edge*) malloc (graph->E * sizeof(struct Edge));
	return graph;
}

int Find (struct subset sub[], int i) {
	if (sub[i].parent != i) {
		sub[i].parent = Find(sub, sub[i].parent);
	}
	return sub[i].parent;
}

void Union (struct subset sub[], int x, int y) {
	int xroot = Find (sub, x);
	int yroot = Find (sub, y);
	if (sub[xroot].rank < sub[yroot].rank) {
		sub[xroot].parent = yroot;
	} else if (sub[xroot].rank > sub[yroot].rank) {
		sub[yroot].parent = xroot;
	} else {
		sub[yroot].parent = xroot;
		sub[xroot].rank++;
	}
}

int myComp (const void* a, const void* b) {
	struct Edge* x = (struct Edge*)a;
	struct Edge* y = (struct Edge*)b;
	return x->weight > y->weight;
}

void KruskalMST (struct Graph *graph) {
	int V = graph->V;
	struct Edge result[V];
	int e = 0;
	int i = 0;
	qsort (graph->edge, graph->E, sizeof(graph->edge[0]), myComp);
	struct subset *sub = (struct subset*) malloc (V * sizeof(struct subset));
	for (int v = 0; v < V; v++) {
		sub[v].parent = v;
		sub[v].rank = 0;
	}
	while (e < V-1) {
		struct Edge next_edge = graph->edge[i++];
		int x = Find (sub, next_edge.src);
		int y = Find (sub, next_edge.dest);
		if (x != y) {
			result[e++] = next_edge;
			Union (sub, x, y);
		}
	}
	cout << "Following are the edges in the constructed MST:" << endl;
	cout << "Source\tDestination\tWeight" << endl;
	for (i = 0; i < e; i++) {
		cout << result[i].src << "\t" << result[i].dest << "\t\t" << result[i].weight << endl;
	}
}

int main () {
	int V = 4;
	int E = 5;
	struct Graph* graph = createGraph (V, E);
	graph->edge[0].src = 0;
	graph->edge[0].dest = 1;
	graph->edge[0].weight = 10;
	graph->edge[1].src = 0;
	graph->edge[1].dest = 2;
	graph->edge[1].weight = 6;
	graph->edge[2].src = 0;
	graph->edge[2].dest = 3;
	graph->edge[2].weight = 5;
	graph->edge[3].src = 1;
	graph->edge[3].dest = 3;
	graph->edge[3].weight = 15;
	graph->edge[4].src = 2;
	graph->edge[4].dest = 3;
	graph->edge[4].weight = 4;
	KruskalMST (graph);
	return 0;
}

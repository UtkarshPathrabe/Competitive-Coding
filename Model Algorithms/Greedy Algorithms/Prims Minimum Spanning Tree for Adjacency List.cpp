#include <bits/stdc++.h>

using namespace std;

struct AdjListNode {
	int dest;
	int weight;
	struct AdjListNode* next;
};

struct AdjList {
	struct AdjListNode* head;
};

struct Graph {
	int V;
	struct AdjList* array;
};

struct AdjListNode* newAdjListNode (int dest, int weight) {
	struct AdjListNode* newNode = (struct AdjListNode*) malloc (sizeof (struct AdjListNode));
	newNode->dest = dest;
	newNode->weight = weight;
	newNode->next = NULL;
	return newNode;
}

struct Graph* createGraph (int V) {
	struct Graph* temp = (struct Graph*) malloc (sizeof (struct Graph));
	temp->V = V;
	temp->array = (struct AdjList*) malloc (temp->V * sizeof (struct AdjList));
	for (int i = 0; i < V; i++) {
		temp->array[i].head = NULL;
	}
	return temp;
}

void addEdge (struct Graph* graph, int src, int dest, int weight) {
	struct AdjListNode* temp = newAdjListNode (dest, weight);
	temp->next = graph->array[src].head;
	graph->array[src].head = temp;
	temp = newAdjListNode (src, weight);
	temp->next = graph->array[dest].head;
	graph->array[dest].head = temp;
}

struct MinHeapNode {
	int v;
	int key;
};

struct MinHeap {
	int size;
	int capacity;
	int *pos;
	struct MinHeapNode **array;
};

struct MinHeapNode* newMinHeapNode (int v, int key) {
	struct MinHeapNode* temp = (struct MinHeapNode*) malloc (sizeof (struct MinHeapNode));
	temp->v = v;
	temp->key = key;
	return temp;
}

struct MinHeap* createMinHeap (int capacity) {
	struct MinHeap* temp = (struct MinHeap*) malloc (sizeof (struct MinHeap));
	temp->size = 0;
	temp->capacity = capacity;
	temp->pos = (int*) malloc (capacity * sizeof(int));
	temp->array = (struct MinHeapNode**) malloc (capacity * sizeof (struct MinHeapNode*));
	return temp;
}

void swapMinHeapNode (struct MinHeapNode** a, struct MinHeapNode** b) {
	struct MinHeapNode* t = *a;
	*a = *b;
	*b = t;
}

void minHeapify (struct MinHeap* minHeap, int index) {
	int smallest, left, right;
	smallest = index;
	left = 2 * index + 1;
	right = 2 * index + 2;
	if ((left < minHeap->size) && (minHeap->array[left]->key < minHeap->array[smallest]->key)) {
		smallest = left;
	}
	if ((right < minHeap->size) && (minHeap->array[right]->key < minHeap->array[smallest]->key)) {
		smallest = right;
	}
	if (smallest != index) {
		struct MinHeapNode* smallestNode = minHeap->array[smallest];
		struct MinHeapNode* indexNode = minHeap->array[index];
		minHeap->pos[smallestNode->v] = index;
		minHeap->pos[indexNode->v] = smallest;
		swapMinHeapNode (&minHeap->array[smallest], &minHeap->array[index]);
		minHeapify (minHeap, smallest);
	}
}

bool isEmpty (struct MinHeap* minHeap) {
	return minHeap->size == 0;
}

struct MinHeapNode* extractMin (struct MinHeap* minHeap) {
	if (isEmpty(minHeap)) {
		return NULL;
	}
	struct MinHeapNode* root = minHeap->array[0];
	struct MinHeapNode* lastNode = minHeap->array[--minHeap->size];
	minHeap->array[0] = lastNode;
	minHeap->pos[root->v] = minHeap->size;
	minHeap->pos[lastNode->v] = 0;
	minHeapify (minHeap, 0);
	return root;
}

void decreaseKey (struct MinHeap* minHeap, int v, int key) {
	int i = minHeap->pos[v];
	minHeap->array[i]->key = key;
	while ((i) && (minHeap->array[i]->key < minHeap->array[(i-1)/2]->key)) {
		minHeap->pos[minHeap->array[i]->v] = (i-1)/2;
		minHeap->pos[minHeap->array[(i-1)/2]->v] = i;
		swapMinHeapNode (&minHeap->array[i], &minHeap->array[(i-1)/2]);
		i = (i-1)/2;
	}
}

bool isInMinHeap (struct MinHeap *minHeap, int v) {
	return minHeap->pos[v] < minHeap->size;
}

void printArr (int arr[], int n) {
	for (int i = 1; i < n; i++) {
		cout << arr[i] << "\t-\t" << i << endl;
	}
}

void PrimMST (struct Graph* graph) {
	int V = graph->V;
	int parent[V];
	int key[V];
	struct MinHeap* minHeap = createMinHeap (V);
	for (int i = 1; i < V; i++) {
		parent[i] = -1;
		key[i] = INT_MAX;
		minHeap->pos[i] = i;
		minHeap->array[i] = newMinHeapNode (i, key[i]);
	}
	key[0] = 0;
	minHeap->array[0] = newMinHeapNode (0,key[0]);
	minHeap->pos[0] = 0;
	minHeap->size = V;
	while (!isEmpty(minHeap)) {
		struct MinHeapNode *minNode = extractMin (minHeap);
		int u = minNode->v;
		struct AdjListNode* crawl = graph->array[u].head;
		while (crawl != NULL) {
			int v = crawl->dest;
			if (isInMinHeap (minHeap, v) && crawl->weight < key[v]) {
				key[v] = crawl->weight;
				parent[v] = u;
				decreaseKey (minHeap, v, key[v]);
			}
			crawl = crawl->next;
		}
	}
	cout << "Source\t-\tDestination" << endl;
	printArr (parent, V);
}

int main (void) {
	int V = 9;
	struct Graph* graph = createGraph(V);
	addEdge(graph, 0, 1, 4);
	addEdge(graph, 0, 7, 8);
	addEdge(graph, 1, 2, 8);
	addEdge(graph, 1, 7, 11);
	addEdge(graph, 2, 3, 7);
	addEdge(graph, 2, 8, 2);
	addEdge(graph, 2, 5, 4);
	addEdge(graph, 3, 4, 9);
	addEdge(graph, 3, 5, 14);
	addEdge(graph, 4, 5, 10);
	addEdge(graph, 5, 6, 2);
	addEdge(graph, 6, 7, 1);
	addEdge(graph, 6, 8, 6);
	addEdge(graph, 7, 8, 7);
	PrimMST(graph);
	return 0;
}

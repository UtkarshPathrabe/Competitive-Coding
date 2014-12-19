/* Author: Utkarsh Pathrabe
*  Algorithm: Prims Minimum Spanning Tree for Adjacency List Representation Algorithm
*/

/* MST-PRIM(G, w, r):
*	1 for each u belonging to V[G]
*	2 		do	key[u] <- Infinity
*	3 			parent[u] <- NIL
*	4 key[r] <- 0
*	5 Q <- V[G]
*	6 while Q != Empty
*	7 		do u <- EXTRACT-MIN(Q)
*	8 			for each v belonging to Adj[u]
*	9 				do if v belonging to Q and w(u, v) < key[v]
*	10 					then parent[v] <- u
*	11 						key[v] <- w(u, v)
*/

/* Time Complexity: The time complexity of the below code/algorithm looks O(V^2) as there are two nested while loops. 
*  If we take a closer look, we can observe that the statements in inner loop are executed O(V+E) times(similar to BFS). 
*  The inner loop has HeapDecreaseKey() operation which takes O(log(V)) time. So overall time complexity is O(E+V)*O(log(V)) which is O((E+V)*log(V)) = O(E*log(V)).
*  (For a connected graph, V = O(E))
*/

#include <bits/stdc++.h>

using namespace std;

struct Edges {
	int to;
	int weight;
	int nextID;
};
typedef struct Edges edge;

struct HeapNodes {
	int vertex;
	int key;
};
typedef struct HeapNodes hnode;

vector <hnode> HeapNode;
vector <int> Node;
vector <edge> Edge;
vector <int> Key;
vector <int> Parent;
vector <hnode>::iterator it;

int V, HeapSize = 0;

int PARENT (int i) {
	return (ceil(i/2.0) - 1);
}

int Left (int i) {
	return ((2*i) + 1);
}

int Right (int i) {
	return ((2*i) + 2);
}

void Swap (hnode *i, hnode *j) {
	hnode temp = *i;
	*i = *j; 
	*j = temp;
}

int Length (vector<hnode> &A) {
	return A.size();
}

bool IsInMinHeap (vector<hnode> &A, int v) {
	for (it = A.begin(); it != A.end(); it++) {
		if ((it -> vertex) == v) {
			return true;
		}
	}
	return false;
}

void MinHeapify (vector<hnode> &A, int i) {							// Each call costs O(lg(n)) time
	int left = Left(i);
	int right = Right(i);
	int smallest;
	if ((left < HeapSize) && (A[left].key < A[i].key)) {
		smallest = left;
	} else {
		smallest = i;
	}
	if ((right < HeapSize) && (A[right].key < A[smallest].key)) {
		smallest = right;
	}
	if (smallest != i) {
		Swap (&A[i], &A[smallest]);
		MinHeapify (A, smallest);
	}
}

hnode HeapMinimum (vector<hnode> &A) {									// It takes O(lg(n)) time because we are calling MinHeapify otherwise, it takes O(1) time, if we don't call MinHeapify.
	MinHeapify(A, 0);
	return A[0];
}

hnode HeapExtractMinimum (vector<hnode> &A) {							// It takes O(lg(n)) time.
	if(HeapSize < 0) {
		printf("\t*****ERROR!!!*****\nHeap Underflow!");
	}
	hnode min = HeapMinimum(A);
	A[0].key = A[HeapSize - 1].key;
	A[0].vertex = A[HeapSize - 1].vertex;
	A.pop_back();
	MinHeapify(A, 0);
	HeapSize = Length(A);
	return min;
}

void HeapDecreaseKey (vector<hnode> &A, int i, int key) {				// Its Running time is O(n)	
	int j = 0;
	for (it = A.begin(); it != A.end(); it++) {
		if ((it -> vertex) != i) {
			j += 1;
		} else {
			break;
		}
	}
	if (key > A[j].key) {
		printf("\t*****ERROR!!!*****\nNew key is greater than the older key.");
	}
	A[j].key = key;
	while((j > 0) && ((A[j].key) < A[PARENT(j)].key)) {
		Swap(&A[j], &A[PARENT(j)]);
		j = PARENT(j);
	}
}

void Prim () {
	hnode n;
	Key[0] = 0;
	HeapNode[0].key = Key[0];
	while (Length(HeapNode) != 0) {
		n = HeapExtractMinimum (HeapNode);
		for (int ID = Node[n.vertex]; ID != -1; ID = Edge[ID].nextID) {
			if (IsInMinHeap (HeapNode, Edge[ID].to) && (Edge[ID].weight < Key[Edge[ID].to])) {
				Key[Edge[ID].to] = Edge[ID].weight;
				Parent[Edge[ID].to] = n.vertex;
				HeapDecreaseKey (HeapNode, Edge[ID].to, Key[Edge[ID].to]);
			}
		}
	}
	cout << "Prims MST for Adjacency List gives:" << endl; 
	for (int i = 1; i < V; i++) {
		cout << (Parent[i] + 1) << "\t" << (i + 1) << "\t" << Key[i] << endl;
	}
	cout << endl;
}

int main (void) {
	int from, to, ID, weight;
	edge e;
	hnode n;
	cout << "Enter the number of nodes in the graph:" << endl;
	cin >> V;
	for (int i = 0; i < V; i++) {
		n.vertex = i;
		n.key = INT_MAX;
		HeapNode.push_back(n);
		Node.push_back(-1);
		Key.push_back(INT_MAX);
		Parent.push_back(-1);
	}
	ID = 0;
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number <Space> Weight of Edge) in each line(Write '-1 -1 -1' if the list of edges is over):" << endl;
	cin >> from >> to >> weight;
	do{
		e.to = (to - 1);
		e.nextID = Node[from - 1];
		e.weight = weight;
		Edge.push_back(e);
		Node[from - 1] = ID;
		ID += 1;
		e.to = from - 1;
		e.nextID = Node[to - 1];
		e.weight = weight;
		Edge.push_back(e);
		Node[to - 1] = ID;
		ID += 1;
		cin >> from >> to >> weight;
	}while (from != -1);
	HeapSize = Length(HeapNode);
	Prim ();
	return 0;
}

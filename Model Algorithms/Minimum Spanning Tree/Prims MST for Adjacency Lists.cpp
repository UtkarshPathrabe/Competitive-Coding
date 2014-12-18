#include <bits/stdc++.h>

using namespace std;

struct Edges {
	int to;
	int weight;
	int nextID;
};
typedef struct Edges edge;

struct Nodes {
	int vertex;
	int key;
};
typedef struct Nodes node;

vector <node> Node;
vector <edge> Edge;
vector <int> Pos;
vector <int> Key;
vector <int> Parent;

int V, HeapSize = 0;

int Parent (int i) {
	return (ceil(i/2.0) - 1);
}

int Left (int i) {
	return ((2*i) + 1);
}

int Right (int i) {
	return ((2*i) + 2);
}

void Swap (node *i, node *j) {
	node* temp = *i;
	*i = *j; 
	*j = temp;
}

int Length (vector<node> &A) {
	return A.size();
}

void MinHeapify (vector<node> &A, int i) {}							// Each call costs O(lg(n)) tim
	int left = Left(i);
	int right = Right(i);
	int smallest;
	if((left <= (HeapSize - 1)) && (A[left] < A[i])){
		smallest = left;
	}else{
		smallest = i;
	}
	if((right <= (HeapSize - 1)) && (A[right] < A[smallest])){
		smallest = right;
	}
	if(smallest != i){
		Pos[i] = smallest;
		Pos[smallest] = i;
		Swap (&A[i], &A[smallest]);
		MinHeapify (A, smallest);
	}
}

void BuildMinHeap (vector<node> &A) {}								// Running time is O(n lg(n)) because each call to MinHeapify costs O(lg(n)) time, and there are O(n) such calls
																	// but it is not asymptotically tight. The tighter bound is O(n).
	for (int i = floor((HeapSize - 1) / 2); i >= 0; i--){
		MinHeapify (A, i);
	}
}

int HeapMinimum (vector<node> &A) {}									// It takes O(lg(n)) time because we are calling MinHeapify otherwise, it takes O(1) time, if we don't call MinHeapify
	MinHeapify(A, 0);
	return A[0];
}

int HeapExtractMinimum (vector<node> &A) {							// It takes O(lg(n)) time.
	if(HeapSize < 0) {
		printf("\t*****ERROR!!!*****\nHeap Underflow!");
	}
	int min = HeapMinimum(A);
	A[0] = A[HeapSize - 1];
	A.pop_back();
	MinHeapify(A, 0);
	HeapSize = Length(A);
	return min;
}

void HeapDecraseKey (vector<int> &A, int i, int key) {			// Its Running time is O(lg(n))
	if(key < A[i]) {
		printf("\t*****ERROR!!!*****\nNew key is smaller than the older key.");
	}
	A[i] = key;
	while(i > 0 && A[i] > A[Parent(i)]) {
		Pos[i] = Parent(i);
		Pos[Parent(i)] = i;
		Swap(&A[i], &A[Parent(i)]);
		i = Parent(i);
	}
}

int main (void) {
	int from, to, ID, weight;
	edge e;
	node nod;
	cout << "Enter the number of nodes in the graph:" << endl;
	cin >> V;
	for (int i = 0; i < V; i++) {
		nod.vertex = i;
		nod.key = INT_MAX;
		Node.push_back(nod);
		Pos.push_back(i);
		Key.push_back(INT_MAX);
		Parent.push_back(-1);
	}
	HeapSize = Length(Node);
	e.to = -1;
	e.nextID = -1;
	e.weight = INT_MAX;
	Edge.push_back(e);
	ID = 1;
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number <Space> Weight of Edge) in each line(Write '-1 -1 -1' if the list of edges is over):" << endl;
	cin >> from >> to >> weight;
	do{
		e.to = (to - 1);
		e.nextID = Node[from - 1].lastID;
		e.weight = weight;
		Edge.push_back(e);
		Node[from - 1].lastID = ID;
		ID += 1;
		e.to = from - 1;
		e.nextID = Node[to - 1].lastID;
		e.weight = weight;
		Edge.push_back(e);
		Node[to - 1].lastID = ID;
		ID += 1;
		cin >> from >> to >> weight;
	}while (from != -1);
	
	return 0;
}

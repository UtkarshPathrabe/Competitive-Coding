/* Author: Utkarsh Pathrabe
*  Algorithm: Strongly Connected Components
*/

/* Time complexity: Theta(V + E) */

#include <bits/stdc++.h>

using namespace std;

struct Edges{
	int to;
	int nextID;
};
typedef struct Edges edge;

struct Nodes{
	bool visited;
	int finish;
	int lastID;
};
typedef struct Nodes node;
	
vector <node> Node1;
vector <node> Node2;
vector <edge> Edge1;
vector <edge> Edge2;
list <int> Stack;

int n, m, timer;

void DFSUtility2 (int x) {
	Node2[x].visited = true;
	cout << x << "\t";
	for (int ID = Node2[x].lastID; ID != -1; ID = Edge2[ID].nextID) {
		if (!Node2[Edge2[ID].to].visited) {
			DFSUtility2 (Edge2[ID].to);
		}
	}
}

void DFS2 () {
	int i;
	Node2[0].visited = true;
	for (i = 1; i <= n; i++) {
		Node2[i].visited = false;
		Node2[i].finish = INT_MIN;
	}
	timer = 0;
	while (!Stack.empty()) {
		i = Stack.back();
		Stack.pop_back();
		if (!Node2[i].visited) {
			DFSUtility2 (i);
			cout << endl;
		}
	}
}

void DFSUtility1 (int x) {
	Node1[x].visited = true;
	++timer;
	for (int ID = Node1[x].lastID; ID != -1; ID = Edge1[ID].nextID) {
		if (!Node1[Edge1[ID].to].visited) {
			DFSUtility1 (Edge1[ID].to);
		}
	}
	Node1[x].finish = ++timer;
	Stack.push_back(x);
}

void DFS1 () {
	Node1[0].visited = true;
	for (int i = 1; i <= n; i++) {
		Node1[i].visited = false;
		Node1[i].finish = INT_MIN;
	}
	timer = 0;
	for (int i = 1; i <= n; i++) {
		if (!Node1[i].visited) {
			DFSUtility1 (i);
		}
	}
}

void SCC () {
	cout << "The Strongly Connected Components are:" << endl;
	DFS1();
	DFS2();
}

int main (void) {
	int from, to, ID;
	node nod;
	edge e;
	cout << "Enter number of nodes in the graph:" << endl;
	cin >> n;
	for (int i = 0; i <= n; i++) {
		nod.visited = false;
		nod.finish = INT_MIN;
		nod.lastID = -1;
		Node1.push_back(nod);
		Node2.push_back(nod);
	}
	e.to = -1;
	e.nextID = -1;
	Edge1.push_back(e);
	Edge2.push_back(e);
	ID = 1;
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number) in each line(Write '-1 -1' if the list of edges is over):" << endl;
	cin >> from >> to;
	do{
		e.to = to;
		e.nextID = Node1[from].lastID;
		Edge1.push_back(e);
		Node1[from].lastID = ID;
		e.to = from;
		e.nextID = Node2[to].lastID;
		Edge2.push_back(e);
		Node2[to].lastID = ID;
		ID += 1;
		cin >> from >> to;
	}while(from != -1);
	SCC();
	Node1.erase(Node1.begin(), Node1.end());
	Node2.erase(Node2.begin(), Node2.end());
	Edge1.erase(Edge1.begin(), Edge1.end());
	Edge2.erase(Edge2.begin(), Edge2.end());
	return 0;
}

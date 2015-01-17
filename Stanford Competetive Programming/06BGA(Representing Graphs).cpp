/* Author: Utkarsh Pathrabe
*  Algorithm: Representing Graphs as Adjacency Matrix and Adjacency List
*/

#include <bits/stdc++.h>

using namespace std;

struct edgeEntry{
	int to;
	int nextID;
};
typedef struct edgeEntry Edges;

int main(void) {
	int n, m, from, to;
	char c;
	cout << "Which type of graph you want to enter? (Type 'd' for directed graph and 'u' for undirected graph):" << endl;
	cin >> c;
	cout << "Enter the number of nodes and edges in the graph:" << endl;
	cin >> n >> m;
	int AdjMat[n + 1][n + 1];
	int Node[n + 1];
	Edges Edge[(2 * m) + 1];
	for (int i = 0; i < n + 1; i++) {
		Node[i] = -1;
		for (int j = 0; j < n + 1; j++) {
			AdjMat[i][j] = 0;
		}
	}
	cout << "Enter the " << m << " edges in the format(From Node Number <Space> To Node Number) in each line:" << endl;
	for (int i = 1; i < m + 1; i++) {
		cin >> from >> to;
		if (c == 'd') {
			AdjMat[from][to] = 1;
			Edge[i].to = to;
			Edge[i].nextID = Node[from];
			Node[from] = i;
		} else {
			AdjMat[from][to] = 1;
			AdjMat[to][from] = 1;
			Edge[i].to = to;
			Edge[i].nextID = Node[from];
			Node[from] = i;
			Edge[i + m].to = from;
			Edge[i + m].nextID = Node[to];
			Node[to] = i + m;
		}
	}
	cout << "The Adjacency Matrix is: " << endl;
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < n + 1; j++) {
			cout << AdjMat[i][j] << "\t";
		}
		cout << endl;
	}
	cout << "The Node entries are: " << endl;
	cout << "From\tLast Edge ID" << endl;
	for (int i = 1; i < n + 1; i++) {
		cout << i << "\t" << Node[i] << endl;
	}
	cout << "The Edge entries are: " << endl;
	cout << "ID\tTo\tNext Egde ID" << endl;
	if (c == 'd') {
		for (int i = 1; i < m + 1; i++) {
			cout << i << "\t" << Edge[i].to << "\t" << Edge[i].nextID << endl;
		}
	} else {
		for (int i = 1; i < (2 * m) + 1; i++) {
			cout << i << "\t" << Edge[i].to << "\t" << Edge[i].nextID << endl;
		}
	}
	cout << "Now, some queries:" << endl;
	do{
		cout << "Enter the Node number whose adjacent edges you want to know: " << endl;
		cin >> from;
		for (int ID = Node[from]; ID != -1; ID = Edge[ID].nextID) {
			cout << Edge[ID].to << "\t";
		}
		cout << endl;
		cout << "Want to query more nodes?(Write 'y' to query more)" << endl;
		cin >> c;
	}while(c == 'y');
	return 0;
}

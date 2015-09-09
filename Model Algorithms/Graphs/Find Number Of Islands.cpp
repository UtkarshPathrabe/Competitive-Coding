/* Time Complexity : O(Row * Col); Space Complexity: O(Row * Col) */

#include <bits/stdc++.h>

using namespace std;

bool isSafe (vector< vector<int> > &graph, vector< vector<bool> > &visited, int x, int y) {
	if ((x >= 0) && (x < graph.size()) && (y >= 0) && (y < graph[0].size()) && (!visited[x][y]) && (graph[x][y])) {
		return true;
	}
	return false;
}

void DFS (vector< vector<int> > &graph, vector< vector<bool> > &visited, int rowN[], int colN[], int x, int y) {
	visited[x][y] = true;
	for (int k = 0; k < 8; k++) {
		if (isSafe(graph, visited, x + rowN[k], y + colN[k])) {
			DFS (graph, visited, rowN, colN, x + rowN[k], y + colN[k]);
		}
	}
}

int countIslands (vector< vector<int> > &graph) {
	int count = 0;
	int row = graph.size();
	int col = graph[0].size();
	vector < vector<bool> > visited;
	for (int i = 0; i < row; i++) {
		vector<bool> temp;
		for (int j = 0; j < col; j++) {
			temp.push_back(false);
		}
		visited.push_back(temp);
		temp.erase(temp.begin(), temp.end());
	}
	int rowN[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
	int colN[8] = {0, 1, 1, 1, 0, -1, -1, -1};
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (!visited[i][j] && graph[i][j]) {
				DFS (graph, visited, rowN, colN, i, j);
				count++;
			}
		}
	}
	return count;
}

int main (void) {
	vector < vector<int> > graph;
	vector <int> temp;
	temp.push_back (1);
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (1);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	printf ("The Number of Islands is %d.\n", countIslands (graph));
	return 0;
}

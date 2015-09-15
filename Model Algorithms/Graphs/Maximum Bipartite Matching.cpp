#include <bits/stdc++.h>

using namespace std;

bool BPM (vector< vector<bool> > &bpGraph, int app, bool seenJob[], int matchAppJob[]) {
	int App = bpGraph.size();
	int Jobs = bpGraph[0].size();
	for (int job = 0; job < Jobs; job++) {
		if ((bpGraph[app][job]) && (!seenJob[job])) {
			seenJob[job] = true;
			if ((matchAppJob[job] < 0) || (BPM (bpGraph, matchAppJob[job], seenJob, matchAppJob))) {
				matchAppJob[job] = app;
				return true;
			}
		}
	}
	return false;
}

int maxBPM (vector< vector<bool> > &bpGraph) {
	int App = bpGraph.size();
	int Jobs = bpGraph[0].size();
	int matchAppJob[Jobs];
	memset (&matchAppJob, -1, sizeof (matchAppJob));
	int result = 0;
	for (int app = 0; app < App; app++) {
		bool seenJob[Jobs];
		memset (&seenJob, 0, sizeof (seenJob));
		if (BPM (bpGraph, app, seenJob, matchAppJob)) {
			result++;
		}
	}
	return result;
}

int main (void) {
	vector< vector<bool> > graph;
	vector<bool> temp;
	temp.push_back(0);
	temp.push_back(1);
	temp.push_back(1);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(1);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(1);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(1);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(1);
	temp.push_back(1);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(1);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	cout << "Maximum number of Applicants that can get Job is " << maxBPM(graph) << "." << endl;
	return 0;
}

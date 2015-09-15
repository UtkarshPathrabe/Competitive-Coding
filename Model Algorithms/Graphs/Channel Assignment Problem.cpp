#include <bits/stdc++.h>

using namespace std;

bool BPM (vector< vector<bool> > &bpGraph, int trans, bool seenReceiver[], int matchTransmitterReceiver[]) {
	int NoTransmitter = bpGraph.size();
	int NoReceiver = bpGraph[0].size();
	for (int rec = 0; rec < NoReceiver; rec++) {
		if ((bpGraph[trans][rec]) && (!seenReceiver[rec])) {
			seenReceiver[rec] = true;
			if ((matchTransmitterReceiver[rec] < 0) || (BPM (bpGraph, matchTransmitterReceiver[rec], seenReceiver, matchTransmitterReceiver))) {
				matchTransmitterReceiver[rec] = trans;
				return true;
			}
		}
	}
	return false;
}

void maxBPM (vector< vector<bool> > &bpGraph) {
	int NoTransmitter = bpGraph.size();
	int NoReceiver = bpGraph[0].size();
	int matchTransmitterReceiver[NoReceiver];
	memset (&matchTransmitterReceiver, -1, sizeof (matchTransmitterReceiver));
	int result = 0;
	for (int trans = 0; trans < NoTransmitter; trans++) {
		bool seenReceiver[NoReceiver];
		memset (&seenReceiver, 0, sizeof (seenReceiver));
		if (BPM (bpGraph, trans, seenReceiver, matchTransmitterReceiver)) {
			result++;
		}
	}
	cout << "The number of Maximum Packets sent in the Time Slot are " << result  << "." << endl;
	for (int x = 0; x < NoReceiver; x++) {
		if (matchTransmitterReceiver[x] != -1) {
			cout << "T" << matchTransmitterReceiver[x]+1 << "\t->\tR" << x+1 << endl;
		}
	}
}

int main (void) {
	vector< vector<bool> > graph;
	vector<bool> temp;
	temp.push_back(0);
	temp.push_back(2);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(3);
	temp.push_back(0);
	temp.push_back(1);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(2);
	temp.push_back(4);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	maxBPM (graph);
	return 0;
}

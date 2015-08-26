/*
* @Author: Utkarsh Pathrabe
* Problem Statement: You are given n activities with their start and finish times. 
*	Select the maximum number of activities that can be performed by a single person, 
*	assuming that a person can only work on a single activity at a time.
* Solution: The Greedy choice is to always pick the next activity whose finish time is least among the remaining activities 
*	and the start time is more than or equal to the finish time of previously selected activity.
*/

#include <bits/stdc++.h>

using namespace std;

struct sort_pred {
    bool operator () (const std::pair<int,int> &left, const std::pair<int,int> &right) {
		if(left.second < right.second)
			return true;
        if(left.second == right.second)
			return left.first < right.first;
        return false;
    }
};

void printMaxActivities (vector<pair <int, int> > &arr) {
	sort (arr.begin(), arr.end(), sort_pred());
	cout << "Following Activities are selected:" << endl << "Index After Sorting\tStart Time\tEnd Time" << endl;
	int i = 0;
	cout << "\t" << i << "\t\t" << arr[i].first << "\t\t" << arr[i].second << endl;
	for (int j = 1; j < arr.size(); j++) {
		if (arr[j].first >= arr[i].second) {
			cout << "\t" << j << "\t\t" << arr[j].first << "\t\t" << arr[j].second << endl;
			i = j;
		}
	}
}

int main (void) {
	vector <pair <int, int> > arr;
	arr.push_back(make_pair(5, 9));
	arr.push_back(make_pair(5, 7));
	arr.push_back(make_pair(8, 9));
	arr.push_back(make_pair(0, 6));
	arr.push_back(make_pair(3, 4));
	arr.push_back(make_pair(1, 2));
	printMaxActivities (arr);
	return 0;
}

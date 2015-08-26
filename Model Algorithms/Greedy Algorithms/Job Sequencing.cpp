//Time Complexity: O(n^2)

#include <bits/stdc++.h>

using namespace std;

struct Job {
	char id;
	int deadline;
	int profit;
};

bool comparator (Job a, Job b) {
	return (a.profit > b.profit);
}

void printJobScheduling (Job arr[], int n) {
	sort (arr, arr+n, comparator);
	int result[n];
	bool slot[n];
	for (int i = 0; i < n; i++) {
		slot[i] = false;
		result[i] = -1;
	}
	for (int i = 0; i < n; i++) {
		for (int j = min(n, arr[i].deadline) - 1; j >= 0; j--) {
			if (!slot[j]) {
				result[j] = i;
				slot[j] = true;
				break;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (slot[i]) {
			cout << arr[result[i]].id << "\t";
		}
	}
	cout << endl;
}

int main (void) {
	Job arr[5] = {{'a', 2, 100}, {'b', 1, 19}, {'c', 2, 27}, {'d', 1, 25}, {'e', 3, 15}};
	int n = sizeof(arr) / sizeof(arr[0]);
	cout << "Following is maximum profit sequence of jobs:" << endl;
	printJobScheduling (arr, n);
	return 0;
}

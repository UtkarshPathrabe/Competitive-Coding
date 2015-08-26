#include <bits/stdc++.h>

using namespace std;

int hasOnlyOneChild (int pre[], int size) {
	int min = 0, max = 0;
	if (pre[size-1] > pre[size-2]) {
		max = pre[size-1];
		min = pre[size-2];
	} else {
		max = pre[size-2];
		min = pre[size-1];
	}
	for (int i = size-3; i >= 0; i--) {
		if (pre[i] < min) {
			min = pre[i];
		} else if (pre[i] > max) {
			max = pre[i];
		} else {
			return 0;
		}
	}
	return 1;
}

int main (void) {
	int pre[] = {8, 3, 5, 7, 6};
	int size = sizeof(pre)/sizeof(pre[0]);
	if (hasOnlyOneChild(pre, size)) {
		printf("Yes\n");
	} else {
		printf("No\n");
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

struct Box {
	int h, w, d;
};

int compare (const void *a, const void *b) {
	return ((((Box*)b)->d * ((Box*)b)->w) - (((Box*)a)->d * ((Box*)a)->w));
}

int maxStackHeight (Box a[], int n) {
	Box array[3*n];
	int index = 0;
	for (int i = 0; i < n; i++) {
		array[index++] = a[i];
		array[index].h = a[i].w;
		array[index].d = max (a[i].h, a[i].d);
		array[index++].w = min (a[i].h, a[i].d);
		array[index].h = a[i].d;
		array[index].d = max (a[i].h, a[i].w);
		array[index++].w = min (a[i].h, a[i].w);
	}
	n = 3*n;
	qsort (array, n, sizeof (array[0]), compare);
	int msh[n];
	for (int i = 0; i < n; i++) {
		msh[i] = array[i].h;
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if ((array[i].w < array[j].w) && (array[i].d < array[j].d) && (msh[i] < msh[j] + array[i].h)) {
				msh[i] = msh[j] + array[i].h;
			}
		}
	}
	int m = msh[0];
	for (int i = 1; i < n; i++) {
		if (m < msh[i]) {
			m = msh[i];
		}
	}
	return m;
}

int main (void) {
	Box arr[] = { {4, 6, 7}, {1, 2, 3}, {4, 5, 6}, {10, 12, 32} };
	int n = sizeof (arr) / sizeof (arr[0]);
	cout << "The Maximum possible height of stack is " << maxStackHeight (arr, n);
	return 0;
}

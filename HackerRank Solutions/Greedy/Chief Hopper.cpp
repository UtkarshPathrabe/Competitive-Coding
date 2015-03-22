#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N, botEnergy = INT_MIN;
	cin >> N;
	int height[N];
	for (int i = 0; i < N; i++) {
		cin >> height[i];
		botEnergy = max (botEnergy, height[i]);
	}
	int low = 0, high = botEnergy, mid;
	while (high > low) {
		mid = (high + low) >> 1;
		double Energy = mid;
		for (int i = 0; i < N; i++) {
			if (height[i] > Energy) {
				Energy -= (height[i] - Energy);
			} else {
				Energy += (Energy - height[i]);
			}
			if (Energy < 0) {
				break;
			}
		}
		if (Energy < 0) {
			low = mid + 1;
		} else {
			high = mid;
		}
	}
	cout << low << endl;
	return 0;
}

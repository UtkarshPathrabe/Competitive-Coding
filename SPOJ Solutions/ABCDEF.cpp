#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int setSize;
	cin >> setSize;
	int *setContent = new int[setSize];
	for (int i = 0; i < setSize; i++)
		cin >> setContent[i];
		
	vector <int> set1, set2;
	for (int i = 0; i < setSize; i++)
		for (int j = 0; j < setSize; j++)
			for (int k = 0; k < setSize; k++)
				set1.push_back (setContent[i] * setContent[j] + setContent[k]);
	
	for (int i = 0; i < setSize; i++)
		for (int j = 0; j < setSize; j++)
			for (int k = 0; k < setSize; k++) {
				if (setContent[k] == 0)
					continue; 
				set2.push_back ((setContent[i] + setContent[j]) * setContent[k]);
			}
	
	sort (set1.begin(), set1.end());
	sort (set2.begin(), set2.end());
	int result = 0, low_bound = 0, up_bound = 0;
	for (int i = 0; i < set1.size(); i++){
		low_bound = lower_bound (set2.begin(), set2.end(), set1[i]) - set2.begin();
		up_bound = upper_bound (set2.begin(), set2.end(), set1[i]) - set2.begin();
		result += (up_bound - low_bound);
	}
	cout << result << endl;
	return 0;
}

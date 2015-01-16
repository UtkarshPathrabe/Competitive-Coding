#include <bits/stdc++.h>

using namespace std;

long long int MergeSort(vector<int> &v) {
    if (v.size() <= 1) {
        return 0;
    }
    long long ans = 0;
    int m = v.size() / 2;
    vector<int> v1(m), v2(v.size() - m);
    vector<int>::iterator it, it1, it2;
    copy(v.begin(), v.begin() + m, v1.begin());
    copy(v.begin() + m, v.end(), v2.begin());
    ans += MergeSort(v1);
    ans += MergeSort(v2);
    it = v.begin();
    it1 = v1.begin();
    it2 = v2.begin();
    while (it1 != v1.end() && it2 != v2.end()) {
        if (*it1 <= *it2) {
            *it++ = *it1++;
        } else {
            ans += v1.end() - it1;
            *it++ = *it2++;
        }
    }
    while (it1 != v1.end()) {
        *it++ = *it1++;
    }
    while (it2 != v2.end()) {
        *it++ = *it2++;
    }
    return ans;
}

int main (void) {
	int ArrSize, Test;
	cin >> Test;
	while (Test--) {
		cin >> ArrSize;
		vector <int> Arr;
		for (int i = 0; i < ArrSize; i++) {
			int temp;
			cin >> temp;
			Arr.push_back(temp);
		}
		cout << MergeSort(Arr) << endl;
		Arr.erase(Arr.begin(), Arr.end());
	}
	return 0;
}

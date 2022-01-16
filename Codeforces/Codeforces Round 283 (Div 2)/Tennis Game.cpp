/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/496/problem/D
*  Algorithms: Binary Search
*/

#include <bits/stdc++.h>

using namespace std;

vector <int> s1, s2;
vector < pair<int, int> > res;

int ans;

bool tty (int pos) {
    vector<int>::iterator st1 = s1.begin(), st2 = s2.begin(), fd1, fd2;
    int wf1 = pos, wf2 = pos;
    int a1 = 0, a2 = 0;
    bool la = false;
    while (true) {
		if ((fd1 == s1.end() - 1 && fd2 == s2.end()) || (fd2 == s2.end() - 1 && fd1 == s1.end())) {
			if (a1 == a2) {
				return false;
			}
			if (la ^ (a1 > a2)) {
				return false;
			}
			ans = max(a1, a2);
			return true;
	    }
	    fd1 = lower_bound(st1, s1.end(), wf1);
	    fd2 = lower_bound(st2, s2.end(), wf2);
		if (fd1 == s1.end() && fd2 == s2.end()) {
	        break;
	    }
	    if (fd1 - s1.begin() < fd2 - s2.begin()) {
	        a1++;
	        la = true;
	        st1 = fd1;
	        st2 = fd1-s1.begin()+s2.begin();
	    } else {
	        a2++;
	        la = false;
	        st2 = fd2;
	        st1 = fd2-s2.begin()+s1.begin();
		}
		wf1 = *st1+pos;
		wf2 = *st2+pos;
	}
	return false;
}

int main(void) {
    int n, te;
    cin >> n;
    s1.clear();
    s2.clear();
    res.clear();
    for (int i = 0; i < n; i++) {
        cin >> te;
        if (te == 1) {
            s1.push_back(1);
            s2.push_back(0);
        } else {
            s1.push_back(0);
            s2.push_back(1);
        }
    }
    for (int i = 1; i < n; i++) {
        s1[i] += s1[i-1];
        s2[i] += s2[i-1];
    }    
    for (int i = 1; i <= n; i++) {
        if (tty(i)) {
            res.push_back(make_pair(ans, i));
        }
    }
    sort(res.begin(), res.end());
    printf("%lu\n", res.size());
    for (int i = 0; i < res.size(); i++) {
        printf("%d %d\n", res[i].first, res[i].second);
    }
    return 0;
}

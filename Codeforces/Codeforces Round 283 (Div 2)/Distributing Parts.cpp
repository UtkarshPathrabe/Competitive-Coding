/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/496/problem/E
*  Algorithms: Greedy
*/

#include <bits/stdc++.h>

using namespace std;

struct Record{
	int type;												//0:parts 1:actors
    int id;
    int low;
    int high;
    int nums;
    Record() { 
		nums = 0; 
	}
    void DecreaseNums() {
		nums--; 
	}
    bool operator < (const Record &rec) const {       
        return (this->high < rec.high);
    }
};

Record all[200010];
multiset<Record> actors;
map <int, int> ans;

bool compare_Record (Record a, Record b){
    if (a.low == b.low)
        return a.type > b.type;
    else 
		return a.low < b.low;
}

int main (void){
    int idx = 0, n, m;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        all[idx].type = 0;
        all[idx].id = i+1;
        cin >> all[idx].low >> all[idx].high;       
        idx++;
    }
    cin >> m;
    for (int i = 0; i < m; ++i) {
        all[idx].type = 1;
        all[idx].id = i+1;
        cin >> all[idx].low >> all[idx].high >> all[idx].nums;
        idx++;
    }
    sort(all, all+idx, compare_Record);
    for (int i = 0; i < idx; ++i){
        Record cur = all[i];
        if (cur.type == 1){
            actors.insert(cur);
        } else {												//cur.type == 0
            if (actors.size() > 0) {
                set<Record>::iterator it = actors.lower_bound(cur);
                if (it != actors.end()){
                    const_cast<Record&>(*it).DecreaseNums();
                    ans[cur.id] = it->id;
                    if (it->nums == 0)
                        actors.erase(it++);
                }
            } else {
                cout << "NO" << endl;
                return 0;
            }
        }
    }
    if (ans.size() == n) {
        cout << "YES" << endl;
        for (int i = 1; i <= n; ++i)
            cout << ans[i] << " ";
    } else 
		cout << "NO" << endl;
    return 0;
}

#include <bits/stdc++.h>
#define maxn 100010

using namespace std;

int main (void) {
	int n, m, k;
	char s[maxn];
	int op, l, r, val;
	memset(s, '\0', sizeof(s));
	scanf("%d %d %d", &n, &m, &k);
	scanf("%s", &s);
	for(int i = 0; i < m + k; i++) {
		scanf("%d %d %d %d", &op, &l, &r, &val);
		--l;
		--r;
		if(op == 1)
			memset(s + l, val + '0', r - l + 1);
		else
			printf(!memcmp(s + l, s + l + val, r - l + 1 - val) ? "YES\n" : "NO\n");
	}
	return 0;
}
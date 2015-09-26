#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
 
struct node {
    long sum;
    long best;
    long left;
    long right;
};
 
int n;
long q[50003];
node tree[200003];
 
node makeNode(long sum, long best, long left, long right) {
    node tmp;
    tmp.sum = sum;
    tmp.best = best;
    tmp.left = left;
    tmp.right = right;
    return tmp;
}
 
node combine (node l, node r) {
    long left = l.left;
    if (l.sum + r.left>left) left =l.sum + r.left;
    long right = r.right;
    if (r.sum + l.right > right) right = r.sum + l.right;
    long best = max(l.right + r.left, max(l.best, r.best));
    return makeNode(l.sum+r.sum,best, left, right);
}
 
node build(int from, int to, int index) {
    if (from == to) {
        tree[index] = makeNode(q[from], q[from], q[from], q[from]);
        return tree[index];
    }
    int mid = (from+to)/2;
    node l = build(from,mid, (index<<1));
    node r = build(mid+1,to, (index<<1)+1);
 
    tree[index] = combine(l,r);
    return tree[index];
}
 
node ans(int index, int from, int to, int a, int b) {
    if (from == a && to == b) {
        return tree[index];
    }
    int mid = (from+to)/2;
    if (b <= mid) {
        return ans((index<<1), from, mid, a, b);
    }
    if (a > mid) {
        return ans((index<<1) + 1, mid+1,to,a,b);
    }
    node l = ans((index<<1), from, mid, a, mid);
    node r = ans((index<<1) + 1, mid+1,to,mid+1,b);
    return combine(l,r);
}
 
 
int main() {
    scanf("%d",&n);
    for (int i = 1; i <= n; ++i) 
		scanf("%ld",&q[i]);
    build(1,n,1);
    int t;
    scanf("%d",&t);
    int a,b;
    for (int i = 0; i < t; ++i) {
        scanf("%d%d",&a,&b);
        printf("%ld\n", ans(1,1,n,a,b).best);
    }
    return 0;
}

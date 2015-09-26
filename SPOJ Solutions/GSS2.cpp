#include <stdio.h>
#include <memory.h>
const int nmax = 100000, pmax = 18;

long long curmax[(1 << pmax) + 18], pasmax[(1 << pmax) + 18], tag[(1 << pmax) + 18], tagmax[(1 << pmax) + 18];
int n, m, l, r, M = 1, H = 0;
int i, nowpos, now;
int last[nmax + 18], num[nmax + 18];
long long ans[nmax + 18];

struct typequest
{
    int x, y, p;
}quest[nmax + 18];

int max (int a, int b)
{
    return a > b ? a : b;
}

void pushdown (int k)
{
    for (int i = H - 1, p; i; ++i)
    {
	p = k >> i;
	if ((tag[p << 1] += tag[p]) > tagmax[p << 1]) tagmax[p << 1] = tag[p << 1];
	if ((tag[(p << 1) + 1] += tag[p]) > tagmax[(p << 1) + 1]) tagmax[(p << 1) + 1] = tag[(p << 1) + 1];
	
    }
}
	
void inc (int l, int r, int t)
{
    for (l += M - 1, r += M + 1, pushdown (l), pushdown (r); l ^ r ^ 1; l >>= 1, r >>= 1)
    {
	if (~l & 1)
	{
	    //if ((tag[l ^ 1] += t) > tagmax[l ^ 1]) tagmax[l ^ 1] = tag[l ^ 1];
	    if ((curmax[l ^ 1] += t) > pasmax[l ^ 1]) pasmax[l ^ 1] = curmax[l ^ 1];
	    for (int i = (l ^ 1) >> 1; i; i >>= 1)
		if ((curmax[i] += t) > pasmax[i]) pasmax[i] = curmax[i];
	}
	if ( r & 1)
	{
	    //if ((tag[r ^ 1] += t) > tagmax[r ^ 1]) tagmax[r ^ 1] = tag[r ^ 1];
	    if ((curmax[r ^ 1] += t) > pasmax[r ^ 1]) pasmax[r ^ 1] = curmax[r ^ 1];
	    for (int i = (r ^ 1) >> 1; i; i >>= 1)
		if ((curmax[i] += t) > pasmax[i]) pasmax[i] = curmax[i];
	}
    }
}
		
long long query (int l, int r)
{
    long long ans = 0;
    for (l += M - 1, r += M + 1; l ^ r ^ 1; l >>= 1, r >>= 1)
    {
	if (~l & 1)
	{
	    subans = max (subans, max (smax[l ^ 1], lrans + lmax[l ^ 1]));
	    lrans = max (rmax[l ^ 1], lrans + sum[l ^ 1]);
        }
	if ( r & 1)
	{
	    subans = max (subans, max (smax[r ^ 1], rlans + rmax[r ^ 1]));
	    rlans = max (lmax[r ^ 1], rlans + sum[r ^ 1]);
        }
    }
    return max (subans, lrans + rlans);
}

int cmper (const void *i, const void *j)
{
    typequest *(typequest *) p, *(typequest *) q;
    return p->y - q->y;
}

int main ()
{
    freopen ("GSS2.in", "r", stdin);
    freopen ("GSS2.out", "w", stdout);
    scanf ("%d", &n);
    memset (curmax, 0xEF, sizeof (curmax));
    memset (pasmax, 0xEF, sizeof (pasmax));
    memset (tag, 0, sizeof (tag));
    memset (tagmax, 0xEF, sizeof (tagmax));
    while (M < n) M <<= 1, ++H;
    for (i = 1; i <= n; ++i)
	scanf ("%d", &num[i]);
    scanf ("%d", &m);
    for (i = 1; i <= m; ++i)
	scanf ("%d%d", &quest[i].x, &quest[i].y), quest[i].p = i;
    qsort (quest + 1, m, sizeof (quest[0]), cmper);
    for (i = 1; i <= m; ++i)
    {
	for (; nowpos <= quest[i].y; ++nowpos)
	    inc (last[num[nowpos] + nmax] + 1, nowpos, num[i]);
	ans[quest[i].p] = query (quest[i].x, quest[i].y);
    }
    for (i = 1; i <= m; ++i)
	printf ("%I64d\n", ans[i]);
    return 0;
}




/*    for (i = M - 1; i; --i)
    {
	lmax[i] = max (lmax[i << 1], sum[i << 1] + lmax[(i << 1) + 1]);
	rmax[i] = max (rmax[(i << 1) + 1], rmax[i << 1] + sum[(i << 1) + 1]);
	sum[i] = sum[i << 1] + sum[(i << 1) + 1];
	smax[i] = max (max (smax[i << 1], smax[(i << 1) + 1]), rmax[i << 1] + lmax[(i << 1) + 1]);
	}*/

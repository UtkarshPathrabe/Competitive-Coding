#include <cstdio>
#include <algorithm>
#define MAX 100000

using namespace std;

struct sum {
    long long int msum;
    long long int m;
};

int array[ MAX + 1 ];
sum tree[ 4 * MAX + 1 ];

void init( int node, int i, int j ) {
    if ( i == j ) {
        tree[ node ] = ( ( sum ) { array[ i ], array[ i ] } );
    }
    else {
        init( node * 2, i, ( i + j ) / 2 );
        init( node * 2 + 1, ( i + j ) / 2 + 1, j );
        sum left = tree[ node * 2 ], right = tree[ node * 2 + 1 ];
        tree[ node ].msum = max( left.msum, max( right.msum, left.m + right.m ) );
        tree[ node ].m = max( left.m, right.m );
    }
}

sum query( int node, int a, int b, int i, int j ) {
    if ( a > b || a > j || b < i ) {
        return ( ( sum ) { 0, 0 } );
    }
    if ( a >= i && b <= j ) {
        return tree[ node ];
    }
    sum left = query( node * 2, a, ( a + b ) / 2, i, j );
    sum right = query( node * 2 + 1, ( a + b ) / 2 + 1, b, i, j );
    return ( ( sum ) {
                max( left.msum, max( right.msum, left.m + right.m ) ),
                max( left.m, right.m ) } );
}

void update( int node, int a, int b, int pos, int val ) {
    if ( a == b && a == pos ) {
        tree[ node ] = ( ( sum ) { val, val } );
        return;
    }
    if ( pos <= ( a + b ) / 2 ) {
        update( node * 2, a, ( a + b ) / 2, pos, val );
    }
    if ( pos > ( a + b ) / 2 ) {
        update( node * 2 + 1, ( a + b ) / 2 + 1, b, pos, val );
    }
    sum left = tree[ node * 2 ], right = tree[ node * 2 + 1 ];
    tree[ node ].msum = max( left.msum, max( right.msum, left.m + right.m ) );
    tree[ node ].m = max( left.m, right.m );
}

int main() {
    int N, Q, l, r, i;
    char c;
    scanf( "%d", &N );
    for ( i = 0; i < N; ++i ) {
        scanf( "%d", array + i );
    }
    init( 1, 0, N - 1 );
    scanf( "%d", &Q );
    for ( i = 0; i < Q; ++i ) {
        scanf( "%*c%c%d%d", &c, &l, &r );
        if ( c == 'U' ) {
            update( 1, 0, N - 1, l - 1, r );
        }
        else {
            printf( "%lld\n", query( 1, 0, N - 1, l - 1, r - 1 ).msum );
        }
    }
    return 0;
}

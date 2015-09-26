#include <stdio.h>
#include <stdlib.h>

#define NDIGITS 10000                   /* maximum digits to compute */
#define LEN     ((NDIGITS/4+1)* 14)          /* array length */
long a[LEN];
long b;
long c = LEN;
long d;
long e = 0;
long f = 10000;
long g;
long h = 0;
int dot = 1;

int myprint(long val) {
  if (dot) {
    printf("%d.%03d", val/1000, val%1000);
    dot = 0;
    return 4;
  }
  else {
    return printf("%04d", val);
  }
}

main(){
  for(; b=c-=14 ; h=myprint(e+d/f))
    //printf("%04d",e+d/f) )
    for(e=d%=f;g=--b*2;d/=g)
      d=d*b+f*(h?a[b]:f/5),a[b]=d%--g;
}

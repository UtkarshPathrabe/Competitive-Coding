f(j){return j<2?2:f(j-1)*(4*j-2)/j;}l="%d\n";main(t,m){for(scanf(l,&t);t--;scanf(l,&m),printf(l,f(m)));return 0;}

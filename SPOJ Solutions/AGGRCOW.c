#include <stdio.h>

int arr[100001], n, c;

int f(int x){
	int cowsplaced=1, i;
	long long int lastpos=arr[0];
	for(i=1;i<n;i++){
		if(arr[i]-lastpos>=x){
			cowsplaced++;
			if(cowsplaced==c)
				return 1;
			lastpos=arr[i];
		}
	}
	return 0;
}

int binSearch(){
	int start=0, end=arr[n-1];
	while(start < end){
		int mid = (start + end) / 2;
		if(f(mid) == 1)
			start = mid + 1;
		else
			end = mid;
	}
	return start - 1;
}

void sort(int a[], int n){
	int i, j, temp;
	for(j=1;j<n;j++){
		temp = a[j];
		i = j - 1;
		while((i > -1) && (a[i] > temp)){
			a[i+1] = a[i];
			i--;
		}
		a[i+1] = temp;
	}
}

int main(){
	int t, i;
	scanf("%d", &t);
	while(t--){
		scanf("%d %d", &n, &c);
		for(i=0;i<n;i++)
			scanf("%d", &arr[i]);
		sort(arr, n);
		printf("%d\n", binSearch());
	}
	return 0;
}

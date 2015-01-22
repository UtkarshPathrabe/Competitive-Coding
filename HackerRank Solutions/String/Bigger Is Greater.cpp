#include <bits/stdc++.h>

using namespace std;

bool cal (char array[]) { 
	int length = strlen(array); 
    if (length == 0) { 
		cout<<"no answer\n";
		return false;
    }
    int i = length - 1;
    while (i > 0 && array[i - 1] >= array[i])
    	i--;
    if (i == 0) { 
		cout<<"no answer\n";
		return false;
    }
    size_t j = length - 1;    
    while (array[j] <= array[i - 1])
    	j--;
    int temp = array[i - 1];
    array[i - 1] = array[j];
    array[j] = temp;
    j = length - 1;   
    while (i < j) {
		temp = array[i];
		array[i] = array[j];
		array[j] = temp;
		i++;
		j--;
    }
	cout << array << "\n";
	return true;
}

int main() {
	long int T;
	cin >> T; 
	char *s;
	s = (char*) malloc (T*sizeof(char));
	for(int i = 0; i < T; i++) { 
		cin >> s;
    	cal (s);
	}
	return 0;
}

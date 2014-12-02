#include <unistd.h>
#include <stdio.h>

int main() {
	int i;
	for(i = 0; i < 5; i++) {
		fork();
		printf("Hello World!!!\n");
	}
	return 0;
}

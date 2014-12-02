#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>

void main() {
	int pfd[2];
	char buf[30];
	if (pipe(pfd) == -1){
		perror("\n Error in pipe creation \n");
		exit(1);
	}
	printf("\n writing to file descriptor %d\n", pfd[1]);
	write(pfd[1], "test", 5);
	printf("\n reading from file descriptor %d\n", pfd[0]);
	read(pfd[0], buf, 5);
	printf("read: %s \n", buf);
}

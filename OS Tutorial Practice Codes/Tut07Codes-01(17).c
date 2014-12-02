#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void signalHandler(int signum) {
	printf("Interrupt signal %d received.\n", signum);
	exit(signum);
}

int main(void) {
	signal(SIGINT, signalHandler);
	while(1) {
		printf("Going to sleep...\n");
		sleep(1);
	}
	return 0;
}

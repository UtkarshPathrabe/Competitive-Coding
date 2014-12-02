#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void alarmHandler(int signum) {
	printf("BITS Pilani!!!\n");
}

int main(void) {
	signal(14, alarmHandler);				//Set up alarm handler
	alarm(1);								//Schedule alarm for 1 second
	pause();								//Do not proceed until signal is handled
	return 0;
}

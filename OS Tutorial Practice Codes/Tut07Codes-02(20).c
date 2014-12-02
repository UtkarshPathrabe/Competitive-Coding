#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int alarmFlag = 0;

void alarmHandler() {							/* signal handler */
	printf("An ALARM clock signal was received\n");
	alarmFlag = 1;
}

int main() {
	signal(14, alarmHandler);					/* Install signal Handler */
	alarm(5);
	printf("Looping ...\n");
	while(!alarmFlag){
		pause();								/* wait for a signal */
	}
	printf("Loop ends due to alarm signal\n");
	return 0;
}

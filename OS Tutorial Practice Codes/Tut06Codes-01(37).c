#include <stdio.h>
#include <signal.h>

int main(void) {
	alarm(5);									/* schedule an alarm signal in 5 seconds */
	printf("Looping forever ...\n");
	while(1);
	printf("This line should never be executed.\n");
	return 0;
}

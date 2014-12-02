#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

const char * const path = "C:\\Users\\Utkarsh\\Desktop\\OS Codes\\Temp";

int main(void) {
	fprintf(stdout, "Changing directory to < %s >\n", path);
	if(chdir(path) == -1) {
		fprintf(stderr, "*****ERROR chdir failed :- %s.\n", strerror(errno));
	}else {
		fprintf(stdout, "chdir done!!!\nDirectory content of < %s >.\n", path);
		system("dir");
	}
	return 0;
}

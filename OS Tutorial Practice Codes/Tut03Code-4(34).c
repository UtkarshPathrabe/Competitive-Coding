#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>

#define PATH_MAX 255

int main(void) {
	char dirName[PATH_MAX + 1];
	if(getcwd(dirName, PATH_MAX) == NULL) {
		fprintf(stderr, "Could not obtain current working directory.\n");
		return 1;
	}else {
		fprintf(stdout, "Current working directory: < %s >\n", dirName);
	}
	return 0;
}

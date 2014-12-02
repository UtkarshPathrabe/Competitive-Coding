#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
	int md, rd;
	DIR *ds;
	struct dirent *dir;
	md = mkdir(argv[1]);
	if(md == 0) {
		fprintf(stdout, "%s directory is created.\n", argv[1]);
	}else {
		fprintf(stdout, "%s directory is not created.\n", argv[1]);
	}
	rd = rmdir(argv[2]);
	if(rd == 0) {
		fprintf(stdout, "%s directory is removed.\n", argv[2]);
	}else {
		fprintf(stdout, "%s directory is not revoved.\n", argv[2]);
	}
	return 0;
}

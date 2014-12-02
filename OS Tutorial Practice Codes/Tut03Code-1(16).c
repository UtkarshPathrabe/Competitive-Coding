#include <stdio.h>
#include <sys/stat.h>				/* defines S_IREAD & S_IWRITE*/
#include <sys/types.h>				/* defines types used by sys/stat.h*/

int main(void) {
	int fd = creat("DataFile.txt", S_IREAD | S_IWRITE);
	if(fd == -1) {
		fprintf(stderr, "Error in opening DataFile.txt.\n");
	}else{
		fprintf(stdout, "DataFile.txt opened for read/write access.\nDataFile.txt is currently empty.\n");
		close(fd);
	}
	return 0;
}

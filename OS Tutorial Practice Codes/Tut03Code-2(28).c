#include <stdio.h>
#include <sys/stat.h>				/* defines S_IREAD & S_IWRITE */
#include <sys/types.h>				/* defines types used by sys/stat.h*/
#include <fcntl.h>					/* defines options flags */

char message[] = "Hello World!!!";

int main(void) {
	char buffer[80];
	int fd = open("DataFile2.txt", O_RDWR | O_CREAT, S_IREAD | S_IWRITE);
	if(fd != -1) {
		fprintf(stdout, "\nDataFile2.txt opened for read/write access.\n");
		write(fd, message, sizeof(message));
		lseek(fd, 0, SEEK_SET);
		if(read(fd, buffer, sizeof(message)) == sizeof(message)) {
			fprintf(stdout, "\"%s\" was written to the DataFile2.txt.\n", buffer);
		}else {
			fprintf(stderr, "*****ERROR Reading DataFile2.txt.*****\n");
		}
		close(fd);
		return 0;
	}else {
		fprintf(stderr, "\n*****ERROR DataFile2.txt already exists.*****\n");
		return 1;
	}
}

#include <stdio.h>
#include <sys/stat.h>				/* defines S_IREAD & S_IWRITE */
#include <sys/types.h>				/* defines types used by sys/stat.h*/
#include <fcntl.h>					/* defines options flags */

int main() {
	int fd, fdNew;
	fd = open("DataFile3.txt", O_WRONLY | O_CREAT, S_IREAD | S_IWRITE);
	fprintf(stdout, "\nOriginal File Descriptor = %d\n", fd);
	if(fd == -1) {
		fprintf(stderr, "*****ERROR*****\n");
		return 1;
	}
	close(1);						/* close standard output */
	fdNew = dup(fd);
	printf("File Descriptor after dup() = %d.\n", fdNew);
	close(fd);
	printf("Hello World!!!\n");
	return 0;
}

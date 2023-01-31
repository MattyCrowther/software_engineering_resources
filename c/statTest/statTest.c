#include <stdio.h>
#include <sys/stat.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return -1;
    }

    char *fname = argv[1];
    struct stat statbuf;

    int status = stat(fname, &statbuf);

    if (!status)
        printf("\"%s\" is %lld bytes\n", fname, statbuf.st_size);
    else
        perror("stat error");

    return status;
}

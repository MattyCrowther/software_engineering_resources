/*
 * Replace the following string of 0s with your student number
 * 150444208
 */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
// you will probably need other system library header files included here

#include "filecmdrlib.h"

#define MODE_S_LEN  11
#define TIME_S_LEN  17

/*
 * is_user_exec helper function to test user execute permission for given
 * file mode and owner uid and gid.
 * Uses getuid() to get the uid of the calling process and getgid() to get the
 * gid of the calling process.
 * This function is not part of the filecmdrlib interface.
 */
bool is_user_exec(mode_t mode, uid_t ouid, gid_t ogid) {
    if (ouid == getuid())
        return mode & S_IXUSR;

    if (ogid == getgid())
        return mode & S_IXGRP;

    return mode & S_IXOTH;
}

/*
 * The following functions are defined in filecmdrlib.h and need to be
 * modified to comply with their definitions and the coursework specification.
 */

int execfile(char *path) {
    return 0;
}

int listdir(char *path) {
    return 0;
}

int listfile(char *path) { //Try this first
    return 0;
}

char *mode2str(mode_t mode, uid_t ouid, gid_t ogid) {
    char *mode_s = (char *) calloc(MODE_S_LEN, sizeof(char));

    return mode_s;
}

int printfinf(char *path) {
    printf("Print information about %s here\n", path);

    return FTYPE_OTH;
}

char *time2str(time_t time) { //or this
    static char *str_fmt = "%02d/%02d/%4d %02d:%02d";
    char *time_s = ""; // you need an appropriate string allocation here

    return time_s;
}

int useraction(int ftype, char *path) {
    static const char *action_prompt[] = {
        "Do you want to list the directory %s (y/n): ",
        "Do you want to execute %s (y/n): ",
        "Do you want to list the file %s (y/n): "
    };

    printf("Prompt for user action on %s type %d here\n", path, ftype);

    return 0;
}

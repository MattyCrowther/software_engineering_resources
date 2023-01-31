#include <stdio.h>
#include <string.h>

void rotate(void*, void*, void*);

int main(void) {
    char books[] = "WXYZABCDEFGHIJKLMNOPQRSTUV";

    printf("%s\n", books);
    // rotate(&books[0], &books[4], &books[26]);
    rotate(books, books + 4, books + 26);
    printf("%s\n", books);

    return 0;
}

void rotate(void *front, void *middle, void *end) {
    int frontsize = (char*)middle - (char*)front;
    int backsize = (char*)end - (char*)middle;
    char buffer[frontsize];

    memcpy(buffer, front, frontsize); //Source cannot overlap
    memmove(front, middle, backsize); //Source can overlap
    memcpy((char*)end - frontsize, buffer, frontsize);
}

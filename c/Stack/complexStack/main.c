typedef struct {
    void *elems;
    int elemsize;
    int loglength;
    int alloclength;
    void (*freefn)(void*);
} stack;

void stacknew(stack*, int, void(*)(void*));
void stackdispose(stack*);
void stackpush(stack*, void*);
void stackpop(stack*, void*);
void stringfree(void *);

#define _GNU_SOURCE // Enable strdup()
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define INITIAL_SIZE 4

int main(void) {
    int i;
    char *copy;
    const char *friends[] = { "Al", "Bob", "Carl" };
    stack s;

    stacknew(&s, sizeof(*friends), stringfree); /* sizeof(char*) */
    for(i = 0; i < 3; i++) {
        copy = strdup(friends[i]);
        stackpush(&s, &copy);
    }
    for(i = 0; i < 3; i++) {
        stackpop(&s, &copy);
        printf("%s\n", copy);
        free(copy);
    }
    stackdispose(&s);


    stacknew(&s, sizeof(*friends), stringfree);
    for(i = 0; i < 3; i++) {
        copy = strdup(friends[i]);
        stackpush(&s, &copy);
    }
    for(i = 0; i < 1; i++) {
        stackpop(&s, &copy);
        printf("%s\n", copy);
        free(copy);
    }
    stackdispose(&s);


    int x;
    stacknew(&s, sizeof(i), NULL);
    for(i = 0; i < 5; i++)
        stackpush(&s, &i);
    for(i = 0; i < 5; i++) {
        stackpop(&s, &x);
        printf("%d\n", x);
    }
    stackdispose(&s);

    return 0;
}

void stacknew(stack *s, int size, void(*freefn)(void*)) {
    assert(size > 0);
    s->elemsize = size;
    s->loglength = 0;
    s->alloclength = INITIAL_SIZE;
    s->elems = malloc(s->alloclength * s->elemsize);
    s->freefn = freefn;
    assert(s->elems != NULL);
}

void stackdispose(stack *s) {
    if(s->freefn != NULL) {
        for(int i = 0; i < s->loglength; i++) {
            s->freefn((char*)s->elems + i * s->elemsize);
        }
    }
    free(s->elems);
}

void stackpush(stack *s, void *i) {
    if(s->loglength == s->alloclength) {
        s->alloclength *= 2;
        s->elems = realloc(s->elems, s->alloclength * s->elemsize);
        assert(s->elems != NULL);
    }
    memcpy((char*)s->elems + s->loglength * s->elemsize, i, s->elemsize);
    s->loglength++;
}

void stackpop(stack *s, void *o) {
    assert(s->loglength > 0);
    s->loglength--;
    memcpy(o, (char*)s->elems + s->loglength * s->elemsize, s->elemsize);
}

void stringfree(void *elem) {
    free(*(char**)elem);
}

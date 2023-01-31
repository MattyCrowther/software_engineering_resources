#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define INITIAL_SIZE 4

typedef struct {
        void *elems;
        int elemsize;
        int loglength;
        int alloclength;
} stack;

void stacknew(stack*, int);
void stackdispose(stack*);
void stackpush(stack*, void*);
void stackpop(stack*, void*);

int main(void) {
        int i;
        int j;
        double x;
        double y;
        stack s;

        stacknew(&s, sizeof(i));
        for(i = 0; i < 10; i++)
                stackpush(&s, &i);
        while(s.loglength) {
                stackpop(&s, &j);
                printf("%d\n", j);
        }
        stackdispose(&s);

        stacknew(&s, sizeof(x));
        for(x = 0.2; x < 10; x++)
                stackpush(&s, &x);
        while(s.loglength) {
                stackpop(&s, &y);
                printf("%.2f\n", y);
        }
        stackdispose(&s);

        return 0;
}

void stacknew(stack *s, int size) {
        assert(size > 0);
        s->elemsize = size;
        s->loglength = 0;
        s->alloclength = INITIAL_SIZE;
        s->elems = malloc(s->alloclength * s->elemsize);
        assert(s->elems != NULL);
}

void stackdispose(stack *s) {
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

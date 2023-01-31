#ifndef STACK_H_INCLUDED
#define STACK_H_INCLUDED



#endif // STACK_H_INCLUDED

typedef struct {
    int *elems;
    int logLength;
    int allocLength;


}stack;

void stackNew(stack *s);
void stackDispose(stack *s);
void stackPush (stack *s,int value);
int stackPop(stack *s);

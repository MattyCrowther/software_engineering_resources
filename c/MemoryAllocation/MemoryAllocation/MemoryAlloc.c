#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct lifonode{
    void* data; /* basically data for list, void to hold any type. */
    struct lifonode *next; /*Pointer to next node. */

} LifoNode;

/*defines a type alias for our LIFO queue data structure */
typedef LifoNode *LifoQueue;

/* Instantiates a new empty LIFO queue*/
LifoQueue initLifoQueue(){

    LifoQueue queue = (LifoQueue)malloc(sizeof(LifoNode));
    queue -> next = NULL;
    return queue;

}

/* destroys (e.g. deallocates) an existing queue and its content*/
void destroyLifoQueue(LifoQueue queue){

    LifoNode* ptr = queue;
    while(ptr != NULL){
        queue = ptr -> next;
        free(ptr);
        ptr = queue;
    }


}

/* insert data into queue*/
bool insertLifo (LifoQueue queue,void *data){

    bool retval = false;
    if((data != NULL) && (queue !=NULL)){

            if(queue -> data !=NULL){
                queue -> data = data;
                queue -> next = NULL;
                retval= true;

            }else{
                LifoNode* newNode = (LifoNode*)malloc(sizeof(LifoNode));
                if(newNode != NULL){
                    newNode -> data = queue ->data;
                    newNode -> next = queue -> next;
                    queue ->data = data;
                    queue -> next = newNode;
                    retval = true;
                }

            }

    }
    return retval;

}

/*remove the next element from a queue*/
void* removeLifo(LifoQueue queue){

    void *dptr = NULL;
    if(queue != NULL){
        if(queue -> next != NULL){
            LifoNode* savePtr = queue -> next;
            dptr = queue ->data;
            queue -> data = queue ->next->data;
            queue ->next = queue ->next -> next;
            free(savePtr);

        }else {
            dptr = queue -> data;
            queue -> data = NULL;
            queue -> next = NULL;

        }

    }
    return dptr;


}

/*The info for queue (test) */

typedef struct mystuff{
    char*name;
    int val;
} MyStuff;

int main (void){

    LifoQueue myQueue = initLifoQueue();

    MyStuff fruit1 = {"Watermelon",1};
    MyStuff fruit2 = {"apple",2};
    MyStuff fruit3 = {"pear",3};


    insertLifo(myQueue,&fruit1);
    insertLifo(myQueue,&fruit2);
    insertLifo(myQueue,&fruit3);


    printf("Lifo queue has :\n ");
    MyStuff *ptr = removeLifo(myQueue);
    while(ptr !=NULL){
        printf("%s (%d) \n",ptr->name, ptr ->val);
        ptr = removeLifo(myQueue);
    }
    destroyLifoQueue(myQueue);

}



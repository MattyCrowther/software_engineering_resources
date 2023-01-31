#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
    printf("Hello world!\n");
    return 0;
}

void *lsearch (void *key,void *base,int n, int elemSize, int(cmpInt)(void*, void*)){

    for(int i = 0;i<n;i++){
        void *elemAddr = (char*)base + i*elemSize;
        if(cmpInt(key,elemAddr)==0){
            return elemAddr;
        }
    }
    return NULL;
}

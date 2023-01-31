#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>


// Pointer to what is trying to be found,Array in question,size of array,size in bytes of elems,Reference to compare function.
void *lsearch (void *key,void *base,int n, int elemSize, int(intcmp)(void*, void*)){
    for(int i = 0;i<n;i++){
        void *elemAddr = (char*)base + i*elemSize;
        if(intcmp(key,elemAddr)==0){
            return elemAddr;
        }
    }
    return NULL;
}

int intcmp(void* vp1, void* vp2){
    char *s1 = *(char**)vp1;
    char *s2 = *(char**)vp2;
    return strcmp(s1,s2);
}
int main()
{
    char *notes[]= {"Ab","F#","B","Gb","D"};
    char* favNote = "Eb";
    char** found = lsearch(&favNote,notes,5,sizeof(char*),strcmp);

}

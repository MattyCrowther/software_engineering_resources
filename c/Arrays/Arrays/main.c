#include <stdio.h>
#include <stdlib.h>

#define MAX 10
int main()
{
    int data [MAX];
    int i,j,tmp;
    FILE *fp;

    system ("cd");
    fp = fopen("input.txt", "r");
    if(fp == NULL){
        printf("File could not open. \n");
        perror("Error");
        return 0;
    }

    for(i=0;i<MAX;i++){
        //printf("Enter item #%d:",i);
        fscanf(fp,"%d",&data[i]);

    }
    fclose(fp);

    printf("You entered the following items: \n");
    for(i=0;i<MAX;i++){
        printf("item#%d: %d\n",i,data[i]);
    }
    for(i=0;i<MAX;i++){
        for(j=i;j<MAX;j++){
            if(data[i]>data[j]){
                tmp = data[i];
                data[i] = data[j];
                data[j]= tmp;
            }
        }
    }
    fp = fopen("output.txt","w");
    if(fp == NULL){
        printf("Could not write file. \n");
        perror("Error");
        return 0;
    }
    fprintf(fp,"\nSorted data\n");
    for(i=0;i<MAX;i++){
        fprintf(fp,"Item #%d : %d \n",i,data[i]);
    }
    fclose(fp);
    return 0;

}

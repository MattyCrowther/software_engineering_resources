#include "Switch.h"
#include <stdio.h>
#include <stdlib.h>

Switch::Switch()
{
        int i, numberOfNums = 0, total = 0,values;
    float average;

    printf("How many numbers are to be read?");
    scanf("%d",&numberOfNums);

    for(i=0;i<numberOfNums;i++){
        printf("Enter number %d : \n",i+1);
        scanf("%d",&values);
        total += values;
        printf("Read %d /n",values);
    }
    average = (float)total / (float) numberOfNums;
    printf("You read %d values. Average = %f. /n",numberOfNums,average);
}

Switch::~Switch()
{
    //dtor
}

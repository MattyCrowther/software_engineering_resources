#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, numberOfNums = 0, total = 0,values, valsRead;
    float average;

    printf("Enter values \n");
    valsRead = scanf("%d", &values);
    while(valsRead>0){
            if(values<0){
                valsRead = scanf("&d");
                continue;
            }
        numberOfNums++;
        total += values;
        printf("Read:   %d \n",values);
        valsRead = scanf("%d",&values);
    }
    average = (float)total / (float) numberOfNums;
    printf("You read %d values. Average = %f. /n",numberOfNums,average);
    return 0;

}

#include <stdio.h>
#include <stdlib.h>


 char f,m,l;
 int age;


int main()
{
    printf("Enter your initials then your age: ");
    scanf("%c %c %c %d", &f,&m,&l,&age);
    printf("Your initials are: %c%c%c and your age is %d. \n",f,m,l,age);
    return 0;
}

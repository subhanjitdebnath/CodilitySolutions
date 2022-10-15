/*
#include <stdio.h>

void main()
{
    char *filename="Data.txt";
    FILE *fp = fopen(filename,"a");

    if(fp == NULL)
    {
        printf("Error in opening");
    }
    fprintf(fp,"New Line 2");

    fclose(fp);
}
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
// Driver code
int main()
{
    FILE* ptr;
    char str[50], *subString;
    ptr = fopen("Data.txt", "a+");
    int a=0;
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 
    printf("content of this file are \n");
 
    while (fgets(str, 50, ptr) != NULL) {

        subString = strtok(str,"<");
        subString = strtok(NULL,">");
        a=atoi(subString);

        printf("%d\n",a);


        //printf("%s", str);
    }
 
    fclose(ptr);
    return 0;
}
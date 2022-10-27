#include<stdio.h>

typedef enum{
    FALSE  ,
    TRUE 
    } boolean;
void swap(int *a,int *b)
{
    int temp=0;
    temp=*a;
    *a=*b;
    *b=temp;
}

void BubbleSort(int a[],int len)
{
    boolean check;
    for(int i=0;i<len;i++)
    {
        check=FALSE;
        for(int j=1;j<len-i;j++)
        {
            if(a[j]<a[j-1])
            {
                swap(&a[j],&a[j-1]);
                check=TRUE;
            }
        }
        if(check==FALSE)
        {
            break;
        }
    }
}

void PrintArr(int a[],int len)
{
    int i=0;
    printf("\n Array={");
    while(i<len)
    {
        printf("%d",a[i]);
        if(i+1<len)
        {
            printf(", ");
        }
        i++;
    }
    printf("}");
}

void main()
{
    int Arr[]={32,12,45,10,8,92,56,74,25,66,72,77,89,40,35};
    int len=(sizeof(Arr)/sizeof(Arr[0]));
    printf("\n Before Sorting");
    PrintArr(Arr,len);
    BubbleSort(Arr,len);
    printf("\n After Sorting");
    PrintArr(Arr,len);

}
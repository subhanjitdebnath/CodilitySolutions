#include<stdio.h>

void swap(int *a, int *b)
{
    int temp=0;
    temp=*a;
    *a=*b;
    *b=temp;
}

void InserstionSort(int a[],int len)
{
    for(int i=0;i<len-1;i++)
    {
        for(int j=i+1;j>0;j--)
        {
            if(a[j]<a[j-1])
            {
                swap(&a[j],&a[j-1]);
            }
            else
                break;
        }
    }
}

void PrintArray(int a[],int len)
{
    printf("\n Array={");
    for(int i=0;i<len;i++)
    {
        printf("%d",a[i]);
        if(i+1<len)
        {
            printf(",");
        }
    }
    printf("}");
}

void main()
{
   int Array[]={32,12,45,10,8,92,56,74,25,66,72,77,89,40,35},len=0;
   len=(sizeof(Array)/sizeof(Array[0]));
   printf("\nBefore Sorting");
   PrintArray(Array,len);
   printf("\nAfter Sorting");
   InserstionSort(Array,len);
   PrintArray(Array,len);

}
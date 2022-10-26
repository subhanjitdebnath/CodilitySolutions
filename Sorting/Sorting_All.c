#include "Sorting_All.h"
#include<stdio.h>

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
void swap(int *a, int *b)
{
    int temp=0;
    temp=*a;
    *a=*b;
    *b=temp;
}
void BubbleSort(int a[],int len)
{
    int check=0;
    while(check==0)
    {
        check=1;
        for(int i=1;i<len-1;i++)
        {
            if(a[i]<a[i-1])
            {
                swap(&a[i],&a[i-1]);
                check=0;
            }
        }
    }

}
void SelectionSort(int a[],int len)
{
    int max=0,k=0;
    for(int i=0;i<len-1;i++)
    {
        max=a[0];
        k=0;
        for(int j=1;j<len-i;j++)
        {
            if(max<a[j])
            {
                max=a[j];
                k=j;
            }
        }
        swap(&a[len-i-1],&a[k]);
    }

}
void InsertionSort(int a[],int len)
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

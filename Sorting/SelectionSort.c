#include<stdio.h>

void SelectionSort(int a[], int len)
{
    int max=0,k=0,temp=0;
    for(int i=0;i<len;i++)
    {
        max=a[0];
        k=0;
        for(int j=1;j<len-i;j++)
        {
            if(max<a[j])          //If the max is less then we need to swap
            {
                max=a[j];
                k=j;
            }
        }
       a[k]=a[len-i-1];
       a[len-i-1]=max;
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
    int Arr[]={32, 12, 45, 10, 8, 92, 56, 74, 25, 66, 72, 77, 89, 40, 35},len=0;
    len=(sizeof(Arr)/sizeof(Arr[0]));
    printf("\n Before sorting");
    PrintArray(Arr,len);
    SelectionSort(Arr,len);
    printf("\n Afetr sorting");
    PrintArray(Arr,len);
}
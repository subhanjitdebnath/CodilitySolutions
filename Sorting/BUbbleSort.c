#include<stdio.h>

void BubbleSort(int a[],int len)
{
    int check=1,temp=0;
    while(check==1)
    {
        check=0;
        for(int i=1;i<len;i++)
        {
            if(a[i-1]>a[i])
            {
                temp=a[i-1];
                a[i-1]=a[i];
                a[i]=temp;
                check=1;
            }
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
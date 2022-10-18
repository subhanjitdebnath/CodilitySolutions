#include <stdio.h>
#include <stdlib.h>

void BinarySearch(int a[],int b,int low,int high)
{
   int mid=(high+low)/2;
   if(a[mid]==b)
   {
    printf("%d is in position %d",b,mid);
   }
   else
   {
    if(a[mid]>b)
    {
        BinarySearch(a,b,low,mid-1);
    }
    else
    {
        BinarySearch(a,b,mid+1,high);
    }
   }
}


void main()
{
    int a[]={22,29,38,56,74,85,89,92,96,104};
    int b=0;
    printf("Enter the value to search\n");
    scanf("%d",&b);
    BinarySearch(a,b,0,9);


}
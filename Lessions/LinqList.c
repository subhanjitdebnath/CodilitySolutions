#include<stdio.h>
#include<stdlib.h>

struct node{
    int key;
    int value;
    struct node *nxt;
};

void main()
{
    struct node *head=NULL,*second=NULL,*place=NULL;
    char check[2];
    int count=0;

    head = (struct node*)malloc(sizeof(struct node));
    head->key=0;
    head->value=0;
    head->nxt=NULL;
    place = head;
    printf("Do you want to add values? y/n   ");
    scanf("%s",&check);

    while(check[0]=='y')
    {
        count=place->key+1;
        place->nxt=(struct node*)malloc(sizeof(struct node));
        place=place->nxt;
        place->key=count;
        printf("Enter the value for key %d --- ",count);
        scanf("%d",&place->value);
        place->nxt=NULL;
        printf("Do you want to add values? y/n   ");
        scanf("%s",&check);
    }

    place = head;
    printf("Now printing the values");
    while(place!=NULL)
    {
        printf("\n %d",place->value);
        place=place->nxt;
    }

    
}
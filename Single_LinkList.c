
#include <stdio.h>
#include <stdlib.h>
/*Declearing the node for the Linq_List*/
struct node
{
    int key;
    int value;
    struct node* next;
};

/*Function to added the LinkList Elements*/
int Addelement(struct node* head)
{
    struct node *ptr , *new=NULL;
    ptr=head;
    int count=0;
    while(ptr->next!=NULL)
    {
        ptr=ptr->next;
        count++;
        if(count>100)
        {
            return 0;
            break;
        }
    }
    
    new=(struct node*)malloc(sizeof(struct node));
    printf("\n Enter the value to be entered \n");
    scanf("%d",&new->value);
    new->key=ptr->key+1;
    new->next=NULL;
    ptr->next=new;

    printf("\n Key = %d and Value = %d ",new->key,new->value);
    return 1;
}
/*Function to delete the Linklist Elements*/
int Delelement(struct node *head)
{
    struct node *ptr,*prev=NULL,*nxt=NULL;
    ptr=head;
    int Key=0,count=0;
    printf("\n Enter the key which you want to delete");
    scanf("%d",&Key);

    while(ptr->key!=Key)
    {
        prev=ptr;
        if(ptr->next==NULL)
        {
            printf("Key = %d not found",Key);
            return 0;
            break;
        }
        ptr=ptr->next;
        if(ptr->next!=NULL)
        {
            nxt=ptr->next;
        }
        else
        {
            nxt=NULL;
        }
        count++;
        if(count>100)
        {
            return 0;
            break;
        }
    }

    prev->next=nxt;

    ptr=head;
    Key=0;

    while(ptr!=NULL)
    {
        ptr->key=Key;
        ptr=ptr->next;
        Key++;
    }
    
    return 1;
        
}

void DelElement_Shtr(struct node *head,int key)
{
    struct node *ptr,*prev=NULL,*nxt=NULL;
    ptr=head;

    while(ptr->key!=key)
    {
        prev=ptr;
        ptr=ptr->next;
        if(ptr->next!=NULL)
        {
            nxt=ptr->next;
        }
    }
    prev->next=nxt;

    ptr=head;
    key=0;
    while(ptr!=NULL)
    {
        ptr->key=key;
        ptr=ptr->next;
        key++;
    }

}

/*Sort the Link List*/



/*Function to print the Linklist Elements*/
void Printelement(struct node *head)
{
    struct node *ptr;
    ptr=head;
    int count=0;
    while(ptr!=NULL)
    {
        if(ptr->key!=0)
        {
            printf("\n Key= %d   Value = %d",ptr->key,ptr->value);
        }
        ptr=ptr->next;
        count++;
        if(count>100)
        {
            return 0;
            break;
        }
    }
}
/*Function to insert a element in Linklist*/
void InsertElement(struct node *head)
{
    struct node *ptr ,*prev,*new;
    ptr=head;
    prev=head;
    int count=0,Key=0;
    while(count==0)
    {
        printf("\n Enter the position where you want to enter --");
        scanf("%d",&Key);
        ptr=head;

        while(ptr!=NULL)
        {
            printf("ptr->Key = %d",ptr->key);
            if(ptr->key==Key)
            {
                count=1;
                break;
            }
            prev=ptr;
            ptr=ptr->next;
        }

        if(count==1)
        {
            break;
        }
        else
        {
            printf("\n Pos= %d Wrong Position Entered",Key);
        }

    }
    
    new=(struct node*)malloc(sizeof(struct node));
    new->key=Key;

    printf("\n Enter the value for position = %d --",Key);
    scanf("%d",&new->value);
    
    prev->next=new;
    new->next=ptr;

    ptr=head;
    Key=0;

    while(ptr!=NULL)
    {
        ptr->key=Key;
        ptr=ptr->next;
        Key++;
    }

    Printelement(head);

}
/*Function to remove dublicate from Linklist*/
void RemoveDublicate(struct node *head)
{
    struct node *ptr,*dub,*chk;
    ptr=head;

    while(ptr!=NULL)
    {
        dub=ptr;
        ptr=ptr->next;
        chk=ptr;
        while(chk!=NULL)
        {
            if(dub->value==chk->value)
            {
                DelElement_Shtr(head,chk->key);
                ptr=head;
                break;
            }
            chk=chk->next;
        }

    }
    Printelement(head);
}

void main()
{
    struct node* head = NULL ;
    struct node *second= NULL;
    int check=1,valid=0;

    head=(struct node*)malloc(sizeof(struct node));
    head->key=0;
    head->value=0;
    head->next=NULL;
    

    while(check==1 || check==2 || check==3|| check==4 || check==5)
    {
        printf("\n \n -------------------------------\n");
        printf("\n Commands for the LinqlistManupulation");
        printf("\n Add - 1");
        printf("\n Print - 2");
        printf("\n Delete - 3");
        printf("\n Insert - 4");
        printf("\n Remove Dublicate - 5");
        printf("\n Sort - 6");
        printf("\n Exit - 7 ");
        printf("\n Enter Value ");
        scanf("%d",&check);

        switch(check)
        {
            case 1:
            valid=Addelement(head);
            if(valid==1)
            {
                printf("\n Element added successfully");
            }
            else{
                printf("\n Element added unsuccessfull");
            }
            break;

            case 2:
            Printelement(head);
            break;

            case 3:
            valid=Delelement(head);
            if(valid==1)
            {
                printf("\n Element deleted successfully");
            }
            else{
                printf("\n Element delete unsuccessfull");
            }
            break;

            case 4:
            InsertElement(head);
            break;
            case 5:
            RemoveDublicate(head);
            break;

            default:
            break;

        }

    }
   
}
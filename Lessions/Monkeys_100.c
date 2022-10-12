
int main()
{
    int doors[102];
    
    /* Assign all the elements with 0 values as doors will be closed*/
    for(int i=1;i<=100;i++)
    {
        doors[i]=0;
    }

    /*Now the main calculation part has started*/
    for(int i=1;i<=100;i++)
    {
        int a=0;
        for(int j=1;j<=100;j++)
        {
            a=i*j;
            if(a<=100)
            {
                doors[a]= doors[a]==0 ? 1:0;               //Checking the doors value for each iteration
            }
        }
    }

    for(int i=1;i<=100;i++)
    {
        if(doors[i]==1)
        {
            printf("\n %d",i);
        }
    }
    return 0;
}
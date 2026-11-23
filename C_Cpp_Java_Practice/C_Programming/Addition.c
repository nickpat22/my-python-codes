#include<stdio.h>

int addition(int Value1, int Value2)
{
    int Result = Value1 + Value2; 

    return Result;
}

int main()
{   
    int No1 = 0, No2 = 0, And = 0;

    printf("Enter First number : \n");
    scanf("%d", &No1);
    printf("Enter Second number : \n");
    scanf("%d", &No2);

    int Ans = addition(No1,No2);

    printf("Addition is : %d ", Ans);


    return 0;
}
# include<stdio.h>

int main()
{
    char ch = 'A';
    int no = 11;
    float Marks = 90.78f;
    double d = 90.56789;

    printf("%d\n",sizeof(ch));
    printf("%d\n",sizeof(no));
    printf("%d\n",sizeof(Marks));
    printf("%d\n",sizeof(d));

    return 0;
}
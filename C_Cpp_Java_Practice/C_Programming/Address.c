#include<stdio.h>

int main()
{
    int no = 21;
    printf("%d\n",no);
    printf("%d\n",sizeof(no));
    printf("%d\n",&no);

    return 0;
}

//gcc Ganesh.c -o Myexe
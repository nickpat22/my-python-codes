#include<stdio.h>

int main()
{ 
    char ch = 'A';
    int i = 11;
    float no = 3.14f;
    double d = 90.353835; 

    printf("%d\n",sizeof(ch));
    printf("%d\n",sizeof(i));
    printf("%d\n",sizeof(no));
    printf("%d\n",sizeof(d));

    return 0;
}

//gcc Ganesh.c -o Myexe
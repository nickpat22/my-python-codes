#include<stdio.h>
#pragma pack(1)     // 1, 2 , 4 , 8. (We can write these nos in bracket[multiple of 2])

struct Demo
{   
    int no;
    float f;
    int *p;
};

int main()
{
    int x =11;

    struct Demo dobj;

    dobj.no = 21;
    dobj.f = 90.99f;
    dobj.p =&x;

    printf("%d\n",*(dobj.p));
    


    return 0;
}
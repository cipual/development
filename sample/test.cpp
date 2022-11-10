#include<stdio.h>
#include<math.h>
void main()
{
    int num,i,a,N,b;
    scanf("%d",&num);
    N=num;
    //判断输入数字的位数
    for(i=1;1;i++)
    {    
        num=num/10;
        if(num==0)
        break;
    }

    for(int n=i-1;n>=1;n--)
    {
        a=N/((int)pow(10.0,n));
        N=N%((int)pow(10.0,n));
        switch(a)
        {
            case 0: printf("zero,");break;
            case 1: printf("one,");break;
            case 2: printf("two,");break;
            case 3: printf("three,");break;
            case 4:printf("four,");break;
            case 5: printf("five,");break;
            case 6: printf("six,");break;
            case 7: printf("seven,");break;
            case 8: printf("eight,");break;
            case 9: printf("nine,");
        }
    }
    a=N/((int)pow(10.0,0));
    switch(a)
        {
            case 0: printf("zero");break;
            case 1: printf("one");break;
            case 2: printf("two");break;
            case 3: printf("three");break;
            case 4:printf("four");break;
            case 5: printf("five");break;
            case 6: printf("six");break;
            case 7: printf("seven");break;
            case 8: printf("eight");break;
            case 9: printf("nine");
        }
}


// #include <stdio.h>
// #include <conio.h>

// int main()
// {

//     printf("Hello world");
//     return 0;
// }
// FIRST PROGRAM

// #include <stdio.h>
// #include <conio.h>
// void main()
// {
//     int principal,time,rate,SI;
//     clrscr();
//     printf("enter the value of principle:");
//     scanf("%d",&principal);
//     printf("enter the value of time :");
//     scanf("%d",&time);
//     printf("enter the valu of rate of interest :");
//     scanf("%d",&rate);

//     SI=(principal*rate*time)/100;
//     printf("The Simple interest is",SI);
// }

// SECOND PROGRAM

// #include<stdio.h>
// #include<conio.h>

// void main()
// {
//     float far,cent;
//     printf("enter the temperature in farhenhite");
//     scanf("%f",&far);
//     cent=5.0/9*(far-32);
//     printf("the temperature in celcius is =%d",cent);
//     getch();

// }

// THIRD PROGRAM
#include <stdio.h>
#include <conio.h>

void main()
{
    int num, sum = 0, A, B;
    printf("enter four digit number to be calculated =");
    scanf("%d", &num);
    A = num / 1000;
    B = num % 10;
    sum = A + B;
    printf("the sum of the first and last digit of the entered number is= %d", sum);
    getch();
}
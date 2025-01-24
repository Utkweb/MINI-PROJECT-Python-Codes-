// class harish{
//     public static void main(String args[]){

//         int marks = 86;

//         if (marks >= 90){
//             System.out.println("Grade A");
//         }
//         else if(marks >= 80){
//             System.out.println("Grade B");
//         }
//         else if(marks >= 70){
//             System.out.println("Grade C");
//         }
//         else{
//             System.out.println("Satisfactory");
//         }
//     }
// }

// Switch case  : 

// 90 > : grade A
// 80 > : grade B
// 70 > : grade C

// conditional statements 

// if statements - it check one condition at a time 
// if-else statements -  it checks two condition at a time
// if-else if else statements - it checks multiple condition at a time 

// class harish{
//     public static void main(String[] args) {
//         int num = 8;
//         int num1 = 9;

//         System.out.println("Choose an operation to perform :");
//         System.out.println("1. Addition");
//         System.out.println("2. Subtraction");
//         System.out.println("3. Multiplication");
//         System.out.println("4. Division");

// switch(2){
//     case 1: 
//     System.out.println(num+num1);
//     break;
//     case 2: 
//     System.out.println(num-num1);
//     break;
//     case 3: 
//     System.out.println(num*num1);
//     break;
//     case 4: 
//     System.out.println(num/num1);
//     break;

// }
//         if (input == 1){
//             System.out.println(num+num1);

//         }
//     }
// }

// 1. for loop - 

// for(int i =0;i<11;i++){
//     System.out.println(i);
// }

// 0 2 4 6 8 10 12 14 16 18 20
// 1 3 5 7 9 11 13 15 17 19 21
// 10 9 8 7 6 5 4 3 2 1 

// i = 4
// System.out.println(++i);    //5
// System.out.println(i++);    //5
// System.out.println(i);     //6

// i++ = post increment operator = first we use the value then increment the value 
// ++i = pre increment operator
// 2. while loop
// 3. do-while loop

// 0 1 1 2 3 5 8 13 21 34 ...... = fibonacci series 

// class harish{
//     public static void main(String args[]){
//         int first_number = 0,second_number = 1;
//         for(int i =1;i<=10;i++){
//             System.out.print(first_number+ " ");

//             int result = first_number+second_number;   //result = 1
//             first_number = second_number;    //first_number = 1
//             second_number = result;    //second_number = 1

//         }
//     }
// }

// 0 1 1 2 3     ......

// a = 0
// b = 1

// a = b
// a = 1

// 0

// int a = 9;
// int b = 10;

// int a = 9,b = 10;

// 8 x 1 = 8
// 8 x 2 = 16 

// 8 x 10 = 80

// class hairsh {
//     public static void main(String[] args) {
//         int times = 8;
//         System.out.println("Mulitplication Table of "+times);
//         for (int i = 1; i <= 10; i++) {
//             System.out.println(times + " x " + i + " = " + times * i);
//         }
//     }
// }

// while (conditions){
//     Statements
// }

// class harish{
//     public static void main(String args[]){
//         int i = 1;
//         while(i <= 5){
//             System.out.print(i+" ");
//             i++;
//         }
//     }
// }

// 1 4 9 16 25 36 49 64 81 100 - Done

// Input :  451 
// 451%10 = 1*10 = 10 + 5 = 15 * 10 = 150 +4 = 154
// 45%10 = 5
// 4%10 = 4

// class harish{
//     public static void main(String[] args) {
//         int num = 782;
//         int sum = 0;
//         while(num > 0){

//             int remainder = num % 10;    //remainder = 7
//             sum = sum*10 + remainder;    // sum = 287
//             num = num / 10;              // num = 7
//         }

//         System.out.println("The reverse of the number would be : "+sum);

//     }
// } 

// Output : 154

// sum of digits :
// num = 123 = 1+2+3 = 6
// 
// result = 6

// class harish{
//     public static void main(String args[]){

//         // Automatic conversion/implicit conversion
//         // int a = 9;
//         // double b = a;    //automatic conversion
//         // System.out.println(a);
//         // System.out.println(b);

//         // manual conversion/explicit conversion

//         // double a = 9;
//         // float b = (float) a;    
//         // System.out.println(a);
//         // System.out.println(b);

//         // break/continue

//         // for(int i=0;i<=9;i++){
//         //     if(i==4){
//         //         continue;
//         //     }
//         //     System.out.println(i);
//         // }

//         // int i = 0;
//         // while(i<10){
//         //     System.out.println(i);

//         //     if(i==7){
//         //         break;
//         //     }
//         //     i++;
//         // }

//         // Nested Loops: 

//         // for(int i =0;i<=6;i++){  //outer loop 
//         //     for(int j = 0;j<6;j++){   //inner loop

//         //     }
//         // }

//     }
// }

// class harish{
//     public static void main(String[] args) {
//         for(int i = 0; i<=6; i++){  
//             for(int j = 0; j<=6; j++){
//                 System.out.println(i+ "\t" +j);
//             }
//         }
//     }
// }

// *
// * *
// * * *
// * * * *
// * * * * *

// 1
// 1 2
// 1 2 3
// 1 2 3 4 
// 1 2 3 4 5

// class harish {
//     public static void main(String[] args) {
//         for (int i = 1; i <=5; i++) {
//             for (int j = 1; j <=i; j++) {
//                 System.out.print(j + " ");
//             }
//             System.out.println();
//         }
//     }
// }
// 1
// 1 2

// 1 2 3 4 5
// 1 2 3 4 5
// 1 2 3 4 5
// 1 2 3 4 5
// 1 2 3 4 5

// class LearnJava{
//     public static void main(String args[]){
//         boolean flag = true;
//         int a = 11;
//         if (a > 10){
//         flag = false;`
//         }
//         else{
//         flag = true;
//         }
//         System.out.println(flag);
//     }
// }

// input:

// a = 11
// b = 15

// output:

// a = 15
// b = 11

// a = 9-2
// b = 7+2

// 1
// 2 3
// 4 5 6 
// 7 8 9 10
// 11 12 13 14 15

// class Pattern {
//     public static void main(String[] args) {
//         int num = 1;
//         for (int i = 1; i <= 5; i++) {
//             for (int j = 1; j <= i; j++) {
//                 System.out.print(num + " ");
//                 num++;
//             }
//             System.out.println();
//         }
//     }
// }
// 1
// 0 1
// 1 0 1
// 0 1 0 1
// 1 0 1 0 1

// 1 2 3 4 5 6 
//  2 3 4 5 6 
//   3 4 5 6 
//    4 5 6 
//     5 6 
//      6 
//     5 6 
//    4 5 6 
//   3 4 5 6 
//  2 3 4 5 6 
// 1 2 3 4 5 6 

// class Pattern2 {
//     public static void main(String[] args) {
//         int n = 6;
//         int i, j;
//         // upper part
//         for (i = 1; i <= n; i++) {
//             // inner loop for printing up the spaces
//             for (j = 1; j < i; j++) {
//                 System.out.print(" ");
//             }
//             // inner loop for printing up the values
//             for (j = i; j <= n; j++) {
//                 System.out.print(j + " ");
//             }
//             System.out.println();
//         }
//         // lower part
//         for (i = n - 1; i >= 1; i--) {
//             // inner loop for printing up the spaces
//             for (j = 1; j < i; j++) {
//                 System.out.print(" ");
//             }
//             // inner loop for printing up the values
//             for (j = i; j <= n; j++) {
//                 System.out.print(j + " ");
//             }
//             System.out.println();
//         }
//     }
// }

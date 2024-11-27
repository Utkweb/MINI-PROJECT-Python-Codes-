import java.util.*;
class Piyush{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number to put the value of A : ");
        int a = sc.nextInt();
        System.out.println("Enter the number to put the value of B : ");
        int b = sc.nextInt();

        
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.println("Enter the choice :");

        int c = sc.nextInt();

        switch(c){
            case 1:
            System.out.println("The addition of two numbers are : "+(a+b));
            break;
            case 2:
            System.out.println("The Subtraction of two numbers are : "+(a-b));
            break;
            case 3:
            System.out.println("The Multiplication of two numbers are : "+(a*b));
            break;
            case 4:
            System.out.println("The Division of two numbers are : "+(a/b));
            break;
            default:
            System.out.println("Invalid choice!");
            break;
        }
    }
}
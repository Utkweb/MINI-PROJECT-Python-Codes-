// import java.util.*;
// class Piyush{
//     public static void main(String args[]){
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter the number to put the value of A : ");
//         int a = sc.nextInt();
//         System.out.println("Enter the number to put the value of B : ");
//         int b = sc.nextInt();

//         System.out.println("1. Addition");
//         System.out.println("2. Subtraction");
//         System.out.println("3. Multiplication");
//         System.out.println("4. Division");
//         System.out.println("Enter the choice :");

//         int c = sc.nextInt();

//         switch(c){
//             case 1:
//             System.out.println("The addition of two numbers are : "+(a+b));
//             break;
//             case 2:
//             System.out.println("The Subtraction of two numbers are : "+(a-b));
//             break;
//             case 3:
//             System.out.println("The Multiplication of two numbers are : "+(a*b));
//             break;
//             case 4:
//             System.out.println("The Division of two numbers are : "+(a/b));
//             break;
//             default:
//             System.out.println("Invalid choice!");
//             break;
//         }
//     }
// }

// String name = "Piyush";
// char c = 'e';

// int and we are going to convert into char
import java.io.IOException;

class Piyush {
    public static void main(String args[]) {
        // int quizGrade;
        // try {
        // quizGrade = Integer.parseInt("110");
        // // System.out.println(quizGrade);
        // System.out.print("Blue ");

        // if (quizGrade < 70 || quizGrade > 105)
        // throw new Exception("Yellow ");
        // } catch (NumberFormatException e) {
        // System.out.print("Orange ");
        // } catch (Exception e) {
        // System.out.print(e.getMessage()
        // + "Green ");
        // } finally {
        // System.out.print("Red ");
        // }

        try {
            readFile("example.txt");

            readFile("");
        } catch (IOException e) {
            System.out.println("An error occured : " + e.getMessage());
        }

    }

    public static void readFile(String filepath) throws IOException {

        if (filepath == null || filepath.isEmpty()) {
            throw new IOException("File path is invalid");
        }
        System.out.println("File read successfully!");

    }
}
// positive index -
// negative index -x
// .length() - it gives out you the length
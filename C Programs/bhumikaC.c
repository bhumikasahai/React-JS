#include <stdio.h>

//C Programming: Input & Output operations and Data Type in C:

//1.Write a program to add and multiply two numbers (5&7) and display it
// void main(){
//    int num1 = 5, num2 = 7;
//    int sum = num1 + num2;
//    int product = num1 * num2;
//    printf("Sum: %d\n", sum);
//    printf("Product: %d", product);
// }

//2. area of circle
// #define PI 3.14159
// void main(){
//    float radius, area;
//    printf("Enter the radius of the circle: ");
//    scanf("%f", &radius);
//    area = PI * radius * radius;
//    printf("Area = %.2f sq. units", area);
// }

//3. Write a program to calculate simple interest for a given P=4000, T=2, R=5.5. (I =P*T*R/100)
// void main() {
//    float principle = 4000, time = 2, rate = 5.5, simple_interest;
//    simple_interest = (principle * time * rate) / 100;
//    printf("The Simple Interest is: %f", simple_interest);
// }

//4. Write a Program to calculate and display the volume of a CUBE having its height (h=10cm), width (w=12cm) and depth (8cm).
// void main() {
//    int height = 10;
//    int width = 12;
//    int depth = 8;
//    int volume = height * width * depth;
//    printf("Volume of the cube is: %d cubic cm", volume);
// }

//Different Operators in C:

//1. Write a program to swap two variables‟ values with and without using third variables
// with third variable
// void main() {
//    int a, b, temp;
//    printf("Enter the value of a and b: ");
//    scanf("%d %d", &a, &b);
//    printf("Before swapping: a = %d, b = %d\n", a, b);
//    temp = a;
//    a = b;
//    b = temp;
//    printf("After swapping, a = %d and b = %d", a, b);
// }
// without third variable
// void main() {
//    int a, b;
//    printf("Enter two numbers: ");
//    scanf("%d %d", &a, &b);
//    printf("Before swapping: a = %d, b = %d\n", a, b);
//    a = a + b;
//    b = a - b;
//    a = a - b;
//    printf("After swapping: a = %d, b = %d", a, b);
//    return 0;
// }

//2.Write a program to print the size of char, float, double, and long double data types in C
// void main() {
//     printf("Size of char: %d bytes\n", sizeof(char));
//     printf("Size of float: %d bytes\n", sizeof(float));
//     printf("Size of double: %d bytes\n", sizeof(double));
//     printf("Size of long double: %d bytes\n", sizeof(long double));
// }

//3. Write a program to convert temperature from degree centigrade to Fahrenheit. °F = °C*9/5+32
// void main() {
//     float celsius, fahrenheit;
//     printf("Enter temperature in Celsius: ");
//     scanf("%f", &celsius);
//     fahrenheit = (celsius * 9/5) + 32;
//     printf("Temperature in Fahrenheit is: %f", fahrenheit);
// }

//4. Write a program to compute the addition, subtraction, product, quotient, and remainder of two given numbers.
// void main() {
//     int num1, num2;
//     printf("Enter numbers: ");
//     scanf("%d %d", &num1, &num2);
//     printf("Sum: %d\n", num1 + num2);
//     printf("Difference: %d\n", num1 - num2);
//     printf("Product: %d\n", num1 * num2);
//     if (num2 != 0){
//         printf("Quotient: %d\n", num1 / num2);
//         printf("Remainder: %d\n", num1 % num2);
//     }
//     else{
//         printf("Cannot divide by zero\n");
//     }
// }

//5. Write a program to find the largest number out of three integer numbers entered by the user using the ternary/conditional/tertiary operator.
// void main() {
//     int num1, num2, num3, max;
//     printf("Enter three numbers: ");
//     scanf("%d %d %d", &num1, &num2, &num3);
//     max = (num1 > num2) ? (num1 > num3 ? num1 : num3) : (num2 > num3 ? num2 : num3);
//     printf("The largest number is %d", max);
// }

//Conditional and looping statements in C:

//1. Write a program to find the largest and smallest among three entered numbers
// void main() {
//     int num1, num2, num3;
//     printf("Enter three numbers: ");
//     scanf("%d %d %d", &num1, &num2, &num3);
//     int largest, smallest;
//     if (num1 >= num2 && num1 >= num3) {
//         largest = num1;
//     } else if (num2 >= num1 && num2 >= num3) {
//         largest = num2;
//     } else {
//         largest = num3;
//     }
//     if (num1 <= num2 && num1 <= num3) {
//         smallest = num1;
//     } else if (num2 <= num1 && num2 <= num3) {
//         smallest = num2;
//     } else {
//         smallest = num3;
//     }
//     printf("Largest: %d\nSmallest: %d", largest, smallest);
// }

//2. Write a program to print whether a given number is even or odd.
// void main() {
//     int num;
//     printf("Enter a number: ");
//     scanf("%d", &num);    
//     if(num % 2 == 0) {
//         printf("%d is even", num);
//     } else {
//         printf("%d is odd", num);
//     }
// }

//3. Write a program to print positive integers from 1 to 100.
// void main() {
//     for (int i = 1; i <= 100; i++) {
//         printf("%d\n", i);
//     }
// }

//4. Write a program to check whether the input alphabet is vowel or not using if-else and switch statements.
// void main() {
//     char ch;
//     int lowercase_vowel, uppercase_vowel;
//     printf("Enter a character: ");
//     scanf("%c", &ch);
//     lowercase_vowel = (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
//     uppercase_vowel = (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U');
//     if (lowercase_vowel || uppercase_vowel)
//         printf("%c is a vowel.", ch);
//     else
//         printf("%c is a consonant.", ch);
// }

//5. Write a program to print the sum of digits of a number using for loop
// void main() {
//     int num, rem, sum = 0;
//     printf("Enter a number: ");
//     scanf("%d", &num);
//     for ( ; num > 0; num = num/10) {
//         rem = num % 10;
//         sum += rem;
//     }
//     printf("Sum of digits: %d", sum);
// }

//Function and Array in C:

//1. Write a program to add, subtract, multiply, and divide two integers using a user-defined type function with return type
// int add(int a, int b) {
//     return a + b;
// }
// int subtract(int a, int b) {
//     return a - b;
// }
// int multiply(int a, int b) {
//     return a * b;
// }
// int divide(int a, int b) {
//     return a / b;
// }
// void main() {
//     int num1, num2;
//     printf("Enter two numbers: ");
//     scanf("%d %d", &num1, &num2);
//     printf("Sum: %d\n", add(num1, num2));
//     printf("Difference: %d\n", subtract(num1, num2));
//     printf("Product: %d\n", multiply(num1, num2));
//     printf("Quotient: %d\n", divide(num1, num2));
// }

//2. Write a program to find the factorial of a given number using a function.
// int factorial(int n) {
//     if (n == 0) {
//         return 1;
//     } else {
//         return n * factorial(n - 1);
//     }
// }
// void main() {
//     int num;
//     printf("Enter a number: ");
//     scanf("%d", &num);
//     printf("Factorial of %d: %d", num, factorial(num));
// }

//3. Write a program to swap two integers using call by value
// void swap(int a, int b) {
//     int temp = a;
//     a = b;
//     b = temp;
// }
// void main() {
//     int x , y, temp;
//     printf(" Enter two number :");
//     scanf("%d%d",&x,&y);
//     printf("Before swapping: x = %d, y = %d\n", x, y);
//     temp = x;
//     x = y;
//     y = temp;
//     printf("After swapping: x = %d, y = %d\n", x, y);
// }

// FUNCTION

// PRACTICE QUESTION 1
#include <stdio.h>
/*int main()
{
    int a;
    printf("Enter the test passed \n");
    scanf("%d", &a);
    printf("If test passesd is equal to 1 the it is fior maths and science test \n if it is 2 then only maths test \n if it is 3 then only science \n");
    if (a == 1)
    {
        printf("For both maths and science you will get 45 points %d ", a);
    }
    else if (a == 2)
    {
        printf("For only maths you will get 15 points %d", a);
    }
    else if (a == 3)
    {
        printf("For only science you will get 15 points %d", a);
    }
    else
    {
        printf("Invalid");
    }
    return 0;
}*/

// PRACTICE QUESTION 2
// declaration prototype
/*void printHello();

// function call
int main()
{
    printHello();
    printHello();
    printHello();
    printHello();
    return 0;
}

// function definition
void printHello()
{
    printf("Hello\n");
    printf("My name is Bhumika\n");
}*/

// PRACTICE QUESTION 3
/*void printHello();
void printGoodbye();

int main()
{
    printHello();
    printGoodbye();
    return 0;
}

void printHello()
{
    printf("Hello\n");
}

void printGoodbye()
{
    printf("Goodbye \n");
}*/

// PRACTICE QUESTION 4
/*void namaste();
void bonjour();

int main()
{
    printf("Enter f for french and i for indian ");
    char ch;
    scanf("%c", &ch);
    if (ch == 'i')
    {
        namaste();
    }
    else
    {
        bonjour();
    }
    return 0;
}

void namaste()
{
    printf("Namaste \n");
}
void bonjour()
{
    printf("Bonjour \n");
}*/

// PRACTICE QQUESTION 5
/*int sum(int a, int b);

int main()
{
    int a, b;
    printf("Enter first number : ");
    scanf("%d", &a);
    printf("Enter second number : ");
    scanf("%d", &b);

    int s = sum(a, b);
    printf("sum is %d", s);
    return 0;
}

int sum(int a, int b)
{
    return a + b;
}*/

// PRACTICE QUESTION 6
/*void printTable(int n);

int main()
{
    int n;
    printf("Enter the no : ");
    scanf("%d", &n);
    printTable(n);
    return 0;
}

void printTable(int n)
{
    for (int i = 1; i <= 10; i++)
    {
        printf("%d\n", i * n);
    }
}*/

// PRACTICE QUESTION 7
/*float squareArea(float side);
float circleArea(float rad);
float rectangleArea(float a, float b);

int main()
{
    float rad = 5.0;
    printf("area is= %f ", circleArea(rad));
    return 0;
}

float squareArea(float side)
{
    return side * side;
}
float circleArea(float rad)
{
    return 3.14 * rad * rad;
}
float rectangleArea(float a, float b)
{
    return a * b;
}*/

// RECURSION

// PRACTICE QUESTION 7
/*void printHW(int count);

int main()
{
    printHW(5);
    return 0;
}

void printHW(int count)
{
    if (count == 0)
    {
        return;
    }
    printf("Hello World \n");
    printHW(count - 1);
}*/

// PRACTICE QUESTION 8
/*int sum(int n);

int main()
{
    printf("sum is : %d", sum(5));
    return 0;
}

int sum(int n)
{
    if (n == 1)
    {
        return 1;
    }
    int sumNm1 = sum(n - 1);
    int sumN = sumNm1 + n;
    return sumN;
}*/

// PRACTICE QUESTION 9
/*int fact(int n);

int main()
{
    printf("factorial is : %d", fact(5));
    return 0;
}

int fact(int n)
{
    if (n == 0)
    {
        return 1;
    }
    int factNm1 = fact(n - 1);
    int factN = factNm1 * n;
    return factN;
}*/

// POINTERS

// ques 1
/*int main()
{
    int age = 22;
    int *ptr = &age;

    printf("%p\n", &age);
    printf("%u\n", &age);
    printf("%u\n", ptr);
    printf("%u\n", &ptr);
}*/

// ques 2
/*int main()
{
    float price = 100.00;
    float *ptr = &price;
    float **pptr = &ptr;
    return 0;
}*/

// ques 3
/*void square(int n);

int main()
{
    int number = 4;
    square(number);
    printf("nuumber = %d\\n", number);
    return 0;
}
void square(int n)
{
    n = n * n;
    printf("square = %d\n", n);
}*/

// ARRAYS

// ques 1
/*int main()
{
    int marks[3];
    printf("enter phy = ");
    scanf("%d", &marks[0]);
    printf("enter math = ");
    scanf("%d", &marks[1]);
    printf("enter chem = ");
    scanf("%d", &marks[3]);

    printf("phy = %d\n", marks[0]);
    printf("chem =%d\n", marks[1]);
    printf("math =%d\n", marks[3]);
}*/

// ques 2
/*int main()
{
    float price[3];
    printf("Enter the price 1: ");
    scanf("%f", &price[0]);
    printf("Enter the price 2: ");
    scanf("%f", &price[1]);
    printf("Enter the price 3: ");
    scanf("%f", &price[2]);

    printf("final cost = %f\n", (price[0] + (0.18 * price[0])));
    printf("final cost = %f\n", (price[1] + (0.18 * price[1])));
    printf("final cost = %f\n", (price[2] + (0.18 * price[2])));
}*/

// ques 3


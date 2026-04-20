#include <stdio.h>
#include <conio.h>
// 1. To print the sum of two numbers
/*int main()
{
    int a, b, c;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", &b);
    c = a + b;
    printf("The resut is:%d", c);
}*/

// 2. To find the area of circle
/*int main()
{
    int r;
    float area;
    printf("Enter the radius of the circle: ");
    scanf("%d", &r);
    area = 3.14 * r * r;
    printf("The area of the circle is=%f ", area);
}*/

// 3. To print the best of twwo average marks out of three marks
/*int main()
{
    int a, b, c, avg1, avg2, avg3;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", b);
    printf("Enter the third number: ");
    scanf("%d", c);
    avg1 = (a + b) / 2;
    avg2 = (b + c) / 2;
    avg3 = (a + c) / 2;
    if (avg1 > avg2)
    {
        printf("Best of tw0:%d ", avg1);
    }
    else if (avg2 > avg3)
    {
        printf("Best of two:%d", avg2);
    }
    else
    {
        printf("Best of two:%d", avg3);
    }
}*/

// 4. To multiply a given number by 4 using bitwise
/*int main()
{
    int x, y;
    printf("Enter the number: ");
    scanf("%d", &x);
    y = x << 2;
    printf("The result is=%d", y);
}*/

// 5. To print the swap of two numbers
/*int main()
{
    int a, b;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("The first number=%d", a);
    printf("The second number=%d", b);
}*/

// 6. To print the largest of two numbers
/*int main()
{
    int a, b, c;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", &b);
    printf("Enter the third number: ");
    scanf("%d", &c);
    if (a > b && a > c)
    {
        printf("largest=%d", a);
    }
    else if (b > a && b > c)
    {
        printf("largest=%d", b);
    }
    else
    {
        printf("largest=%d", c);
    }
}*/

// 7. To check whether the entered year is a leap year
/*int main()
{
    int year;
    printf("Enter the year: ");
    scanf("%d", &year);
    if ((year % 100 == 0) && (year % 400 == 0))
    {
        printf("Leap year=%d", year);
    }
    else if (year % 4 == 0 && year % 100 != 0)
    {
        printf("Leap year=%d", year);
    }
    else
    {
        printf("Not a Leap year=%d", year);
    }
}*/

// 7. To print the factorial of a number
/*int main()
{
    int fact, a;
    fact = 1;
    printf("Enter the number: ");
    scanf("%d", &a);
    if (a < 0)
    {
        printf("Factorial doesnt eist=%d", a);
    }
    else if (a == 1)
    {
        printf("Fatorial is 1=%d", a);
    }
    else
    {
        for (int i = 1; i <= a; i++)
        {
            fact = fact * i;
        }
        printf("Fatorial is=%d", fact);
    }
}*/

// 8. A menu driven program to find the sum,product,divide and subtract
/*int main()
{
    int ch, a, b, c;
    printf("Enter 1 for addition , enter 2 for subtraction , enter 3 for divide=");
    scanf("%d", &ch);
    switch (ch)
    {
    case 1:
        printf("Enter two numbers=");
        scanf("%d,%d", &a, &b);
        c = a + b;
        printf("The result is=%d", c);
        break;
    case 2:
        printf("Enter two numbers=");
        scanf("%d,%d", &a, &b);
        c = a * b;
        printf("The result is=%d", c);
        break;
    case 3:
        printf("Enter two numbers=");
        scanf("%d,%d", &a, &b);
        c = a / b;
        printf("The result is=%d", c);
    }
}*/

// 9. Print the star pattern(pyramid)
/*int main()
{
    int i, j, n;
    printf("Enter the n number of rows= ");
    scanf("%d", n);
    for (i = 0; i <= n; i++)
    {
        for (j = 0; j <= n - i - 1; j++)
        {
            printf(" ");
        }
        for (j = 0; j <= i; j++)
        {
            printf("*");
        }
        printf(" ");
    }
}*/

// 10. To print the fibonacci series
/*int main()
{
    int n, a, b;
    a = 0, b = 1;
    printf("Enter the n number of terms= ");
    scanf("%d", &n);
    while (a <= n)
    {
        printf("%d", a);
        a, b = b, a + b;
    }
}*/

// 11. Print the table of given number
/*int main()
{
    int n, i, table;
    table = 1;
    printf("Enter the number whose table needs to be printed= ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        table = n * i;
    }
}*/

// 12. To print the sum of two numbers using function

/*int add()
{
    int a, b, add;
    printf("Enter the two numbers: ");
    scanf("%d %d", &a, &b);
    add = a + b;
    printf("%d", add);
    return 0;
}
void main()
{
    add();
}*/

// 13. To swap two numbers without using third variable by using functions
/*void swap()
{
    int a, b;
    printf("Enter the number: ");
    scanf("%d %d", &a, &b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("a is %d b is %d", a, b);
}
void main()
{
    swap();
}*/

// 14. To swap two numbers using third variable using functions
/*void swap()
{
    int a, b, swap;
    swap = 0;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    swap = a;
    a = b;
    b = swap;
    printf("The first number is:%d ", a);
    printf("The second number is:%d ", b);
}
void main()
{
    swap();
}*/

// 15. To add two matrix
/*int main()
{
    int m, n;
    printf("Enter the number of rows and columns of the matrix: ");
    scanf("%d %d", &m, &n);
    int M1[m][n], M2[m][n], result[m][n];
    printf("Enter the elements of the M1 matrix\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &M1[i][j]);
        }
    }
    printf("Enter the elements of the M2 matrix\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &M2[i][j]);
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i][j] = M1[i][j] + M2[i][j];
        }
    }
    printf("Sum of the matrices:\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d\t", result[i][j]);
        }
        printf("\n");
  /  }
}*/

#include <stdio.h>

int square(int x)
{
    return x * x;
}

int main(void)
{
    // int a, b;

    // printf("%s\n", "Enter values for a and b:");

    // scanf("%d\n%d", &a, &b);

    // printf("%d + %d = %d\n", a, b, a + b);

    // ---------------------------------

    // char name[20];

    // fgets(name, 20, stdin);

    // printf("%s", name);

    // for (int i = 1; i < 10; i++)
    // {
    //     int value = square(i);
    //     printf("%d^%d = %d   ", i, i, value);
    // }
    // printf("%s\n", "");

    // int num = 10;

    // int *ptr;

    // ptr = &num;

    // printf("%d\n", num);
    // printf("%d\n", &num);
    // printf("%d\n", ptr);
    // printf("%d\n", *ptr + 4);
    // printf("%d\n", *ptr);

    // int a[5] = {1, 2, 3, 4, 5};

    // int *ptr;

    // ptr = a;

    // for (int i = 0; i < 5; i++)
    // {
    //     printf("%d", *ptr++);
    // }

    int n = 1;

    while (n < 10000000)
    {
        printf("%d\n", n);
        n++;
    }

    return 0;
}

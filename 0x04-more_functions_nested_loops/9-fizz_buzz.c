#include "main.h"

/**
 * main - Prints the number 1 to 100, but prints fizz in place
 * of multiples of three, buzz for multiples of five and
 * FizzBuzz for both multiples of five and three.
 *
 * Return: 0, when sucessful and 1 if otherwise.
 */

int main (void)
{
int num;

for (num = 0; num <= 100; num++)
{
if (num % 3 == 0 && num % 5 == 0)
    printf("FizzBuzz");
else if (num % 3 == 0)
    printf("Fizz");
else if
    printf("Buzz");
else
    printf("%d", num);

if (num != 100)
    printf(" ");
}
printf("\n");
return (0);
}

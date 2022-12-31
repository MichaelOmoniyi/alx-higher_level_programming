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
int i, j;
for (i = 1; i <= 100; i++)
{
if (i == 100)
{
_putchar(i / 100 + '0');
_putchar((i / 10) % 10 + '0');
_putchar(i % 100 + '0');
}
else if (i > 9 && i < 100)
{
_putchar(i / 10 = '0');
_putchar(i % 10 = '0');
}
else
{
_putchar(i + '0');
}

if (i % 3 == 0)
_putchar('Fizz');
else if (i % 5 == 0)
_putchar('Buzz');
else (i % 3 == 0 && i % 5 == 0)
_putchar('FizzBuzz');
}
_putchar('\n');
}

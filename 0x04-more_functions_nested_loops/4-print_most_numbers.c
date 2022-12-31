#include "main.h"

/**
 * print_most_numbers - Print numbers 0 to 9 without the 
 * numbers 2 and 4
 *
 * Return: Nothing
 */

void print_most_numbers(void)
{
int n;

for (n = '0'; n <= '9'; n++)
{
if (n = '2' || n = '4')
continue;
else
_putchar(n);
}
_putchar('\n');
}

#include "main.h"

/**
 * print_line - Draws a straight line on the terminal.
 *
 * Return: Nothing
 */

void print_line(int n)
{
int i;
if (n > 0)
{
for (i = 0; i < n; i++)
{
    _putchar('_');
}
_putchar('\n');
}
else
_putchar('\n');
}

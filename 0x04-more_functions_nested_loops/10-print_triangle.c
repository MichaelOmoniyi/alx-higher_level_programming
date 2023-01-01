#include "main.h"

/**
 * print_triangle - Prints a triangle, followed by a new line.
 *
 * @size: Input for triangle size.
 *
 * Return: Returns void(Nothing).
 */

void print_triangle(int size)
{
int i, j, k;

if (size > 0)
{
for (i = 0; i < size; i++)
{
for (j = size - 1; j > i; j--)
{
_putchar(' ');
}
for (k = 0; k <= i; k++)
{
_putchar('#');
}
}
_putchar('\n');
}
else
_putchar('\n');
}

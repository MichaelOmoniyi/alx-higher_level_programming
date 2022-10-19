#include "main.h"

/**
 * print_sign - prints the sign of a number
 * @n: input character
 * Return: 1 when positive, 0 when zero, -1 when negative
 */

int print_sign(int n)
{
	int N = n;
	int sign = 0;

	if (N > 0)
		_putchar ('+');
		sign = 1;
	else if (N < 0)
		_putchar ('-');
		sign = -1;
	else
		_putchar ('0');
		sign = 0;
	return (sign);
}

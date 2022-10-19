#include "main.h"

/**
 * print_to_98 - print all natural numbers from n to 98
 * @n: An input character
 */

void print_to_98(int n)
{
	while (n <= 98)
	{
		_putchar ((n / 10) + '0');
		_putchar ((n % 10) + '0');
		if (n == 98)
			continue;
		_putchar (',');
		_putchar (' ');
		n++;
	}
	while (n >= 98)
	{
		_putchar ((n / 10) + '0');
		_putchar ((n % 10) + '0');
		if (n == 98)
			continue;
		_putchar (',');
		_putchar (' ');
		n--;
	}
	if (n == 98)
		_putchar ((n / 10) + '0');
}

#include "main.h"
#include <stdio.h>

/**
 * print_to_98 - print all natural numbers from n to 98
 * @n: An input character
 */

void print_to_98(int n)
{
	while (n <= 98)
	{
		if (n != 98)
			printf ("%d, ", n);

		if (n == 98)
			printf ("%d\n");
		n++;
	}
	while (n >= 98)
	{
		if (n != 98)
			printf ("%d, ", n);

		if (n == 98)
			printf ("%d\n", n);
		n--;
	}
	if (n == 98)
		printf ("%d\n", n);
}

#include "main.h"

/**
 * print_times_alphabet - prints the n times table
 * @n: Input character
 */

void print_times_table(int n)
{
	int a, b, c;

	if (n >= 0 && n <= 15)
	{
		for (a = 0; a <= 15; a++)
		{
			for (b = 0; b <= 15; b++)
			{
				c = a * b;

				if (a == 0)
				{
					_putchar (c + '0');
				}
				if (c < 10)
				{
					_putchar (c + '0');
					_putchar (',');
					_putchar (' ');
				}
				if (c >= 10 && c < 100)
				{
					_putchar ((c / 10) + '0');
					_putchar ((c % 10) + '0');
					_putchar (',');
					_putchar (' ');
				} else if (c >= 100)
				{
					_putchar (',');
					_putchar (' ');
					_putchar ((c / 100) + '0');
					_putchar (((c / 10) % 10) + '0');
					_putchar ((c % 10) + '0');
				}
			}
		}i
	}
	else
	{
		_putchar ('\n');
	}
}

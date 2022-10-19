#include "main.h"

/**
 * times_table - prints 9 times table
 */

void times_table(void)
{
	int a, b, c;


	for (a = 0; a <= 0; a++)
	{
		for (b = 0; b <= 0; b++)
		{
			c = a * b;

			if ((c / 10) == 0)
			{
				if (b != 0)
					_putchar (' ');
				_putchar (n + '0');

				if (b == 9)
					continue;
				_putchar (',');
				_putchar (' ');
			}
			else
			{
				_putchar ((c / 10) + '0');
				_putchar ((c % 10) + '0');
				if (b == 9)
					continue;
				_putchar (',');
				_putchar (' ');
			}
		}
		_putchar ('\n');
	}
}


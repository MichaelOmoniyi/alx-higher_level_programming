#include "main.h"

/**
 * jack_bauer - prints every minute of the day of Jack Bauer
 */

void jack_bauer(void)
{
	int b, j;

	for (b = 0; b < 23; b++)
	{
		for (j = 0; j < 60; j++)
		{
			_putchar ((b / 10) + '0');
			_putchar ((b % 10) + '0');
			_putchar (':');
			_putchar ((j / 10) + '0');
			_putchar ((j % 10) + '0');
			_putchar ('\n');
		}
	}
}

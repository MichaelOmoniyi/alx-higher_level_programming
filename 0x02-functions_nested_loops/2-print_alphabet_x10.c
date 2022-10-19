#include "main.h"

/**
 * print_alphabet_x10 - prints alphabets
 */


void print_alphabet_x10(void)
{
	char az;
	int i;

	for (i = 0; i < 10; i++)
	{
		for (az = 'a'; az <= 'z'; az++)
		{
			_putchar ('\n');
		}
		_putchar ('\n');
	}
}

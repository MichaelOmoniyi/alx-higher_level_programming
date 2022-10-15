#include <stdio.h>

/**
 * main - prints all possible combinations of single-digit numbers.
 * Return: 0
*/

int main(void)
{
	int n;

	for (n = 48; n <= 57; n++)
	{
		putchar (n);
		if (n < 57)
		{
			putchar (44);
			putchar (32);
		}
	}
	putchar ('\n');
	return (0);
}

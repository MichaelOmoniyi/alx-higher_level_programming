#include <stdio.h>

/**
 * main - displays all decimal digits of base 10
 * starting from zero starting with a newline
 * using putchar
 * Return: 0 when succesful
*/

int main(void)
{
	int a;


	for (a = 48; a < 58; a++)
	{
		putchar (a);
	}
	putchar ('\n');
	return (0);
}

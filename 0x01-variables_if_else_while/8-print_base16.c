#include <stdio.h>

/**
 * main - prints all the numbers of base 16 in lowercase,
 * followed by a new line.
 * Return: 0
*/

int main(void)
{
	int a;
	char af;

	for (a = 48; a <= 57; a++)
	{
		putchar (a);
	}
	for (af = 'a'; af < 'g'; af++)
	{
		putchar (af);
	}
	putchar ('\n');
	return (0);
}

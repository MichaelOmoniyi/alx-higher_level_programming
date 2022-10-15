#include <stdio.h>

/**
 * main - prints the lowercase alphabet in reverse,
 * followed by a new line.
 * Return: 0
*/

int main(void)
{
	char za;

	for (za = 'z'; za >= 'a'; za--)
	{
		putchar (za);
	}
	putchar ('\n');
	return (0);
}

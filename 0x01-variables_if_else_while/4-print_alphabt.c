#include <stdio.h>

/**
 * main - executes statements
 * Return: 0
*/

int main(void)
{
	char ch;
	char exclude;

	exclude = 'q' + 'e';

	for (ch = 'a'; ch <= 'z' && ch != exclude; ch++)
	{
		putchar (ch);
	}
	putchar ('\n');
	return (0);
}

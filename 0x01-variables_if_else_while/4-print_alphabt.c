#include <stdio.h>

/**
 * main - executes statements
 * Return: 0
*/

int main(void)
{
	char ch;

	for (ch = 'a'; ch <= 'z' && ch != 'q', 'e'; ch++)
	{
		putchar (ch);
	}
	putchar ('\n');
	return (0);
}

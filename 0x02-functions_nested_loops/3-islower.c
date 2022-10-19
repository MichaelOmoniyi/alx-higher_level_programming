#include "main.h"

/**
 * _islower - checks for lower case character
 *@c: An input character
 * Return: 0, if character is uppercase and 1 if otherwise
 */

int _islower(int c)
{
	char ch;

	for (ch = 'a'; ch <= 'z'; ch++)
	{
		if (c >= 'a' && c <= 'z')
			c = 1;
		else
			c = 0;
	}
	return (c);
}

#include "main.h"

/**
 * _isalpha - check alphabets, both lower and upper case
 * @c: input character
 * Return: 1 when successful
 */

int _isalpha(int c)
{
	char ch;
	int alpha = 0;

	for (ch = 'a'; ch <= 'z'; ch++)
	{
		if (ch == c)
			alpha = 1;
		return (alpha);
	}
	for (ch = 'A'; ch <= 'Z'; ch++)
	{
		if (ch == c)
			alpha = 1;
		return (alpha);
	}
	return (alpha);
}

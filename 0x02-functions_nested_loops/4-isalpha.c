#include "main.h"

/**
 * _isalpha - check alphabets, both lower and upper case
 * @c: input character
 * Return: 1 when successful
 */

int _isalpha(int c)
{
	char lower, upper;
	int alpha = 0;

	for (lower = 'a'; lower <= 'z'; lower++)
	{
		if (lower == c)
			alpha = 1;
		return (alpha);
	}
	for (upper = 'A'; upper <= 'Z'; upper++)
	{
		if (upper == c)
			alpha = 1;
		return (alpha);
	}
	return (alpha);
}

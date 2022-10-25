#include "main.h"
#include <string.h>

/**
 * _strlen - Returns the length of a string
 * @s: input character parameter
 */

int _strlen(char *s)
{
	int i = 0;

	while (s[i] != '\0')
		i++;
	return (i);
}

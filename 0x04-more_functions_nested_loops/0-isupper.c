#include "main.h"

/**
 * _isupper - checks for uppercase characters.
 *
 * @c: input character
 *
 * Return: Returns 1, if c is uppercase and 0 if otherwise.
 */
int _isupper(int c)
{
    char ch;
    int upper = 0;

    for (ch = 'A'; ch <= "Z"; ch++)
    {
    if (c == ch)
        upper = 1;
    }
    return (upper);
}


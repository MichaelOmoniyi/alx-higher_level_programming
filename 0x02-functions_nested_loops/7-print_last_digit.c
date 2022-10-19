#include "main.h"

/**
 * print_last_digit - print last digit of the number
 * @n: input character
 * Return: last digit of number when succesful
 */

int print_last_digit(int n)
{
	int lastDigit = n % 10;

	if (n < 0)
		n = -n;

	if (lastDigit < 0)
		lastDigit = -lastDigit;

	_putchar(lastDigit + '0');
	return (lastDigit);
}

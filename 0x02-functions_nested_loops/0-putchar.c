#include <unistd.h>
#include "main.h"

/**
 * main - prints _putchar
 *
 * Return: 0, when successful
 */

int main(void)
{
	char word[8] = "_putchar";
	int p;

	for (p = 0; p <= 8; p++)
	{
		_putchar(word[p]);
	}
	_putchar ('\n');
	return (0);
}

#include <stdio.h>

/**
 * main - prints all possible different combinations of three digits.
 *
 *
 *
 * Numbers must be separated by ,, followed by a space
 *
 * The three digits must be different
 *
 * 012, 120, 102, 021, 201, 210 are considered
 * the same combination of the three digits 0, 1 and 2
 *
 * Print only the smallest combination of three digits
 *
 * Numbers should be printed in ascending order, with three digits
 *
 * You can only use the putchar function
 * (every other function (printf, puts, etc…) is forbidden)
 *
 * You can only use putchar six times maximum in your code
 *
 * You are not allowed to use any variable of type char
 * Return: 0 when sucessful
*/

int main(void)
{
	int a, b, c;

	for (a = '0'; a < '8'; a++)
	{
		for (b = a + 1; b < '9'; b++)
		{
			for (c = b + 1; c <= '9'; c++)
			{
				if ((a != b) != c)
				{
					putchar (a);
					putchar (b);
					putchar (c);
					if (a == '7' && b == '8' && c == '9')
						continue;
					putchar (',');
					putchar (' ');
				}
			}
		}
	}
	putchar ('\n');
	return (0);
}

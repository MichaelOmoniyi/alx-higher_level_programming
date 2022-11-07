#include <stdio.h>
#include <stdlib.h>

/**
 * main - multiplies two numbers
 * @argc: The number of arguments supplied into the program
 * @argv: Pointer to the arguments the program receives
 *
 * Return: 1, if one of the arguments contain symbols
 * 0, if otherwise
 */

int main(int argc, char *argv[])
{
	int num, digit, add = 0;

	for (num = 1; num < argc; num++)
	{
		for (digit = 0; argv[num][digit]; digit++)
		{
			if (argv[num][digit] < '0'  || argv[num][digit] > '9')
			{
				printf("Error\n");
				return (1);
			}
		}

		add += atoi(argv[num]);
	}

	printf("%d\n", add);

	return (0);
}

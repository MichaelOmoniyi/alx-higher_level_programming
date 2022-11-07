#include <stdio.h>

/**
 * main - prints all arguments it receives
 * @argc: The number of arguments supplied into the program
 * @argv: Pointer to the arguments the program receives
 *
 * Return: 0 when successful
 */

int main(int argc, char *argv[])
{
	int i;

	for (i = 0, i < argc, i++)
	{
		printf("%s\n", argv[i]);

		return (0);
	}
}

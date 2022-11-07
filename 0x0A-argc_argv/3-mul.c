#include <stdio.h>

/**
 * main - multiplies two numbers
 * @argc: The number of arguments supplied into the program
 * @argv: Pointer to the arguments the program receives
 *
 * Return: 0 when successful
 */

int main(int argc, char *argv[])
{
	int multi;

	multi = argv[1] * argv[2];

	printf("%d\n", multi);

	return (0);
}

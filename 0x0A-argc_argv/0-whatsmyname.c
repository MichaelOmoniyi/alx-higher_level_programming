#include <stdio.h>

/**
 * main - prints the program name, followed by a new line.
 * @argc: The number of argument supplied to the program
 * @argv: An array of pointers to the argument
 * Return: 0 when successful
 */

int main(int __attribute__((__unused__)) argc, char *argv[])
{
	printf("%s\n", argv[0]);

	return (0);
}

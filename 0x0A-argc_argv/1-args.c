#include <stdio.h>

/**
 * main - Prints the number of arguments passed into the program
 * @argc: The nummber of arguments passed into the program
 * @argv: Pointer to the arguments passed into the program
 * Return: 0 when successful
 */

int main(int argc, char __attribute__((__unsused__)) *argv[])
{
	printf("%d\n", argc - 1);

	return (0);
}

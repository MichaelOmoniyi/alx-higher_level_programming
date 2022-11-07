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
	int num1, num2, multi;
	
	if (argc != 3)
	{
		printf("Error\n");
		return (1);
	}
	
	num1 = atoi(argv[1]);
	num2 = atoi(argv[2]);
	multi = num1 * num2
	
	printf("%d\n", multi);

	return (0);
}

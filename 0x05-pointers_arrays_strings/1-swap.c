#include "main.h"

/**
 * swap_int - swaps the values of two integers
 * @a: input pointer parameter
 * @b: input pointer parameter
 */

void swap_int(int *a, int *b)
{
	int swap;

	swap = *a;
	*a = *b;
	*b = swap;
}

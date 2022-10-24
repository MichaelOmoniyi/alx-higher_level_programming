#include "main.h"

/**
 * reset_to_98 - Updates the value of a pointer
 * @n: Input pointer
 */

void reset_to_98(int *n)
{
	int a = 98;

	*n = a;

	printf("n=%d\n", n);
}

#include <stdio.h>

/**
 * program that prints the name of the file it was compiled from, followed by a new line.
 */
int main(void)
{
	printf("Filename:%s\n",__FILE__);
	return(0);
}

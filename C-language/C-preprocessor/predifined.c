#include <stdio.h>

void printInfo()
{
	printf("File: %s\n", __FILE__);
	printf("Date: %s\n", __DATE__);
	printf("Time: %s\n", __TIME__);
        printf("Line: %d\n", __LINE__);
}

int main()
{
	printf("Standard C: %d\n", __STDC__);
	printInfo();
	return 0;
}


#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int rangeUpper, input;
    int missing = 1;

    scanf("%d", &rangeUpper);
    for (int i = 2; i <= rangeUpper; i++)
    {
        scanf("%d", &input);
        missing = missing ^ input ^ i;
    }

    printf("The missing number is %d\n", missing);
}